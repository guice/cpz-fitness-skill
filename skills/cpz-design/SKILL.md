---
name: cpz-design
description: CPZ Fitness visual design system. Use for image generation prompts, carousel graphic specs, social media graphic design, Canva specs, or any visual output. Extends cpz-fitness root — load cpz-fitness first.
---

# CPZ Fitness — Brand Design Skill

## Visual Quick Reference

### Colors
| Role             | Name           | Hex                   |
|:-----------------|:---------------|:----------------------|
| Background       | Coco's Black   | `#191a1b`             |
| Surface          | Dark Surface   | `#22262b`             |
| Card             | Card Surface   | `#3c3f42`             |
| **Accent / CTA** | **CPZ Orange** | **`#ff8c00`**         |
| Text Primary     | Warm White     | `#f0ede8`             |
| Text Muted       | Slate Muted    | `#8a8f96`             |
| Code / Status    | Terminal Green | `#4ade80`             |
| Border           | Orange Border  | `rgba(255,130,0,0.2)` |

### Typography
| Font                 | Role                                            | Weights                            |
|:---------------------|:------------------------------------------------|:-----------------------------------|
| **League Spartan**   | logo wordmark only (not general use)            |                                    |
| **Barlow Condensed** | Headlines, CTAs, stats                          | 700 / 800 / 900 — always uppercase |
| **Space Grotesk**    | Body copy, descriptions                         | 400 / 500                          |
| **Space Grotesk**    | social media graphic body text only (carousels) | 400                                |
| **JetBrains Mono**   | Code, labels, data, section labels              | 400                                |

### Logo & Assets
- Logo file: `templates/cpz-logo.svg` (ZF vectorized mark — orange on transparent)
- Font files: `fonts/` directory
- Always use on dark backgrounds only

### Section Label Pattern (brand signature)
`— // section.name` — 2rem orange horizontal rule + JetBrains Mono label in `#ff8c00`, uppercase, 0.1em letter-spacing

### Aspect Ratios
| Platform                        | Ratio  | Pixels    |
|:--------------------------------|:-------|:----------|
| Instagram Feed                  | 4:5    | 1080×1350 |
| Instagram Stories / Reels cover | 9:16   | 1080×1920 |
| TikTok cover                    | 9:16   | 1080×1920 |
| LinkedIn post                   | 1.91:1 | 1200×628  |
| Twitter/X post                  | 16:9   | 1200×675  |
| Facebook post                   | 1.91:1 | 1200×628  |

### Print / Document Size
- Brand documents: **US Letter 8.5×11in / 816×1056px** (not A4)

## Reference File

| File                         | Load When                                                        |
|:-----------------------------|:-----------------------------------------------------------------|
| `references/design-guide.md` | Always — for any visual work requiring full design system detail |

## Visual Checklist

Before finalizing any graphic:

1. Background is `#191a1b` or `#1a1d21` (not a custom dark)
2. Orange (`#ff8c00`) appears on **one element only** per frame
3. Headlines use Barlow Condensed 700+ in **uppercase**
4. Body copy uses Space Grotesk
5. Code/system references use JetBrains Mono
6. ZF logo mark is present as watermark or identifier
7. No fourth typeface introduced
8. No rounded corners beyond 4px on cards
9. Padding 48–64px on social graphics
10. One focal element per slide — eye knows immediately where to look

## Image Generation Prompt Framework

When building prompts for carousel slides or social graphics, specify:
- **Background:** Coco's Black `#191a1b` or `#1a1d21`
- **Text:** Warm White `#f0ede8` for body; CPZ Orange `#ff8c00` for key stats/callouts
- **Typography feel:** Clean, sharp, minimal — no decorative flourishes
- **Slide type:** cover / data slide / action slide / CTA slide
- **Key text:** Headline + subtext if applicable
- **Elements:** Section label, logo watermark position, any icons

## Font Context Rules

| Font             | Use for                                                  | Never use for                      |
|:-----------------|:---------------------------------------------------------|:-----------------------------------|
| Barlow Condensed | All display text, headlines, CTAs, button labels, covers | Body paragraphs, long-form reading |
| Space Grotesk    | Website body, PDF paragraphs, email copy, slide body     | Carousel-only social graphics      |
| Open Sans        | Social carousel body text only (clean-bg slides)         | Website, PDF, print documents      |
| JetBrains Mono   | Code snippets, data labels, section IDs, stats           | Body copy, headlines               |
