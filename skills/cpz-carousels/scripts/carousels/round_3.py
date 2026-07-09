"""
CPZ Fitness — Round 3 Carousel Content (Earns the Conversation)
---------------------------------------------------------------
Carousels #13–#18. Round 1 stopped the scroll. Round 2 built the trust.
Round 3 handles the real objection behind each topic and closes toward
a free consultation — see cpz-carousels/SKILL.md CTA Slide Options.
Run: python generate.py --round round_3 && python export.py
"""

CAROUSELS = {

    # ── #13 — Pillar 3: Nutrition & Protein Strategy ────────────────────────
    "c13_alcohol_honest_math": {
        "meta": {
            "id":      "c13",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "You don't have to quit drinking to make progress. You just have to stop pretending it's free. Here's the honest math.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Nutrition",
                "heading": "You don't have\nto quit\ndrinking.",
                "subhead": "You just have to stop pretending a night out costs nothing. It costs something specific — and it's knowable.",
            },
            {
                "bg":     "light",
                "tag":    "The Honest Version",
                "heading":      "It's not a\nmoral failure.\nIt's a number.",
                "heading_size": 42,
                "body":   "A drink is calories, full stop. Not a cheat, not a setback — just a number you can plan around instead of feel guilty about.",
                "bullets": [
                    {"label": "Bank a little from earlier meals on a big night.", "sub": "Not starving yourself — just shifting where the calories land."},
                    {"label": "Lower-calorie drinks aren't a personality trait.", "sub": "They're just math that leaves more room for the rest of your day."},
                    {"label": "One night doesn't undo a month of consistency.", "sub": "Only a pattern of nights does."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Want a plan\nthat fits your\nactual social life?",
                "subhead":  "No lecture. Just a system that accounts for the life you're actually living.",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "We build the plan around your week, not a fantasy version of it.",
            },
        ],
    },

    # ── #14 — Pillar 4: Consistency & Habit Systems ─────────────────────────
    "c14_two_minute_rule": {
        "meta": {
            "id":      "c14",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "On your worst day, the goal isn't a good workout. It's two minutes. Here's why that's not a cop-out — it's the whole strategy.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Consistency",
                "stripe":  "Worst day?",
                "heading": "Two minutes\nis the goal.",
                "subhead": "Not a good session. Not a great one. Two minutes. That's the entire ask on the days you have nothing left.",
            },
            {
                "bg":     "dark",
                "tag":    "Why This Works",
                "heading":      "It's not\nabout the\ntwo minutes.",
                "heading_size": 42,
                "body":   "It's about not becoming someone who skips. The two minutes protects your identity as someone who shows up — the actual training happens on the other days.",
                "info_card": {
                    "label": "The real risk on bad days",
                    "body": "Isn't a weak session. It's the story you start telling yourself about who you are when you skip twice in a row.",
                },
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Never miss\ntwice.\nThat's the rule.",
                "subhead":  "Want a program built with a floor for your actual bad days — not just your good ones?",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "We plan for your real week, including the days that fall apart.",
            },
        ],
    },

    # ── #15 — Pillar 5: Body Image, Confidence & Gay Culture ────────────────
    "c15_getting_lean_confidence": {
        "meta": {
            "id":      "c15",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "Getting leaner didn't fix my confidence. Here's what actually did — and why the physique alone was never going to be enough.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Body Image",
                "heading": "Getting lean\ndidn't fix\nmy confidence.",
                "subhead": "I thought it would. I got the body and brought the same insecure guy along with it.",
            },
            {
                "bg":     "light",
                "tag":    "What Actually Did",
                "heading":      "The body work\nand the story\nwork happen\ntogether.",
                "heading_size": 38,
                "body":   "The physique gave me a reason to stop hiding. It didn't give me permission — I had to build that separately, on purpose, at the same time.",
                "bullets": [
                    {"label": "Training built the body I wanted.", "sub": "That part was straightforward — show up, progress the load."},
                    {"label": "Confidence had to be practiced, not earned.", "sub": "Showing up shirtless before I felt 'ready' is what actually moved it."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Build both.\nOn purpose.\nAt the same time.",
                "subhead":  "This is what my coaching actually is — not just a training plan.",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "We work on the physique and the self-worth story running underneath it.",
            },
        ],
    },

    # ── #16 — Pillar 1: Data-Driven Insights ────────────────────────────────
    "c16_sleep_recovery_data": {
        "meta": {
            "id":      "c16",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "6 hours of sleep isn't a lifestyle choice. It's a tax on every rep you did that week. Here's what the data actually says.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Data",
                "stripe":  "6 hours",
                "heading": "is costing\nyou gains.",
                "subhead": "Not a guilt trip. Just what the recovery research actually shows.",
            },
            {
                "bg":     "surface",
                "tag":    "What The Research Shows",
                "heading":      "Sleep is where\nthe muscle\nactually gets built.",
                "heading_size": 36,
                "data_card": {
                    "rows": [
                        {"label": "Recommended sleep", "value": "7–9 hrs", "kind": "accent"},
                        {"label": "Under 6 hrs, protein synthesis", "value": "measurably reduced", "kind": "negative"},
                        {"label": "Training + poor sleep", "value": "diminished returns", "kind": "negative"},
                    ],
                },
                "body": "The workout is the stimulus. Sleep is when your body actually does the rebuilding. Skimp on one and you're taxing the other.",
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Want a plan\nthat treats\nrecovery as\npart of the work?",
                "subhead":  "Not just sets and reps — the whole picture.",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "Training, nutrition, and recovery, built as one system — not three separate guesses.",
            },
        ],
    },

    # ── #17 — Pillar 2: Workout Tips & Micro-Workouts ───────────────────────
    "c17_bodyweight_overload": {
        "meta": {
            "id":      "c17",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "No gym access isn't a legitimate reason to stop progressing. Here's how progressive overload works with just your bodyweight.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Workout Tips",
                "heading": "\"No gym\" isn't\nthe real\nproblem.",
                "subhead": "You can still get stronger with nothing but your bodyweight. Most people just don't know how to progress it.",
            },
            {
                "bg":     "light",
                "tag":    "How To Progress It",
                "heading":      "Overload\nwithout\nadding weight.",
                "heading_size": 40,
                "bullets": [
                    {"label": "Slow the tempo down.", "sub": "A 4-second lowering phase makes bodyweight squats brutal, fast."},
                    {"label": "Reduce leverage.", "sub": "Single-leg, single-arm versions of anything you've mastered."},
                    {"label": "Shrink the rest, not the effort.", "sub": "Same reps, less recovery — the work gets harder without adding a single plate."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Want a real\nprogram for\nwherever you\nactually train?",
                "subhead":  "Home, hotel room, or full gym — the plan should fit your access, not the other way around.",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "Your equipment shouldn't be the reason your progress stalls.",
            },
        ],
    },

    # ── #18 — Pillar 3: Nutrition & Protein Strategy ────────────────────────
    "c18_50g_protein_breakfast": {
        "meta": {
            "id":      "c18",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "50 grams of protein before you leave the house. No powder required. Here's what that actually looks like on a plate.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Nutrition",
                "stripe":  "50g protein.",
                "heading": "Before 9am.",
                "subhead": "Not a supplement stack. Real food, and less of it than you'd think.",
            },
            {
                "bg":     "dark",
                "tag":    "What It Looks Like",
                "heading":      "Front-load\nthe day. Coast\nthe rest of it.",
                "heading_size": 38,
                "body":   "Hitting your protein target gets dramatically easier when the first meal isn't an afterthought. This is the one change that moves the needle most.",
                "data_card": {
                    "rows": [
                        {"label": "4 whole eggs", "value": "24g", "kind": "neutral"},
                        {"label": "150g Greek yogurt", "value": "15g", "kind": "neutral"},
                        {"label": "1 cup cottage cheese", "value": "~14g extra", "kind": "accent"},
                    ],
                },
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Want the full\nnutrition system?\nNot just breakfast.",
                "subhead":  "Protein targets, real food, zero rigid meal plans.",
                "cta_text": "Free Consultation → link in bio",
                "glass_text": "This is one meal. The full plan covers the whole week.",
            },
        ],
    },

}
