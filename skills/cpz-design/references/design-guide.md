# CPZ Fitness — Brand & Design System Guide

**Version 1.2 — April 2026** *Derived from the philipz.fit website design system. Use this document to maintain visual and tonal cohesion across all brand touchpoints: social media, carousels, future websites, course materials, and community content.*

---

## 1. Brand Identity

Full identity facts (company name, community name, tagline, core promise, CTAs, voice archetype) are owned by `cpz-fitness` — see `cpz-fitness/SKILL.md` Key Facts table. The one identity fact repeated here is the social handle, since it's rendered directly into exported designs (watermarks, slide footers, caption sign-offs):

| Element | Value |
| --- | --- |
| Social Handle | @philipz.fit |

---

## 2. Color System

### 2.1 Core Palette

The color system is built around three primary values that define the "Spartan" aesthetic: a near-black background that communicates seriousness and focus, a high-energy orange that signals action and transformation, and a warm off-white that provides readable contrast without the clinical harshness of pure white.

| Role | Name | Hex | Usage |
| --- | --- | --- | --- |
| **Background** | Coco's Black | `#191a1b` | Page background, hero sections, full-bleed dark areas |
| **Surface** | Dark Surface | `#1a1d21` | Cards, accent containers, elevated containers |
| **Card** | Card Surface | `#22262b` | Secondary cards, nested containers |
| **Accent / CTA** | CPZ Orange | `#ff8c00` | Primary buttons, highlights, section labels, active states |
| **Accent Dim** | Orange Dim | `rgba(255,130,0,0.15)` | Hover glows, background tints, subtle orange fills |
| **Text Primary** | Warm White | `#f0ede8` | Headlines, body text, primary readable content |
| **Text Muted** | Slate Muted | `#8a8f96` | Secondary text, captions, nav links at rest |
| **Code Green** | Terminal Green | `#4ade80` | Status indicators, positive-value accents |
| **Border** | Orange Border | `rgba(255,130,0,0.2)` | Card borders, dividers, container edges |

### 2.2 Color Usage Rules

**Orange is earned, not decorative.** Use `#ff8c00` only on elements that demand attention: CTAs, active states, section labels, and key data points. Overusing orange dilutes its impact. On the website, it appears on the primary button, the section label lines, stat numbers, and card hover accents — nothing else.

**Backgrounds layer in three steps.** The darkest value (`#191a1b`) is the page foundation. The surface (`#1a1d21`) lifts content one level. The card (`#22262b`) creates a third level for nested elements. Never skip levels — the depth creates visual hierarchy without borders.

**Warm white, not pure white.** `#f0ede8` has a slight warm cast that prevents eye strain against the dark background and feels more human than `#ffffff`. Pure white should never appear as body text in this system.

**The orange border is a whisper, not a shout.** `rgba(255,130,0,0.2)` is used at 20% opacity to define card edges without competing with the content inside. Increase to 30% on hover states only.

### 2.3 Social Media Color Application

For social media posts and carousels, the same three-level depth system applies. The background of any graphic should be `#191a1b` or `#1a1d21`. Orange is reserved for the single most important element on the frame — a headline word, a stat, a CTA label. Muted text (`#8a8f96`) handles supporting copy.

---

## 3. Typography

### 3.1 Font Stack

Three typefaces form the complete typographic system, each assigned a specific semantic role:

| Font | Role | Weights Used | Source |
| --- | --- | --- | --- |
| **Barlow Condensed** | Headlines, CTAs, nav, stats | 700 (Bold), 800 (ExtraBold), 900 (Black) | Google Fonts |
| **Inter** | Body copy, descriptions, paragraphs | 400 (Regular), 500 (Medium) | Google Fonts |
| **Poppins** | Section labels, data callouts, small labels | 400 (Regular), 500 (Medium) | Google Fonts |

