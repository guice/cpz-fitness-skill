---
name: cpz-longform
description: CPZ Fitness long-form content writing. Use for blog posts, newsletters, LinkedIn articles, and full-length Skool classroom lessons. Extends cpz-fitness root — load cpz-fitness first.
---

# CPZ Fitness — Long-Form Content Skill

> Builds on **cpz-fitness** for brand DNA, voice, ICA, and colors. Load cpz-fitness first.

## Identity Quick Reference

| Field               | Value                                     |
|:--------------------|:------------------------------------------|
| **Website**         | https://www.philipz.fit                   |
| **Skool Community** | https://lnk.philipz.fit/skool             |
| **Handle**          | @philipz.fit                              |
| **Booking CTA**     | https://lnk.philipz.fit/free-system-audit |
| **PDF Asset CTA**   | https://lnk.philipz.fit/pdf-system-audit  |
| **Voice Archetype** | The "Sarcastic Sage"                      |

## Reference Files

| File                     | Load When                                                       |
|:-------------------------|:----------------------------------------------------------------|
| `references/platform.md` | When writing Skool classroom lessons or course-specific content |

---

## Format 1: Blog Post

**Length:** 800–1,500 words  
**Target platform:** philipz.fit blog or LinkedIn article  
**SEO note:** Write for the ICA first, algorithm second. If there's a natural keyword (e.g., "fitness coaching for gay men"), use it in the headline and once or twice in the body — but never at the expense of voice.

**Arc:**
1. **Hook** — Names the specific wrong belief or relatable failure. Philip's version of the mistake comes first. (100–150 words)
2. **Diagnosis** — Why this happens, plainly. No judgment. (200–300 words)
3. **Insight** — The reframe or data point that changes how the ICA sees the problem. (150–200 words)
4. **The Fix** — Clear, step-by-step guidance. No hedging. Trust the reader. (300–500 words)
5. **One next action** — Final paragraph: a single thing to do today. Not a question, not a summary — an action. (75–100 words)

**Formatting rules:**
- Headers use H2 for major sections, H3 for sub-points
- No bullet-heavy sections — write in full paragraphs except for genuine lists (exercises, steps)
- Bold used sparingly — only the single most important phrase per section
- No "in conclusion" or summary paragraph — the fix section IS the conclusion

---

## Format 2: Newsletter

**Length:** 400–600 words  
**Target platform:** Email list (Skool or external)  
**Cadence context:** Weekly, ideally tied to something happening in the community or a recent lesson

**Subject line formula:**
- `[The thing they're doing wrong]: [why it matters]` — "Skipping the gym isn't laziness: it's a pattern you can break"
- `The [counterintuitive truth] about [familiar topic]` — "The counterintuitive truth about eating more protein"
- `[Number] [specific thing]` — "One habit that changed how I train"

**Arc:**
1. **Personal observation** — Something Philip noticed this week: in the community, in his own training, in the world. First person, specific, brief. (75–100 words)
2. **Data or insight** — The insight layer. A stat, a reframe, a connection the ICA hasn't made. (150–200 words)
3. **Single CTA** — One action. Not three options, not a menu. One thing to do. Link or action. (75–100 words)

**Formatting rules:**
- No headers in newsletters — it should read like a thoughtful message, not a document
- One paragraph break per section
- Sign-off: Philip's name only. No "until next time" filler.
- P.S. line is acceptable and often performs well — use it for a secondary CTA or a one-liner observation

---

## Format 3: Skool Classroom Lesson

**Length:** 400–700 words per lesson  
**Target platform:** Skool Classroom

Load `references/platform.md` for the full course structure, lesson status, and module summaries before writing.

### Course 1 & 2 Lesson Format

1. **Opening hook** — Sarcastic or empathetic observation that names the problem. Philip's version of the mistake first.
2. **The diagnosis** — Why the problem exists, plainly. 1–2 paragraphs.
3. **The fix** — Clear, actionable guidance in logical steps. Full paragraphs — not bullet lists.
4. **The bridge** — One direct sentence pointing to the next lesson or action.

### Course 3 Lesson Format — ⚠️ Name Pending (was "Deployment Blueprint")

⚠️ This course's entire lesson architecture is built on a Kubernetes/Terraform deployment metaphor and is flagged for a dedicated redesign session — see `cpz-skool/references/platform.md`. Format mechanics below apply once that's resolved:

**Trigger Shift:** Opening sentence IS the H3 header. No welcome-back filler. No "in this lesson we'll cover." The first words the reader sees are the point.

**Active Reflection checkpoints** (all three types must appear, distributed across the lesson):
- `**Pause for a moment:**` — reflective
- `**Dig a little deeper:**` — reflective
- `**Take Action:**` — execution

**Key Takeaway:** Final element of every lesson. Bolded. Stated plainly — no metaphor needed (currently still written in the old deployment vocabulary pending the redesign above).

**No module-level overview pages.** Course-wide intro only. Modules go straight into content.

**Formatting rules (all lessons):**
- Full paragraphs — avoid bullet-point formatting except for numbered exercise steps
- Headers: H2 for sections, H3 for the Trigger Shift opener in Course 3
- Conversational and readable — this is a person talking, not a textbook

---

## Voice for Long-Form

1. Write in Philip's first person — he is the author, not AI
2. Self-implication before coaching — Philip's version of the mistake appears before the lesson
3. State the fix once, directly — no hedging, no "but of course everyone is different"
4. End with one clear action — not a reflection, not a question
5. Avoid hype language, excessive emojis, and motivational filler (see `references/brand.md` vocabulary guide)
6. Bold and italics are structural, not decorative — one bold phrase per paragraph maximum
