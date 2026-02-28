# CatWeb Code Generator

`catweb_generator.py` generates a tiny CatWeb starter project (HTML/CSS/JS).

This repository now also includes a root `index.html`, `styles.css`, and `app.js` so platforms like Vercel can serve a page immediately instead of returning `404: NOT_FOUND`.

## Usage

```bash
python3 catweb_generator.py my-catweb
```

Optional flags:

- `--title "My CatWeb"`
- `--heading "Welcome"`
- `--overwrite`

## View in Microsoft Edge (no install)

- Open the repository on GitHub in Edge and click files directly to read code.
- For an in-browser editor, open `https://github.dev/<owner>/<repo>` in Edge (or press `.` on GitHub).
- To preview generated static files online, publish them with GitHub Pages and open the page URL in Edge.

## Vercel deploy note

If you deploy this repository directly to Vercel, it will now serve the root `index.html`.
If you want your generated site instead, deploy the generated folder contents (`index.html`, `styles.css`, `app.js`, `README.md`).

## Vercel routing fix for repeated URL paths

If someone opens a malformed URL like `/https://crispy-stank-fart.vercel.app/...`, Vercel can return 404 by default.
This repo includes `vercel.json` with a catch-all rewrite so any path resolves to `/index.html`.

## Test

```bash
python3 -m unittest discover -s tests
```