⚠️ Known issue: the Barlow Condensed font file is currently missing from `cpz-carousels/fonts/` (removed when the folder was swapped over to Inter/Poppins). This spec still calls for Barlow Condensed on headlines — the font file itself needs restoring in a separate design-focused pass.

### 3.2 Typographic Hierarchy

The hierarchy is intentionally aggressive. Headlines are large, condensed, and uppercase — they command attention. Body copy is compact and readable. Labels are small and precise. The contrast between these three registers is a core part of the brand's visual identity.

| Level | Font | Size | Weight | Transform | Tracking |
| --- | --- | --- | --- | --- | --- |
| **Hero Headline** | Barlow Condensed | 5–7rem (responsive) | 900 | Uppercase | -0.01em |
| **Section Headline** | Barlow Condensed | 2.5–3.5rem | 800 | Uppercase | -0.01em |
| **Card Headline** | Barlow Condensed | 1.25–1.5rem | 700 | Uppercase | 0 |
| **Body Copy** | Inter | 1rem–1.1rem | 400–500 | None | 0 |
| **Section Label** | Poppins | 0.75rem | 500 | Uppercase | 0.1em |
| **Nav Links** | Barlow Condensed | 0.95rem | 600 | Uppercase | 0.06em |
| **Data / Small Label** | Poppins | 0.8–0.85rem | 400 | None | 0 |
| **Stat Numbers** | Barlow Condensed | 3.5rem | 900 | None | 0 |

### 3.3 Typography Rules

**Headlines are always uppercase and condensed.** Barlow Condensed at weight 800+ in uppercase is the brand's most recognizable typographic signature. It communicates strength, directness, and confidence. Do not use Barlow Condensed in sentence case for headlines — it loses its impact.

**The section label pattern is a brand signature.** Every section opens with a small Poppins label in orange, uppercase, preceded by a 2rem orange horizontal rule. Example: `ABOUT ME`, `THE PLAN`, `WHO THIS IS FOR`. This pattern must be preserved across all brand materials.

**Body copy is never bold-heavy.** Inter at regular weight is the reading voice. Bold within body copy is used sparingly — only to mark the single most important phrase in a paragraph, not for decoration.

**Poppins carries the label/data signal.** Whenever the content is a label, a stat, or a small supporting data point, Poppins is the correct typeface. It is not a display font — it is a precision instrument for anything that needs to feel compact and exact.

### 3.4 Social Media Typography

On social media graphics and carousels, the same three-font system applies. The headline occupies the dominant visual space in Barlow Condensed at maximum weight. Supporting copy uses Inter. Any label, stat, or data callout uses Poppins. Never introduce a fourth typeface.

---

## 4. Logo

### 4.1 The ZF Mark

The logo is a vectorized ZF lettermark in `#ff8c00` orange on a transparent background. It is a custom mark — not a wordmark, not an icon from a library. The mark is always paired with the "CPZ FITNESS" wordmark in Barlow Condensed 700, uppercase, at `#f0ede8`.

| Context | Mark Size | Wordmark |
| --- | --- | --- |
| Desktop navbar | 38px | Paired |
| Footer | 32px | Paired |
| Social media profile | 400×400px minimum | Optional |
| Carousel watermark | 24–32px | Optional |

### 4.2 Logo Usage Rules

**Never place the logo on a light background without testing contrast.** The orange mark is designed for dark backgrounds. On light backgrounds, the mark becomes less legible and loses brand impact.

**The ZF mark is always inline SVG on the web.** Using an `<img>` tag with an `.svg` source creates cross-browser rendering inconsistencies. All web implementations must use the inline SVG component.

**Minimum clear space** around the logo is equal to the height of the ZF mark on all sides. Do not crowd it with other elements.

---

## 5. Design Language

### 5.1 The "Spartan" Aesthetic

The design philosophy is named for the discipline and minimalism of a Spartan warrior. Every design decision should reinforce restraint and function. Decoration that does not serve function is removed. Hierarchy is enforced through scale and weight, not color variety.

