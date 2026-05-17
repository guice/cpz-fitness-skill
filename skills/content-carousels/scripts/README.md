# Carousel PNG Export Pipeline

Generates self-contained HTML carousel files and exports each slide to PNG using headless Chromium.

## Requirements

```bash
pip install playwright
playwright install chromium
```

## Workflow

### Step 1 — Write or update carousel content

Carousel content lives in `carousels/`:
- `round_1.py` — Hook carousels (awareness, problem framing)
- `round_2.py` — Systems carousels (solution framework, builds trust)
- `round_3.py` — Offer carousels (objection handling, earns the DM)

Each file defines a `CAROUSELS` dict. Each carousel is a key → dict with `meta` and `slides`. Ask Claude to write new carousel content in this format using the `content-carousels` skill.

### Step 2 — Generate HTML

```bash
# All carousels
python generate.py

# One round only
python generate.py --round round_2

# Specific carousel(s) by ID
python generate.py --carousel c07_workday_boundary
```

HTML files are written to `html/`. Open in a browser to review.

### Step 3 — Review and approve

Open each `html/<carousel_id>.html` in a browser. Swipe through the slides. Approve before exporting.

### Step 4 — Export to PNG

```bash
# All approved carousels
python export.py

# Specific carousel(s) only
python export.py --carousel c07_workday_boundary c09_hardware

# Custom HTML directory
python export.py --html-dir /path/to/html/
```

PNGs are written to `output/<carousel_id>/slide_1.png`, `slide_2.png`, etc.
Output resolution: ~1080×1350px (420×525 viewport at 2.57× device scale).

## Adding a New Carousel

1. Open the appropriate round file in `carousels/` (or create a new one)
2. Add a new key to the `CAROUSELS` dict following the existing structure
3. If creating a new round file:
   - Name it `round_N.py`
   - Add it to `ALL_ROUNDS` in `generate.py`
4. Run `python generate.py --carousel <new_carousel_id>` to preview

## File Map

| File | Purpose |
|---|---|
| `generate.py` | Builds HTML from content dicts |
| `export.py` | Renders HTML → PNG via Playwright |
| `template.py` | HTML/CSS template engine (do not edit) |
| `fonts_b64.py` | Base64-encoded font data (do not edit) |
| `carousels/round_1.py` | Hook carousels (c3, c5, c6) |
| `carousels/round_2.py` | Systems carousels (c07–c12) |
| `carousels/round_3.py` | Offer carousels (c13–c18) |
| `html/` | Generated HTML files (gitignored) |
| `output/` | Exported PNG files (gitignored) |
