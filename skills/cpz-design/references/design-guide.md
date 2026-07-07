# CPZ Fitness — Brand & Design System Guide

**Version 1.3 — July 2026** *Derived from the philipz.fit website design system and refined per the CPZ Fitness Brand Guide v1 (July 2026). Use this document to maintain visual and tonal cohesion across all brand touchpoints: social media, carousels, future websites, course materials, and community content.*

---

## 1. Brand Identity

Full identity facts (company name, community name, tagline, core promise, CTAs, voice archetype) are owned by `cpz-fitness` — see `cpz-fitness/SKILL.md` Key Facts table. The one identity fact repeated here is the social handle, since it's rendered directly into exported designs (watermarks, slide footers, caption sign-offs):

| Element | Value |
| --- | --- |
| Social Handle | @philipz.fit |

---

## 2. Color System

### 2.1 Core Palette — Dark

The color system is built around three primary values that define the "Spartan" aesthetic: a near-black background that communicates seriousness and focus, a high-energy orange that signals action and transformation, and a warm off-white that provides readable contrast without the clinical harshness of pure white.

| Role | Name | Hex | Usage |
| --- | --- | --- | --- |
| **Background** | Coco's Black | `#1c1a17` | Page background, hero sections, full-bleed dark areas |
| **Card** | Card Surface | `#2c2925` | Cards, containers, elevated elements |
| **Accent / CTA** | CPZ Orange | `#ff8c00` | Primary buttons, highlights, section labels, active states |
| **Accent Dim** | Orange Dim | `rgba(255,140,0,0.15)` | Hover glows, background tints, subtle orange fills |
| **Text Primary** | Warm White | `#f2ece2` | Headlines, body text, primary readable content |
| **Text Muted** | Warm Muted | `#9b948a` | Secondary text, captions, nav links at rest |
| **Border** | Orange Border | `rgba(255,140,0,0.2)` | Card borders, dividers, container edges |

Default across the app, decks, and social creative. Accent (`#ff8c00`) carries emphasis only — CTAs, key numbers, highlighted words — never a large fill.

⚠️ *Retired: "Terminal Green" (`#4ade80`), the status/code-green accent from the software-engineer era, is dropped as of the July 2026 Brand Guide v1. It's absent from the current system and was already vestigial after the terminal/code-comment visual language was retired in the original rebrand. See §10.*

### 2.2 Secondary Palette — Light

Used only where a dark background doesn't work: email, printed handouts, one-pagers, lead magnets. Accent stays `#ff8c00` in both palettes — only the ground and ink flip.

| Role | Name | Hex | Usage |
| --- | --- | --- | --- |
| **Background** | Light Ground | `#f5f3ef` | Page/email background |
| **Card** | Light Card | `#ffffff` | Cards, containers |
| **Accent / CTA** | CPZ Orange | `#ff8c00` | Same as dark palette |
| **Ink** | Ink | `#17181a` | Headlines, body text |
| **Muted** | Light Muted | `#7a7f87` | Secondary text, captions |

This formalizes what was previously an ad hoc "Warm Linen" reference into one canonical light-mode palette for the brand.

### 2.3 Color Usage Rules

**Orange is earned, not decorative.** Use `#ff8c00` only on elements that demand attention: CTAs, active states, section labels, and key data points. Overusing orange dilutes its impact.

**Backgrounds layer in two steps.** The darkest value (`#1c1a17`) is the page foundation. The card (`#2c2925`) lifts content one level. Never skip levels — the depth creates visual hierarchy without borders.

**Warm white, not pure white.** `#f2ece2` has a slight warm cast that prevents eye strain against the dark background and feels more human than `#ffffff`. Pure white should never appear as body text in the dark palette.

**The orange border is a whisper, not a shout.** `rgba(255,140,0,0.2)` is used at 20% opacity to define card edges without competing with the content inside. Increase to 30% on hover states only.

### 2.4 Social Media Color Application

