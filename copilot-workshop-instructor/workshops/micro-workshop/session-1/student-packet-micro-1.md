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
- [ ] Learn research-backed principles for writing effective AI rules
- [ ] Write custom rules using best practices
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

## 📋 Writing Effective AI Rules - The Context Multiplier

### The Rules Ecosystem - Where Instructions Live

**There's not just one place for AI rules - there's an entire ecosystem!**

| Location | Scope | When Active |
|----------|-------|-------------|
| `.github/copilot-instructions.md` | Repo-wide | Always (Chat, Agent, Code Review) |
| `.github/instructions/*.instructions.md` | Path-specific | Only on matching files |
| `.github/agents/*.agent.md` | Custom agents | When agent is selected |
| `AGENTS.md` | Cross-tool | Works with Copilot, Claude, Cursor |
| VS Code settings | Per-operation | Code gen, test gen, review, commits |

**Today we focus on repo-wide instructions - the skill applies to all layers!**

---

### Research-Backed Principles - What Makes Rules Work

**These principles come from GitHub, Anthropic, and AI engineering community research:**

#### Principle 1: Short, Imperative, Self-Contained Statements

**BAD:** "We generally try to follow industry best practices for code quality and maintainability, so please write code that is clean and well-tested."

**GOOD:** "Use type hints on all function signatures."

**Why it works:** Specific, actionable, scannable.

---

#### Principle 2: Tell the AI What TO DO, Not What to Avoid

**BAD:** "Don't use print statements for debugging."

**GOOD:** "Use `logging` module at DEBUG level for diagnostic output."

**Why it works:** LLMs are poor at negations. Positive directives work better.

---

#### Principle 3: Be Specific and Actionable

**BAD:** "Follow good naming conventions."

**GOOD:** "Use camelCase for JavaScript variables and functions. Use PascalCase for classes."

**Why it works:** Zero ambiguity = better compliance.

---

#### Principle 4: Use Structured Markdown (or XML for Claude-based tools)

**For Copilot:** Use distinct headings, bullet points, code examples.

**For Claude-based tools (Claude Code, etc.):** Use XML tags:

```markdown
<role>Senior Python developer specializing in FastAPI</role>

<architecture>
  - 3-tier: API routes → Service layer → Models
  - All database operations use async/await
</architecture>

<constraints>
  - Never use raw SQL — always use SQLAlchemy ORM
  - Include type hints on every function signature
</constraints>
```

**Why it works:** Clear boundaries prevent AI from mixing up context, instructions, and examples.

---

#### Principle 5: Include Code Examples Where They Clarify Intent

**Instead of:** "Use proper error handling"

**Show this:**
```python
# GOOD - Do this
async def get_user(user_id: str) -> User:
    try:
        return await db.get(User, user_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
```

**Why it works:** A before/after code snippet removes ambiguity.

---

#### Principle 6: Keep Files Under ~1,000 Lines

**Why it matters:** GitHub explicitly warns that beyond 1,000 lines, quality deteriorates.

**Best practice:** Start minimal. Add iteratively based on what you actually need.

---

#### Principle 7: Iterate Based on What Works

**Why it matters:** Rules writing is empirical.

**Process:**
1. Start with 5-10 rules
2. Test them
3. See if Copilot follows them
4. Refine

**Remember:** Rules are a living document!

---

## ⚡ Speed Challenge: Write Your Own Rules (2 min)

**Task:** Create `.github/copilot-instructions.md` in your practice project. Write 3-5 custom rules using the principles you just learned.

**Guidelines:**
- Short imperative statements
- Positive directives (what TO do)
- Specific and actionable
- Organized with clear Markdown headings

**Think:** "What would a new developer on my team need to know to write code that fits this project?"

**My custom rules:**

```markdown
# Todo API Project

## Coding Standards
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________

## Architecture Patterns
1. _____________________________________________________________
2. _____________________________________________________________

## Error Handling
1. _____________________________________________________________
```

**Time completed:** ______ minutes

**How I'll verify Copilot is using my rules:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Rules Writer" unlocked

---

## 📋 Path-Specific Instructions - Rules That Scope

**Want different rules for different parts of your code?**

**Example:** `.github/instructions/testing.instructions.md`

```yaml
---
applyTo: "**/tests/**"
---

# Testing Guidelines

- Use pytest fixtures for database setup
- Every test function name starts with test_
- Use AAA pattern: Arrange, Act, Assert
- Mock external API calls
```

**How it works:**
- Path-specific instructions + repo-wide instructions **stack together**
- When working on test files, Copilot sees both!

**My notes on path-specific instructions:**
_____________________________________________________________________

---

## 📋 How Rules Connect to Everything Else

**Rules are the foundation of the professional workflow you'll learn in Session 2:**

**Rules + PRD + Memory Bank = Copilot that truly knows your project**

**Why this matters:**
- Custom instructions are **always-on context**
- Saves you from repeating yourself in every prompt
- Every prompt you write from now on benefits from these rules
- This is context mastery - what separates AI amateurs from AI professionals

**Verification tip:** Check the **References** section in Copilot Chat responses. It'll show `.github/copilot-instructions.md` when it's reading your rules.

🏆 **Achievement:** [ ] "Context Multiplier" unlocked

---

## Session 1 Achievement Summary

### Achievements Unlocked Today:

- [ ] 🛡️ **Fortress Builder** - Security setup complete
- [ ] 🏗️ **Project Generator** - Created practice project
- [ ] 🔐 **Secret Keeper** - .copilotignore configured
- [ ] ⚡ **Command Guardian** - Understand terminal approval
- [ ] 🎮 **Mode Master** - All AI modes practiced
- [ ] 🎯 **Context Master** - #mentions mastered
- [ ] 📋 **Rules Writer** - Custom rules written using research-backed principles
- [ ] 🔄 **Context Multiplier** - Understand how rules connect to everything

**Total Achievements:** ______ / 8

---

## Self-Assessment

Rate your confidence (1-5):

| Skill | Before | After | Growth |
|-------|--------|-------|--------|
| .copilotignore setup | ___ | ___ | ___ |
| Using Ask Mode | ___ | ___ | ___ |
| Using Agent Mode | ___ | ___ | ___ |
| Using #mentions | ___ | ___ | ___ |
| Writing effective AI rules | ___ | ___ | ___ |
| Understanding rules ecosystem | ___ | ___ | ___ |

**Biggest "aha!" moment:**
_____________________________________________________________________

**What I'm most excited about:**
_____________________________________________________________________

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
