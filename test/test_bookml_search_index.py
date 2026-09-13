import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
INDEXER = REPOSITORY / "bookml-search-index.py"


class BookMLSearchIndexerTests(unittest.TestCase):
    def run_indexer(self, root):
        return subprocess.run(
            [sys.executable, str(INDEXER), str(root)],
            cwd=REPOSITORY,
            capture_output=True,
            text=True,
            timeout=5,
        )

    def test_indexes_bookml_html_without_external_xml_dependencies(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "index.html").write_text(
                """<!doctype html>
<html><head><title>Livro traduzido</title>
<link rel="up" href="Ptx1.html"><link rel="up" href="Ch1.html">
</head><body>
<nav>Menu que não deve ser indexado</nav>
<main><h1>Capítulo</h1><p>Texto pesquisável.</p>
<img alt="Descrição da figura"></main>
<script>texto que não deve ser indexado</script>
<style>texto que não deve ser indexado</style>
</body></html>""",
                encoding="utf-8",
            )
            (root / "broken.html").write_text(
                "<html><head><title>HTML incompleto</title></head><body><p>Fim",
                encoding="utf-8",
            )

            result = self.run_indexer(root)

            self.assertEqual(result.returncode, 0, result.stderr)
            index = json.loads((root / "search_index.json").read_text(encoding="utf-8"))
            self.assertEqual(len(index), 2)

            indexed_page = next(entry for entry in index if entry[0][-1] == "index.html")
            self.assertEqual(indexed_page[0], ["Ch1.html", "Ptx1.html", "index.html"])
            self.assertEqual(indexed_page[1], "Livro traduzido")
            self.assertIn("Texto pesquisável.", indexed_page[2])
            self.assertIn("Descrição da figura", indexed_page[2])
            self.assertNotIn("Menu que não deve ser indexado", indexed_page[2])
            self.assertNotIn("texto que não deve ser indexado", indexed_page[2])


if __name__ == "__main__":
    unittest.main()