**Three defining characteristics:**

1. **Dark-first.** The default state is dark. Light is used as an accent, not a base. This communicates seriousness, focus, and the quiet discipline of showing up for an early-morning or late-night training session.

2. **Orange as signal, not decoration.** Every orange element is a call to action or a data point. If it is orange, the user should pay attention to it.

3. **Discipline as culture.** The brand's audience values consistency and self-respect over hype. The design reflects this through restraint: minimal color, strong hierarchy, no decorative flourishes — every element earns its place.

**Asymmetric and direct.** Layouts are left-aligned and asymmetric. Content does not sit in centered, symmetrical grids. The hero headline stacks vertically on the left while the gym background bleeds to the right. This asymmetry communicates confidence and forward momentum.

### 5.2 Signature Visual Elements

**The section label.** A 2rem orange horizontal rule followed by a Poppins label in orange, uppercase, with 0.1em letter-spacing. This appears at the top of every section and is the most consistent brand signature across the site. Example: `ABOUT ME`

**The accent card.** A dark surface (`#1a1d21`) container with an orange-tinted border (`rgba(255,130,0,0.15)`) and a thin orange top accent bar. Used for callouts, testimonials, the booking widget, and any content that should feel elevated and set apart.

**The process card.** A dark card with a 3px left-side orange accent bar that animates from 0% to 100% height on hover. Used for the program's stages/steps. The hover animation communicates progress and activation — the card "comes alive" when you engage with it.

**The diagonal cut.** Section transitions use CSS `clip-path` polygon cuts rather than straight horizontal dividers. The hero section ends with a diagonal cut from bottom-right to bottom-left, creating a sense of forward momentum rather than a static page break.

**The orange glow.** Radial gradient glows in `rgba(255,130,0,0.06)` appear in the bottom corners of the hero and other dark sections. They are subtle — barely visible — but they give the dark background warmth and prevent it from feeling flat.

### 5.3 Motion & Animation

**Entrance animations use `fade-up`.** Content enters the viewport by fading in and translating 24px upward over 0.6 seconds with an ease curve. This is the only entrance animation in the system — do not introduce additional animation types.

**Hover states are fast.** All hover transitions use 0.2s ease. This feels responsive without being jarring. Longer transitions (0.3s+) are reserved for the process card left-bar animation only.

**The navbar scroll state** transitions from a 70% opaque background to 97% opaque with an orange bottom border when the user scrolls past 40px. This is a 0.3s transition. The effect communicates that the user has left the hero and entered the content.

**No parallax, no scroll-triggered animations beyond fade-up.** The design is disciplined. Adding scroll-triggered transforms or parallax effects would dilute the Spartan aesthetic.

---

## 6. UI Components

### 6.1 Buttons

Two button variants exist in the system. No additional variants should be introduced without strong justification.

**Primary Button (`btn-primary`):**

- Background: `#ff8c00` | Text: `#191a1b` | Border: 2px solid `#ff8c00`

- Font: Barlow Condensed 700, uppercase, 1rem, 0.05em tracking

- Padding: 0.875rem 2rem | Border-radius: 2px (nearly square)

- Hover: Background transparent, text `#ff8c00` (inverted fill)

**Secondary Button (`btn-secondary`):**

- Background: transparent | Text: `#f0ede8` | Border: 2px solid `rgba(240,237,232,0.3)`

- Same font and padding as primary

- Hover: Border and text both shift to `#ff8c00`

The 2px border-radius is intentional — it is almost a right angle, communicating precision and rigidity rather than the rounded softness of consumer apps.

### 6.2 Cards

Cards follow the three-level depth system. The surface color (`#1a1d21`) is the default card background. The orange border at 15–20% opacity defines the edge without competing with content. Cards do not use drop shadows — depth is communicated through background color contrast alone.

### 6.3 The Accent Card

