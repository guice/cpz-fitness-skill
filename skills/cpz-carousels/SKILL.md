---
name: cpz-carousels
description: "CPZ Fitness Instagram carousel production. Use for end-to-end carousel creation: slide structure, per-slide copy, image generation prompts, and platform captions. The primary content format for this brand. Extends cpz-fitness root — load cpz-fitness first."
---

# CPZ Fitness — Content Carousels Skill

> Builds on **cpz-fitness** for brand DNA, voice, ICA, and colors. Load cpz-fitness first.

## Identity Quick Reference

| Field             | Value                                     |
|:------------------|:------------------------------------------|
| **Handle**        | @philipz.fit                              |
| **Booking CTA**   | https://lnk.philipz.fit/free-system-audit |
| **PDF Asset CTA** | https://lnk.philipz.fit/pdf-system-audit  |
| **Tagline**       | "From desk-bound to damn-strong."         |

## Reference Files

| File                                  | Load When                                                               |
|:--------------------------------------|:------------------------------------------------------------------------|
| `references/carousel-structure.md`    | Always — slide blueprints, design rules, CTA options, caption structure |
| `references/design-guide.md`          | When writing image generation prompts or specifying visual design       |
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
| "Follow @philipz.fit for more system-level fitness."                       | Data/myth posts                         |
| "Free System Audit → link in bio" (`lnk.philipz.fit/free-system-audit`)    | Any carousel driving coaching inquiries |
| "Download the free PDF → link in bio" (`lnk.philipz.fit/pdf-system-audit`) | Lead magnet / PDF download carousels    |

---

## Image Generation Prompt Framework

Every slide prompt should specify these 6 fields:

```
Background: #191a1b (cover/CTA) or #1a1d21 (body slides)
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
3. **Slide count → Copy → Visual direction** — Run the **carousel-creator** skill. Pass the carousel type as tone context and supply the CPZ brand voice. See Skill Integration below for arc mapping and overrides.
4. **Image prompts** — One image generation prompt per slide using the framework above. CPZ design specs from `references/html-rendering-spec.md` override carousel-creator's generic DESIGN SPECS block.
5. **Captions** — Run the **caption-writer** skill for all 5 platforms: TikTok, Facebook, Instagram, Threads, BlueSky. Deliver as a single multi-platform block. Goal and flavor are driven by carousel type — see Skill Integration below.

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
- Brand voice: Analytical with sarcasm on hooks. Orange on one word per slide. Max 30 words per internal slide.

### caption-writer

Invoke caption-writer for step 5. Generate captions for exactly these 5 platforms: **TikTok, Facebook, Instagram, Threads, BlueSky**.

**Default flavor by carousel type:**

| CPZ Type | caption-writer Flavor |
|:---|:---|
| Data / Myth Bust | Value |
| Micro-Workout | Straight-CTA |
| Nutrition / Protein | Value |
| Consistency / Habit | Story |

**CPZ overrides:**
- Tone: Analytical with sarcasm on hooks — never motivational-poster voice
- Platform specs from `references/carousel-structure.md` (Caption Structure by Platform table) override caption-writer defaults
- BlueSky: hard 300-character limit — rewrite to fit, do not thread
- No LinkedIn output

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

## Voice for Carousels

Carousels apply the 4 Voice Pillars in a specific visual rhythm:

- **Slide copy = one claim + one proof.** Headline is the sarcastic or analytical observation. Body is 1–2 lines max — the data or logical proof that backs it.
- **Cover slide:** Pillar 1 (Sarcastic/Humorous) leads — the hook must earn the swipe. Frame it as a bold, slightly provocative claim.
- **Body slides:** Pillar 2 (Analytical) drives — stats and data over assertions. If you can quantify it, quantify it.
- **CTA slide:** Pillar 4 (Direct) closes — one action, no options, no hedging.
- **No compound sentences in headlines.** One idea per slide, stated plainly.
- **Orange is reserved for the single most important word or number per slide** — not decoration.

---

## Quick Design Rules (Inline)

- **Padding:** 64px on all sides — dark background needs breathing room
- **Focal element:** One dominant element per slide. Never two competing focal points.
- **Orange:** One element per slide maximum — a key word, a stat, or the section label
- **Section label:** `— // slide.topic` in JetBrains Mono, top-left on body slides (orange on light, muted on dark)
- **Logo badge:** ZF mark in dark circle + `@philipz.fit` handle, top-left — on cover and light slides
- **Slide number watermark:** Oversized numeral (380px, Barlow 900) in top-right at ~4% opacity
- **Light/dark alternation:** Slides alternate between `#191a1b` (dark) and `#f5f2ed` (light) for rhythm
- **CTA slide:** Full orange gradient, centered layout, diagonal line texture, frosted glass card
- **Headlines:** 104px minimum on body slides — text dominates the slide
- **Text density:** Max 3–4 short lines of body copy per slide — split if more
- **Info card:** Orange left-border card for explanations — `// LABEL` + body text
- **Pill tags:** First pill orange-filled, rest outlined/muted — for muscle groups or key concepts