For social media posts and carousels, the same two-level depth system applies. The background of any graphic should be `#1c1a17` or `#2c2925`. Orange is reserved for the single most important element on the frame — a headline word, a stat, a CTA label. Muted text (`#9b948a`) handles supporting copy.

---

## 3. Typography

### 3.1 Font Stack

Four typefaces form the complete typographic system, each assigned a specific semantic role:

| Font | Role | Weights Used | Source |
| --- | --- | --- | --- |
| **Schibsted Grotesk** | Display, headlines, section titles | 600 (SemiBold), 700 (Bold) | Google Fonts |
| **Inter** | Body copy, UI, buttons | 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold) | Google Fonts |
| **Poppins** | Eyebrows, section labels, data callouts, tags | 500 (Medium), 600 (SemiBold) | Google Fonts |
| **League Spartan** | Logo wordmark only — the "CPZ Fitness" name, not general use | Variable | Already in `fonts/` |

Schibsted Grotesk replaces Barlow Condensed as of the July 2026 Brand Guide v1. The font file (variable + italic) is now present in both `cpz-design/fonts/` and `cpz-carousels/fonts/`. League Spartan is unaffected by this change and its font file is already present in both directories.

⚠️ Having the `.ttf` files on disk doesn't automatically fix the PNG export pipeline: `cpz-carousels/scripts/fonts_b64.py` and `template.py` still hardcode Bebas Neue as the base64-embedded headline font (see `cpz-carousels/SKILL.md` PNG Export Pipeline section) — someone needs to re-encode and wire in Schibsted Grotesk there before rendered PNGs will actually reflect it. That's a separate step from font sourcing.

See §4 for how the ZF lettermark (the icon-only shorthand) relates to the full "CPZ Fitness" wordmark.

### 3.2 Typographic Hierarchy

| Level | Font | Size | Weight | Transform | Tracking |
| --- | --- | --- | --- | --- | --- |
| **Display** | Schibsted Grotesk | 64–88px | 700 | None | -0.01em |
| **Headline** | Schibsted Grotesk | 36–44px | 700 | None | -0.01em |
| **Card Headline** | Schibsted Grotesk | 26–32px | 600 | None | 0 |
| **Body Copy** | Inter | 24–26px | 400 | None | 0 |
| **Eyebrow / Section Label** | Poppins | 24px | 600 | Uppercase | 0.14–0.16em |
| **UI / Buttons** | Inter | 24px | 600 | None | 0 |
| **Data / Small Label** | Poppins | 20–24px | 500 | None | 0 |

### 3.3 Typography Rules

**Headlines no longer default to uppercase.** Schibsted Grotesk headlines are set in sentence case at 700 weight — a deliberate softening from the previous all-caps Barlow Condensed convention. One key word per headline may still be set in the accent orange for emphasis.

**The eyebrow/section label pattern is a brand signature.** Every section opens with a small Poppins label in orange, uppercase, at 600 weight with 0.14–0.16em tracking, placed directly above the headline. Example: `BRAND GUIDE`, `APPLIED`, `TYPOGRAPHY`. This pattern must be preserved across all brand materials.

**Body copy is never bold-heavy.** Inter at regular weight is the reading voice. Bold within body copy is used sparingly — only to mark the single most important phrase in a paragraph, not for decoration. Inter also now carries UI/button text at 600 weight, a role previously held by Barlow Condensed.

**Poppins carries the label/data signal.** Whenever the content is a label, a stat, or a small supporting data point, Poppins is the correct typeface. It is not a display font — it is a precision instrument for anything that needs to feel compact and exact.

### 3.4 Social Media Typography

On social media graphics and carousels, the same three-font system applies. The headline occupies the dominant visual space in Schibsted Grotesk at 700 weight. Supporting copy uses Inter. Any label, stat, or data callout uses Poppins. Never introduce a fourth typeface.