The accent card pattern is a core brand component. Structure:

1. **Header bar**: `rgba(255,255,255,0.03)` background, 0.625rem 1rem padding

2. **Body**: `#1a1d21` background, 1.25–1.5rem padding

3. **Border**: 1px solid `rgba(255,130,0,0.15)`

4. **Border-radius**: 4px

Use this pattern whenever content should feel elevated and set apart: callouts, testimonials, booking widgets, highlighted quotes.

---

## 7. Voice & Tone

Voice, vocabulary, and language rules are owned by `cpz-fitness` — this design guide only covers visual specs. See `cpz-fitness/SKILL.md` for the Voice Pillars, Vocabulary Guide, and content arc, and `cpz-fitness/references/brand.md` for the Inclusive "We" Principle, Authentic Voice Patterns, and Tone Quick-Reference.

---

## 8. Social Media Application

### 8.1 Post Design System

Social media graphics should feel like they were exported from the website — not designed separately. The same color system, typography, and design language apply. A follower who visits the website after seeing a post should feel immediate visual continuity.

**Single-image post structure:**

- Background: `#191a1b` or `#1a1d21`

- Headline: Barlow Condensed 800+, uppercase, `#f0ede8` or `#ff8c00` for the key word

- Section label: Poppins, orange, with the 2rem orange rule — e.g., `THE FIX`

- Body copy: Inter 400, `#f0ede8` or `#8a8f96`

- Logo watermark: ZF mark at 24–32px, bottom-right corner, `#ff8c00`

- Orange accent: One element only — the headline key word, a stat, or a CTA label

**Aspect ratios by platform:**

| Platform | Ratio | Pixels |
| --- | --- | --- |
| Instagram Feed | 4:5 | 1080×1350 |
| Instagram Stories / Reels cover | 9:16 | 1080×1920 |
| TikTok cover | 9:16 | 1080×1920 |
| LinkedIn post | 1.91:1 | 1200×628 |
| Twitter/X post | 16:9 | 1200×675 |
| Facebook post | 1.91:1 | 1200×628 |

### 8.2 Carousel Design System

Carousels are the highest-leverage content format for this brand — they allow the ICA to consume a structured argument in a familiar, sequential format. Each carousel should follow a consistent structure:

**Slide 1 — The Hook:** Full-bleed dark background. A single provocative statement in Barlow Condensed at maximum size. One key word in orange. The section label in the top-left corner. No body copy — just the hook.

**Slides 2–5 — The Content:** Consistent layout: section label top-left, headline in Barlow Condensed, body copy in Inter, one orange accent element per slide. If the slide contains a stat, the number is in Barlow Condensed 900 at 3.5rem+ in orange. For labels or data callouts, use Poppins.

**Final Slide — The CTA:** Return to the full-bleed dark background. The CTA in Barlow Condensed, orange. The section label reads `NEXT STEP`. The handle `@philipz.fit` in Poppins, muted. The ZF logo mark, centered or bottom-right.

**Carousel spacing rules:**

- Consistent padding: 48–64px on all sides

- Never crowd the edges — the dark background needs breathing room

- One focal element per slide — the eye should know immediately where to look

### 8.3 Caption Voice

Captions follow the same voice pillars as all other content. On Instagram and TikTok, the first line is the hook — it must stand alone as a complete thought that stops the scroll. The body of the caption delivers the diagnosis and fix. The final line is always the single clear next action, followed by the handle or a link-in-bio reference.

**Caption length by platform:**

| Platform | Recommended Length |
| --- | --- |
| Instagram | 150–300 words (long-form performs well with this ICA) |
| TikTok | 50–100 words (shorter — video carries the content) |
| LinkedIn | 200–400 words (professional context supports longer reads) |
| Twitter/X | 1–3 sentences or a thread |
| Threads | 150–250 words |

---

## 9. Brand Consistency Checklist

