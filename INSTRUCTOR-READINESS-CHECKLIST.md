# Workshop Instructor Readiness Checklist

## 🎯 Purpose
This checklist ensures you're 100% ready to deliver the GitHub Copilot Power User Workshop with confidence. Complete this 1-2 days before the workshop.

---

## ✅ Pre-Workshop Verification (Do This Now)

### 1. Demo Repo Verification (5 minutes)

**Note:** You'll work from `copilot-student-v2-demo`, students get `copilot-student-v2`

```bash
cd ~/Desktop/copilot-student-v2-demo

# Test Main Branch
git checkout main
cat src/schemas/todo.py | head -15
# ✅ Should see TODO comments, NOT full implementations

# Test Session-3-Start Branch
git checkout session-3-start
python create_db.py
pytest tests/api/test_todos.py -v
# ✅ Should show "8 passed" with NO DELETE tests (clean output, no warnings!)

# Test Session-4-Start Branch
git checkout session-4-start
rm todos.db
python create_db.py
pytest tests/api/test_todos.py -v
# ✅ Should show "10 passed" including DELETE tests (clean output!)

# Verify Tag model exists only in session-4-start
ls src/models/tag.py
# ✅ Should show file exists

git checkout session-3-start
ls src/models/tag.py 2>&1
# ✅ Should show "No such file or directory"
```

**Expected Results:**
- ✅ Main: Empty stubs with TODO comments
- ✅ Session-3-start: 8 tests pass, no DELETE, no Tag model
- ✅ Session-4-start: 10 tests pass, with DELETE, with Tag model
- ✅ All test output is clean (no warning noise thanks to pytest config!)

---

### 2. Instructor Materials Check (3 minutes)

```bash
cd ~/Desktop/Copilot/copilot-workshop-instructor/workshops/micro-workshop

# Verify all instructor guides exist
ls -la session-1/instructor-guide-micro-1.md
ls -la session-2/instructor-guide-micro-2.md
ls -la session-3/instructor-guide-micro-3.md
ls -la session-4/instructor-guide-micro-4.md

# Verify slide decks exist
ls -la slides/session-*-slides.md
ls -la slides/SLIDE-DECK-GUIDE.md
```

**Expected Results:**
- ✅ All 4 instructor guides present
- ✅ All slide decks present

---

### 3. Student Materials Check (3 minutes)

```bash
cd ~/Desktop/copilot-student-v2

# Verify student materials in each session folder
ls -la session-1/
ls -la session-2/
ls -la session-3/
ls -la session-4/

# Each should contain:
# - student-packet-micro-X.md
# - PROMPT-SHEET-SESSION-X.md
# - student-reference-micro-X.md
```

**Expected Results:**
- ✅ All session folders have 3 student files each

**Note:** This checks the STUDENT delivery repo. You'll demo from `copilot-student-v2-demo`.

---

## 📋 Day Before Workshop (30 minutes)

### 1. Practice the TDD Demo (Session 3)

This is the most technical part of the workshop. Practice it once:

```bash
cd ~/Desktop/copilot-student-v2-demo
git checkout session-3-start

# Open in VS Code
code .

# Practice Flow:
# 1. Show tests: pytest tests/api/test_todos.py -v (8 passing)
# 2. Open tests/api/test_todos.py
# 3. Write test_delete_todo() with Copilot
# 4. Run pytest - see it FAIL
# 5. Implement DELETE endpoint in src/api/v1/todos.py
# 6. Implement delete_todo() in src/services/todo_service.py
# 7. Run pytest - see it PASS
# 8. Repeat for test_delete_todo_not_found()
```

**Time this!** It should take 8-10 minutes. If it's taking longer, simplify your narration.

---

### 2. Review Your Timing for Each Session

Open each instructor guide and review the minute-by-minute timing:

- **Session 1:** 60 minutes (p. 1 of instructor-guide-micro-1.md)
- **Session 2:** 30 minutes (p. 1 of instructor-guide-micro-2.md)
- **Session 3:** 30 minutes (p. 1 of instructor-guide-micro-3.md)
- **Session 4:** 30 minutes (p. 1 of instructor-guide-micro-4.md)

**Total: 150 minutes (2.5 hours)**

Set alarms on your phone:
- 60 min mark → "Start Session 2"
- 90 min mark → "Start Session 3"
- 120 min mark → "Start Session 4"

---

### 3. Prepare Your Screen Setup

**What to have open on workshop day:**

**Monitor 1 (Main - Students see this):**
- VS Code with student repo
- Terminal window