⚠️ Note: carousel pixel specs in `cpz-carousels/references/html-rendering-spec.md` were tuned for Barlow Condensed's condensed proportions. Schibsted Grotesk is not condensed and will behave differently at the same pixel sizes — that spec needs a visual recalibration pass, not a blind find-replace. See `cpz-carousels/SKILL.md`.

---

## 4. Logo

### 4.1 The Mark

The logo is the **ZF lettermark** — a vectorized mark in `#ff8c00` orange on a transparent background. It isn't a generic icon: the full brand logotype is "CPZ Fitness," and the lettermark IS the seam of that word — the **Z** (end of "CPZ") and the **F** (start of "Fitness") are combined into one custom glyph, read in context as "CP[ZF]itness."

The ZF lettermark is the **icon-only shorthand** for the logo — used on its own wherever a compact mark is more appropriate than the full name (watermarks, favicons, small spaces, social profile photos). It is not a replacement for the full wordmark. The full "CPZ Fitness" logotype is still set in **League Spartan** — that typeface is unchanged by the July 2026 Brand Guide v1 and remains reserved exclusively for the logo, not general use (see §3.1).

**Clearspace:** equal to the height of the mark on every side. Never let text or imagery cross that line.

**Minimum size:** 28px tall on screen · 0.4in tall in print.

Channel-specific sizing (still applicable, not contradicted by the new guide):

| Context | Mark Size |
| --- | --- |
| Desktop navbar | 38px |
| Footer | 32px |
| Social media profile | 400×400px minimum |
| Carousel watermark | 24–32px |

### 4.2 Don't

- Recolor the mark outside the palette
- Add drop shadows, outlines, or bevels
- Place it on busy, low-contrast photography
- Stretch, skew, or rotate it
- Place it on a light background without testing contrast — the orange mark is designed for dark backgrounds first

### 4.3 Implementation

The ZF mark is always inline SVG on the web. Using an `<img>` tag with an `.svg` source creates cross-browser rendering inconsistencies.

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

**The section label.** A Poppins eyebrow in orange, uppercase, 600 weight, 0.14–0.16em tracking, placed directly above the headline. This appears at the top of every section and is the most consistent brand signature across the site. Example: `TYPOGRAPHY`

**The accent card.** A card-surface (`#2c2925`) container with an orange-tinted border (`rgba(255,140,0,0.15)`) and a thin orange top accent bar. Used for callouts, testimonials, the booking widget, and any content that should feel elevated and set apart.

**The lead magnet card.** A lighter-weight sibling to the accent card, introduced in the July 2026 Brand Guide v1 — see §6.5.

**The process card.** A dark card with a 3px left-side orange accent bar that animates from 0% to 100% height on hover. Used for the program's stages/steps. The hover animation communicates progress and activation — the card "comes alive" when you engage with it.

**The diagonal cut.** Section transitions use CSS `clip-path` polygon cuts rather than straight horizontal dividers. The hero section ends with a diagonal cut from bottom-right to bottom-left, creating a sense of forward momentum rather than a static page break.

**The orange glow.** Radial gradient glows in `rgba(255,140,0,0.06)` appear in the bottom corners of the hero and other dark sections. They are subtle — barely visible — but they give the dark background warmth and prevent it from feeling flat.

**Border-radius now varies by element role, not one fixed rule.** Structural cards stay tight (4px). Buttons are rounded (14px). Status pills/tags are fully rounded (~20px). See §6 and §9.

### 5.3 Motion & Animation

**Entrance animations use `fade-up`.** Content enters the viewport by fading in and translating 24px upward over 0.6 seconds with an ease curve. This is the only entrance animation in the system — do not introduce additional animation types.

**Hover states are fast.** All hover transitions use 0.2s ease. This feels responsive without being jarring. Longer transitions (0.3s+) are reserved for the process card left-bar animation only.

**The navbar scroll state** transitions from a 70% opaque background to 97% opaque with an orange bottom border when the user scrolls past 40px. This is a 0.3s transition. The effect communicates that the user has left the hero and entered the content.