Before publishing any piece of brand content — a post, a graphic, a page, a carousel — verify the following:

**Visual:**

- [ ] Background is `#191a1b` or `#1a1d21` (not a custom dark color)

- [ ] Orange (`#ff8c00`) appears on one element only per frame/section

- [ ] Headlines use Barlow Condensed 700+ in uppercase

- [ ] Body copy uses Inter

- [ ] Labels/data callouts use Poppins

- [ ] The ZF logo mark is present as a watermark or brand identifier

- [ ] No fourth typeface has been introduced

- [ ] No rounded corners beyond 4px on cards (no pill buttons, no soft UI)

**Voice:**

- [ ] Run the Writing Checklist in `cpz-fitness/SKILL.md` before publishing

---

## 10. Design Decisions Log

This section documents the reasoning behind key design decisions made during the philipz.fit build. Reference this when making future decisions to ensure consistency.

*Entries below predate the July 2026 rebrand and describe the original software-engineer-era brand. Several of the practices they justify — the terminal/code-comment section labels, the "pipeline" card name, "Help me debug" as the primary CTA — have since been retired; see the July 2026 entry at the bottom. Kept here for institutional history, not as current guidance.*

| Decision | Rationale |
| --- | --- |
| Dark-first theme | The original ICP worked late, thought in dark-mode IDEs, and associated dark interfaces with seriousness and craft. A light-first design would feel like a consumer wellness app — wrong positioning. |
| Barlow Condensed for headlines | Condensed type at heavy weight communicates strength and directness without being aggressive. It also allows large type at smaller widths, which is critical for mobile. |
| 2px border-radius on buttons | Rounds the corner just enough to prevent a harsh right angle, but keeps the button feeling precise rather than soft and consumer-friendly. |
| Section labels as code comments *(retired)* | `// about.me` and `// pipeline.yml` immediately signaled to the original engineer ICP that this was their world. Retired in the July 2026 rebrand along with the rest of the code-comment visual language. |
| Terminal card pattern *(retired)* | Wrapping content in a terminal window frame spoke the original engineer ICP's language. Retired and replaced with the plain accent card in the July 2026 rebrand. |
| Orange at 6% opacity for glow effects | Enough to add warmth and depth to the dark background without competing with the primary orange accent. The glow is felt, not seen. |
| Asymmetric hero layout | Left-aligned headline with gym background bleeding right communicates forward momentum and confidence. A centered hero would feel generic and passive. |
| Diagonal section cuts | Straight horizontal dividers between sections feel static. The diagonal cut creates a sense of motion — the page is going somewhere. |
| Warm white (`#f0ede8`) instead of pure white | Pure white against near-black creates harsh contrast that fatigues the eye. The warm cast of `#f0ede8` is more comfortable for long reading sessions and feels more human. |
| Three-level card depth | Using background color alone (no shadows) to create depth keeps the interface feeling clean and precise. Shadows can feel decorative; color contrast feels structural. |
| Inclusive "we" in hero copy | The hero subheadline uses "we keep putting off" instead of "they keep putting off" — Philip includes himself in the struggle, which builds immediate trust and signals that this is a peer relationship, not a coach-client hierarchy. |
| "Since high school" anchor in About copy | Using "since high school" instead of a specific age creates a more universal emotional anchor — most people have a clear memory of their high school body as a baseline, regardless of their current age. |
| Rebrand from software-engineer ICA to gay-men ICA (July 2026) | The brand repositioned from software-engineer clients to "I help gay men build muscle and lose fat." Terminal cards, code-comment section labels, monospace-as-signal, and debug-themed CTAs were retired as they no longer reflect the audience or positioning. Barlow Condensed stays for headlines; Inter and Poppins replace Space Grotesk, Open Sans, and JetBrains Mono elsewhere. The "Sarcastic Sage" voice archetype carries forward unchanged — it was never engineering-specific, it's just Philip's actual personality. |
