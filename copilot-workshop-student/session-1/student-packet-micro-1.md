# Student Packet: Micro Session 1
## Security & Superpowers 🛡️⚡

**Name:** _________________________  
**Date:** _________________________  
**Achievement Goal:** 🏆 "Fortress Builder"

---

## Learning Objectives

- [ ] Configure secure AI development environment
- [ ] Master all 4 AI interaction modes
- [ ] Use all #mention types effectively
- [ ] Understand Custom Instructions
- [ ] Create first .github/copilot-instructions.md file

---

## The Power User Promise

**In 2 hours, you'll:**
- ✅ Build a complete todo app
- ✅ Create reusable prompt files
- ✅ Measure your productivity gains
- ✅ Become significantly faster forever

**Let's go! 🚀**

---

## ⚡ Speed Challenge 1: .copilotignore Setup (3 min)

**Task:** Create `.copilotignore` with security + performance patterns

**Required patterns:**
- [ ] .env files
- [ ] API keys (*_TOKEN, *_SECRET, *_API_KEY)
- [ ] Credentials/secrets folders
- [ ] Build artifacts (node_modules, __pycache__)
- [ ] At least 10 patterns total

**Your .copilotignore:**
```bash
# Add your patterns here:




```

**Verification:**
```bash
# Test it works:
echo "test-secret" > .env
# In Chat: "#file:.env"
# Should show: "This file is ignored" ✅
```

**Time:** ______ minutes

🏆 **Micro-Achievement:** [ ] "Secret Keeper" unlocked

---

## 🛡️ Security Checklist

### Terminal Command Safety

**Copilot's approach:** Confirmation before execution

**What happens when Agent Mode wants to run a command:**
1. Shows you the exact command
2. Displays [Continue] and [Cancel] buttons
3. You review and approve/reject

**Commands I feel safe approving:**
```
# Examples:
pip install, pytest, git status, ls, pwd
```

**My rule for approving commands:**
_____________________________________________________________________

🏆 **Micro-Achievement:** [ ] "Command Guardian" unlocked

---

### Problems Tab

**Location:** (usually bottom panel)

**Test it:**
- [ ] Created file with intentional error
- [ ] Saw error in Problems tab
- [ ] Used #problems to reference errors

**What I learned:**
_____________________________________________________________________

---

## 🔧 Controlling What Copilot Can Do

### VS Code Settings for Copilot

Beyond .copilotignore, you can control Copilot's behavior through VS Code settings:

**Key Settings:**
- `chat.tools.autoApprove` - Whether Copilot can auto-execute all tools without prompting
- `chat.tools.terminal.autoApprove` - Whether terminal commands are auto-approved
- `github.copilot.editor.enableAutoCompletions` - Inline suggestion behavior

**How to Configure:**
1. Open Command Palette (Cmd+Shift+P / Ctrl+Shift+P)
2. Type "Preferences: Open User Settings (JSON)"
3. Search for "copilot" or "chat.tools"

**Example Configuration:**
```json
{
  "chat.tools.terminal.autoApprove": false,  // Always ask before running terminal commands
  "chat.tools.autoApprove": false,           // Always ask before any tool use
  "github.copilot.editor.enableAutoCompletions": true
}
```

### Agent Tool Controls

**In Agent Mode, you can control which tools Copilot can use:**

1. Open Chat view (Ctrl+Alt+I / Ctrl+Cmd+I)
2. Select "Agent" from agent picker
3. Click **"Configure Tools"** (wrench icon)
4. See which tools are enabled:
   - File editing
   - Terminal commands
   - Running tests
   - MCP servers (if configured)

**Toggle tools on/off** based on your trust level and workflow needs!

### When to Restrict Tool Access

**Restrict terminal auto-approval when:**
- Working with production systems
- Unfamiliar with commands Copilot might suggest
- Learning phase (you want to review every command)

**Allow auto-approval when:**
- Well-tested development environment
- High confidence in prompts
- Speed is critical (but still review!)

**My settings preference:**
_____________________________________________________________________

🏆 **Micro-Achievement:** [ ] "Settings Master" unlocked

---

## 🏗️ Practice Project Setup

### Generated with Agent Mode (2 min)