**No parallax, no scroll-triggered animations beyond fade-up.** The design is disciplined. Adding scroll-triggered transforms or parallax effects would dilute the Spartan aesthetic.

---

## 6. UI Components

### 6.1 Buttons

Two button variants exist in the system, updated per the July 2026 Brand Guide v1 to a rounder, softer shape than the previous near-square style.

**Primary Button:**

- Background: `#ff8c00` | Text (dark ground): `#1c1a17` | Text (light ground): `#17181a`

- Font: Inter 600, 24px

- Padding: 16px 26px | Border-radius: **14px**

- Hover (dark ground): background transparent, text `#ff8c00`

**Secondary Button:**

- Background: transparent

- Dark ground: `#f2ece2` text, `rgba(242,236,226,.22)` border. Light ground: `#17181a` text, `rgba(23,24,26,.18)` border

- Same font, padding, and radius as primary

- Hover: border and text both shift to `#ff8c00`

⚠️ *Updated: border-radius changes from 2px (near-square) to 14px (rounded) as of the July 2026 Brand Guide v1 — this supersedes the earlier "precision over softness" rationale for the old radius. See §10.*

### 6.2 Status Pills / Tags

New component, introduced in the July 2026 Brand Guide v1. Fully rounded pills (~20px radius), Poppins 500, used for status/quality indicators — e.g., protein-completeness tags on nutrition content ("Complete" / "Complementary" / "Incomplete").

| Variant | Dark Ground | Light Ground |
| --- | --- | --- |
| Complete (accent) | `rgba(255,140,0,.16)` bg, `#ff8c00` text | `rgba(255,140,0,.14)` bg, `#a35d00` text |
| Complementary (neutral) | `rgba(255,255,255,.06)` bg, `#c9c2b6` text | `#eeeeec` bg, `#5a5e64` text |
| Incomplete (muted) | `rgba(255,255,255,.04)` bg, `#9b948a` text | `#f2f1ee` bg, `#9a9ea3` text |

This component directly supersedes the old checklist rule "no pill buttons, no soft UI" — see §9.

### 6.3 Cards

Cards follow the two-level depth system. The card color (`#2c2925` dark / `#ffffff` light) is the default background. The orange border at 15–20% opacity defines the edge without competing with content. Cards do not use drop shadows — depth is communicated through background color contrast alone.

### 6.4 The Accent Card

The accent card pattern is a core brand component. Structure:

1. **Header bar**: `rgba(255,255,255,0.03)` background, 0.625rem 1rem padding

2. **Body**: `#2c2925` background, 1.25–1.5rem padding

3. **Border**: 1px solid `rgba(255,140,0,0.15)`

4. **Border-radius**: 4px

Use this pattern whenever content should feel elevated and set apart: callouts, testimonials, booking widgets, highlighted quotes.

### 6.5 The Lead Magnet Card

New component, introduced in the July 2026 Brand Guide v1. A lighter-weight sibling to the accent card — no header bar, no left accent bar, just a bordered container:

- Background: `#1c1a17` (dark) / `#f5f3ef` (light)

- Border: 1px solid `rgba(255,140,0,.18)`

- Border-radius: ~16px

- Content: Poppins eyebrow label (uppercase, orange, ~0.08–0.1em tracking) + Inter body copy, optionally paired with status pills (§6.2)

- Used for: downloadable lead magnets, resource callouts (e.g., a "Protein Guide")

---

## 7. Voice & Tone

Voice, vocabulary, and language rules are owned by `cpz-fitness` — this design guide only covers visual specs. See `cpz-fitness/SKILL.md` for the Voice Pillars, Vocabulary Guide, and content arc, and `cpz-fitness/references/brand.md` for the Inclusive "We" Principle, Authentic Voice Patterns, and Tone Quick-Reference.

---

## 8. Social Media Application

### 8.1 Post Design System

