---
name: cpz-fitness
description: CPZ Fitness brand DNA root. Contains identity, voice architecture, ICA, colors, and typography. Load this skill first for any CPZ Fitness task. All focused skills extend this root.
---

# CPZ Fitness — Brand Root

## Key Facts

| Field                 | Value                                                                             |
|:----------------------|:----------------------------------------------------------------------------------|
| **Owner**             | Philip — fitness coach, out 10 years, former software engineer                    |
| **Company**           | CPZ Fitness (no program/framework name)                                          |
| **Website**           | https://www.philipz.fit/                                                          |
| **Social Media**      | @philipz.fit (Instagram, TikTok, Facebook, Threads, Bluesky)                      |
| **Skool Community**   | ⚠️ NEEDS INPUT — "Geek 2 Greek Starter Zone" needs a new name. Placeholder: "CPZ Fitness Community" — https://lnk.philipz.fit/skool |
| **Logo**              | `templates/cpz-logo.svg` (ZF vectorized mark — orange on transparent)             |
| **Voice Archetype**   | The "Sarcastic Sage" — dry humor + direct guidance + empathy (no more engineering/systems framing) |
| **Core Promise**      | "I help gay men build muscle and lose fat."                                       |
| **Tagline**           | ⚠️ NEEDS INPUT — placeholder: "Strong. Confident. Undeniable." (replaces "From desk-bound to damn-strong.") |
| **Booking CTA**       | ⚠️ NEEDS INPUT — recommend relabeling button text from "Free System Audit" to "Free Consult Call" (URL stays `/free-system-audit`) |
| **PDF CTA Link**      | Same relabeling as above if used                                                  |

---

## Brand Philosophy

Philip is a gay man who spent years hiding, minimizing, and not fully
occupying who he was — sexually and physically. He came out roughly a
decade ago. The body work came later, and it followed the same pattern:
avoidance, comparison, finally doing the work.

Publicly, CPZ Fitness is simple: a coach who helps gay men build muscle
and lose fat, and who's actually lived the process himself. The deeper
identity/confidence layer is real and present in how Philip coaches —
it is not the headline. Nobody hires a coach to be "reclaimed" publicly;
they hire a coach to get strong. The depth shows up in the relationship,
not the ad copy.

---

## Brand Archetype: The "Sarcastic Sage"

Philip is the guy who's already made every mistake in the book — and isn't shy about admitting it. He calls out bad excuses and common mistakes with dry humor, then immediately hands the client the exact fix. Sarcasm always lands with empathy: the joke is at the *situation's* expense, with Philip pointing at himself first.

---

## The Voice Pillars

**1. Direct & Confident (The Hook)**
State things plainly. No hedging, no disclaimers, no "just my opinion."
> "Most guys don't need a new program. They need to stop restarting the same one every six weeks."

**2. Dry & Self-Aware (The Humor)**
Humor lands because Philip points at himself first, not the client.
> "I spent three years perfecting my gym selfie lighting before I ever hit a real PR."

**3. Empathetic, Not Soft (The Foundation)**
Acknowledge real struggles — gym intimidation, body comparison, cyclical motivation — without softening the truth about what it takes to fix them.
> "I know what it's like to avoid the pool because you don't want anyone to see you without a shirt on. I also know what it's like to not think about it anymore."

**4. Clear & Actionable (The Close)**
One next step. No hedging after the point is made.
> "Stop comparing your week 2 to someone else's year 3. Show up again tomorrow."

---

## Vocabulary Guide

| Use These                                    | Avoid These                                                       |
|:----------------------------------------------|:-------------------------------------------------------------------|
| Build / Strong / Consistent                   | Debugging / Refactoring / Legacy code / Technical debt / Optimize |
| Show up / Stick with it                       | Systems / Inputs-outputs / Metrics (as metaphor)                  |
| Confidence / Presence                         | Excessive emojis (🚀🔥💯)                                          |
| Progress / Momentum                           | Bro / Boss / Chief                                                |
| Straightforward / Practical                   | "No-BS"                                                           |
| Lean gain / Slow gain                         | Cookie-cutter / Generic                                           |
| Comparison (as something to name and reject)  | Shredded / Ripped / Swole as the *goal framing* (fine as casual vocabulary, not as the pitch) |

