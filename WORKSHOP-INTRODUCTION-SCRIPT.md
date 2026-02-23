# Workshop Introduction Script
**Duration:** 10 minutes (before Session 1 starts)
**Purpose:** Set the stage, verify setup, build excitement

---

## [0:00-0:01] Welcome & Personal Introduction

**ENERGY:** Warm, welcoming, confident

**SAY:**
> "Good morning/afternoon everyone! Welcome to the GitHub Copilot Power User Workshop."
>
> "I'm [YOUR NAME], and I'm excited to spend the next 2.5 hours with you learning how to work with AI as a professional developer."
>
> *(Optional: Add 1-2 sentences about your background - keep it brief!)*
> "I've been working with GitHub Copilot for [timeframe], and what we're covering today represents the patterns that actually work in production."

**PAUSE - Let that land.**

---

## [0:01-0:03] Workshop Overview (What We're Building)

**ENERGY:** Building excitement

**SAY:**
> "Here's what we're building today: a production-ready Todo API using FastAPI."
>
> "But more importantly, you're learning HOW to work with AI effectively. Not just 'autocomplete for code' - we're talking about:"
>
> - **Security patterns** that keep your secrets safe
> - **Context management** that gets AI to understand your codebase
> - **Professional workflows** like Test-Driven Development with AI
> - **When to trust AI** and when to take control yourself

**SAY:**
> "By the end of today, you'll be able to build features 3-5x faster than writing everything by hand, while maintaining code quality."

**PAUSE.**

---

## [0:03-0:07] Technical Setup Verification (Critical!)

**ENERGY:** Systematic, helpful

**SAY:**
> "Before we start, let's make sure everyone has what they need. This is important - if you hit a blocker here, raise your hand and I'll help."

### Step 1: GitHub Copilot Access

**SAY:**
> "First: GitHub Copilot. Open VS Code, and look for the Copilot icon in the bottom right."

**SHOW ON YOUR SCREEN:** Point to Copilot icon in VS Code status bar.

**SAY:**
> "If you see this icon, click it. You should see your GitHub username and 'Copilot is active.'"
>
> "If you DON'T see this, or it says 'Copilot not active,' raise your hand now."

**PAUSE - Look around the room, give people 30 seconds to check.**

**ACTION:** Help anyone who's blocked (common issues: not signed in, no license, extension not installed).

---

### Step 2: Student Repository

**SAY:**
> "Second: The student repository. You should have received a link to clone the workshop materials."
>
> *(If using GitHub):* "The repo URL is: [YOUR-GITHUB-URL]"
>
> *(If using zip file):* "You should have downloaded and unzipped the `copilot-student-v2` folder."

**SHOW ON YOUR SCREEN:** Your file explorer with the student repo open.

**SAY:**
> "Your folder should look like this. You should see:"
> - `src/` folder
> - `tests/` folder
> - `README.md`
> - `pyproject.toml`

**SAY:**
> "If your folder doesn't look like this, raise your hand."

**PAUSE - Help anyone who's blocked.**

---

### Step 3: Python Environment

**SAY:**
> "Third: Python environment. Open a terminal in VS Code."

**SHOW ON YOUR SCREEN:** Open VS Code terminal (Ctrl+` or Cmd+`).

**SAY:**
> "Run these commands with me:"

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

**SAY:**
> "This will take 30-60 seconds. You should see packages installing."

**WAIT** - Let everyone run this. Walk around if needed.

**SAY:**
> "Last check - run this command:"

```bash
python -c "import fastapi; print('✅ Ready to go!')"
```

**SAY:**
> "If you see '✅ Ready to go!' - you're all set. If you see an error, raise your hand."

**PAUSE - Help anyone who's blocked.**

---

## [0:07-0:09] Workshop Structure & Expectations

**ENERGY:** Clear, organized

**SAY:**
> "Here's how today is structured. We have 4 sessions:"
>
> **Session 1 (60 min):** Security & Superpowers - Learn the AI interaction modes
> **Session 2 (30 min):** Context is King - Master the key to great AI output
> **Session 3 (30 min):** Build Sprint - TDD Edition - Watch me, then you build
> **Session 4 (30 min):** Boss Fight - Put it all together on your own
>
> "Total: 2.5 hours with short breaks between sessions."

**SAY:**
> "Here's how this works:"
>
> ✅ **I'll demonstrate first** - You watch and learn the pattern
> ✅ **Then you practice** - Hands-on with the same pattern
> ✅ **Questions are encouraged** - Raise your hand anytime
> ✅ **We have safety nets** - If something breaks, we can reset

**SAY:**
> "One important thing: In Sessions 1 and 2, you'll practice with small examples - games, scripts, whatever you want. We're learning the TOOLS."
>
> "In Session 3, we switch to our Todo API project and start building real features. That's when it all comes together."

---

## [0:09-0:10] Set the Mindset

**ENERGY:** Inspiring, professional

**SAY:**
> "Last thing before we dive in: This workshop is about learning to work WITH AI, not being replaced BY AI."
>
> "You're the architect. You're the reviewer. You're the decision-maker."
>
> "AI is your extremely fast, sometimes brilliant, sometimes wrong assistant. Your job is to guide it, verify it, and ship quality code faster than ever before."
>
> "Let's go build something."

**PAUSE.**

**SAY:**
> "Alright! Let's start Session 1. Open your VS Code, and let's talk about security first."

---

## Quick Troubleshooting Guide (For You)

**If someone doesn't have Copilot access:**
- Check they're signed into GitHub in VS Code (bottom left icon)
- Verify they have a Copilot license (they should have received this beforehand)
- Last resort: They can watch Session 1, get access during break

**If someone can't clone the repo:**
- Give them the zip file backup
- Or have them pair with a neighbor

**If Python/venv isn't working:**
- Check Python version: `python --version` (needs 3.9+)
- Try `python3` instead of `python`
- Last resort: They can watch demos, fix during first break

**If pip install fails:**
- Check internet connection
- Try `pip install --upgrade pip` first
- Check for proxy/firewall issues

---

## Visual Aids to Have Ready

**On your screen BEFORE workshop starts:**
- ✅ VS Code open with student repo
- ✅ Terminal open and ready
- ✅ Copilot icon visible in status bar
- ✅ File explorer showing repo structure

**On backup screen/monitor:**
- ✅ Instructor Guide for Session 1 open
- ✅ Timer visible (for your pacing)

---

## Energy & Tone Tips

**Do:**
- ✅ Make eye contact, smile, be welcoming
- ✅ Show enthusiasm about what they'll learn
- ✅ Be patient during setup (it ALWAYS takes longer than planned)
- ✅ Acknowledge this is new for many people

**Don't:**
- ❌ Rush through setup (you'll pay for it later)
- ❌ Assume everyone has the same skill level
- ❌ Skip introductions ("let's just dive in") - rapport matters
- ❌ Be apologetic about AI ("I know some people don't like AI...") - be confident!

---

**After this introduction, transition directly into Session 1, starting with [0:02-0:10] Security First.**

Your students are now oriented, equipped, and ready to learn! 🚀
