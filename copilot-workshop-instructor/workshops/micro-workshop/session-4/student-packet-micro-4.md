# Student Packet: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Name:** _________________________
**Date:** _________________________
**Duration:** 30 minutes
**Achievement Goal:** 🏆 "Copilot Champion"

---

## Learning Objectives

- [ ] Verify checkpoint and understand starting point
- [ ] Use Copilot Code Review for quality assurance
- [ ] Create Custom Agents for persistent expertise
- [ ] Build a Memory Bank for project continuity
- [ ] Understand the 70% Problem and your critical 30%
- [ ] Complete Boss Fight using ALL workshop techniques
- [ ] Earn Power User Certification

---

## 🚦 Checkpoint Verification (Start Here!)

**Before beginning, verify you're on the session-4-start checkpoint:**

### Step 1: Switch to Checkpoint Branch
```bash
git checkout session-4-start
```

### Step 2: Initialize Database
```bash
python create_db.py
```

### Step 3: Run Tests
```bash
pytest tests/api/test_todos.py -v
```

**Expected:** 10 tests passing ✅

```
✅ test_create_todo
✅ test_create_todo_minimal
✅ test_get_todos_empty
✅ test_get_todos
✅ test_update_todo
✅ test_update_todo_partial
✅ test_update_todo_not_found
✅ test_create_todo_validation
✅ test_delete_todo
✅ test_delete_todo_not_found
========== 10 passed ==========
```

### What This Checkpoint Gives You

**Pre-built endpoints:**
- [ ] POST /api/v1/todos (create)
- [ ] GET /api/v1/todos (list with pagination)
- [ ] PUT /api/v1/todos/{id} (update)
- [ ] DELETE /api/v1/todos/{id} (delete)

**Pre-built infrastructure:**
- [ ] Tag model with many-to-many relationship
- [ ] todo_tags association table
- [ ] Complete service layer pattern
- [ ] Comprehensive test suite

**Your checkpoint status:**
```
[ ] All 10 tests passing
[ ] Database initialized
[ ] Server can start (uvicorn src.main:app --reload)
```

🏆 **ACHIEVEMENT UNLOCKED:** "Checkpoint Master"

---

## 🔍 Copilot Code Review

### Two Ways to Review Code

**1. On GitHub Pull Requests:**
```
1. Create a Pull Request on GitHub
2. Request review from "Copilot" as a reviewer
3. Copilot analyzes your changes
4. Get inline comments and suggestions
```

**2. In VS Code Chat (Try This Now):**

Copy this prompt into Copilot Chat:
```
Review my implementation in #file:src/api/v1/todos.py

Check for:
1. Security issues (auth, validation, ownership checks)
2. Error handling completeness
3. Performance concerns (N+1 queries, missing indexes)
4. Best practice violations

Be thorough and critical. Point out specific line numbers.
```

### My Code Review Results

**Issues Copilot found:**
```
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________
```

**What I learned from the review:**
_____________________________________________________________________

**Why Code Review matters:**
```
AI generates fast → Code Review ensures quality
This is YOUR 30% work ensuring production readiness!
```

🏆 **ACHIEVEMENT UNLOCKED:** "Review Master"

---

## 🤖 Custom Agents - Persistent Expertise

### What Are Custom Agents?

Custom Agents are `.agent.md` files that pre-load AI with your project's:
- Architecture patterns
- Coding standards
- File structure
- Domain knowledge

**Think of it as:** Creating a senior developer persona who KNOWS your codebase.

### Exercise: Create a Todo API Expert Agent

**Create this file:** `.github/agents/todo-api-expert.agent.md`

