# CPZ Fitness — HTML Carousel Rendering Specification

This document defines the exact visual patterns for rendering carousel slides as 1080×1350px HTML panels. It codifies the approved design language derived from production slides.

---

## Slide Canvas

| Property | Value |
|:---------|:------|
| Width | 1080px |
| Height | 1350px |
| Padding | 64px all sides |
| Overflow | hidden |
| Position | relative |

---

## Background Modes

Slides alternate between three background modes for visual rhythm. The standard pattern is: **Cover (dark) → Light → Dark → Light → Dark → CTA (orange gradient)**.

| Mode | Background | Text Color | Accent |
|:-----|:-----------|:-----------|:-------|
| **Dark** | `#191a1b` | `#f0ede8` | `#ff8c00` |
| **Surface** | `#1a1d21` | `#f0ede8` | `#ff8c00` |
| **Light** | `#f5f2ed` | `#191a1b` | `#ff8c00` |
| **CTA Gradient** | `linear-gradient(155deg, #cc7000 0%, #ff8c00 50%, #ffaa33 100%)` | `#ffffff` | N/A |

---

## Slide Number Watermark

A massive oversized numeral positioned in the top-right corner as a background texture element.

| Property | Value |
|:---------|:------|
| Font | Barlow Condensed 900 |
| Size | 380px |
| Position | `top: -40px; right: -30px` |
| Color (dark) | `rgba(255,255,255,0.04)` |
| Color (light) | `rgba(0,0,0,0.05)` |
| Color (CTA) | `rgba(255,255,255,0.1)` |
| z-index | 1 (behind content) |
| Clipping | Partially off right edge |

---

## Logo Badge

Positioned top-left on cover slides and light slides. Contains the ZF mark inside a dark circle with the handle text beside it.

| Property | Value |
|:---------|:------|
| Position | `top: 48px; left: 64px` |
| Circle diameter | 72px |
| Circle background | `#2a2a2a` (dark on light: `#333`) |
| Logo size inside | 40×34px |
| Handle font | Inter 500, 28px |
| Handle color (dark) | `#8a8f96` |
| Handle color (light) | `#555` |

---

## Typography Scale (Carousel-Specific)

Headlines are significantly larger than web usage to command attention at mobile scale.

| Element | Font | Size | Weight | Transform |
|:--------|:-----|:-----|:-------|:----------|
| Headline (body slides) | Barlow Condensed | 104px | 900 | Uppercase |
| Headline (CTA slide) | Barlow Condensed | 100–120px | 900 | Uppercase |
| Section label | Poppins | 28px | 400 | Uppercase, 0.12em tracking |
| Sub-label (category) | Barlow Condensed | 32px | 700 | Uppercase, 0.08em tracking |
| Body copy | Inter | 36px | 400 | None |
| Info card label | Poppins | 22px | 500 | Uppercase, 0.1em tracking |
| Info card body | Inter | 32px | 400 | None |
| Pill tag | Poppins | 24px | 400 | None |

---

## Section Label Pattern

A small-caps label (e.g. `TOPIC NAME`) appears on every body slide.

| Context | Color |
|:--------|:------|
| Dark slides | `#8a8f96` (muted) |
| Light slides | `#ff8c00` (orange) |

---

## Sub-Label

An optional secondary label below the section label (e.g., exercise name, category). Always in orange (`#ff8c00`), Barlow Condensed 700, uppercase.

---

## Info Card Component

A bordered card containing a label and body text. Used for explanations, "what it fixes" blocks, and implementation details.

| Property | Dark Slides | Light Slides |
|:---------|:------------|:-------------|
| Background | `rgba(255,140,0,0.04)` | `rgba(0,0,0,0.03)` |
| Border | `1px solid rgba(255,140,0,0.25)` | `1px solid rgba(0,0,0,0.08)` |
| Left border | `4px solid #ff8c00` | `4px solid #ff8c00` |
| Border radius | 8px | 8px |
| Padding | 32px 36px | 32px 36px |
| Label color | `#ff8c00` | `#ff8c00` |
| Body color | `#c8c5c0` | `#444` |

---

## Data Card Component

For presenting numerical data (calorie math, stats, comparisons).

| Property | Value |
|:---------|:------|
| Background | `#22262b` |
| Border | `1px solid rgba(255,140,0,0.2)` |
| Border radius | 8px |
| Padding | 36px |
| Row separator | `1px solid rgba(255,255,255,0.06)` |
| Label font | Poppins 26px, `#8a8f96` |
| Value font | Barlow Condensed 800, 34px |
| Positive value | `#4ade80` |
| Negative value | `#ff4444` |
| Accent value | `#ff8c00` |

