# Sessions 1 & 2: Student Setup Guide

## Key Understanding

**Sessions 1 & 2 are NOT about building the Todo API.**

They're about learning Copilot fundamentals with practice projects. Students will build the Todo API starting in Session 3 using the checkpoint branches.

---

## Session 1: Security & Superpowers (60 min)

### What Students Should Have Open

**Option A: Separate Practice Folder (Recommended)**
```bash
# Students create a new practice workspace
mkdir ~/copilot-practice
cd ~/copilot-practice
code .
```

This gives them a clean space to experiment without worrying about the workshop repo.

**Option B: Main Branch**
```bash
# Students can use the student repo on main branch
cd ~/Desktop/copilot-student-v2
git checkout main
code .
```

The empty stubs won't matter - they'll create new files for practice.

---

### What Students Actually Do (Session 1)

#### 1. Security Setup [0:00-0:08]
**Students DO:**
- Create `.copilotignore` file (you show template)
- Add sensitive patterns (.env, credentials.json, etc.)
- Practice terminal safety (what NOT to share)

**They create:**
- `.copilotignore` file in their practice folder

---

#### 2. All 4 Modes Demo [0:08-0:18]
**Students WATCH:**
- You demo Ask Mode, Edit Mode, Agent Mode, Plan Mode
- They take notes in student packet (checkboxes to fill)

**No coding required** - just observation and note-taking

---

#### 3. #mentions Power [0:18-0:25]
**Students PRACTICE:**
- Create a simple Python file: `practice.py`
- Type: `# function to calculate fibonacci`
- Press Enter, watch Copilot suggest
- Try `#file` references
- Try `#codebase` search

**Example practice.py:**
```python
# function to calculate fibonacci
# (Copilot will suggest implementation)

# function to reverse a string
# (Copilot will suggest implementation)
```

**Goal:** Get comfortable with Copilot suggestions, not build anything specific

---

#### 4. Writing Effective Rules [0:25-0:42]
**Students DO:**
- Create custom instructions file
- Student packet has fill-in exercise (page 3-4)
- Write 3-5 rules for their own coding style

**Example custom instructions students might write:**
```
- Always use type hints in Python functions
- Prefer list comprehensions over loops when appropriate
- Include docstrings for all public functions
- Use descriptive variable names (no single letters except i, j for loops)
```

**No coding** - just writing good rules

---

#### 5. Agent Mode Practice [0:42-0:60]
**Students DO:**
- Ask Copilot Agent to create a small project
- **Example prompts:**
  - "Create a Python script that fetches weather data from wttr.in"
  - "Create a simple todo CLI app in Python"
  - "Create a Rock Paper Scissors game"

**They're NOT building the workshop Todo API** - just practicing Agent Mode

**This creates separate files/folders:**
```
copilot-practice/
├── .copilotignore
├── custom-instructions.md
├── weather_script.py  (from Agent Mode)
└── todo_cli.py  (from Agent Mode)
```

---

## Session 2: Context Mastery (30 min)

### What Students Should Have Open

**Same as Session 1:**
- Their `copilot-practice` folder OR
- The `main` branch of student repo

**Still NOT building the Todo API yet.**

---

### What Students Actually Do (Session 2)

#### 1. Thinking Modes [0:00-0:05]
**Students WATCH:**
- You demo extended thinking mode
- Show difference between quick vs deep thinking

**No hands-on** - just observation

---

#### 2. Explore → Plan → Code [0:05-0:12]
**Students WATCH:**
- You demo the professional workflow
- Show how you explore before coding

**Example you might demo:**
```python
# In their practice folder, show:
# 1. Ask Copilot to explore what weather APIs exist
# 2. Ask Copilot to plan a weather app structure
# 3. Ask Copilot to generate the code
```

**Students observe workflow** - not required to code along

---

#### 3. PRD Creation [0:12-0:20]
**Students DO:**
- Write a PRD for ONE of their practice projects from Session 1
- Student packet has PRD template (page 8-9)

**Example PRD students fill out:**
```markdown
# Product Requirements Document: Weather CLI App

## Problem
Users need quick weather info without opening a browser

## Solution
Command-line tool that fetches and displays weather

## Requirements
- Accept city name as argument
- Display current temperature
- Display conditions (sunny, rainy, etc.)
- Handle errors gracefully

## Technical Approach
- Use wttr.in API (no key required)
- Python requests library
- argparse for CLI
```

**No coding** - just planning on paper (student packet)

---

#### 4. 6-Element Prompt Framework [0:20-0:27]
**Students PRACTICE:**
- Learn the framework: Persona, Context, Task, Constraints, Format, Examples
- Write 1-2 structured prompts in student packet

