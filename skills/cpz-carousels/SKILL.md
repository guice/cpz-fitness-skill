---
name: cpz-carousels
description: "CPZ Fitness Instagram carousel production. Use for end-to-end carousel creation: slide structure, per-slide copy, image generation prompts, and platform captions. The primary content format for this brand. Extends cpz-fitness root — load cpz-fitness first."
---

# CPZ Fitness — Content Carousels Skill

> Builds on **cpz-fitness** for brand DNA, voice, and ICA, and **cpz-design** for the full color/typography system. Load cpz-fitness first.

## Identity Quick Reference

| Field             | Value                                     |
|:------------------|:------------------------------------------|
| **Handle**        | @philipz.fit                              |
| **Booking CTA**   | https://lnk.philipz.fit/free-consult      |
| **PDF Asset CTA** | https://lnk.philipz.fit/pdf-consult       |
| **Tagline**       | "Lifting to be seen."                     |

## Reference Files

| File                                  | Load When                                                               |
|:--------------------------------------|:------------------------------------------------------------------------|
| `references/carousel-structure.md`    | Always — slide blueprints, design rules, CTA options, caption structure |
| `../cpz-design/references/design-guide.md` | When writing image generation prompts or specifying visual design — owned by cpz-design, not duplicated here |
| `references/html-rendering-spec.md`   | When building HTML carousel slides — exact pixel specs, components, colors |

---

## The 4 Carousel Types (Quick Reference)

| Type                    | Slides | Use When                                                      |
|:------------------------|:-------|:--------------------------------------------------------------|
| **Data / Myth Bust**    | 3–5    | Correcting a belief with data, presenting a surprising metric |
| **Micro-Workout**       | 4–6    | Delivering a complete, actionable workout routine             |
| **Nutrition / Protein** | 4–6    | Macro math, protein targets, debunking nutrition myths        |
| **Consistency / Habit** | 3–5    | Addressing the psychology and mechanics of showing up         |

Load `references/carousel-structure.md` for full slide-by-slide blueprints.

---

## CTA Slide Options

| CTA                                                                        | Best For                                |
|:---------------------------------------------------------------------------|:----------------------------------------|
| "Drop your biggest gym obstacle in the comments."                          | Consistency/habit carousels             |
| "Save this for your next training day."                                    | Workout carousels                       |
| "Follow @philipz.fit for more straightforward fitness breakdowns."         | Data/myth posts                         |
| "Free Consultation → link in bio" (`lnk.philipz.fit/free-consult`)        | Any carousel driving coaching inquiries |
| "Download the free PDF → link in bio" (`lnk.philipz.fit/pdf-consult`)     | Lead magnet / PDF download carousels    |

---

## Image Generation Prompt Framework

Every slide prompt should specify these 6 fields:

```
Background: #1c1a17 (cover/CTA) or #2c2925 (body slides)
Text: #f2ece2 (body) / #ff8c00 (key word or stat)
Typography: Schibsted Grotesk 700 for headlines (sentence case), Inter for body, Poppins for labels/data
Slide type: cover | data slide | workout slide | nutrition slide | CTA slide
Key text: [Headline] + [subtext if applicable]
Elements: [Section label text] + [ZF logo watermark: bottom-right 24–32px] + [any icons/visuals]
Bodies: real, varied gay male bodies — not exclusively stage-lean physiques (Content Safety Rules, cpz-fitness/SKILL.md)
```

---

## Production Workflow

Work through these steps in order for every carousel:

1. **Pillar** — Which of the 5 content pillars does this post belong to?
2. **Type** — Which carousel type matches the content?
3. **Slide count → Copy → Visual direction** — Run the **carousel-creator** skill. Pass the carousel type as tone context and supply the CPZ brand voice. See Skill Integration below for arc mapping and overrides.
4. **Image prompts** — One image generation prompt per slide using the framework above. CPZ design specs from `references/html-rendering-spec.md` override carousel-creator's generic DESIGN SPECS block.
5. **Captions** — Run the **caption-writer** skill for all 6 platforms: TikTok, Facebook, Instagram, Threads, BlueSky, LinkedIn. Deliver as a single multi-platform block. Goal and flavor are driven by carousel type — see Skill Integration below.

---

## Skill Integration

### carousel-creator

Invoke carousel-creator for slide count, outline, per-slide copy, and visual direction.

**CPZ overrides (these take precedence over carousel-creator defaults):**
- Slide count: **3–7** (not 8–10)
- Arc mapping by carousel type:

| CPZ Type | carousel-creator Arc |
|:---|:---|
| Data / Myth Bust | HPASCTA |
| Micro-Workout | LIST |
| Nutrition / Protein | LIST or HPASCTA |
| Consistency / Habit | HPASCTA or STORY |

- Design specs come from `references/html-rendering-spec.md` — ignore carousel-creator's generic DESIGN SPECS output
- Brand voice: Direct, with dry sarcasm on hooks. Orange on one word per slide. Max 30 words per internal slide.

### caption-writer

Invoke caption-writer for step 5. Generate captions for exactly these 6 platforms: **TikTok, Facebook, Instagram, Threads, BlueSky, LinkedIn**.

**Default flavor by carousel type:**

| CPZ Type | caption-writer Flavor |
|:---|:---|
| Data / Myth Bust | Value |
| Micro-Workout | Straight-CTA |
| Nutrition / Protein | Value |
| Consistency / Habit | Story |

**CPZ overrides:**
- Tone: Direct, with dry sarcasm on hooks — never motivational-poster voice
- Platform specs from `references/carousel-structure.md` (Caption Structure by Platform table) override caption-writer defaults
- BlueSky: hard 300-character limit — rewrite to fit, do not thread

---

## PNG Export Pipeline

After carousel copy and HTML are reviewed and approved, use the scripts in `scripts/` to render final PNGs.

**Requirements (one-time setup):**
```bash
pip install playwright
playwright install chromium
```

Fully dynamic — there's no pre-registered carousel list to edit. Write content as JSON and pass it directly.

**Step 1 — Write content** as a JSON file — either `{"meta": {...}, "slides": [...]}` for one carousel, or `{"id": {"meta":..., "slides":...}, ...}` for several. See `scripts/example_carousel.json` for a worked example and `scripts/template.py`'s module docstring for the full key reference.

**Step 2 — Generate HTML:**
```bash
cd scripts/
python generate.py my_carousel.json              # -> html/<id>.html
python generate.py a.json b.json --out /path/to/html/
```
Open the HTML files in a browser to review before exporting.

**Step 3 — Export PNGs (after approval):**
```bash
python export.py html/my_carousel.html           # one file
python export.py html/                           # every .html in a directory
```
PNGs are written to `scripts/output/<carousel_id>/slide_1.png`, `slide_2.png`, etc.
Output resolution: ~1080×1350px.

---

## Voice for Carousels

Carousels apply the Voice Pillars in a specific visual rhythm:

- **Slide copy = one claim + one proof.** Headline is the dry, sarcastic observation. Body is 1–2 lines max — the data or logic that backs it.
- **Cover slide:** Dry & Self-Aware leads — the hook must earn the swipe. Frame it as a bold, slightly provocative claim.
- **Body slides:** Direct & Confident drives — stats and specifics over vague assertions. If you can quantify it, quantify it.
- **CTA slide:** Clear & Actionable closes — one action, no options, no hedging.
- **No compound sentences in headlines.** One idea per slide, stated plainly.
- **Orange is reserved for the single most important word or number per slide** — not decoration.

---

## Quick Design Rules (Inline)

- **Padding:** 64px on all sides — dark background needs breathing room
- **Focal element:** One dominant element per slide. Never two competing focal points.
- **Orange:** One element per slide maximum — a key word, a stat, or the section label
- **Section label:** small-caps label text, Poppins Medium, top-left on body slides (orange on light, muted on dark)
- **Logo badge:** ZF mark in dark circle + `@philipz.fit` handle, top-left — on cover and light slides
- **Slide number watermark:** Oversized numeral (380px ⚠️, Schibsted Grotesk 700) in top-right at ~4% opacity
- **Light/dark alternation:** Slides alternate between `#1c1a17` (dark) and `#f5f3ef` (light) for rhythm
- **CTA slide:** Full orange gradient, centered layout, diagonal line texture, frosted glass card
- **Headlines:** 104px ⚠️ minimum on body slides — text dominates the slide
- **Text density:** Max 3–4 short lines of body copy per slide — split if more
- **Info card:** Orange left-border card for explanations — small-caps label + body text
- **Pill tags:** 14px radius, first pill orange-filled, rest outlined/muted — for muscle groups or key concepts

⚠️ = pixel size carried over from the retired Barlow Condensed spec, pending recalibration for Schibsted Grotesk — see `references/html-rendering-spec.md`.
