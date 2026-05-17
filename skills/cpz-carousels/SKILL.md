---
name: cpz-carousels
description: "CPZ Fitness Instagram carousel production. Use for end-to-end carousel creation: slide structure, per-slide copy, image generation prompts, and platform captions. The primary content format for this brand."
---

# CPZ Fitness — Content Carousels Skill

## Identity Quick Reference

| Field | Value |
| :--- | :--- |
| **Handle** | @philipz.fit |
| **Booking CTA** | https://lnk.philipz.fit/free-system-audit |
| **PDF Asset CTA** | https://lnk.philipz.fit/pdf-system-audit |
| **Tagline** | "From desk-bound to damn-strong." |

## Reference Files

| File | Load When |
| :--- | :--- |
| `references/carousel-structure.md` | Always — slide blueprints, design rules, CTA options, caption structure |
| `references/design-guide.md` | When writing image generation prompts or specifying visual design |

---

## The 4 Carousel Types (Quick Reference)

| Type | Slides | Use When |
| :--- | :--- | :--- |
| **Data / Myth Bust** | 3–5 | Correcting a belief with data, presenting a surprising metric |
| **Micro-Workout** | 4–6 | Delivering a complete, actionable workout routine |
| **Nutrition / Protein** | 4–6 | Macro math, protein targets, debunking nutrition myths |
| **Consistency / Habit** | 3–5 | Addressing the psychology and mechanics of showing up |

Load `references/carousel-structure.md` for full slide-by-slide blueprints.

---

## CTA Slide Options

| CTA | Best For |
| :--- | :--- |
| "Drop your biggest gym obstacle in the comments." | Consistency/habit carousels |
| "Save this for your next training day." | Workout carousels |
| "Follow @philipz.fit for more system-level fitness." | Data/myth posts |
| "Free System Audit → link in bio" (`lnk.philipz.fit/free-system-audit`) | Any carousel driving coaching inquiries |
| "Download the free PDF → link in bio" (`lnk.philipz.fit/pdf-system-audit`) | Lead magnet / PDF download carousels |

---

## Image Generation Prompt Framework

Every slide prompt should specify these 6 fields:

```
Background: #0f1012 (cover/CTA) or #1a1d21 (body slides)
Text: #f0ede8 (body) / #ff8c00 (key word or stat)
Typography: Barlow Condensed 800+ for headlines (uppercase), Space Grotesk for body, JetBrains Mono for labels/data
Slide type: cover | data slide | workout slide | nutrition slide | CTA slide
Key text: [Headline] + [subtext if applicable]
Elements: [Section label text] + [ZF logo watermark: bottom-right 24–32px] + [any icons/visuals]
```

---

## Production Workflow

Work through these steps in order for every carousel:

1. **Pillar** — Which of the 4 content pillars does this post belong to?
2. **Type** — Which carousel type matches the content?
3. **Slide count** — How many slides does the content need? (3–7 range)
4. **Outline** — Assign a purpose to each slide before writing copy
5. **Copy** — Write per-slide copy following the visual hierarchy from `carousel-structure.md`
6. **Image prompts** — One image generation prompt per slide using the framework above
7. **Caption** — Write the full caption using the platform caption structure from `carousel-structure.md`

---

## PNG Export Pipeline

After carousel copy and HTML are reviewed and approved, use the scripts in `scripts/` to render final PNGs.

**Requirements (one-time setup):**
```bash
pip install playwright
playwright install chromium
```

**Step 1 — Write content** in `scripts/carousels/round_N.py` using the Python dict structure (ask Claude to generate this)

**Step 2 — Generate HTML:**
```bash
cd scripts/
python generate.py                              # all carousels
python generate.py --round round_2              # one round only
python generate.py --carousel c07_workday_boundary  # one carousel by ID
```
Open the HTML files in a browser to review before exporting.

**Step 3 — Export PNGs (after approval):**
```bash
python export.py                                # all carousels
python export.py --carousel c07_workday_boundary  # one carousel by ID
```
PNGs are written to `scripts/output/<carousel_id>/slide_1.png`, `slide_2.png`, etc.
Output resolution: ~1080×1350px.

**Adding a new carousel:** Add a new key to the appropriate `carousels/round_N.py` file. See `scripts/README.md` for the full content dict structure.

---

## Quick Design Rules (Inline)

- **Padding:** 48–64px on all sides — dark background needs breathing room
- **Focal element:** One dominant element per slide. Never two competing focal points.
- **Orange:** One element per slide maximum — a key word, a stat, or the section label
- **Section label:** `— // slide.topic` in JetBrains Mono orange, top-left on body slides
- **Logo watermark:** ZF mark at 24–32px, bottom-right, `#ff8c00` — on cover and CTA minimum
- **Text density:** Max 3–4 short lines of body copy per slide — split if more
