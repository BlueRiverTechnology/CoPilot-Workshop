# Day-of-Workshop Quick Reference

## 🖥️ What to Have Open

### Your Main Screen (students see this):
```
┌─────────────────────────────────┐
│  VS Code (demo copy)            │
│  ~/Desktop/copilot-student-v2-demo│
│                                 │
│  Terminal (16pt font)           │
└─────────────────────────────────┘
```

### Your Reference Screen (only you see):
```
┌─────────────────────────────────┐
│  Current instructor guide       │
│  Current slide deck (notes)     │
│  Timer                          │
│  This cheat sheet               │
└─────────────────────────────────┘
```

---

## ⏱️ Timeline at a Glance

| Time | Session | What You're Doing | Branch |
|------|---------|-------------------|--------|
| 0:00 | Session 1 (60 min) | Security, Modes, Rules | `main` |
| 1:00 | Session 2 (30 min) | Context, Planning | `main` |
| 1:30 | Session 3 (30 min) | **TDD Demo**, Student builds | `session-3-start` |
| 2:00 | Session 4 (30 min) | Tools, Boss Fight | `session-4-start` |
| 2:30 | Done! | Victory lap | |

---

## 🎬 Session-by-Session Script

### SESSION 1: Security & Superpowers (60 min) - `main` branch

**⚠️ NOTE: Students are NOT building the Todo API yet - they're learning Copilot features with practice projects**

**Your setup:**
```bash
cd ~/Desktop/copilot-student-v2-demo
git checkout main
code .
```

**Student setup:**
- Students clone/download `copilot-student-v2` from GitHub
- Students can create practice folder: `mkdir ~/copilot-practice && code ~/copilot-practice`
- OR use `main` branch of their student repo (doesn't matter - they won't touch Todo API yet)

**Tell students:** "Today we're learning Copilot fundamentals with practice projects. We'll build the real Todo API starting in Session 3."

**Your flow:**
1. [0:00-0:08] Security (.copilotignore, terminal safety) → DEMO
2. [0:08-0:18] All 4 modes (Ask, Edit, Agent, Plan) → DEMO each
3. [0:18-0:25] #mentions power → DEMO #file, #codebase, #terminalSelection
   - Students practice with simple files (not Todo API)
4. [0:25-0:42] **Writing Effective Rules** → DEMO custom instructions, students write rules
   - Students fill out exercise in student packet (paper-based)
5. [0:42-0:60] Agent Mode project → Students do hands-on
   - Example: "Ask Copilot to create a weather CLI app"
   - **Separate from Todo API** - just practice

**Key deliverable:** Students have custom instructions file & understand Copilot modes

**If running over:** Skip Agent Mode demo (students can do it themselves)

---

### SESSION 2: Context Mastery (30 min) - `main` branch

**⚠️ NOTE: Still using practice projects - Todo API work starts in Session 3**

**Your setup:** Same as Session 1 (stay on `main`)

**Student setup:** Same as Session 1 (practice folder or `main` branch)

**Tell students:** "We're still learning fundamentals. You'll write a PRD and practice prompts for your practice projects. The real Todo API work starts next session."

**Your flow:**
1. [0:00-0:05] Thinking modes → DEMO extended thinking
2. [0:05-0:12] Explore → Plan → Code workflow → DEMO
   - Use a simple example (weather app, calculator, etc.)
3. [0:12-0:20] PRD creation → Students write PRD
   - **For their practice project from Session 1**
   - Student packet has template (mostly paper-based)
4. [0:20-0:27] 6-element prompts → DEMO format
   - Students write 1-2 example prompts in packet
5. [0:27-0:30] Q&A buffer

**Key deliverable:** Students have a PRD and understand structured prompts

**If running over:** Skip extended thinking demo (not critical)

**Transition to Session 3:** "Next session we'll switch to a working Todo API and build real features. Everyone will run `git checkout session-3-start` to get the foundation."

---

### SESSION 3: TDD Build Sprint (30 min) - `session-3-start` branch

**⚠️ CRITICAL: Switch branches before this session!**

```bash
cd ~/Desktop/copilot-student-v2-demo
git checkout session-3-start
rm todos.db
python create_db.py
pytest tests/api/test_todos.py -v
# Should show 8 passed
```

**Your setup:**
- VS Code open to `session-3-start` branch
- Terminal showing `pytest` output (8 tests passed)
- Have `tests/api/test_todos.py` file ready to open

**Your flow:**
1. [0:00-0:03] **Checkpoint verification**
   - SAY: "Everyone run `git checkout session-3-start` and `pytest -v`"
   - SAY: "You should see 8 tests passing. If not, raise your hand."
   - SHOW: Your terminal with 8 tests

2. [0:03-0:13] **TDD Demo (students WATCH)**
   - OPEN: `tests/api/test_todos.py`
   - SAY: "I'm going to write the test FIRST, watch my screen"
   - DO: Write `test_delete_todo()` with Copilot
   - RUN: `pytest -v` → Show it FAILS (9 tests, 1 failure)
   - SAY: "Good! Test fails. Now let's make it pass."
   - OPEN: `src/api/v1/todos.py`
   - DO: Add DELETE endpoint with Copilot
   - OPEN: `src/services/todo_service.py`
   - DO: Add `delete_todo()` method with Copilot
   - RUN: `pytest -v` → Show it PASSES (9 tests, 9 passed)
   - SAY: "That's Test-Driven Development with Copilot!"