**Avoid these patterns:** "Genuinely" / "Honestly" as filler. Restarting after a point is made. Hedging after a direct claim. Trailing off instead of completing the thought.

---

## Writing Checklist

Before finalizing any content:
1. Is it clear and actionable?
2. Does it speak to confidence and visibility, not comparison or shame?
3. Is there a dry, sarcastic observation about a common mistake?
4. Does it ultimately guide toward a solution with empathy?
5. Are emojis used purposefully, not as punctuation?
6. Does Philip implicate himself before coaching on the topic?
7. Is the position stated once, plainly — without repeating or over-justifying?
8. Is emphasis (italics/bold) used structurally, not decoratively?
9. Is the failure context as specific as the win?
10. Does this avoid feeding body comparison or perfectionism? (Important — this ICA carries elevated risk for disordered exercise/eating patterns. See ICA doc, Coaching System Requirements section.)

---

## Ideal Client Profile

The target client is a gay man, roughly 25–50, who wants to build muscle
and lose fat and feel confident in his body and in gay social/dating
spaces. Full psychographic detail — including body-image research,
comparison-culture dynamics, and coaching-safety requirements around
disordered eating/exercise risk — lives in:

> `references/ICA-Master-Psychographics-v3-Reclaim-Yourself.md`

The old software-engineer ICA (`client-profile.md`) is archived, not
deleted — it's been renamed `client-profile-v2-engineer-ARCHIVED.md` and kept
for any legacy engineer clients still active in coaching.

---

## Brand Colors

| Role             | Name           | Hex                   |
|:-----------------|:---------------|:----------------------|
| Background       | Coco’s Black   | `#191a1b`             |
| Surface          | Dark Surface   | `#22262b`             |
| Card             | Card Surface   | `#3c3f42`             |
| **Accent / CTA** | **CPZ Orange** | **`#ff8c00`**         |
| Text Primary     | Warm White     | `#f0ede8`             |
| Text Muted       | Slate Muted    | `#8a8f96`             |
| Code / Status    | Terminal Green | `#4ade80`             |
| Border           | Orange Border  | `rgba(255,130,0,0.2)` |

**Color usage rules:**
- Background is always `#191a1b` or `#1a1d21` for dark/digital outputs
- Warm Linen `#f2f0eb` is used for carousel light-mode backgrounds and print/PDF documents
- Orange appears on **one focal element per frame** — never scattered

---

## Typography

- **Barlow Condensed** — all display/headlines, UPPERCASE, 700–900 weight
- **Inter** — body copy (web, print, email, slides)
- **Poppins** — labels, data, section identifiers, and social media graphic body text (carousels)
- **League Spartan** — logo wordmark only (not general use)

⚠️ Known issue: the Barlow Condensed font file is currently missing from `cpz-carousels/fonts/` (it was removed when the font folder was swapped over to Inter/Poppins). Text and design specs still call for Barlow Condensed on headlines — the font file itself needs restoring in a separate design-focused pass.

> Full type specs (weights, usage rules, design application): `cpz-design/SKILL.md`

---

## Reference Files

| File                                                          | Load When                                                                                 |
|:---------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| `references/brand.md`                                          | Deeper voice work — authentic voice patterns, tone quick-reference, content structure arc |
| `references/ICA-Master-Psychographics-v3-Reclaim-Yourself.md`  | Audience-facing copy, marketing, community content — current ICA                          |
| `references/client-profile-v2-engineer-ARCHIVED.md`            | Legacy reference only — engineer-era clients still in active coaching                     |

---

## Focused Skills — Extend This Root

| Task                                         | Use This Skill    |
|:---------------------------------------------|:------------------|
| Image prompts, graphic specs, visual design  | **cpz-design**    |
| Skool classroom lessons, community posts     | **cpz-skool**     |
| Brainstorming post angles, content calendars | **cpz-research**  |
| Instagram carousel production end-to-end     | **cpz-carousels** |
| Reel and TikTok scripts, short-form video    | **cpz-reels**     |
| Blog posts, newsletters, long-form LinkedIn  | **cpz-longform**  |