**The prompt I used:**
```
Create a minimal FastAPI learning project:

Structure (6 files total):
├── routes/        # 3 files
│   ├── hello.py   (basic endpoint)
│   ├── users.py   (user endpoints with auth)
│   └── items.py   (CRUD operations)
├── helpers/       # 2 files
│   ├── auth.py    (simple authentication)
│   └── validate.py (input validation)
└── main.py        # 1 file (app entry point)

Make each file 20-40 lines with:
- Clear docstrings, type hints, error handling,
  authentication patterns, validation logic.
```

**Files created:**
- [ ] routes/hello.py
- [ ] routes/users.py
- [ ] routes/items.py
- [ ] helpers/auth.py
- [ ] helpers/validate.py
- [ ] main.py

**Generation time:** _____ seconds

**Why this prompt works well:**
_____________________________________________________________________

---

## 🎮 AI Modes Overview

### The Four Modes (Learn First!)

| Mode | Symbol | Purpose | When to Use |
|------|--------|---------|-------------|
| Ask | ❓ | Think WITH you | Planning/questions |
| Edit | ✏️ | Controlled edits | Precise multi-file changes |
| Agent | 🤖 | Build FOR you | Autonomous implementation |
| Plan | 📋 | Create implementation plans | Complex features |

### Plus: Inline Tools

| Tool | Shortcut | Purpose |
|------|----------|---------|
| Inline Chat | Cmd+I | Quick edits without chat panel |
| Ghost Text | (automatic) | Code completions as you type |
| @workspace | @workspace query | Search entire codebase |

---

## 🏗️ Agent Mode - My First Real Use!

**I generated a complete practice project!**

**Time to generate:** _____ seconds  
**Time it would take manually:** ~60 minutes

**What impressed me:**
_____________________________________________________________________

**Files I now have:**
- [ ] routes/hello.py
- [ ] routes/users.py
- [ ] routes/items.py
- [ ] helpers/auth.py
- [ ] helpers/validate.py
- [ ] main.py

🏆 **Achievement:** [ ] "Agent Mode First Use" unlocked

---

## 🛡️ Safety Features - Your Safety Net!

### Undo and Git Integration

**Ways to recover from AI changes:**

1. **Standard Undo:** Cmd+Z / Ctrl+Z
   - Works for individual file changes

2. **Git Integration:**
   - Stage changes you like
   - Discard changes you don't (right-click → Discard)
   - Commit at checkpoints

3. **Accept/Reject in Edit Mode:**
   - Review diffs BEFORE applying
   - Accept or Discard each change

**My recovery strategy:**
_____________________________________________________________________

**When I'll use each method:**
1. Undo: _____________________________________________________________
2. Git: ______________________________________________________________
3. Reject changes: ___________________________________________________

---

### Review Before Accepting

**Golden rule:** Review before you accept!

**In Edit Mode I see:**
- [ ] Diff preview
- [ ] Accept button
- [ ] Discard button

**In Agent Mode I see:**
- [ ] Working set files
- [ ] Changes being made
- [ ] Terminal commands before approval

**Why this matters:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Safety First" - Understand review workflow

---

## ⚡ Inline AI Tools - Superpowers!

### Ghost Text / Inline Completions

**What I saw:**
- AI predicts code as I type (gray text)
- Tab to accept, Esc to reject

**Example that impressed me:**
_____________________________________________________________________

**When I'll use this:**
_____________________________________________________________________

---

### Inline Chat (Cmd+I) - Quick Edits

**What is it:** Quick inline edits without opening chat

**How to use:**
1. Select code (or place cursor)
2. Press **Cmd+I** (Mac) or **Ctrl+I** (Windows/Linux)
3. Type instruction
4. See DIFF PREVIEW
5. Accept or reject

**Example I tried:**
_____________________________________________________________________

**Why this is faster than Agent Mode for quick edits:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Inline Tools Master" unlocked

---

## ⚡ Other Modes Quick Demo

**Ask Mode example I saw:**
_____________________________________________________________________

**Plan Mode example I saw:**
_____________________________________________________________________

---

## 🔄 Mode Switching Practice

### Task 1: Ask Mode - Understanding (30 sec)
**What I asked:**
_____________________________________________________________________

**What I learned:**
_____________________________________________________________________

### Task 2: Agent Mode - Implementation (30 sec)
**What I asked:**
_____________________________________________________________________

**What was generated:**
_____________________________________________________________________

### Task 3: Agent Mode First (30 sec)
**Prompt used:**
_____________________________________________________________________

**What was generated:**
_____________________________________________________________________

### Task 4: Ask Mode - Explanation (30 sec)
**What I asked:**
_____________________________________________________________________

