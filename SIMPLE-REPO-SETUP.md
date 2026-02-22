# Simple Workshop Repo Setup

## The Two-Folder System

### 📦 `/Users/lwgray/Desktop/copilot-student-v2`
**Purpose:** Clean student delivery repo
**Who uses it:** Students (they clone or download this)
**Keep this:** Pristine and clean

```bash
# This is what students get
# They'll clone it from GitHub or download a zip
# DO NOT work from this during your demos!
```

---

### 🎬 `/Users/lwgray/Desktop/copilot-student-v2-demo`
**Purpose:** Your demo/working copy
**Who uses it:** YOU during workshop delivery
**Get messy:** Make mistakes, demo features, experiment

```bash
# This is YOUR copy
# Work from here during the workshop
# All your instructor support docs reference this path
```

---

## Tonight's Prep (The Only Thing You Need)

### 1. Make sure students can get the clean repo

**Option A: GitHub (recommended)**
```bash
cd /Users/lwgray/Desktop/copilot-student-v2
git push origin main session-3-start session-4-start
# Send students the GitHub URL to clone
```

**Option B: Zip file**
```bash
cd /Users/lwgray/Desktop
zip -r copilot-student-v2.zip copilot-student-v2
# Email or upload this zip to students
```

### 2. Test YOUR demo copy works

```bash
cd /Users/lwgray/Desktop/copilot-student-v2-demo
git checkout session-3-start
source venv/bin/activate
pytest tests/ -v
# Should see 8 passed, clean output (no warnings!)
```

---

## Tomorrow During Workshop

### You Open This:
```bash
cd /Users/lwgray/Desktop/copilot-student-v2-demo
code .
```

### Students Open This:
```bash
# After cloning/downloading copilot-student-v2
cd ~/Desktop/copilot-student-v2  # or wherever they cloned it
code .
```

---

## What About copilot-workshop-student?

The folder `/Users/lwgray/Desktop/Copilot/copilot-workshop-student` is an older copy or might be part of your instructor materials structure. You can ignore it for delivery.

**All you need:**
- ✅ `copilot-student-v2` = Student delivery repo
- ✅ `copilot-student-v2-demo` = Your working copy

---

## Your Support Files Reference the Demo Copy

These files now correctly reference `copilot-student-v2-demo`:
- ✅ [DAY-OF-WORKSHOP-SCRIPT.md](DAY-OF-WORKSHOP-SCRIPT.md)
- ✅ [INSTRUCTOR-READINESS-CHECKLIST.md](INSTRUCTOR-READINESS-CHECKLIST.md)

Just follow them and you'll be working from the right folder!

---

## Quick Mental Model

```
copilot-student-v2          →  Students download/clone this
                               (Keep clean!)

copilot-student-v2-demo     →  You work from this during workshop
                               (Get messy! Demo here!)

Your instructor guides       →  Tell you what to say and do
                               (Follow the SAY/DO blocks)
```

**That's it. Simple!** 🎉
