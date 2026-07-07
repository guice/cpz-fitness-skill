# CPZ Fitness: Platform Architecture

> ⚠️ **DEPRECATED — DO NOT USE for current content.** The Skool community is closed for now, not accepting members, no live URL (see `cpz-fitness/SKILL.md` Key Facts). Everything below describes the prepared/intended structure for whenever it relaunches — treat it as historical/reference material, not a live spec. This does not apply to the Everfit-delivered 1:1 program (`references/program.md`), which is a separate, still-active offer.

## Overview

The platform runs on two engines working in tandem: Skool as the free community and lead-nurturing hub, and Everfit as the premium 1:1 coaching delivery engine.

## Platform Stack

| Platform | Role | Notes |
| :--- | :--- | :--- |
| **Social Media** | Discovery & Marketing | @philipz.fit on Instagram, TikTok, Facebook, Threads, and Bluesky. |
| **Skool** | Free community funnel | Entry point for new leads. Free tier builds trust and delivers foundational education. |
| **Everfit** | 1:1 coaching delivery | Paid clients receive custom programs, nutrition guidance, check-in forms, and messaging here. |
| **Zapier** | Bridge automation | Automates the transition from Skool free member → Everfit paid client. |
| **Zoom** | Bi-weekly check-in calls | Supplementary to Everfit messaging. |

## The Client Journey (4 Phases)

**Phase 1 — Discovery (Skool Free)**
Prospects join the free Skool community, consume foundational content in the Classroom, and engage in the community forums. The goal is to build trust through education and personality.

**Phase 2 — Onboarding (Everfit)**
Converted clients are moved into Everfit. An automated Autoflow sequence handles the welcome message, intake questionnaire, and initial program setup.

**Phase 3 — Program Execution (Everfit, 16 weeks)**
Daily workout delivery, weekly automated check-in forms, bi-weekly Zoom calls, and 1:1 in-app messaging. Programs are custom-built from pre-built templates.

**Phase 4 — Graduation & Retention**
90-day review, renewal offer for continued 1:1 coaching, or downsell into a paid group tier on Skool.

## Coaching Model

Philip's initial model is **1:1 online coaching**. The 16-week program is the primary offer. Nutrition guidance is provided as macro education and food direction — not prescribed meal plans (Philip is not currently certified as a nutritionist).

## Skool Community Structure

### Categories (7 total)

| # | Category | Purpose |
| :--- | :--- | :--- |
| 1 | 👋 Start Here | Introductions |
| 2 | 📢 Announcements | Announcements — admin only |
| 3 | 💬 The Breakroom | General Chat |
| 4 | 🏋️ Form Checks & Feedback | Video form reviews |
| 5 | 🥩 Fuel & Macros | Nutrition questions |
| 6 | 🏆 Level Ups | Wins & Progress |
| 7 | ❓ Q&A | Ask Philip |

---

## Classroom Lesson Formats

### Course 1 & 2 Format (4-Step Structure)

All lessons in Course 1 (⚠️ name pending — placeholder "CPZ Fitness Starter Pack") and Course 2 (⚠️ name pending — placeholder "Training Foundations") follow this arc:

1. **Opening hook** — a sarcastic or empathetic observation that names the problem
2. **The diagnosis** — explain why the problem exists, plainly
3. **The fix** — clear, actionable guidance broken into logical steps
4. **The bridge** — a direct sentence pointing to the next lesson or action

**Target length:** 400–700 words per lesson. Full paragraphs — avoid bullet-point-heavy formatting. Conversational and readable.

### Course 3 Format — ⚠️ Name Pending (placeholder "The Consistency Blueprint")

All lessons in Course 3 follow these additional standards:

**Trigger Shift:** The opening sentence IS the H3 header. No "welcome back," no "in this lesson we'll cover." The first thing the reader sees is the point.

**Active Reflection checkpoints:** Every lesson includes all three types, distributed across the lesson body:
- `**Pause for a moment:**` — reflective checkpoint
- `**Dig a little deeper:**` — reflective checkpoint
- `**Take Action:**` — execution checkpoint

**Key Takeaway:** Every lesson ends with a bolded Key Takeaway stated plainly — one sentence, no metaphor needed.

**No module-level overview pages** — the course-wide intro covers orientation; individual modules dive straight into content.

## Classroom Course Library

### Course 1: ⚠️ "CPZ Fitness Starter Pack" (was "Geek to Greek Starter Pack") (Free — Orientation)

**Purpose:** Orientation and foundational education. Establishes trust and introduces CPZ Fitness. Ends with first upsell.

| Module | Lessons | Status |
| :--- | :--- | :--- |
| Module 1 — Getting Oriented | 1.1 How to Use This Community; 1.2 The Skinny-Fat Problem Explained | ✅ Complete |
| Module 2 — Translating the Gym | 2.1 Gym Terminology 101; 2.2 Why Fuckarounditis is Killing Your Gains; 2.3 The Big 5 Lifts | ✅ Complete |
| Module 3 — Fueling the Machine | 3.1 Macros Explained; 3.2 Why You Don't Need a Rigid Meal Plan; 3.3 The Protein Priority | ✅ Complete |
| Module 4 — The Next Level | 4.1 Ready to Stop Guessing and Start Executing? (Upsell) | ✅ Complete |