**Example prompt students write:**
```
Persona: You are a Python CLI expert
Context: I'm building a weather app that uses wttr.in
Task: Write a function to fetch weather data
Constraints: Must handle network errors, timeout after 5s
Format: Return a dictionary with temp, conditions, city
Examples: get_weather("Seattle") → {"temp": "65°F", "conditions": "cloudy", "city": "Seattle"}
```

**They write prompts in student packet** - don't have to execute them yet

---

#### 5. Q&A Buffer [0:27-0:30]
**Open discussion** - students ask questions

---

## When Does the Todo API Work Begin?

### Session 3 - THE SWITCH

**At the start of Session 3, students CHANGE BRANCHES:**

```bash
cd ~/Desktop/copilot-student-v2
git checkout session-3-start
pytest -v  # Should see 8 passing tests
```

**From this point forward:**
- Session 3: Work on `session-3-start` (working Todo API)
- Session 4: Switch to `session-4-start` (working Todo API + more)

---

## Summary: What's Open When

| Session | What Students Have Open | What They're Building |
|---------|-------------------------|----------------------|
| **1** | Practice folder OR main branch | Practice projects (weather app, CLI, games) |
| **2** | Same as Session 1 | PRDs and prompts for practice projects |
| **3** | `session-3-start` branch | **Todo API** (priority field) |
| **4** | `session-4-start` branch | **Todo API** (tag endpoint) |

---

## Key Points for Instructor

1. **Don't worry about the empty stubs on `main`**
   - Students won't use the Todo API structure in Sessions 1-2
   - They'll create separate practice files
   - The stubs are there for students who want to explore, but not required

2. **Sessions 1-2 are learning time**
   - No pressure to build "the right thing"
   - Students experiment with Copilot features
   - Practice projects can be anything

3. **Session 3 is when structure matters**
   - That's when you switch to `session-3-start`
   - Working API gives students confidence
   - They build ONE focused feature

4. **Reassure students:**
   - "Don't worry if your practice code is messy - that's the point!"
   - "Sessions 1-2 are for learning, Session 3 is for building"
   - "The checkpoint branches will give you a clean foundation"

---

## Student Instructions (Give Them This)

### Before Session 1

**Option A (Recommended):**
```bash
mkdir ~/copilot-practice
cd ~/copilot-practice
code .
```

**Option B:**
```bash
cd ~/Desktop/copilot-student-v2
git checkout main
code .
```

### Sessions 1-2
- Experiment freely
- Create practice projects
- Don't worry about "breaking" anything
- Take notes in student packet

### Session 3
```bash
cd ~/Desktop/copilot-student-v2
git checkout session-3-start
pytest -v  # Verify 8 tests pass
code .
```

Now you're working on the real Todo API!

---

## Your Instructor Script (Sessions 1-2)

**Before Session 1:**
```bash
# You can demo from anywhere
cd ~/Desktop/copilot-student-v2
git checkout main  # Or use a separate practice folder
code .
```

**Tell students:**
"Today we're learning Copilot fundamentals. Create a practice folder or use the main branch - doesn't matter. We'll start building the real Todo API in Session 3."

**During Session 1:**
- Show features using simple examples
- Students follow along in their own practice space
- No pressure to match your exact code

**During Session 2:**
- Continue with practice projects
- Students write PRDs and prompts on paper (student packet)
- Minimal live coding

**At start of Session 3:**
- **Critical moment:** "Everyone run `git checkout session-3-start`"
- Verify: `pytest -v` shows 8 passing tests
- **Now** students have working Todo API to build on

---

## FAQ

**Q: What if students ask "should I follow along coding in Sessions 1-2?"**
A: "You can if you want, but it's optional. The important part is understanding the concepts. We'll have structured coding time in Sessions 3-4."

**Q: What if students mess up their practice code?**
A: "That's totally fine! Practice code is meant to be messy. You'll get a clean foundation in Session 3."

**Q: Do students need the student repo for Sessions 1-2?**
A: "Not strictly necessary. They can use a practice folder. But if they clone the repo, they can use the `main` branch for exploration."

**Q: Will the empty stubs confuse students?**
A: "We won't even look at the Todo API structure in Sessions 1-2. We're focused on learning Copilot features with simple examples."

---

## Bottom Line

**Sessions 1-2 = Learning playground (any folder, any files)**
**Sessions 3-4 = Structured building (checkpoint branches with working API)**

The empty stubs on `main` are fine - students won't need the Todo API structure until Session 3.

---

**Generated:** February 22, 2026
**Purpose:** Clarify Sessions 1-2 setup and expectations