```markdown
# Todo API Expert Agent

You are an expert in our Todo API codebase.

## Architecture
- FastAPI with async/await
- 3-tier architecture: API → Services → Models
- SQLAlchemy with async sessions (aiosqlite)
- Pydantic v2 for validation and serialization

## Key Patterns
- All endpoints use fixed owner_id = "default-user" (no JWT auth)
- Service layer handles business logic
- Models use UUID string primary keys
- All database operations are async
- Responses use Pydantic schemas

## File Structure
- src/api/v1/ - API endpoints (FastAPI routers)
- src/services/ - Business logic (service classes)
- src/models/ - SQLAlchemy ORM models
- src/schemas/ - Pydantic request/response schemas
- tests/api/ - API endpoint tests (pytest-asyncio)

## Database Models
- User: id (UUID), username, email, hashed_password
- Todo: id (UUID), title, description, completed, owner_id
- Tag: id (UUID), name, created_at
- todo_tags: Association table (todo_id, tag_id)

## Coding Standards
- Use async/await for all database operations
- Return appropriate HTTP status codes (200, 201, 204, 400, 403, 404, 500)
- Include comprehensive error handling (try/except with HTTPException)
- Write tests for all new endpoints (TDD preferred)
- Follow patterns in existing code

## When Asked to Implement Features
1. Follow the 3-tier architecture
2. Create Pydantic schemas first
3. Implement service layer logic
4. Add API endpoint with proper error handling
5. Include ownership validation where applicable
6. Write tests to verify functionality
```

### Try Using Your Custom Agent

Test it with this prompt:
```
Using context from #file:.github/agents/todo-api-expert.agent.md:

Review the patterns in our codebase and suggest best practices
for adding a new feature.
```

**What the agent helped with:**
_____________________________________________________________________

**How Custom Agents improve results:**
```
Without Agent: You explain architecture every time
With Agent: AI KNOWS your patterns automatically

Less explaining → Better results → Consistent code!
```

🏆 **ACHIEVEMENT UNLOCKED:** "Agent Creator"

---

## 🧠 Memory Bank - Persistent Project Context

### The Problem

Every new Copilot chat session starts with ZERO memory:

```
Monday:    "We use FastAPI with 3-tier architecture..."
Tuesday:   "Remember, FastAPI with 3-tier..."
Wednesday: "I TOLD you yesterday..."
Thursday:  *gives up explaining*
```

### The Solution: Memory Bank

A structured set of markdown files that Copilot reads at the start of EVERY conversation.

```
your-project/
├── .github/
│   └── copilot-instructions.md    ← Tell Copilot to read Memory Bank
├── memory-bank/                    ← 6 context files
│   ├── projectbrief.md            (What is this project?)
│   ├── productContext.md          (Why does it exist?)
│   ├── techContext.md             (What tech do we use?)
│   ├── systemPatterns.md          (How do we build things?)
│   ├── activeContext.md           (What's happening RIGHT NOW?) ⚡
│   └── progress.md                (Where do we stand?)
└── src/
```

### The 6 Files Explained

| File | Updates | Purpose |
|------|---------|---------|
| `projectbrief.md` | Rarely | Project name, goals, scope, requirements |
| `productContext.md` | Rarely | Why it exists, who it's for, UX goals |
| `techContext.md` | Occasionally | Stack, setup, constraints |
| `systemPatterns.md` | Occasionally | Architecture, file structure, conventions |
| `activeContext.md` | **Daily** | Current focus, recent changes, next steps |
| `progress.md` | **Daily** | What works, what's left, known issues |

### Quick Exercise: activeContext.md Template

**This is the MOST IMPORTANT file** - update it daily!

```markdown
# Active Context

## Current Focus
Session 4 Boss Fight - implementing tag endpoint

## Recent Changes
- Session 3: Built full CRUD for todos
- Checkpoint provides Tag model pre-built
- DELETE endpoint already exists

## Active Decisions
- Tags stored in existing Tag model
- Many-to-many via todo_tags association table
- Using simplified auth (default-user)

## Next Steps
- Build POST /todos/{id}/tags endpoint
- Verify ownership validation
- Test tag functionality
```

### Update copilot-instructions.md

