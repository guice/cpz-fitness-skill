---
name: morning-boot
description: Daily morning boot sequence for CPZ Fitness — runs at 6am, outputs motivation frame, training brief, reflection prompt, and content angle to ~/morning/
---

Run Philip's morning boot sequence. Today's date is determined by the system clock.

## Context
- Owner: Philip, CPZ Fitness / Geek to Greek coaching program
- ICA: Desk-bound male tech professionals, 30s–40s, skinny-fat, want to build muscle and confidence
- Brand voice: Sarcastic Sage — dry humor, analytical framing, empathy, direct guidance
- Social: @philipz.fit on Instagram, TikTok, Threads, Facebook, BlueSky
- Weekly training split: Push (Mon) / Pull (Tue) / Legs (Wed) / Rest (Thu) / Push (Fri) / Pull (Sat) / Rest (Sun)
- Baseline energy: 7/10 unless focus.txt says otherwise

## Steps

1. Read ~/morning/focus.txt if it exists. Use its contents as this week's focus. If it doesn't exist, default to: "Growing CPZ Fitness — building the Geek to Greek content pipeline and converting free community to paid coaching."

2. Determine today's training session from the weekly split above using the current day of the week.

3. Generate all four modules (see below).

4. Write the output to ~/morning/YYYY-MM-DD.md using today's date in the filename.

5. Confirm the file was written and state the output path.

## Output format

Write a markdown file with this exact structure:

---
date: [full date, e.g. Friday, May 23, 2026]
training: [today's session]
focus: [one-line focus pulled from focus.txt or default]
---

# Morning boot — [date]

## Motivation
[One sharp frame for the day. Why this work matters. Who Philip is building it for. Written in Sarcastic Sage voice — dry, direct, empathetic. Max 3 sentences. No hype language.]

## Training brief
[Today's session name. Primary lift or movement focus. RPE target. One paragraph. Specific enough that Philip knows exactly what to do when he gets to the gym — no guesswork.]

## Reflection
[One single journaling question. Calibrated to the current focus. Should require actual thought — not a checkbox. No bullet points. Just the question.]

## Content angle
[One post angle for today. Include: hook (one line), format (Reel / carousel / single post), and the core idea in 2–3 sentences. Ready to develop — not a finished script.]