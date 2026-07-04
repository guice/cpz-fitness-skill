---
name: morning-boot
description: Daily morning boot sequence for CPZ Fitness — runs at 6am, generates motivation frame, training brief, reflection prompt, and content angle, then pushes directly to Notion Daily Journal*
---

Run Philip's morning boot sequence. Today's date is determined by the system clock. Use skill /cpz-fitness

## Context
- Owner: Philip, CPZ Fitness (no program/framework name)
- ICA: Gay men, roughly 25–50, who want to build muscle, lose fat, and feel confident in their bodies and in gay social/dating spaces
- Brand voice: Sarcastic Sage — dry humor, empathy, direct guidance
- Social: @philipz.fit on Instagram, TikTok, Threads, Facebook, BlueSky
- Weekly training split: Push (Mon) / Pull (Tue) / Legs (Wed) / Rest (Thu) / Push (Fri) / Pull (Sat) / Rest (Sun)

## Steps

1. Focus: Look for any over due tasks or any upcoming in the next week. Summerize their focus for the day, in priority by Important, Focus, and Date.

2. Determine today's training session from the weekly split above using the current day of the week.

3. Generate all four modules (see Output format below).

4. Push to Notion: create a new page in the **Daily Journal*** database using the `notion-create-pages` tool.

   Before writing the content string, fetch `notion://docs/enhanced-markdown-spec` to ensure correct Notion markdown syntax.

   **Parent:** `data_source_id` = `2f637b91-75fa-8199-a254-000b86a30139`

   **Properties to set:**
   - `Name` → full date string, e.g. "Friday, May 23, 2026"
   - `date:Date:start` → ISO-8601 date string, e.g. "2026-05-23"
   - `date:Date:is_datetime` → 0
   - `Training` → today's session as one of: Push / Pull / Legs / Rest

   **Page content** — one content string, two sections:

   **Section 1 — Morning Boot (pre-filled from today's output):**

   ```
   ## 🌅 Morning Boot

   **Focus:** [one-line focus]
   **Training:** [today's session, e.g. Push / Pull / Legs / Rest]

   ### Motivation
   [motivation paragraph]

   ### Training Brief
   [training brief paragraph]

   ### Reflection Prompt
   [the single reflection question]

   ### Content Angle
   **Hook:** [hook line]
   **Format:** [Reel / carousel / single post]
   [core idea, 2–3 sentences]
   ```

   **Section 2 — Daily Journal template (left blank for evening fill-in):**

   Reproduce the @Today template structure using correct Notion markdown:
   - A horizontal rule (`---`) followed by a heading `## 🌙 Evening Reflection` to visually divide the morning and evening sections
   - `### ✨ Highlight of the Day` with four to-do checkboxes: Achievements, Memorable Moments, Challenges Overcome, Lessons Learned
   - `### 📓 Daily Reflection` with six callout blocks:
     - Self-Reflection — embed today's reflection question as the opening prompt, followed by the standard text
     - Accomplishments
     - Challenges
     - Goals
     - Personal Growth
     - Tomorrow's Focus
   - `### 🙏 Daily Gratitude Journal` with 3 blank numbered lines
   - `### 💬 Daily Affirmation` with a blank line

5. Reply with only the Notion page URL so Philip can open it directly.

## Output format

Four modules, generated in step 3 and written into the Notion page:

**Motivation** — One sharp frame for the day. Why this work matters. Who Philip is building it for. Written in Sarcastic Sage voice — dry, direct, empathetic. Max 3 sentences. No hype language.

**Training brief** — Today's session name. Primary lift or movement focus. RPE target. One paragraph. Specific enough that Philip knows exactly what to do when he gets to the gym — no guesswork.

**Reflection** — One single journaling question. Calibrated to the current focus. Should require actual thought — not a checkbox. No bullet points. Just the question.

**Content angle** — One post angle for today. Include: hook (one line), format (Reel / carousel / single post), and the core idea in 2–3 sentences. Ready to develop — not a finished script.