---

## Pill Tags

A row of tags at the bottom of body slides indicating muscle groups, time commitments, or key concepts.

| Property | Primary Pill | Muted Pill |
|:---------|:-------------|:-----------|
| Background | `#ff8c00` | transparent |
| Text color | `#191a1b` | `#8a8f96` (dark) / `#666` (light) |
| Border | none | `1px solid rgba(255,255,255,0.2)` (dark) / `rgba(0,0,0,0.15)` (light) |
| Border radius | 6px | 6px |
| Padding | 10px 20px | 10px 20px |
| Font | Poppins 24px | Poppins 24px |

The first pill is always primary (orange-filled). Subsequent pills are muted (outlined).

---

## Progress Bar

Present on every slide at the absolute bottom.

| Property | Value |
|:---------|:------|
| Position | `absolute; bottom: 0; left: 0; right: 0` |
| Padding | `16px 28px 24px` |
| Track height | 4px |
| Track radius | 2px |
| Fill width | `((slideIndex + 1) / totalSlides) * 100%` |

| Context | Track Color | Fill Color | Label Color |
|:--------|:------------|:-----------|:------------|
| Dark | `rgba(255,255,255,0.1)` | `#ffffff` | `rgba(255,255,255,0.4)` |
| Light | `rgba(0,0,0,0.1)` | `#ff8c00` | `rgba(0,0,0,0.3)` |
| CTA | `rgba(255,255,255,0.3)` | `#ffffff` | `rgba(255,255,255,0.6)` |

Label format: `{current}/{total}` in Poppins 24px weight 500.

---

## Swipe Arrow

Present on every slide except the final CTA slide.

| Property | Value |
|:---------|:------|
| Position | `right: 32px; top: 50%; transform: translateY(-50%)` |
| Size | 52×52px circle |
| Background (dark) | `rgba(255,255,255,0.06)` |
| Background (light) | `rgba(0,0,0,0.04)` |
| Icon | Chevron-right SVG, 22×22px |
| Stroke (dark) | `rgba(255,255,255,0.3)` |
| Stroke (light) | `rgba(0,0,0,0.2)` |

---

## CTA Slide

The final slide uses a completely different visual treatment to signal the end of the carousel and drive action.

| Element | Specification |
|:--------|:--------------|
| Background | Orange gradient: `linear-gradient(155deg, #cc7000 0%, #ff8c00 50%, #ffaa33 100%)` |
| Texture overlay | Diagonal lines at -45°, 21px spacing, `rgba(255,255,255,1)` at 6% opacity |
| Layout | Centered, flex-column |
| Logo | 120×120px dark circle (`rgba(0,0,0,0.3)`) with white ZF mark (64×55px) |
| Handle | Poppins 28px, `rgba(255,255,255,0.8)` |
| Headline | Barlow Condensed 900, 100–120px, white, centered |
| Glass card | `background: rgba(0,0,0,0.2); backdrop-filter: blur(12px); border-radius: 12px; padding: 36px 48px` |
| Glass card text | Inter 32px weight 500, white |
| Glass card link | Poppins 24px, `rgba(255,255,255,0.6)` |
| Website | Poppins 24px, `rgba(255,255,255,0.5)`, below glass card |
| No swipe arrow | Absence signals end of carousel |

---

## Background Images

When used (typically cover slides and select body slides), images are dimmed to avoid competing with text.

| Property | Value |
|:---------|:------|
| Position | absolute, full bleed (top/left/right/bottom: 0) |
| Size | cover, center |
| Opacity | 0.15–0.25 |
| z-index | 0 (behind all content) |

---

## Google Fonts Import

```
https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Inter:wght@400;500&family=Poppins:wght@400;500&display=swap
```

---

## Slide Rhythm Pattern

For a typical 5-slide carousel:

| Slide | Background | Logo Badge | Content Position |
|:------|:-----------|:-----------|:-----------------|
| 1 (Cover) | Dark + image | Yes | Bottom-aligned |
| 2 | Light | Yes | Top-aligned |
| 3 | Dark | No | Top-aligned |
| 4 | Light | Yes | Top-aligned |
| 5 (CTA) | Orange gradient | Centered large | Centered |

For 6 slides, add a dark `bg-surface` slide before the CTA. For 4 slides, compress to: Dark → Light → Dark → CTA.
