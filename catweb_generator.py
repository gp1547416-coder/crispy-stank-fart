#!/usr/bin/env python3
"""CatWeb code generator.

Generates a tiny CatWeb starter project with HTML/CSS/JS files.
"""

from __future__ import annotations

import argparse
from pathlib import Path

INDEX_TEMPLATE = """<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{title}</title>
    <link rel=\"stylesheet\" href=\"styles.css\" />
  </head>
  <body>
    <main class=\"container\">
      <h1>{heading}</h1>
      <p>Welcome to your CatWeb app. Click for a random cat fact.</p>
      <button id=\"factButton\">New Cat Fact</button>
      <blockquote id=\"fact\" class=\"fact\">Cats sleep 12–16 hours a day.</blockquote>
    </main>
    <script src=\"app.js\"></script>
  </body>
</html>
"""

CSS_TEMPLATE = """* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  background: linear-gradient(160deg, #f8fafc 0%, #e2e8f0 100%);
  color: #0f172a;
}

.container {
  max-width: 680px;
  margin: 15vh auto;
  padding: 2rem;
  border-radius: 1rem;
  background: white;
  box-shadow: 0 20px 50px rgba(15, 23, 42, 0.12);
}

button {
  border: none;
  border-radius: 0.7rem;
  padding: 0.7rem 1rem;
  background: #2563eb;
  color: white;
  font-size: 1rem;
  cursor: pointer;
}

button:hover {
  background: #1d4ed8;
}

.fact {
  margin-top: 1rem;
  padding-left: 1rem;
  border-left: 4px solid #2563eb;
}
"""

JS_TEMPLATE = """const facts = [
  \"A group of cats is called a clowder.\",
  \"Cats can rotate their ears 180 degrees.\",
  \"The oldest known pet cat existed 9,500 years ago.\",
  \"A cat's purr can have calming effects on humans.\",
  \"Cats have whiskers on the backs of their front legs too.\",
];

const button = document.getElementById(\"factButton\");
const fact = document.getElementById(\"fact\");

button.addEventListener(\"click\", () => {
  const index = Math.floor(Math.random() * facts.length);
  fact.textContent = facts[index];
});
"""

README_TEMPLATE = """# {title}

Generated with **catweb_generator.py**.

## Files

- `index.html` - App markup
- `styles.css` - App styles
- `app.js` - Cat fact behavior

## Run

Open `index.html` directly in your browser.
"""


def write_file(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def generate_project(output_dir: Path, title: str, heading: str, overwrite: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "index.html": INDEX_TEMPLATE.format(title=title, heading=heading),
        "styles.css": CSS_TEMPLATE,
        "app.js": JS_TEMPLATE,
        "README.md": README_TEMPLATE.format(title=title),
    }

    for filename, content in files.items():
        write_file(output_dir / filename, content, overwrite)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a CatWeb starter project.")
    parser.add_argument("name", help="Directory name for the generated project")
    parser.add_argument("--title", default="CatWeb App", help="HTML title and README title")
    parser.add_argument("--heading", default="🐱 CatWeb", help="Main heading shown on the page")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.name)
    generate_project(output_dir, args.title, args.heading, args.overwrite)
    print(f"Generated CatWeb project in: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