---

### Course 2: ⚠️ "Training Foundations" (was "The Training OS") (Free — Execution)

**Purpose:** Teaches the 5 movement patterns, training week structure, progressive overload, and progress tracking. Ends with second upsell.

| Module | Lessons | Status |
| :--- | :--- | :--- |
| Module 1 — The 5 Movement Patterns | 1.1 The Hinge; 1.2 The Squat; 1.3 The Pull; 1.4 The Horizontal Push; 1.5 The Vertical Push | ✅ Complete |
| Module 2 — Training Week Structure | 2.1 How to Structure a Training Week; 2.2 The Push/Pull/Legs Split; 2.3 Progressive Overload in Practice | ✅ Complete |
| Module 3 — Progress Tracking | 3.1 How to Read Your Progress Data; 3.2 When to Deload; 3.3 How to Know If the Program Is Working | ✅ Complete |
| Module 4 — The Missing Piece | 4.1 The Missing Piece (Upsell — DIY vs. guided coaching analogy) | ✅ Complete |

---

### Course 3: ⚠️ "The Consistency Blueprint" (was "Deployment Blueprint") (Free — Psychology & Habit Architecture)

⚠️ **Flagged for a dedicated redesign session, not rewritten here.** This entire course's module and lesson architecture (below) is built on a Kubernetes/Terraform deployment metaphor — "The Real Bug," "Event-Driven Architecture," "Garbage Collection," "Building the OS," etc. — spanning all 21 lessons across 6 modules. Renaming the course title is a one-line fix; replacing the master metaphor and every lesson concept it's built on is a real curriculum-design decision that affects content that may already be recorded/published. Rather than silently inventing 21 new lesson concepts, this is left intact below and flagged for you to redesign directly (or confirm you want it regenerated).

**Purpose:** Addresses the behavioral and psychological reasons clients don't execute. Ends with third upsell.

**Writing Standards (ALL lessons) — pending the redesign above:**
- Active Reflection checkpoints: "Pause for a moment:", "Dig a little deeper:", "Take Action:" — every lesson must include all three types across the module
- Trigger Shift: Opening sentence is the H3 header — no "welcome back" filler
- Key Takeaway: Every lesson ends with a bolded Key Takeaway, stated plainly — no metaphor needed (currently still written in the old deployment vocabulary pending the redesign above)
- No module-level overview pages — course-wide intro only

| Module | Lessons | Status |
| :--- | :--- | :--- |
| Module 1 — The Real Bug | 1.1 The Error Log; 1.2 The Optimization Trap; 1.3 The Identity Mismatch; 1.4 The Perfectionism Paradox | ✅ Complete |
| Module 2 — The Habit Stack | 2.1 The Willpower Memory Leak; 2.2 The Minimum Viable Deploy; 2.3 Event-Driven Architecture; 2.4 Pre-Caching Dependencies | ✅ Complete |
| Module 3 — Environmental Design | 3.1 The Path of Least Resistance; 3.2 Calendar as Configuration; 3.3 The Gym Sandbox; 3.4 The Digital Environment | ✅ Complete |
| Module 4 — The Inner World | 4.1 Sleep as Garbage Collection; 4.2 Stress as Background Processing; 4.3 The Recovery Protocol; 4.4 Graceful Degradation | ✅ Complete |
| Module 5 — Building the OS | 5.1 The Health Check; 5.2 Reading the Logs; 5.3 Handling the Plateau; 5.4 The Long Game | ✅ Complete |
| Module 6 — Upgrading Your Hardware | 6.1 Upgrading Your Hardware (Third Upsell) | ✅ Complete |

#### Course 3 Module Summaries

**Module 1 — The Real Bug:** Identifies the psychological friction points that stop clients before they start. Covers motivation as a byproduct (not a prerequisite), the optimization trap (over-researching instead of executing), identity mismatch (running the wrong OS), and the perfectionism paradox.

**Module 2 — The Habit Stack:** Engineers a consistency system that doesn't rely on willpower. Covers willpower as finite RAM, the Minimum Viable Deploy (start small), event-driven habit stacking (binding new habits to existing triggers), and pre-caching dependencies (removing friction in advance).

**Module 3 — Environmental Design:** Refactors the physical and digital environment to make the right actions the path of least resistance. Covers physical infrastructure (staging the deployment), calendar as configuration (hardcoding workouts), the gym sandbox (always enter with a spec), and the digital environment (auditing the feed and protecting sleep windows).

**Module 4 — The Inner World:** Reframes sleep, stress, and recovery as critical system inputs. Covers sleep as garbage collection (you build muscle in bed, not the gym), stress as background processing (high CPU = poor workout performance), active recovery as defragmentation (movement clears the cache), and graceful degradation (50% workout beats 0% on bad days).

**Module 5 — Building the OS:** Delivers the long-term maintenance protocol. Covers accountability as uptime monitoring (three layers: self, social, coach), progress tracking with a minimal viable 4-metric dashboard (weight trend, strength, energy, body composition), plateau debugging (change one variable at a time; the 90-Day Rule), and the final identity shift from fitness-as-project to fitness-as-infrastructure.