**What I learned:**
_____________________________________________________________________

**Key insight about using the right mode:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Mode Master" unlocked

---

## 🎮 MENTION BINGO!

**Goal:** Use each #mention at least once

```
┌─────────────────────────────────┐
│  🎮 MENTION BINGO               │
├─────────────────────────────────┤
│  [ ] #file                      │
│  [ ] #folder                    │
│  [ ] #terminalSelection         │
│  [ ] #problems                  │
│  [ ] #codebase / @workspace     │
│  [ ] #fetch (web content)       │
└─────────────────────────────────┘
```

### #file - Specific File Context
**I used it to:**

**Example:** `#file:routes/hello.py` or `#file:helpers/auth.py`

_____________________________________________________________________

### #folder - Directory Context
**I used it to:**

**Example:** `#folder:routes` or `#folder:helpers`

_____________________________________________________________________

### #terminalSelection - Command Output
**I used it to:**
_____________________________________________________________________

### #problems - IDE Errors
**I used it to:**
_____________________________________________________________________

### @workspace - Codebase Search
**I used it to:**
_____________________________________________________________________

---

## ⚡ Speed Challenge 2: Mention Mastery (3 min)

**Task:** Use all 5 #mentions while creating a FastAPI app

**Time completed:** ______ minutes

**Challenges faced:**
_____________________________________________________________________

**Most useful #mention:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Context Master" unlocked

---

## 📋 Custom Instructions - Your AI's Personality

### What Custom Instructions Do

| Aspect | Description |
|--------|-------------|
| **Purpose** | HOW you want AI to behave |
| **Location** | `.github/copilot-instructions.md` |
| **Scope** | Applied to ALL interactions automatically |
| **Examples** | Coding standards, naming conventions, architecture |

### Why This Matters

**Without custom instructions:**
- Repeat context in every prompt
- Inconsistent code style
- AI doesn't know your preferences

**With custom instructions:**
- Set once, applied everywhere
- Consistent code across all AI interactions
- AI understands your project

---

## 📋 My First Custom Instructions File

**Created:** [ ] Yes [ ] No

**File location:** `.github/copilot-instructions.md`

**My custom instructions content:**
```markdown
# Project: _______________

## Overview


## Coding Standards
-
-
-

## Naming Conventions
-
-

## Error Handling
-
-
```

**What I included:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Instruction Writer" unlocked

---

## Session 1 Achievement Summary

### Achievements Unlocked Today:

- [ ] 🛡️ **Fortress Builder** - Security setup complete
- [ ] 🏗️ **Project Generator** - Created practice project
- [ ] 🔐 **Secret Keeper** - .copilotignore configured  
- [ ] ⚡ **Command Guardian** - Understand terminal approval
- [ ] 🎮 **Mode Master** - All AI modes practiced
- [ ] 🎯 **Context Master** - #mentions mastered
- [ ] 📋 **Instruction Writer** - Custom Instructions created

**Total Achievements:** ______ / 7

---

## Self-Assessment

Rate your confidence (1-5):

| Skill | Before | After | Growth |
|-------|--------|-------|--------|
| .copilotignore setup | ___ | ___ | ___ |
| Using Ask Mode | ___ | ___ | ___ |
| Using Agent Mode | ___ | ___ | ___ |
| Using #mentions | ___ | ___ | ___ |
| Custom Instructions | ___ | ___ | ___ |

**Biggest "aha!" moment:**
_____________________________________________________________________

**What I'm most excited about:**
_____________________________________________________________________

---

## 🎯 What Happens to the Practice Project?

The practice project you created (routes/, helpers/, main.py) was for **learning purposes only**.

**Next session:** You'll switch to a pre-built Todo API project with professional structure. The practice project can be deleted - you won't need it again.

**Think of it as:** Session 1 = Training wheels. Session 2+ = Real bike! 🚴

---

## Preview: Session 2

**Next up: Context Mastery & Planning! 🧠⚡**

You'll learn:
- Professional workflow: Explore → Plan → Code → Commit
- Prompting formula: Context + Task + Constraints + Format
- Thinking modes for complex decisions
- Set up todo app structure

**Prepare to level up! 🚀**

---

## Notes & Questions

_____________________________________________________________________

_____________________________________________________________________

_____________________________________________________________________

_____________________________________________________________________

---

**End of Student Packet: Micro Session 1** 🎓
