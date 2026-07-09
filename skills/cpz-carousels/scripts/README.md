# Carousel PNG Export Pipeline

Generates self-contained HTML carousel files and exports each slide to PNG using headless Chromium.

Fully dynamic — there is no pre-registered carousel list to edit. Content is authored as JSON at runtime (by hand, or by an autonomous agent) and passed directly to `generate.py`.

## Requirements

```bash
pip install playwright
playwright install chromium
```

## Workflow

### Step 1 — Write carousel content as JSON

See `example_carousel.json` for a worked example, and `template.py`'s module docstring for the full slide/meta key reference (fonts, colors, and components are already handled — you're just supplying content).

JSON shape — either a single carousel:
```json
{"meta": {...}, "slides": [...]}
```
or multiple carousels keyed by id:
```json
{"carousel_id_1": {"meta": {...}, "slides": [...]}, "carousel_id_2": {...}}
```

Ask Claude to write the carousel content in this format using the `cpz-carousels` skill.

### Step 2 — Generate HTML

```bash
# One file (single or multi-carousel JSON)
python generate.py my_carousel.json

# Multiple JSON files at once
python generate.py carousel_a.json carousel_b.json

# Custom output directory (default: html/)
python generate.py my_carousel.json --out /path/to/html/
```

HTML files are written one per carousel, named `<id>.html`. Open in a browser to review.

### Step 3 — Review and approve

Open the generated HTML in a browser. Swipe through the slides. Approve before exporting.

### Step 4 — Export to PNG

```bash
# A single HTML file
python export.py html/my_carousel.html

# Multiple files
python export.py html/carousel_a.html html/carousel_b.html

# Every HTML file in a directory
python export.py html/

# Custom output directory (default: output/)
python export.py html/ --out /path/to/output/
```

PNGs are written to `output/<carousel_id>/slide_1.png`, `slide_2.png`, etc.
Output resolution: ~1080×1350px (420×525 viewport at 2.57× device scale).

## File Map

| File | Purpose |
|---|---|
| `generate.py` | Builds HTML from a JSON content spec — takes direct file path(s) |
| `export.py` | Renders HTML → PNG via Playwright — takes direct file/directory path(s) |
| `template.py` | HTML/CSS template engine — rebuilt against `html-rendering-spec.md`; update it when the design system changes, don't let it drift stale again |
| `fonts_b64.py` | Base64-encoded font data, generated from the real files in `cpz-carousels/fonts/` — regenerate (don't hand-edit the blobs) if those font files change |
| `example_carousel.json` | Worked example of the content JSON schema |
| `html/` | Generated HTML files (gitignored) |
| `output/` | Exported PNG files (gitignored) |
