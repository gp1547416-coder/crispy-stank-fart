import tempfile
import unittest
from pathlib import Path

from catweb_generator import generate_project


class CatWebGeneratorTests(unittest.TestCase):
    def test_generate_project_creates_expected_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "my-catweb"
            generate_project(out, title="My Cat Site", heading="Hello Cat", overwrite=False)

            expected = ["README.md", "app.js", "index.html", "styles.css"]
            self.assertEqual(sorted(p.name for p in out.iterdir()), expected)
            self.assertIn("My Cat Site", (out / "index.html").read_text(encoding="utf-8"))
            self.assertIn("Hello Cat", (out / "index.html").read_text(encoding="utf-8"))

    def test_refuses_to_overwrite_without_flag(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "my-catweb"
            generate_project(out, title="Cat", heading="Cat", overwrite=False)

            with self.assertRaises(FileExistsError):
                generate_project(out, title="New", heading="New", overwrite=False)


if __name__ == "__main__":
    unittest.main()