Add this to `.github/copilot-instructions.md`:

```markdown
## Memory Bank

This project uses a Memory Bank for persistent context.
At the start of every task, read the memory-bank/ files
in this order:

1. memory-bank/projectbrief.md (project goals and scope)
2. memory-bank/techContext.md (tech stack and setup)
3. memory-bank/systemPatterns.md (architecture and patterns)
4. memory-bank/activeContext.md (current focus and recent changes)
5. memory-bank/progress.md (what works, what's left)

Use this context to inform all responses. If you notice
the memory bank is outdated based on our conversation,
suggest updates.

When I say "update memory bank", review ALL memory-bank
files and update them to reflect the current project state.
Focus especially on activeContext.md and progress.md.
```

### The Daily Workflow

```
MORNING:
  Copilot reads memory-bank/ → Full context
  No more re-explaining your project!

DURING WORK:
  Better suggestions because Copilot knows your patterns

END OF DAY:
  Say: "update memory bank"
  → activeContext.md and progress.md updated automatically

NEXT DAY:
  Zero context lost. Pick up where you left off.
```

### How It All Connects

| Workshop Concept | Memory Bank Equivalent |
|------------------|------------------------|
| copilot-instructions.md (Session 1) | Tells Copilot to read Memory Bank |
| PRD.md (Session 2) | projectbrief.md + productContext.md |
| Custom Agents (Session 4) | systemPatterns.md + techContext.md |

**Key Insight:**
- **Custom Agents** tell Copilot HOW you work (patterns, rules)
- **Memory Bank** tells Copilot WHERE you are (current state)

🏆 **ACHIEVEMENT UNLOCKED:** "Memory Architect"

---

## ⚠️ The 70% Problem - Critical Understanding

### The Reality of AI-Assisted Development

Research shows a consistent pattern:

```
THE 70/30 SPLIT

AI Delivers Fast (70%):
┌────────────────────────────────────┐
│ ✅ Boilerplate code                │
│ ✅ Standard patterns               │
│ ✅ Happy path implementation       │
│ ✅ Basic structure                 │
│ ✅ Common use cases                │
└────────────────────────────────────┘

YOU Must Add (30%):
┌────────────────────────────────────┐
│ 🎯 Edge cases AI missed            │
│ 🎯 Ownership validation            │
│ 🎯 Performance optimization        │
│ 🎯 Security hardening              │
│ 🎯 Production-readiness            │
│ 🎯 Business logic nuances          │
│ 🎯 Real-world error handling       │
│ 🎯 "What if" scenarios             │
└────────────────────────────────────┘
```

### Why This Matters

**Organizations that understand this:**
- 26% productivity gains
- Sustainable AI workflows
- High code quality maintained

**Organizations that don't:**
- Accumulating technical debt
- Bugs in production
- Decreased trust in AI

### Your Professional Value = The 30%

**Example from our Todo API:**

**AI's 70%:**
- Creates the endpoint structure ✓
- Connects to database ✓
- Returns data ✓
- Basic validation ✓

**YOUR 30%:**
- Checks: Can user only tag THEIR OWN todos? 🎯
- Handles: What if todo doesn't exist? 🎯
- Optimizes: Is there an N+1 query problem? 🎯
- Secures: Could this leak another user's data? 🎯

### Reflection

Think about code you've seen that "worked" but wasn't production-ready:

**What was missing?**
_____________________________________________________________________

**Who caught it?**
_____________________________________________________________________

**What could have gone wrong?**
_____________________________________________________________________

**In the Boss Fight, ask yourself:**
```
"What could go wrong?"
"What did AI assume?"
"What edge cases exist?"
```

🏆 **ACHIEVEMENT UNLOCKED:** "70/30 Understander"

---

## 🎮 BOSS FIGHT - The Ultimate Challenge

### The Challenge

Build ONE powerful API endpoint using the many-to-many relationship:

