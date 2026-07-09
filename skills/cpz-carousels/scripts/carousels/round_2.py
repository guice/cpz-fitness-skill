"""
CPZ Fitness — Round 2 Carousel Content (Builds the Trust)
-------------------------------------------------------------
Carousels #07–#12. These deliver on the promise made in Round 1 —
practical, specific, useful. Each is a 3-slide arc (Hook / Content / CTA).
Run: python generate.py --round round_2 && python export.py
"""

CAROUSELS = {

    # ── #07 — Pillar 2: Workout Tips & Micro-Workouts ───────────────────────
    "c07_big_5_lifts": {
        "meta": {
            "id":      "c07",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "You don't need 12 exercises. You need 5 done consistently for a year. Here's the list I'd keep if everything else got cut.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Workout Tips",
                "heading": "5 lifts.\nEverything\nelse is optional.",
                "subhead": "I spent two years chasing exercise variety before I noticed the guys with real progress were doing almost none of it.",
            },
            {
                "bg":     "light",
                "tag":    "The List",
                "heading":      "If I had to\nkeep 5\nmovements.",
                "heading_size": 44,
                "pills": ["Squat", "Hinge", "Push", "Pull", "Carry"],
                "info_card": {
                    "label": "Why this works",
                    "body": "These five cover every major muscle group and movement pattern you actually need. More exercises just means less practice on the ones that matter.",
                },
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Master 5.\nSkip the\nother 40.",
                "subhead":  "Save this and build your next session around these.",
                "cta_text": "Save this post",
                "glass_text": "Simple isn't the beginner version. It's the version that still works at year three.",
            },
        ],
    },

    # ── #08 — Pillar 3: Nutrition & Protein Strategy ────────────────────────
    "c08_no_rigid_meal_plan": {
        "meta": {
            "id":      "c08",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "I don't hand out meal plans. Not because I'm lazy — because rigid meal plans have a 100% failure rate the first time real life happens.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Nutrition",
                "stripe":  "No meal plan.",
                "heading": "On purpose.",
                "subhead": "I tried the rigid version for years. It worked great, right up until the first dinner invite.",
            },
            {
                "bg":     "dark",
                "tag":    "What I Do Instead",
                "heading":      "One number.\nFlexible\neverything else.",
                "heading_size": 42,
                "body":   "Hit your protein target. Build the rest of your day around food you actually like. That's the whole system — and it survives contact with a real week.",
                "bullets": [
                    {"label": "Protein first, every meal.", "sub": "Everything else flexes around it."},
                    {"label": "No foods are banned.", "sub": "Just budgeted for."},
                    {"label": "One dinner out doesn't reset the week.", "sub": "It's a meal, not a verdict."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Structure,\nnot a cage.",
                "subhead":  "Follow for nutrition that fits an actual social life.",
                "cta_text": "Follow @philipz.fit",
                "glass_text": "The plan that survives your real life beats the perfect plan that doesn't.",
            },
        ],
    },

    # ── #09 — Pillar 4: Consistency & Habit Systems ─────────────────────────
    "c09_habit_stacking": {
        "meta": {
            "id":      "c09",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "I stopped trying to add a new habit into empty space. I started binding it to something I already do without thinking. That's the whole trick.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Consistency",
                "heading": "Stop trying\nto remember\nto train.",
                "subhead": "Memory is a bad system. Triggers are a good one.",
            },
            {
                "bg":     "light",
                "tag":    "Habit Stacking",
                "heading":      "Bind it to\nsomething you\nalready do.",
                "heading_size": 42,
                "body":   "You already have habits running on autopilot — coffee, commute, the first thing you do when you get home. Attach the new habit to one of those, and you stop needing willpower at all.",
                "info_card": {
                    "label": "Try this",
                    "body": "\"After I [thing I already do], I will [put on my shoes / do one set / open the app].\" Small enough that skipping it feels weirder than doing it.",
                },
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Pick your\ntrigger\ntoday.",
                "subhead":  "Comment the habit you're binding it to — I'll read every one.",
                "cta_text": "Drop it in the comments",
                "glass_text": "The habit doesn't need motivation once it's attached to something automatic.",
            },
        ],
    },

    # ── #10 — Pillar 5: Body Image, Confidence & Gay Culture ────────────────
    "c10_profile_photo_problem": {
        "meta": {
            "id":      "c10",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "I rewrote my dating profile four times before I ever changed my body. The anxiety wasn't about the photo. It was about what I thought the photo proved.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Body Image",
                "stripe":  "The photo",
                "heading": "isn't the\nproblem.",
                "subhead": "I spent more time picking the angle than I ever spent actually training.",
            },
            {
                "bg":     "dark",
                "tag":    "What's Actually Happening",
                "heading":      "You're not\nanxious about\na photo.",
                "heading_size": 42,
                "body":   "You're anxious about being seen and judged in one frame, by strangers, with no context. That fear doesn't fully go away with a better body — it goes down when you stop needing everyone's approval to feel solid.",
                "bullets": [
                    {"label": "A stronger body helps. It's not the whole fix.", "sub": "The confidence has to be built alongside it, not after it."},
                    {"label": "Nobody is scrutinizing you as hard as you are.", "sub": "Most people scroll past in under a second."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Build both\nat once.",
                "subhead":  "Follow for a coach who works on the body and the story you tell yourself about it.",
                "cta_text": "Follow @philipz.fit",
                "glass_text": "You don't have to wait to be 'ready' to post the photo, take the trip, or show up.",
            },
        ],
    },

    # ── #11 — Pillar 1: Data-Driven Insights ────────────────────────────────
    "c11_protein_targets_math": {
        "meta": {
            "id":      "c11",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "Most guys are eating half the protein they think they are. Here's the actual math — not the bro-science version.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Data",
                "heading": "You're probably\neating half the\nprotein you think.",
                "subhead": "Not a guess. This is the most common gap I see when someone actually tracks for a week.",
            },
            {
                "bg":     "surface",
                "tag":    "The Real Number",
                "heading":      "1.6–2.2g per\nkg of\nbodyweight.",
                "heading_size": 40,
                "data_card": {
                    "rows": [
                        {"label": "175 lb (79 kg) man", "value": "126–174g/day", "kind": "accent"},
                        {"label": "Typical actual intake", "value": "~70–90g/day", "kind": "negative"},
                        {"label": "The gap", "value": "40–100g short", "kind": "negative"},
                    ],
                },
                "body": "That's the range that supports muscle retention and growth. Most guys are nowhere close — not from lack of effort, just lack of tracking.",
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Do the math\non your own\nnumber.",
                "subhead":  "Save this and check your intake against it this week.",
                "cta_text": "Save this post",
                "glass_text": "You can't hit a target you've never actually measured yourself against.",
            },
        ],
    },

    # ── #12 — Pillar 2: Workout Tips & Micro-Workouts ───────────────────────
    "c12_rpe_explained": {
        "meta": {
            "id":      "c12",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "RPE sounds like jargon. It's actually the simplest tool in the gym: how many more reps could you have done? That's it.",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Workout Tips",
                "stripe":  "RPE",
                "heading": "isn't as\ncomplicated\nas it sounds.",
                "subhead": "I avoided learning it for a year because the name made it sound technical. It's not.",
            },
            {
                "bg":     "dark",
                "tag":    "How It Actually Works",
                "heading":      "How many more\nreps could\nyou have done?",
                "heading_size": 42,
                "body":   "That question is RPE — Rate of Perceived Exertion. Rate the set 1 to 10. A 10 means you couldn't have done one more rep with good form.",
                "bullets": [
                    {"label": "RPE 7–8 for most working sets.", "sub": "2–3 reps left in the tank — hard, but repeatable week to week."},
                    {"label": "RPE 9–10 occasionally, not every set.", "sub": "Grinding every set to failure burns you out faster than it builds you up."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Rate your\nnext set.\nThat's it.",
                "subhead":  "Save this before your next session and try it on one lift.",
                "cta_text": "Save this post",
                "glass_text": "No app, no equipment — just an honest read on effort.",
            },
        ],
    },

}
