"""
CPZ Fitness — Round 1 Carousel Content (Stop the Scroll)
-----------------------------------------------------------
Carousels #3, #5, #6. Pattern-interrupt hooks — the job here is to
stop the scroll and earn the follow, not to close anything.
Run: python generate.py --round round_1 && python export.py
"""

CAROUSELS = {

    # ── Carousel 3 — Pillar 4: Consistency & Habit Systems ──────────────────
    "c3_not_laziness": {
        "meta": {
            "id":      "c3",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "You're not skipping the gym because you're lazy. You're skipping it because the plan needs a decision every time, and decisions are the thing you're out of by 6pm.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Consistency",
                "heading": "You're not\nlazy.",
                "subhead": "You're just out of decisions by the time you'd need to make one about the gym.",
            },
            {
                "bg":     "light",
                "tag":    "The Real Reason",
                "heading":      "Willpower runs\nout. Habits\ndon't ask.",
                "heading_size": 44,
                "body":   "I used to think I had a discipline problem. I didn't — I had a design problem. Every day I was re-deciding whether to go, and some days the answer lost.",
                "info_card": {
                    "label": "The fix",
                    "body": "Remove the decision. Same days, same time, same first exercise, every week. You're not choosing anymore — you're just following the plan you already made.",
                },
                "pills": ["Habit Design", "No Willpower Needed", "Pre-Decided"],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Stop deciding.\nStart\nscheduling.",
                "subhead":  "Save this for the next time you're negotiating with yourself at 6pm.",
                "cta_text": "Save this post",
                "glass_text": "Follow for more on building a body you don't have to talk yourself into.",
            },
        ],
    },

    # ── Carousel 5 — Pillar 5: Body Image, Confidence & Gay Culture ─────────
    "c5_shirtless_dread": {
        "meta": {
            "id":      "c5",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "I avoided pools for years because I didn't want anyone to see me without a shirt. The fix wasn't abs. It was deciding I got to show up as I was.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Body Image",
                "stripe":  "I skipped",
                "heading": "three summers\nof pool invites.",
                "subhead": "Not because I was busy. Because I didn't want anyone to see me without a shirt on.",
            },
            {
                "bg":     "light",
                "tag":    "What Actually Changed",
                "heading":      "The fix\nwasn't abs.",
                "heading_size": 46,
                "body":   "I got stronger eventually, sure. But I went to the pool the summer before that happened too — because I got tired of missing my life waiting for a body I hadn't built yet.",
                "info_card": {
                    "label": "The pattern",
                    "body": "Waiting to be seen until you're 'ready' isn't caution. It's a decade you don't get back, spent auditing yourself instead of living.",
                },
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Show up as\nyou are.\nToday.",
                "subhead":  "Follow for a coach who's actually been where you are.",
                "cta_text": "Follow @philipz.fit",
                "glass_text": "This isn't about being ripped by summer. It's about not skipping your own life.",
            },
        ],
    },

    # ── Carousel 6 — Pillar 1: Data-Driven Insights ─────────────────────────
    "c6_slow_gain_pattern": {
        "meta": {
            "id":      "c6",
            "handle":  "@philipz.fit",
            "brand":   "CPZ Fitness",
            "caption": "2 to 6 pounds a year. That's the whole pattern. It never feels like an emergency, which is exactly why it works.",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Data",
                "heading": "You didn't\ngain 20 lbs\nthis year.",
                "subhead": "You gained 2 to 6. Every year. For a while. That's the part nobody warns you about.",
            },
            {
                "bg":     "surface",
                "tag":    "The Math",
                "heading":      "Slow enough\nto ignore.\nFast enough\nto add up.",
                "heading_size": 40,
                "data_card": {
                    "rows": [
                        {"label": "Typical yearly gain", "value": "2–6 lbs", "kind": "neutral"},
                        {"label": "Over 5 years", "value": "10–30 lbs", "kind": "negative"},
                        {"label": "Feels like, each year", "value": "\"Nothing\"", "kind": "accent"},
                    ],
                },
                "body": "It's invisible year to year because it's supposed to be. Nobody panics over 3 pounds. That's exactly the problem.",
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "heading":  "Catch it\nwhile it's\nstill small.",
                "subhead":  "Save this. Check in with your own numbers this week.",
                "cta_text": "Save this post",
                "glass_text": "The earlier you notice the trend, the smaller the fix has to be.",
            },
        ],
    },

}