3. [0:13-0:25] **Student hands-on**
   - SAY: "Now YOU build ONE feature: add a 'priority' field to todos"
   - GIVE: Prompt from PROMPT-SHEET-SESSION-3.md
   - DO: Circulate, help students

4. [0:25-0:27] **Quick reflection**
   - SAY: "How was TDD different from just asking Copilot to build everything?"
   - LISTEN: 2-3 student responses

5. [0:27-0:30] **Buffer time**

**If a student breaks their code:**
```bash
git checkout session-3-start
git reset --hard
```

**If running over:** Skip reflection (save 2 min), shorten student hands-on to 10 min

---

### SESSION 4: Advanced Tools & Boss Fight (30 min) - `session-4-start` branch

**⚠️ CRITICAL: Switch branches before this session!**

```bash
cd ~/Desktop/copilot-student-v2-demo
git checkout session-4-start
rm todos.db
python create_db.py
pytest tests/api/test_todos.py -v
# Should show 10 passed (includes DELETE tests from Session 3)
```

**Your setup:**
- VS Code open to `session-4-start` branch
- Terminal showing `pytest` output (10 tests passed)
- Have `src/models/tag.py` ready to show

**Your flow:**
1. [0:00-0:03] **Checkpoint verification**
   - SAY: "Everyone run `git checkout session-4-start` and `pytest -v`"
   - SAY: "You should see 10 tests. Notice DELETE tests are now here!"

2. [0:03-0:08] **Code Review with Copilot**
   - SHOW: How to ask Copilot to review code
   - DEMO: In-editor review vs PR review

3. [0:08-0:12] **Custom Agents**
   - SHOW: `.agent.md` file example
   - DEMO: Creating a simple custom agent

4. [0:12-0:18] **Memory Bank**
   - SHOW: The 6-file pattern
   - DEMO: Creating memory files for project context

5. [0:18-0:20] **The 70% Problem**
   - SAY: "Copilot gets you 70% there. YOU provide the critical 30%."
   - DISCUSS: What does that mean for your work?

6. [0:20-0:25] **Boss Fight**
   - SAY: "Build ONE endpoint: `POST /todos/{id}/tags`"
   - SAY: "The Tag model already exists. Look at `src/models/tag.py`"
   - SHOW: Tag model briefly
   - GIVE: Exact prompt from PROMPT-SHEET-SESSION-4.md
   - DO: Students build, you circulate

7. [0:25-0:30] **Victory lap**
   - SAY: "You just built a FastAPI app with many-to-many relationships using AI!"
   - CELEBRATE: Students did it!
   - SHARE: Certification info if applicable

**If students struggle with Boss Fight:**
- Remind them Tag model exists (`src/models/tag.py`)
- Give them the exact prompt from prompt sheet
- Let them pair program
- Worst case: Show solution and explain it

**If running over:** Skip Code Review demo (not critical for learning)

---

## 🚨 Emergency Phrases

**When you're running behind:**
- "We're a bit tight on time, so let's move quickly to..."
- "I'll skip the demo, but this is in your reference guide"
- "Let's take just ONE question and then continue"

**When a student is stuck:**
- "Let me see your screen after the session"
- "Try checking out the checkpoint branch again: `git checkout session-X-start`"
- "Ask Copilot: 'Why is this failing?'"

**When YOU make a mistake:**
- "That's actually perfect - this shows that Copilot isn't magic!"
- "Let me ask Copilot to fix this..."
- "This is why we have checkpoints - let me reset"

---

## ✅ Pre-Session Checklist (Quick!)

**Before Session 1:**
- [ ] VS Code open on `main` branch
- [ ] Terminal font size 16+
- [ ] Instructor guide open on reference screen
- [ ] Timer set for 60 minutes

**Before Session 3:**
- [ ] Switch to `session-3-start` branch
- [ ] Run `pytest -v` to confirm 8 tests pass
- [ ] Open `tests/api/test_todos.py` ready to edit
- [ ] Timer set for 30 minutes

**Before Session 4:**
- [ ] Switch to `session-4-start` branch
- [ ] Run `pytest -v` to confirm 10 tests pass
- [ ] Open `src/models/tag.py` to show students
- [ ] Timer set for 30 minutes

---

## 💪 Mantras for During the Workshop

1. **"The guides have my back"** - Follow SAY blocks, you'll be fine
2. **"Checkpoints are safety nets"** - Students can't break anything permanently
3. **"It's okay to improvise"** - If something's not working, pivot
4. **"I'm the guide, not the expert"** - Show students how to learn with AI
5. **"Energy matters"** - Smile, be enthusiastic, students will mirror you

---

## 📱 Set These Phone Alarms

- **60 min in:** "Start Session 2"
- **90 min in:** "Start Session 3 - SWITCH TO session-3-start"
- **120 min in:** "Start Session 4 - SWITCH TO session-4-start"
- **145 min in:** "5 minutes left - wrap up"

---

## 🎬 You're On!

**Right before you start:**
1. Deep breath
2. Smile
3. Open instructor-guide-micro-1.md
4. Start timer
5. Follow SAY blocks

**You've got this!** The materials are solid, the tech works, and you know your content.

Now go teach them to be Copilot power users! 🚀

---

**Keep this open on your reference screen during the workshop.**
