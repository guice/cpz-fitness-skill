"""
CPZ Fitness — Round 2 Carousel Content (Systems — Builds the Trust)
---------------------------------------------------------------------
Carousels #07–#12. These deliver on the promise made in Round 1.
Each is a 3-slide Arc B (Hook / Content / CTA) in Tension mode.
Run: python generate_r2.py && python export_r2.py
"""

CAROUSELS = {

    # ── #07 ────────────────────────────────────────────────────────────────
    "c07_workday_boundary": {
        "meta": {
            "id":      "c07",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "The workout slot doesn't get added to your schedule. It IS the schedule. 🗓️",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Systems",
                "heading": "Your workday\nhas no\noff switch.",
                "subhead": "That's not a productivity flex. That's why you can't train.",
                "ghost":   "OFF",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Fix",
                "heading":      "Work ends\nwhen you\nclose the tab.",
                "heading_size": 46,
                "body":   "Except you never close the tab. Training isn't failing to compete with work — it's failing to exist on the calendar at all.",
                "bullets": [
                    {"label": "A shutdown ritual isn't soft. It's a system.", "sub": "Workday ends → 5-min reset → you move. Non-negotiable."},
                    {"label": "The slot has to be blocked like a prod deploy.", "sub": "Flexible everything else. Fixed on this."},
                    {"label": "Your calendar reflects your priorities.", "sub": "Right now it reflects everyone else's. That's the bug."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Make training\nthe default.\nNot the exception.",
                "subhead":  "Follow for systems that make the\nworkout slot untouchable.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── #08 ────────────────────────────────────────────────────────────────
    "c08_home_gym": {
        "meta": {
            "id":      "c08",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "The gear was never the problem. The environment around the gear was. 🏠",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Systems",
                "stripe":  "Expensive",
                "heading": "clothes rack.",
                "subhead": "You bought the equipment. Used it for two weeks. We both know what happened next.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The Diagnosis",
                "heading":      "The gear\nwasn't the\nbug. Your env\nwas.",
                "heading_size": 44,
                "body":   "Every cue in your space said: work, scroll, eat. The rack was surrounded by signals pointing the other way.",
                "bullets": [
                    {"label": "Path of least resistance wins. Every time.", "sub": "If the couch is closer than the barbell, the couch wins."},
                    {"label": "Environment design isn't décor.", "sub": "It's your default behaviour rendered in physical space."},
                    {"label": "Refactor the space. Not just the habits.", "sub": "Friction removal is the actual system upgrade."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Refactor your\nenvironment.\nNot your will.",
                "subhead":  "Follow to learn how to design a space\nthat trains you by default.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── #09 ────────────────────────────────────────────────────────────────
    "c09_hardware": {
        "meta": {
            "id":      "c09",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "You wouldn't run prod on a server that never reboots. Stop doing it to your body. 🖥️",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Systems",
                "heading": "You protect\nyour setup.\nNot yourself.",
                "subhead": "Dual monitors. Mech keyboard. Ergonomic chair. The hardware running all of it? Neglected.",
                "ghost":   "CPU",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Reframe",
                "heading":      "Your body\nis the\ninfrastructure.",
                "heading_size": 46,
                "body":   "The cognitive edge you're protecting is being eroded by the same sedentary routine you think is saving you time.",
                "bullets": [
                    {"label": "Sleep is RAM. You're running on 2GB.", "sub": "No patch fixes a server that never reboots."},
                    {"label": "Training is garbage collection.", "sub": "Skip it long enough and the memory leaks take over."},
                    {"label": "Stress without recovery is a runaway process.", "sub": "Kill it properly or it kills your output."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Maintain the\nhardware.\nProtect the output.",
                "subhead":  "Follow to treat your body like the\ninfrastructure it actually is.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── #10 ────────────────────────────────────────────────────────────────
    "c10_lower_threshold": {
        "meta": {
            "id":      "c10",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "Motivation follows action. It doesn't precede it. Start small. Start now. ⚡",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Systems",
                "stripe":  "Motivation",
                "heading": "isn't coming.",
                "subhead": "Waiting to feel ready after a 10-hour deep work session is a strategy with a 0% success rate.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The System",
                "heading":      "Lower the\nthreshold\nto start.",
                "heading_size": 48,
                "body":   "The men who stay consistent don't wait to feel ready. They designed a version so small it's almost impossible to skip.",
                "bullets": [
                    {"label": "20 minutes. Pre-decided. No choices.", "sub": "Decision fatigue is the enemy. Eliminate it before 6pm."},
                    {"label": "The threshold to start < the threshold to quit.", "sub": "That's the whole architecture. That's it."},
                    {"label": "Motivation follows action — not the other way.", "sub": "The feeling comes after the first rep. Never before."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Build the\nsystem that\nstarts itself.",
                "subhead":  "Follow for the minimum effective dose\napproach that actually compounds.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── #11 ────────────────────────────────────────────────────────────────
    "c11_wrong_program": {
        "meta": {
            "id":      "c11",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "The failure wasn't you. It was a compatibility issue. Here's the patch. 🔧",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "Systems",
                "heading": "6 programs.\nZero results.\nNot your fault.",
                "subhead": "You don't lose interest because you lack discipline. You're running fitness software built for a different brain.",
                "ghost":   "ERR",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Diagnosis",
                "heading":      "It's a\ncompatibility\nissue.",
                "heading_size": 46,
                "body":   "Standard programs assume linear motivation, low novelty needs, and emotional consistency. That's not your stack.",
                "bullets": [
                    {"label": "Your brain needs strong cues to initiate.", "sub": "Vague 'go to the gym' tasks don't compile."},
                    {"label": "Variety within structure — not chaos.", "sub": "Flexible enough to hold your interest. Fixed enough to compound."},
                    {"label": "The fix isn't more discipline.", "sub": "It's an architecture built for high-output analytical minds."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Run the right\nprogram for\nyour brain.",
                "subhead":  "Follow for routines actually built for\nhow analytical, high-output people work.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

    # ── #12 ────────────────────────────────────────────────────────────────
    "c12_stress_eating": {
        "meta": {
            "id":      "c12",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "The kitchen at 9pm isn't a nutrition problem. It's a nervous system problem. Here's what fixes it. 🧠",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "Systems",
                "stripe":  "9pm.",
                "heading": "Not hungry.\nIn the kitchen.",
                "subhead": "You know this feeling. And you know it has nothing to do with food.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The Root Cause",
                "heading":      "Your nervous\nsystem is\noverloaded.",
                "heading_size": 44,
                "body":   "10 hours of high-focus cognitive work with no physical discharge. The food, the scroll, the drink — these aren't bad habits. They're stress regulation attempts.",
                "bullets": [
                    {"label": "Your body is trying to discharge tension.", "sub": "The only way it knows how, because you never moved."},
                    {"label": "Training isn't more stress on top of your day.", "sub": "It's the mechanism that lets your system actually reset."},
                    {"label": "A 20-min session changes the 9pm entirely.", "sub": "Not willpower. Physiology. The urge drops because the need is met."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "Fix the system.\nNot the\nsymptom.",
                "subhead":  "Follow to learn what emotional recovery\nactually looks like for someone like you.",
                "cta_text": "Follow @philipz.fit",
            },
        ],
    },

}
