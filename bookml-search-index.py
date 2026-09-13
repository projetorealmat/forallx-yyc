#!/usr/bin/env python3
"""Create the search index consumed by BookML's GitBook output.

The BookML container already provides Python 3, while its optional Perl XML
modules are not reliable for this generated HTML.  The standard-library HTML
parser is deliberately forgiving, which is useful for LaTeXML's output and
keeps this post-processing step deterministic.
"""

from html.parser import HTMLParser
import json
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


class SearchPageParser(HTMLParser):
    """Extract the same three fields as BookML's search indexer."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.body_parts = []
        self.up_urls = []
        self.title_depth = 0
        self.body_depth = 0
        self.skip_depth = 0
        self.open_elements = []

    @staticmethod
    def attributes(attrs):
        return {name.lower(): value for name, value in attrs if name}

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attributes = self.attributes(attrs)

        if tag == "link":
            rel = (attributes.get("rel") or "").lower().split()
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

        if tag not in VOID_ELEMENTS:
            self.open_elements.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()

        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        elif tag == "body" and self.body_depth:
            self.body_depth -= 1

        if tag in SKIPPED_ELEMENTS and self.skip_depth:
            self.skip_depth -= 1

        if tag in VOID_ELEMENTS:
            return

        # LaTeXML emits well-formed HTML, but matching backwards also lets the
        # indexer recover from a truncated page without getting stuck.
        for position in range(len(self.open_elements) - 1, -1, -1):
            if self.open_elements[position] == tag:
                del self.open_elements[position:]
                return

    def handle_data(self, data):
        if self.title_depth:
            self.title_parts.append(data)
        if self.body_depth and not self.skip_depth:
            self.body_parts.append(data)

    @staticmethod
    def normalize(parts):
        return " ".join("".join(parts).split())

    def result(self, filename):
        urls = list(reversed(self.up_urls))
        urls.append(filename)
        return [urls, self.normalize(self.title_parts), self.normalize(self.body_parts)]


def build_index(html_directory):
    root = Path(html_directory)
    if not root.is_dir():
        raise ValueError(f"HTML directory does not exist: {root}")

    index = []
    files = sorted(
        path for path in root.rglob("*") if path.is_file() and path.suffix.lower() == ".html"
    )
    for path in files:
        parser = SearchPageParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        parser.close()
        filename = path.relative_to(root).as_posix()
        index.append(parser.result(filename))

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