**Monitor 2 (Your reference - Students don't see):**
- Instructor guide PDF/markdown (current session)
- Slide deck markdown (for speaker notes)
- Timer/clock

**Have ready to share:**
- Student repo URL (you'll zip and upload or use GitHub)
- Slide deck (if using PowerPoint version)

---

## 🎬 Day of Workshop Setup (15 minutes before start)

### 1. Clean Your Demo Environment

```bash
cd ~/Desktop/copilot-student-v2-demo
git checkout main
rm -f todos.db
git status
# Should be clean, no uncommitted changes
```

---

### 2. Open Your Tools

**VS Code:**
```bash
cd ~/Desktop/copilot-student-v2
code .
```

**Terminal:**
- Keep a terminal window open next to VS Code
- Set font size to 16+ so students can read

**Instructor Guide:**
- Open `instructor-guide-micro-1.md` in a separate window (your reference screen)

---

### 3. Test Your Copilot Access

In VS Code:
1. Open any Python file
2. Type a comment: `# function to calculate fibonacci`
3. Hit Enter
4. ✅ Copilot should suggest code

If Copilot isn't working:
- Check you're logged into GitHub Copilot
- Restart VS Code
- Check internet connection

---

## 🎤 Your Instructor Workflow (What to Actually Do)

### Before Each Session

1. **Open instructor guide** for that session on your reference screen
2. **Load slide deck** markdown for speaker notes
3. **Set a timer** for the session length
4. **Take a breath** - you've got this!

### During Each Session

1. **Follow the SAY blocks** in instructor guide (exact words you can use)
2. **Follow the DO blocks** in instructor guide (specific actions)
3. **Watch the ENERGY cues** (when to pause, speed up, slow down)
4. **Use the Time Flexibility notes** if running ahead/behind

### Between Sessions

1. **Quick break** (2-3 minutes)
2. **Check in with students** - "Any questions before we move on?"
3. **Switch to next session's materials**
4. **Reset timer**

---

## 🚨 Common Issues & Quick Fixes

### Issue: Student falls behind during Session 3

**Fix:**
```bash
# Tell student:
git checkout session-3-start
git reset --hard
```

This resets them to the checkpoint instantly.

---

### Issue: TDD demo fails (endpoint works without test failing first)

**Fix:** You're on session-4-start instead of session-3-start

```bash
git checkout session-3-start
# DELETE endpoint doesn't exist here, demo will work
```

---

### Issue: Student's Copilot isn't working

**Quick checks:**
1. Are they logged into GitHub Copilot?
2. Is the file saved? (Copilot doesn't work on unsaved files)
3. Try reloading VS Code window (Cmd+Shift+P → "Reload Window")

---

### Issue: Running out of time in Session 3

**Use Time Flexibility:**
- Skip the reflection discussion (save 2 min)
- Do only ONE feature instead of letting students choose (save 1 min)
- Skip the git reset demo (save 1 min)

---

### Issue: Boss Fight in Session 4 too hard for students

**Reminder:** Students only build ONE endpoint: `POST /todos/{id}/tags`

If still too hard:
- Give them the exact prompt from PROMPT-SHEET-SESSION-4.md
- Let them pair program
- Show them the Tag model first (it's already built in session-4-start)

---

## 💪 Confidence Boosters

### You Have Everything You Need

✅ **Technical setup is solid** - All branches verified
✅ **Materials are complete** - Instructor guides, slides, student packets
✅ **Checkpoints are working** - Safety nets for students
✅ **Timing is realistic** - 3-min buffer built into Session 3
✅ **You know your content** - You built this workshop!

### Remember

1. **Students WANT to learn** - They're rooting for you
2. **Mistakes are okay** - It's a workshop, not a performance
3. **You have checkpoints** - No student can truly "break" their environment
4. **The guides have your back** - SAY blocks give you exact words
5. **You're teaching them to use AI** - Show them it's okay to ask Copilot for help!

---

## 📞 Emergency Contact

If something goes catastrophically wrong during the workshop:

1. **Take a breath** - Students don't know what "should" happen
2. **Use the checkpoints** - Have everyone `git checkout session-X-start`
3. **Pivot to discussion** - Use "Common Issues & Solutions" section from instructor guides
4. **Keep moving** - Don't spend more than 2 minutes debugging live

---

## ✅ Final Pre-Workshop Checklist

**Technical:**
- [ ] Verified all 3 git branches work (main, session-3-start, session-4-start)
- [ ] Practiced TDD demo once
- [ ] Tested Copilot in VS Code
- [ ] Set font sizes to 16+ in terminal and VS Code

**Materials:**
- [ ] All instructor guides accessible
- [ ] Slide decks ready
- [ ] Student repo ready to distribute
- [ ] Timer/clock ready

**Mental:**
- [ ] Reviewed Session 1 timing
- [ ] Know where SAY blocks are in instructor guides
- [ ] Have emergency fixes memorized
- [ ] Took a deep breath

---

## 🎉 You're Ready!

You've done the hard work:
- ✅ Restructured the entire workshop
- ✅ Built checkpoint branches
- ✅ Created comprehensive materials
- ✅ Verified everything works

Now you just need to **show up and guide**.

Your instructor guides will tell you exactly what to say and do. Trust them. Trust yourself.

**You've got this!** 💪

---

**Generated:** February 22, 2026
**Location:** `/Users/lwgray/Desktop/Copilot/`
**Purpose:** Give you confidence and clarity for workshop delivery
