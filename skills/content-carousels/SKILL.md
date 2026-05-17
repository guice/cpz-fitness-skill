---
name: content-carousels
description: CPZ Fitness Instagram carousel production. Use for end-to-end carousel creation: slide structure, per-slide copy, image generation prompts, and platform captions. The primary content format for this brand.
---

# CPZ Fitness — Content Carousels Skill

## Identity Quick Reference

| Field | Value |
| :--- | :--- |
| **Handle** | @philipz.fit |
| **Booking CTA** | https://im.philipz.fit/free-debug-session |
| **Free System Audit CTA** | https://lnk.philipz.fit/free-system-audit |
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
| "Book a Free System Audit → link in bio" | Any carousel driving conversions |

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

## Quick Design Rules (Inline)

- **Padding:** 48–64px on all sides — dark background needs breathing room
- **Focal element:** One dominant element per slide. Never two competing focal points.
- **Orange:** One element per slide maximum — a key word, a stat, or the section label
- **Section label:** `— // slide.topic` in JetBrains Mono orange, top-left on body slides
- **Logo watermark:** ZF mark at 24–32px, bottom-right, `#ff8c00` — on cover and CTA minimum
- **Text density:** Max 3–4 short lines of body copy per slide — split if more