Social media graphics should feel like they were exported from the website — not designed separately. The same color system, typography, and design language apply. A follower who visits the website after seeing a post should feel immediate visual continuity.

**Single-image post structure:**

- Background: `#1c1a17` or `#2c2925`

- Headline: Schibsted Grotesk 700, sentence case, `#f2ece2` or `#ff8c00` for the key word

- Section label: Poppins, orange, eyebrow style — e.g., `THE FIX`

- Body copy: Inter 400, `#f2ece2` or `#9b948a`

- Logo watermark: mark at 24–32px, bottom-right corner, `#ff8c00`

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

**Slide 1 — The Hook:** Full-bleed dark background. A single provocative statement in Schibsted Grotesk at maximum size. One key word in orange. The section label in the top-left corner. No body copy — just the hook.

**Slides 2–5 — The Content:** Consistent layout: section label top-left, headline in Schibsted Grotesk, body copy in Inter, one orange accent element per slide. If the slide contains a stat, the number is in Schibsted Grotesk 700 at 3.5rem+ in orange. For labels or data callouts, use Poppins.

**Final Slide — The CTA:** Return to the full-bleed dark background. The CTA in Schibsted Grotesk, orange. The section label reads `NEXT STEP`. The handle `@philipz.fit` in Poppins, muted. The logo mark, centered or bottom-right.

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

### 8.4 Applied Examples

Three reference layouts from the July 2026 Brand Guide v1, illustrating the system in context. The Tagline ("Lifting to be seen.") and primary CTA ("Free Consultation") are now finalized — see `cpz-fitness/SKILL.md` Key Facts for the real copy to use in these layouts going forward.

**Social Post** (700×700, dark palette): Logo mark + brand name in a header row → dominant Schibsted Grotesk headline with one word in accent orange → footer row with the handle (muted, left) and a small primary-button CTA (right).

**Landing Page Hero** (dark palette): Nav bar (logo + brand name, nav links in Inter medium, primary CTA button, right-aligned) → hero headline in Schibsted Grotesk with one accent word → subhead in Inter, max ~920px width for readability.

**Email / Lead Magnet** (light palette): Logo + brand name header → Schibsted Grotesk headline (sentence case) → Inter body copy → a lead-magnet card (§6.5) with status pills (§6.2) → full-width primary CTA button.

---

## 9. Brand Consistency Checklist

Before publishing any piece of brand content — a post, a graphic, a page, a carousel — verify the following:

**Visual:**

- [ ] Background is `#1c1a17` or `#2c2925` (not a custom dark color)

- [ ] Orange (`#ff8c00`) appears on one element only per frame/section

- [ ] Headlines use Schibsted Grotesk 700, sentence case

- [ ] Body copy uses Inter

- [ ] Labels/eyebrows/data callouts use Poppins

- [ ] The logo mark is present as a watermark or brand identifier

- [ ] No fourth typeface has been introduced

- [ ] Buttons use 14px border-radius; status pills/tags may be fully rounded (~20px); structural cards stay at 4px

**Voice:**

- [ ] Run the Writing Checklist in `cpz-fitness/SKILL.md` before publishing

---

## 10. Design Decisions Log

This section documents the reasoning behind key design decisions made during the philipz.fit build. Reference this when making future decisions to ensure consistency.

*Entries below predate the July 2026 rebrand and describe the original software-engineer-era brand. Several of the practices they justify — the terminal/code-comment section labels, the "pipeline" card name, "Help me debug" as the primary CTA — have since been retired; see the July 2026 entries at the bottom. Kept here for institutional history, not as current guidance.*