**POST /api/v1/todos/{todo_id}/tags**

### What's ALREADY BUILT (session-4-start checkpoint)

✅ Tag model (id, name, created_at)
✅ todo_tags association table
✅ Relationship defined in Todo model
✅ All CRUD endpoints for todos

### What YOU Build

**Endpoint:** POST /api/v1/todos/{todo_id}/tags

**Request body:** `{ "name": "urgent" }`

**Functionality:**
- Creates tag if doesn't exist (case-insensitive)
- Associates tag with todo
- Returns updated TodoResponse with tags included

**Error handling:**
- 404 if todo not found
- 403 if todo not owned by user
- Clear, helpful error messages

**THE CRITICAL 30%:**
- Ownership validation works
- Edge cases handled
- Error messages are clear
- Tags are case-insensitive

### Scoring

| Time | Level | Description |
|------|-------|-------------|
| ≤3 min | 🏆 PLATINUM | Top 1% - Elite |
| ≤4 min | 🥇 GOLD | Top 10% - Expert |
| ≤5 min | 🥈 SILVER | Top 25% - Skilled |
| Completed | ✅ CERTIFIED | Passed! |

**Bonus Points (+1 level each):**
- [ ] Used 'think hard' for planning
- [ ] Used TDD approach
- [ ] Used Custom Agent context
- [ ] Verified ownership validation (the 30%)

---

### My Boss Fight Tracker

**Start Time:** ___:___

#### Phase 1: Planning (Recommended: 30 seconds)

**My approach:**
```
[ ] 'think hard' planning
[ ] Direct implementation
[ ] Plan Mode (/plan)
```

**My plan:**
```
_____________________________________________
_____________________________________________
_____________________________________________
```

#### Phase 2: Implementation (Target: 3 min)

**Files I need to create/update:**
```
[ ] src/schemas/tag.py (TagCreate, TagResponse)
[ ] src/schemas/todo.py (add tags to TodoResponse)
[ ] src/services/todo_service.py (add_tag_to_todo method)
[ ] src/api/v1/todos.py (POST endpoint)
```

**Prompt I used:**
```
_____________________________________________
_____________________________________________
_____________________________________________
_____________________________________________
```

#### Phase 3: The Critical 30% (Target: 30 seconds)

**Verification checklist:**
```
[ ] Ownership validation - Can only tag own todos?
[ ] Case sensitivity - Tags normalized to lowercase?
[ ] Idempotency - What if tag already on todo?
[ ] Error messages - Clear and helpful?
[ ] Edge cases - Todo not found? Tag already exists?
```

**Issues I fixed:**
```
_____________________________________________
_____________________________________________
```

#### Phase 4: Testing (Target: 30 seconds)

**Quick tests:**
```bash
# Create a todo
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Todo"}'

# Add tag (copy todo_id from above)
curl -X POST http://localhost:8000/api/v1/todos/<todo_id>/tags \
  -H "Content-Type: application/json" \
  -d '{"name":"urgent"}'

# Verify tags appear
curl http://localhost:8000/api/v1/todos/<todo_id>
```

**Tests passed:**
```
[ ] Tag created successfully
[ ] Tag appears in todo response
[ ] Case-insensitive (URGENT = urgent)
[ ] Ownership validated
```

**End Time:** ___:___

---

### My Boss Fight Results

**Total Time:** _____ minutes

**Base Level:**
```
[ ] ≤3 min = PLATINUM
[ ] ≤4 min = GOLD
[ ] ≤5 min = SILVER
[ ] Completed = CERTIFIED
```

**Bonus Points Earned:**
```
[ ] Used 'think hard' (+1 level)
[ ] Used TDD (+1 level)
[ ] Used Custom Agent (+1 level)
[ ] Verified ownership (the 30%) (+1 level)
```

**FINAL LEVEL:** _________________

🏆 **ACHIEVEMENT UNLOCKED:** "Boss Fighter"

---

