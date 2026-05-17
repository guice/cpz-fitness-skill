"""
CPZ Fitness — Carousel Content Definitions
-------------------------------------------
Each carousel is a list of slide dicts fed to build_carousel().
Add new carousels here. Run generate.py to rebuild HTML files.
"""

CAROUSELS = {

    # ── Carousel 3 ─────────────────────────────────────────────────────────
    "c3_smart_guys": {
        "meta": {
            "id":      "c3",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "You've done more research than most trainers. You still haven't done the work. Let's fix the actual bug. 🧠",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Mindset",
                "heading": "You've read more\nabout fitness than\nyour PT has.",
                "subhead": "And you haven't been to the gym in three weeks. Interesting.",
                "ghost":   "NO",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Bug",
                "heading":      "Knowledge\n≠\nExecution.",
                "heading_size": 44,
                "body":   "The men who changed their bodies didn't know more than you. They stopped optimizing and started moving.",
                "quote":  "You're not under-educated. You're under-started. The gap isn't information — it's that first rep.",
                "bullets": [
                    {"label": "You've watched the tutorials.",      "sub": "The algorithm thinks you're already in shape."},
                    {"label": "You know the compounds, the macros.", "sub": "Your body has not received this information."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Stop reading.\nStart lifting.",
                "subhead":  "Follow for systems built\naround how you actually work.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── Carousel 5 ─────────────────────────────────────────────────────────
    "c5_all_or_nothing": {
        "meta": {
            "id":      "c5",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "All-or-nothing thinking is a feature in your codebase. In fitness, it's a bug. Here's the patch. 🔧",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Mindset",
                "stripe":  "All in.",
                "heading": "Or nothing.",
                "subhead": "Two weeks on. Two weeks of guilt. Repeat forever. Sound familiar?",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The Fix",
                "heading":      "Binary thinking\nis a bug\nin this context.",
                "heading_size": 46,
                "body":   "You run it everywhere else in life. In fitness, it's destroying your progress.",
                "bullets": [
                    {"label": "A 60% session still counts.",       "sub": "A degraded deploy beats a cancelled one every time."},
                    {"label": "One bad meal ≠ corrupted week.",    "sub": "Stop running rm -rf on your progress over one dinner."},
                    {"label": "The goal is fault-tolerant, not perfect.", "sub": "Systems that survive imperfection beat systems that don't start."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Build a system\nthat survives\nreal life.",
                "subhead":  "Follow for fitness built around\nhow analytical brains actually work.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── Carousel 6 ─────────────────────────────────────────────────────────
    "c6_too_tired": {
        "meta": {
            "id":      "c6",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "It's not laziness. It's cognitive depletion. Here's how to train around it instead of fighting it. 💻",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Mindset",
                "heading": "You're not\nlazy.",
                "stripe":  "You're fried.",
                "subhead": "And telling yourself to 'just be more disciplined' is the worst possible diagnosis.",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Diagnosis",
                "heading":      "10hrs of deep\nwork depletes\nyour start fuel.",
                "heading_size": 40,
                "body":   "After a full day of high-focus coding, your prefrontal cortex is genuinely empty. The motivation isn't coming back tonight. That's physiology, not character.",
                "quote":  "You don't need motivation to start. You need a lower threshold. The workout that exists beats the perfect one that doesn't.",
                "bullets": [
                    {"label": "20 minutes. Pre-decided. No choices.", "sub": "Decision fatigue is the enemy. Remove it entirely."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Lower the\nthreshold.\nStart anyway.",
                "subhead":  "Follow if you've ever been too tired\nto want it — but still want to change.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

}
