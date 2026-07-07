---
name: cpz-design
description: CPZ Fitness visual design system. Use for image generation prompts, carousel graphic specs, social media graphic design, Canva specs, or any visual output. Extends cpz-fitness root — load cpz-fitness first.
---

# CPZ Fitness — Brand Design Skill

## Visual Quick Reference

### Colors
| Role             | Name           | Hex                   |
|:-----------------|:---------------|:----------------------|
| Background       | Coco's Black   | `#1c1a17`             |
| Card             | Card Surface   | `#2c2925`             |
| **Accent / CTA** | **CPZ Orange** | **`#ff8c00`**         |
| Text Primary     | Warm White     | `#f2ece2`             |
| Text Muted       | Warm Muted     | `#9b948a`              |
| Border           | Orange Border  | `rgba(255,140,0,0.2)` |

⚠️ "Terminal Green" (`#4ade80`) was retired as of the July 2026 Brand Guide v1 — see `references/design-guide.md` §2.1.

### Typography
| Font                    | Role                                        | Weights   |
|:------------------------|:---------------------------------------------|:----------|
| **Schibsted Grotesk**   | Headlines, display, section titles          | 600 / 700 |
| **Inter**               | Body copy, UI, buttons                      | 400 / 500 / 600 / 700 |
| **Poppins**             | Eyebrows, labels, data, tags                | 500 / 600 |
| **League Spartan**      | Logo wordmark only ("CPZ Fitness"), not general use | Variable |

⚠️ Font-asset action item: Schibsted Grotesk replaces Barlow Condensed as of the July 2026 Brand Guide v1, but the font files still need sourcing into `cpz-design/fonts/` and `cpz-carousels/fonts/` in a separate design-focused pass. League Spartan is unaffected and its font file is already present.

### Logo & Assets
- Logo file: `templates/cpz-logo.svg` (ZF lettermark — the Z of "CPZ" and F of "Fitness" combined into one glyph, orange on transparent; the icon-only shorthand for the full "CPZ Fitness" logo, which is set in League Spartan)
- Font files: `fonts/` directory
- Always use on dark backgrounds only

### Section Label Pattern (brand signature)
Poppins eyebrow label in `#ff8c00`, uppercase, 600 weight, 0.14–0.16em letter-spacing, placed directly above the headline — no rule line (e.g. `SECTION NAME`)

### Aspect Ratios
| Platform                        | Ratio  | Pixels    |
|:--------------------------------|:-------|:----------|
| Instagram Feed                  | 4:5    | 1080×1350 |
| Instagram Stories / Reels cover | 9:16   | 1080×1920 |
| TikTok cover                    | 9:16   | 1080×1920 |
| LinkedIn post                   | 1.91:1 | 1200×628  |
| Twitter/X post                  | 16:9   | 1200×675  |
| Facebook post                   | 1.91:1 | 1200×628  |

---

## PDF / Print Document Design System

### Page Fundamentals

| Property      | Value                                                      |
|:--------------|:-----------------------------------------------------------|
| Page size     | 816 × 1056px (US Letter)                                   |
| Page padding  | 52px all sides                                             |
| Body text min | 14px — never smaller for print                             |
| Print CSS fix | `height:1056px !important` + `min-height:unset` on `.page` |
| Border radius | 3px max on cards and containers                            |

### Page Types

| Type         | Background  | Top Border           | Use For                               |
|:-------------|:------------|:---------------------|:--------------------------------------|
| `light`      | `#ffffff`   | 5px solid `#ff8c00`  | Standard content pages                |
| `dark`       | `#0f1012`   | none                 | Timelines, section dividers, closer   |
| `photo-page` | `#0f1012`   | none, no padding     | Cover, full-bleed photo layouts       |

### Extended Color Palette (light pages)

Base tokens (surface/card/body/muted) are rebased onto the canonical Secondary/Light palette in `references/design-guide.md` §2.2. The rows below add print-only extras layered on top of that base.

| Role           | Hex                    |
|:---------------|:-----------------------|
| Light surface  | `#f5f3ef`              |
| Light card     | `#ffffff`              |
| Divider        | `#e2e5ea`              |
| Body text      | `#17181a`              |
| Muted text     | `#7a7f87`              |
| Orange tint bg | `#fff5e6`              |
| Orange border  | `rgba(255,140,0,0.35)` |
| Dark border    | `rgba(255,140,0,0.2)`  |

### Light Page Chrome
- Top: 5px solid orange border
- Corner brackets: 16×16px at top-right and bottom-left, `rgba(255,140,0,0.22)`, 2px stroke, via `::before` / `::after`
- Logo corner mark: top-right, 38px wide, opacity 0.12
- Footer: `margin-top:auto` to flush to bottom — always. Three-column: brand name · domain · page number in orange

### Type Scale