### What Made the Difference

**Most helpful technique:**
_____________________________________________________________________

**What I'd do differently:**
_____________________________________________________________________

**Biggest challenge:**
_____________________________________________________________________

**How I solved it:**
_____________________________________________________________________

---

## 🎉 Victory Lap & Certification

### You've Completed the GitHub Copilot Power User Workshop!

**In 4 sessions, you learned:**

**Session 1:**
- Security-first development (.copilotignore, approval models)
- All Copilot modes (Ask, Edit, Agent, Plan)
- Writing effective rules and instructions

**Session 2:**
- Context mastery with #mentions
- Professional workflows (Explore → Plan → Code)
- 6-Element Prompt Framework

**Session 3:**
- TDD with AI
- Subagents and parallel work
- Building features FAST

**Session 4:**
- Code Review and Custom Agents
- Memory Bank pattern
- The critical 70/30 understanding
- Boss Fight completion!

---

## Session 4 Achievement Summary

### Achievements Unlocked Today:

- [ ] 🚦 **Checkpoint Master** - Verified session-4-start checkpoint
- [ ] 🔍 **Review Master** - Used Copilot Code Review
- [ ] 🤖 **Agent Creator** - Created Custom Agent
- [ ] 🧠 **Memory Architect** - Built Memory Bank
- [ ] ⚠️ **70/30 Understander** - Knows where to add value
- [ ] 🎮 **Boss Fighter** - Completed final challenge
- [ ] 🏆 **COPILOT CHAMPION** - Full workshop complete!

**Total Achievements:** ______ / 7

---

## Power User Certification

```
┌─────────────────────────────────────────────┐
│                                             │
│       GITHUB COPILOT POWER USER             │
│              CERTIFIED                      │
│                                             │
│   Successfully completed Power User         │
│   Workshop and demonstrated mastery of:     │
│                                             │
│   ✅ Security-first development             │
│   ✅ All Copilot modes                      │
│   ✅ Context mastery & prompting            │
│   ✅ Professional workflows                 │
│   ✅ Test-Driven Development                │
│   ✅ Subagents & Plan Mode                  │
│   ✅ Code Review & Custom Agents            │
│   ✅ Memory Bank pattern                    │
│   ✅ Boss Fight completion                  │
│                                             │
│   Name: _____________________               │
│   Level: ____________________               │
│   Date: _____________________               │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Final Reflection

### What I Learned

**Most valuable technique:**
```
_____________________________________________
```

**Biggest mindset shift:**
```
_____________________________________________
```

**What I'll use Monday morning:**
```
_____________________________________________
```

### My Action Plan

**This week, I will:**
```
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________
```

**In 30 days, I want to:**
```
_____________________________________________
_____________________________________________
```

---

## Key Takeaways

1. **Security First** - Never expose secrets to AI
2. **Context is King** - Better context = better results
3. **Plan Before Code** - Explore → Plan → Code
4. **Trust but Verify** - Review ALL AI output
5. **Know Your 30%** - YOU add the critical value

---

## Continue Learning

### GitHub Awesome Copilot

👉 **https://github.com/github/awesome-copilot**

This curated collection includes:
- 💡 Advanced tips and tricks
- 📖 Community best practices
- 🎯 Use case examples
- 🔧 Tool integrations
- ✨ Latest updates and features

⭐ **Star this repo and check it regularly!**

### Official Documentation

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot Chat Documentation](https://docs.github.com/en/copilot/github-copilot-chat)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

## Notes & Questions

_____________________________________________________________________

_____________________________________________________________________

_____________________________________________________________________

---

**End of Student Packet: Micro Session 4** 🎓

**🎉 CONGRATULATIONS - You're a Copilot Power User! 🎉**

**You're not a beginner anymore.**
**You're a POWER USER.**
**You're an AI-AUGMENTED PROFESSIONAL.**

**Go transform how your team codes! 💪🚀**
