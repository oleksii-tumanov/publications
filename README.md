# publications

Static publications site for Oleksii Tumanov.

## Files

- `build_site.py` - generates the static site from one metadata list
- `index.html` - publications landing page
- `*.html` - individual publication pages with citation metadata
- `sitemap.xml` - sitemap for indexing
- `robots.txt` - crawler instructions

## Publishing

This repo is intended for GitHub Pages style static hosting.

## Updating

Run:

```bash
python3 build_site.py
```

Then commit and push the generated files.