| Decision | Rationale |
| --- | --- |
| Dark-first theme | The original ICP worked late, thought in dark-mode IDEs, and associated dark interfaces with seriousness and craft. A light-first design would feel like a consumer wellness app — wrong positioning. |
| Barlow Condensed for headlines *(retired)* | Condensed type at heavy weight communicates strength and directness without being aggressive. It also allows large type at smaller widths, which is critical for mobile. Retired in favor of Schibsted Grotesk — see the July 2026 Brand Guide v1 entry below. |
| 2px border-radius on buttons *(retired)* | Rounds the corner just enough to prevent a harsh right angle, but keeps the button feeling precise rather than soft and consumer-friendly. Retired in favor of a 14px radius — see the July 2026 Brand Guide v1 entry below. |
| Section labels as code comments *(retired)* | `// about.me` and `// pipeline.yml` immediately signaled to the original engineer ICP that this was their world. Retired in the July 2026 rebrand along with the rest of the code-comment visual language. |
| Terminal card pattern *(retired)* | Wrapping content in a terminal window frame spoke the original engineer ICP's language. Retired and replaced with the plain accent card in the July 2026 rebrand. |
| Orange at 6% opacity for glow effects | Enough to add warmth and depth to the dark background without competing with the primary orange accent. The glow is felt, not seen. |
| Asymmetric hero layout | Left-aligned headline with gym background bleeding right communicates forward momentum and confidence. A centered hero would feel generic and passive. |
| Diagonal section cuts | Straight horizontal dividers between sections feel static. The diagonal cut creates a sense of motion — the page is going somewhere. |
| Warm white instead of pure white | Pure white against near-black creates harsh contrast that fatigues the eye. A warm off-white cast is more comfortable for long reading sessions and feels more human. |
| Three-level card depth *(retired)* | Using background color alone (no shadows) to create depth kept the interface feeling clean and precise. Collapsed to a two-level system (background + card) in the July 2026 Brand Guide v1 — the middle "surface" tier was redundant in practice. |
| Inclusive "we" in hero copy | The hero subheadline uses "we keep putting off" instead of "they keep putting off" — Philip includes himself in the struggle, which builds immediate trust and signals that this is a peer relationship, not a coach-client hierarchy. |
| "Since high school" anchor in About copy | Using "since high school" instead of a specific age creates a more universal emotional anchor — most people have a clear memory of their high school body as a baseline, regardless of their current age. |
| Rebrand from software-engineer ICA to gay-men ICA (July 2026) | The brand repositioned from software-engineer clients to "I help gay men build muscle and lose fat." Terminal cards, code-comment section labels, monospace-as-signal, and debug-themed CTAs were retired as they no longer reflect the audience or positioning. The "Sarcastic Sage" voice archetype carries forward unchanged — it was never engineering-specific, it's just Philip's actual personality. |
| Brand Guide v1 refresh (July 2026) | A new internal brand guide deck refined the visual system: Schibsted Grotesk replaces Barlow Condensed for display/headlines, set in sentence case rather than uppercase. League Spartan is unaffected — it remains the typeface for the full "CPZ Fitness" logo wordmark; the ZF lettermark is the separate icon-only shorthand version. "Terminal Green" is retired as unused. Buttons move from a 2px near-square radius to a 14px rounded radius, and a new fully-rounded status-pill component is introduced — both superseding the earlier "no pill buttons, no soft UI" rule. The three-level dark palette (background/surface/card) collapses to two levels (background/card). A formal Secondary/Light palette (`#f5f3ef` / `#ffffff` / `#17181a` / `#7a7f87`) replaces the ad hoc "Warm Linen" reference. |
| Brand facts finalized (July 2026) | Tagline set to "Lifting to be seen." (replacing the placeholder "Strong. Confident. Undeniable." and, before that, "From desk-bound to damn-strong."). Booking CTA finalized as "Free Consultation" → `lnk.philipz.fit/free-consult` (replacing the retired "Free System Audit" label and URL). PDF CTA URL updated to `lnk.philipz.fit/pdf-consult`, following a `{channel}-consult` naming pattern applied across all consultation links (e.g. a future email-consult or social-consult link would follow the same shape). The Skool community is closed for now — `lnk.philipz.fit/community` is reserved as a placeholder for a future relaunch and does not currently resolve anywhere. |