| Element    | Size    | Font              | Weight |
|:-----------|:--------|:------------------|:-------|
| `.h1`      | 72px+   | Schibsted Grotesk | 700    |
| `.h2`      | 44px    | Schibsted Grotesk | 700    |
| `.h3`      | 24px    | Schibsted Grotesk | 600    |
| `.h4`      | 15px    | Schibsted Grotesk | 600    |
| `.body`    | 14px    | Inter             | 400    |
| `.body.sm` | 12.5px  | Inter             | 400    |
| `.body.xs` | 11px    | Inter             | 400    |
| `.mono`    | 11px    | Poppins           | 400    |

### Card Types

| Class                    | Description                                                       |
|:-------------------------|:------------------------------------------------------------------|
| `.card`                  | `#f7f8fa` bg, 1px `#e2e5ea` border, 3px radius, 18px 20px padding |
| `.card.accent`           | Left border 3px `#ff8c00`, radius 0 3 3 0                         |
| `.card.callout`          | `#fff5e6` bg, orange border — used for tips and notes             |
| `.card.dark-card`        | `#2c2925` bg, dark border                                         |
| `.card.dark-card.accent` | Dark bg + left orange border                                      |

---

## PDF Cover Page Design

The cover is the most important page. It sets tone and expectation. Always treat it as a designed object, not just a title page.

### Cover Structure (photo-hybrid)
- **Full-bleed photo** behind everything — use a high-quality, relevant subject image
- **Gradient overlay** fading from near-transparent at top to solid dark (`#0f1012`) at the bottom ~75% mark — this preserves photo impact at top while creating a clean dark panel for text at the bottom
- **Gradient formula:** `linear-gradient(to bottom, rgba(10,10,12,0.18) 0%, rgba(10,10,12,0.45) 38%, rgba(10,10,12,0.88) 58%, #0f1012 76%)`
- **Logo** top-left, 52px, full colour
- **Document tag** top-right, Poppins, muted warm white, small
- **Title block** bottom-left area: mono section label above, Schibsted Grotesk H1 in white + H1 in orange below it, 64px orange rule separator, short descriptor paragraph in `rgba(240,237,232,0.72)`
- **Identity strip** at very bottom: name + handle left, "Prepared by" right, separated by a faint orange border-top

### Cover Photo Selection
- Choose imagery that relates directly to the document subject (food for nutrition docs, athlete for training docs, lifestyle/confidence imagery for identity-focused content)
- Portrait or square crops work better than landscape — the gradient needs vertical space to work
- Subject should have weight in the upper portion of the frame so it's visible above the gradient transition
- Avoid busy, high-contrast images — the overlay needs to blend smoothly

---

## Image Strategy for Content Pages

Photography and imagery should be used intentionally throughout a PDF — not on every page, but enough to break visual monotony and give the document a produced, premium feel.

### The Four Image Treatments

**1. Top Photo Band**
Full-width photo band bleeding edge-to-edge at the top of a light page, 180–230px tall. A bottom-fade gradient (`linear-gradient(to bottom, rgba(15,16,18,0.2) 0%, rgba(255,255,255,0.97) 88%)`) dissolves it into the white page. Section label overlaid at the bottom of the band. Use on pages that open a major new section — it signals a shift in topic.

**2. Side Column Photo**
A vertical photo occupying one column of a two-column grid layout, typically 240–285px wide. Used alongside text content. Gives the page a magazine-editorial quality. Always pair with a callout card below the photo in the same column to fill the space and add value. Height should be fixed in px (not `height:100%`) for cross-browser rendering.

**3. Card-Top Photo**
Small photos (130–160px tall) sitting above a content card, forming a single unit. Image on top, card text below, together inside a bordered container with `overflow:hidden`. Used for metric grids, feature lists, or tip collections where each item benefits from a visual anchor. Label the image with a gradient overlay + Schibsted Grotesk text at the bottom of the photo.

**4. Dark Split Layout (photo left / content right)**
A full-height photo occupying a fixed-width left column (220–230px), with content in the right panel on a dark background. The photo bleeds top to bottom. A right-edge fade gradient on the photo column creates a seamless transition into the dark content panel. Use for high-impact section pages — timelines, phase breakdowns, key concepts. Vertical ghost text (large Schibsted Grotesk, rotated -90°, `rgba(255,255,255,0.16)`, `bottom:175px`) labels the page content within the photo column.

### Photo Usage Rules
- **Data/diagram pages** — no photos. Let the diagram breathe. Faint radial gradient wash as background texture is sufficient.
- **Info/content pages** — at least one photo treatment per page to build visual interest.
- **Closer/CTA pages** — no photos. Dark background, logo, type, and stats only.
- **Maximum one full-bleed photo per page** — never two competing full-width images on the same page.
- Photos should always have a gradient overlay when text is placed over or near them.
- Never use `height:100%` on `<img>` tags inside flex or grid containers — Safari/WebKit and macOS PDF export will not resolve the height. Always use explicit pixel values.

