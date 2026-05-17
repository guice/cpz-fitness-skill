"""
CPZ Fitness — Round 3 Carousel Content (Offer — Earns the DM)
---------------------------------------------------------------
Carousels #13–#18.
These handle the 6 core objections and end with DM "DEBUG" as the CTA.
Round 1 stopped the scroll. Round 2 built the trust. Round 3 earns the conversation.
Run: python generate_r3.py && python export_r3.py
"""

CAROUSELS = {

    # ── #13 — Objection: "I should be able to figure this out myself" ──────
    "c13_figure_it_out": {
        "meta": {
            "id":      "c13",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "Senior engineers don't brag about doing everything alone. They bring in the right specialist. DM me DEBUG. 🔧",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "The Offer",
                "heading": "You should\nnot have to\nfigure this out.",
                "subhead": "You're smart enough to fix this alone. You've also been smart enough to not fix it for 3 years.",
                "ghost":   "FIX",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The Reframe",
                "heading":      "Senior devs\nbring in\nspecialists.",
                "heading_size": 46,
                "body":   "Needing a co-architect isn't a hit to your ego. It's how high-performers remove bottlenecks from the one system they can't replace.",
                "bullets": [
                    {"label": "You bring the constraints and the brain.", "sub": "I bring the system, the guardrails, and the reps."},
                    {"label": "10% teaching. 90% doing.", "sub": "No more research rabbit holes. Just a plan that compiles in your actual life."},
                    {"label": "Built around your stack — not a template.", "sub": "Remote work, on-call rotations, late deploys. All of it accounted for."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "Tell me what's broken. I'll tell you\nexactly what we build first.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

    # ── #14 — Objection: "I don't have time" ───────────────────────────────
    "c14_no_time": {
        "meta": {
            "id":      "c14",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "If your plan only works when life is calm, it's not a plan. It's a vacation. DM me DEBUG. ⏱️",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "The Offer",
                "stripe":  "No time",
                "heading": "is not the\nproblem.",
                "subhead": "You have time for standups, Slack, and 45 minutes of doomscrolling. The time exists. The system doesn't.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The System",
                "heading":      "We design\naround your\nactual week.",
                "heading_size": 46,
                "body":   "Not a fantasy schedule where you wake up at 5am and have zero meetings. Your real week — with crunch, on-call, and kids.",
                "bullets": [
                    {"label": "A plan, B plan, C plan. Always a valid option.", "sub": "Full session. 20-minute compressed. 10-minute floor. No zeroes."},
                    {"label": "Pre-decided slots. Zero decision fatigue.", "sub": "The only question is which version you run — not whether you run."},
                    {"label": "Missed weeks are data, not failure.", "sub": "We treat them like a bug report and adjust the system. Not your character."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "Show me your calendar. I'll show you\nwhere the sessions already live.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

    # ── #15 — Objection: "Online coaching won't work for me" ───────────────
    "c15_online_coaching": {
        "meta": {
            "id":      "c15",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "You already work remotely, collaborate async, and ship without anyone standing over you. This is the same thing. DM me DEBUG. 💻",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "The Offer",
                "heading": "Online\ncoaching\nwon't work.",
                "subhead": "You're right — generic online coaching won't. But you've never had a system built for how you actually work.",
                "ghost":   "ASYNC",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "How It Works",
                "heading":      "Built for the\nway your\nbrain works.",
                "heading_size": 44,
                "body":   "You already ship code remotely, run async standups, and deliver without a manager watching. This is that — but for your body.",
                "bullets": [
                    {"label": "Clear binary compliance checks.", "sub": "Did you train 2x this week? Did you hit protein 4 days? That's the whole report."},
                    {"label": "Accountability that feels like a teammate.", "sub": "Not a drill sergeant. A co-architect who reviews the system with you weekly."},
                    {"label": "When you miss — we treat it as architecture data.", "sub": "Cool. Let's adjust the system so it handles this scenario next time."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "Let's run a quick audit on your current\nstack and find the actual bottleneck.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

    # ── #16 — Objection: "What if I invest and still fail?" ────────────────
    "c16_fear_of_failure": {
        "meta": {
            "id":      "c16",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "Every previous failure was a data point. Not a verdict. DM me DEBUG. 📊",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "The Offer",
                "stripe":  "What if I",
                "heading": "fail again?",
                "subhead": "That question has kept you stuck longer than any bad program ever did.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The Truth",
                "heading":      "Every failure\nwas a bad\nsystem. Not you.",
                "heading_size": 44,
                "body":   "You didn't fail because you're undisciplined. You failed because the program wasn't built for your life. That's fixable.",
                "bullets": [
                    {"label": "We don't build for perfect conditions.", "sub": "We build for your worst weeks — because that's when systems actually get tested."},
                    {"label": "Early wins are non-negotiable.", "sub": "2 weeks of consistent training. Noticeably better sleep. Fewer 3pm crashes. Fast."},
                    {"label": "Failure is treated as a bug report.", "sub": "Not a character verdict. We adjust the architecture and run the test again."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "Tell me what broke last time.\nI'll tell you exactly why — and what's different now.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

    # ── #17 — Objection: "I'll start when work calms down" ─────────────────
    "c17_wait_for_calm": {
        "meta": {
            "id":      "c17",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "The calm season is a myth. We build for the chaos. DM me DEBUG. 🌪️",
        },
        "slides": [
            {
                "bg":      "dark",
                "layout":  "bottom",
                "is_hook": True,
                "tag":     "The Offer",
                "heading": "Work will\nnever calm\ndown.",
                "subhead": "There will always be a release, a sprint, a reorg. You know this. You've been waiting 18 months.",
                "ghost":   "SOON",
            },
            {
                "bg":     "light",
                "layout": "bottom",
                "tag":    "The System",
                "heading":      "We design\nfor crunch\nseason.",
                "heading_size": 46,
                "body":   "Not the version of your life where everything is calm. The version with on-call, late PRs, and back-to-back meetings.",
                "bullets": [
                    {"label": "Crunch mode has a training protocol.", "sub": "3 days become 2. Full sessions become 20 minutes. The system degrades gracefully."},
                    {"label": "Starting now is the advantage.", "sub": "The engineer who starts in chaos builds a system that actually survives. Waiting builds nothing."},
                    {"label": "The compounding started the day you began.", "sub": "Not the day your calendar cleared. That day never comes."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "Start now. In the chaos.\nThat's exactly what the system is built for.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

    # ── #18 — Objection: "I'm just not a disciplined person" ───────────────
    "c18_not_disciplined": {
        "meta": {
            "id":      "c18",
            "handle":  "@philipz.fit",
            "brand":   "Geek to Greek",
            "caption": "You ship code under pressure, hit deadlines, and lead teams. That's not someone without discipline. DM me DEBUG. 💪",
        },
        "slides": [
            {
                "bg":      "light",
                "layout":  "bottom",
                "is_hook": True,
                "diag":    True,
                "tag":     "The Offer",
                "stripe":  "Not a",
                "heading": "discipline\nproblem.",
                "subhead": "You've shipped under pressure. Hit deadlines. Kept systems running at 2am. You have discipline. It just hasn't been pointed here yet.",
            },
            {
                "bg":     "dark",
                "layout": "bottom",
                "tag":    "The Reframe",
                "heading":      "Port your\nexisting\ndiscipline.",
                "heading_size": 46,
                "body":   "You're not trying to become a different person. You're trying to redirect the same drive that already runs the rest of your life.",
                "bullets": [
                    {"label": "You already are a disciplined person.", "sub": "We just need to port that discipline into your body with the right constraints."},
                    {"label": "Guardrails over willpower.", "sub": "Systems that run when motivation is low — because that's most evenings after a sprint."},
                    {"label": "Identity shifts faster with early proof.", "sub": "'I'm someone who trains' isn't a goal. It's what you become after 3 consistent weeks."},
                ],
            },
            {
                "bg":       "gradient",
                "is_cta":   True,
                "brand":    "Geek to Greek",
                "heading":  "DM me\n\"DEBUG\".",
                "subhead":  "The discipline is already there.\nLet's build the system that uses it.",
                "cta_text": "DM \"DEBUG\" to start",
            },
        ],
    },

}
