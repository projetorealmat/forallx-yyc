#!/usr/bin/env python3
"""Create the search index consumed by BookML's GitBook output.

The BookML container already provides Python 3, while its optional Perl XML
modules are not reliable for this generated HTML.  This scanner deliberately
uses a single forward pass over each file.  It does not build a DOM or recurse
through a tag tree, so malformed or very large LaTeXML pages cannot make the
post-processing step stall.
"""

from html import unescape
import json
import os
from pathlib import Path
import sys


SKIPPED_ELEMENTS = {"annotation", "nav", "script", "style"}
VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


def find_tag_end(source, start):
    """Return the first `>` outside an attribute quote, or -1."""
    quote = None
    for position in range(start, len(source)):
        character = source[position]
        if quote:
            if character == quote:
                quote = None
        elif character in "\"'":
            quote = character
        elif character == ">":
            return position
    return -1


def parse_tag(raw):
    """Parse only the tag name and attributes needed for the search index."""
    position = 0
    length = len(raw)
    while position < length and raw[position].isspace():
        position += 1

    if position == length or raw[position] in "!?":
        return None, {}, False, False

    closing = raw[position] == "/"
    if closing:
        position += 1
        while position < length and raw[position].isspace():
            position += 1

    name_start = position
    while position < length and not raw[position].isspace() and raw[position] not in "/=>":
        position += 1
    name = raw[name_start:position].lower()
    if not name:
        return None, {}, closing, False
    if closing:
        return name, {}, True, False

    attributes = {}
    while position < length:
        while position < length and raw[position].isspace():
            position += 1
        if position == length or raw[position] == "/":
            break

        attribute_start = position
        while (
            position < length
            and not raw[position].isspace()
            and raw[position] not in "=/"
        ):
            position += 1
        attribute_name = raw[attribute_start:position].lower()
        if not attribute_name:
            position += 1
            continue

        while position < length and raw[position].isspace():
            position += 1
        value = ""
        if position < length and raw[position] == "=":
            position += 1
            while position < length and raw[position].isspace():
                position += 1
            if position < length and raw[position] in "\"'":
                quote = raw[position]
                position += 1
                value_start = position
                while position < length and raw[position] != quote:
                    position += 1
                value = raw[value_start:position]
                if position < length:
                    position += 1
            else:
                value_start = position
                while position < length and not raw[position].isspace() and raw[position] != "/":
                    position += 1
                value = raw[value_start:position]
        attributes.setdefault(attribute_name, unescape(value))

    return name, attributes, False, raw.rstrip().endswith("/")


class SearchPageScanner:
    """Extract BookML's [URLs, title, body text] entry without a DOM."""

    def __init__(self):
        self.title_parts = []
        self.body_parts = []
        self.up_urls = []
        self.title_depth = 0
        self.body_depth = 0
        self.skip_depth = 0

    def add_text(self, text):
        if self.title_depth:
            self.title_parts.append(unescape(text))
        if self.body_depth and not self.skip_depth:
            self.body_parts.append(unescape(text))

    def start(self, tag, attributes):
        if tag == "link":
            rel = attributes.get("rel", "").lower().split()
            href = attributes.get("href")
            if href and "up" in rel:
                self.up_urls.append(href)

        if tag == "title":
            self.title_depth += 1
        elif tag == "body":
            self.body_depth += 1

        if tag in SKIPPED_ELEMENTS:
            self.skip_depth += 1

        if self.body_depth and not self.skip_depth:
            for attribute in ("alt", "alttext", "aria-label"):
                value = attributes.get(attribute)
                if value:
                    self.body_parts.append(" ")
                    self.body_parts.append(value)
                    self.body_parts.append(" ")
                    break

    def end(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        elif tag == "body" and self.body_depth:
            self.body_depth -= 1

        if tag in SKIPPED_ELEMENTS and self.skip_depth:
            self.skip_depth -= 1

    def feed(self, source):
        position = 0
        while position < len(source):
            opening = source.find("<", position)
            if opening < 0:
                self.add_text(source[position:])
                break
            if opening > position:
                self.add_text(source[position:opening])

            if source.startswith("<!--", opening):
                comment_end = source.find("-->", opening + 4)
                if comment_end < 0:
                    break
                position = comment_end + 3
                continue

            tag_end = find_tag_end(source, opening + 1)
            if tag_end < 0:
                self.add_text(source[opening:])
                break

            tag, attributes, closing, self_closing = parse_tag(
                source[opening + 1 : tag_end]
            )
            if tag:
                if closing:
                    self.end(tag)
                else:
                    self.start(tag, attributes)
                    if self_closing and tag not in VOID_ELEMENTS:
                        self.end(tag)
            position = tag_end + 1

    @staticmethod
    def normalize(parts):
        return " ".join("".join(parts).split())

    def result(self, filename):
        urls = list(reversed(self.up_urls))
        urls.append(filename)
        return [urls, self.normalize(self.title_parts), self.normalize(self.body_parts)]


def html_files(root):
    files = []
    for directory, directories, filenames in os.walk(root, followlinks=False):
        directories.sort()
        for filename in sorted(filenames):
            path = Path(directory) / filename
            if path.suffix.lower() == ".html" and path.is_file():
                files.append(path)
    return files


def build_index(html_directory):
    root = Path(html_directory)
    if not root.is_dir():
        raise ValueError(f"HTML directory does not exist: {root}")

    index = []
    for path in html_files(root):
        scanner = SearchPageScanner()
        scanner.feed(path.read_text(encoding="utf-8", errors="replace"))
        filename = path.relative_to(root).as_posix()
        index.append(scanner.result(filename))

    (root / "search_index.json").write_text(
        json.dumps(index, ensure_ascii=False), encoding="utf-8"
    )


def main(argv):
    if len(argv) != 2:
        raise SystemExit("usage: bookml-search-index.py HTML_DIRECTORY")
    build_index(argv[1])


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (OSError, ValueError) as error:
        raise SystemExit(str(error))