### Gradient Overlay Formulas
| Use Case                       | Formula                                                                                    |
|:-------------------------------|:-------------------------------------------------------------------------------------------|
| Photo band → white page        | `linear-gradient(to bottom, rgba(15,16,18,0.2) 0%, rgba(255,255,255,0.97) 88%)`            |
| Card-top photo label           | `linear-gradient(to top, rgba(15,16,18,0.72) 0%, transparent 55%)`                         |
| Dark split photo → dark panel  | `linear-gradient(to right, rgba(15,16,18,0.1) 0%, rgba(15,16,18,0.6) 100%)`                |
| Cover full-bleed → dark bottom | `linear-gradient(to bottom, rgba(10,10,12,0.18) 0%, rgba(10,10,12,0.88) 58%, #0f1012 76%)` |

### Image Sources
- Unsplash embed URLs are acceptable for draft/review builds: `https://images.unsplash.com/photo-{id}?w=1200&q=80&fit=crop`
- Production PDFs should use owned or licensed photography where possible
- For cross-browser and PDF export compatibility, always test in Brave/Chrome for PDF output — Safari preview may show images that don't export

---

## Logo Usage in PDF

- **URL:** `https://res.cloudinary.com/dzjucinkn/image/upload/q_auto/f_auto/v1776803729/zf-logo_erjtr7.svg`
- Always reference via `<img src="...">` — never inline or re-encode the SVG in a PDF document
- Do not attempt to reconstruct the logo from path data — use the Cloudinary URL

| Context          | Size   | Opacity | Notes                          |
|:-----------------|:-------|:--------|:-------------------------------|
| Cover top-left   | 52px   | 100%    | Full colour on dark background |
| Page corner mark | 38px   | 0.12    | Watermark on light pages       |
| Closer/end page  | 100px  | 100%    | Centred, full colour on dark   |
| Page watermark   | 560px  | 0.05    | Final page only                |

---

## PDF Print Checklist

Before exporting any PDF document:

1. Footer has `margin-top:auto` — always aligns to bottom of page 
2. All photos tested in Brave/Chrome before PDF export 
3. Logo referenced via Cloudinary URL `<img>` — not inline SVG
4. Body text minimum 14px — nothing smaller in the main content
5. Section label present on every content page

---

### CTA Link Standard (PDF documents)
- **PDF lead magnets:** `https://lnk.philipz.fit/pdf-system-audit`
- **Workshop/audit booking:** `https://lnk.philipz.fit/free-system-audit`
- Always wrap in `<a href="..." target="_blank">` — never a plain `<div>`
- Style: `background: rgba(255,140,0,0.12)` pill, `border: 1px solid rgba(255,140,0,0.2)`, Poppins 13px

### CTA Page
Always include two versions of the final page:
* One for a lead magnet, intended for COLD traffic, with a ⚠️ CTA to book a call (label pending decision, was "free system audit") with a QR code (see [pdf-link-qr-code.svg](references/pdf-link-qr-code.svg))
* One that does NOT use the CTA or QR Code intended for existing clients.

### Call Duration Standard
- ⚠️ Consult call (label pending decision, was "Free System Audit") = **15 minutes**

---

## Reference File

| File                              | Load When                                                        |
|:----------------------------------|:-----------------------------------------------------------------|
| `references/design-guide.md`      | Always — for any visual work requiring full design system detail |
| `references/pdf-link-qr-code.svg` | Lead Magnet QR Code, unless otherwise stated                     |

## Visual Checklist

Before finalizing any graphic:

1. Background is `#1c1a17` or `#2c2925` (not a custom dark)
2. Orange (`#ff8c00`) appears on **one element only** per frame
3. Headlines use Schibsted Grotesk 700, sentence case
4. Body copy uses Inter
5. Labels/data callouts use Poppins
6. ZF logo mark is present as watermark or identifier
7. No fourth typeface introduced
8. Buttons use 14px radius; status pills/tags may be fully rounded (~20px); structural cards stay at 4px
9. Padding 48–64px on social graphics
10. One focal element per slide — eye knows immediately where to look

## Image Generation Prompt Framework

When building prompts for carousel slides or social graphics, specify:
- **Background:** Coco's Black `#1c1a17` or `#2c2925`
- **Text:** Warm White `#f2ece2` for body; CPZ Orange `#ff8c00` for key stats/callouts
- **Typography feel:** Clean, sharp, minimal — no decorative flourishes
- **Slide type:** cover / data slide / action slide / CTA slide
- **Key text:** Headline + subtext if applicable
- **Elements:** Section label, logo watermark position, any icons
- **Bodies shown:** Default to real, varied gay male bodies — not exclusively stage-lean physiques (Content Safety Rules, `cpz-fitness/SKILL.md`)
