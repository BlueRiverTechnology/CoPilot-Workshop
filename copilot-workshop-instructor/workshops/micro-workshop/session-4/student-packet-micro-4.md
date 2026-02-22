# Student Packet: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Duration:** 33 minutes  
**Achievement:** 🏆 "Copilot Champion"

---

## What You'll Master

| Technique | Why It Matters |
|-----------|----------------|
| Copilot Code Review | Catch issues before they ship |
| Custom Agents | Pre-loaded context for your project |
| The 70% Problem | Know where YOU add value |
| Boss Fight | Prove complete mastery |

---

## 🔍 Copilot Code Review

### On GitHub (Pull Requests)

```
HOW TO USE:
1. Create a Pull Request on GitHub
2. Request review from "Copilot" as a reviewer
3. Copilot analyzes your changes
4. Get inline comments and suggestions

WHAT IT CHECKS:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns
```

### In-Editor Review

Copy this prompt to review your own code:

```
Review my recent changes in #file:src/api/v1/todos.py.

Check for:
1. Security issues (auth, validation)
2. Error handling completeness
3. Performance concerns
4. Best practice violations

Be thorough and critical.
```

**Exercise:** Run a code review on any file you've created in this workshop.

What issues did Copilot find?
```
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Review Master"

---

## 🤖 Custom Agents

### What Are Custom Agents?

Custom Agents are pre-configured AI specialists for your project:

```
Location: .github/agents/*.agent.md

What they do:
- Define specialized AI personas
- Include project-specific knowledge
- Set constraints and patterns
- Reusable across conversations
```

### Create Your First Custom Agent

Create this file: `.github/agents/todo-api.agent.md`

```markdown
# Todo API Expert Agent

You are an expert in our Todo API codebase. You know:

## Architecture
- FastAPI with async/await
- 3-tier architecture: API → Services → Models
- SQLAlchemy with async sessions
- Pydantic for validation

## Key Patterns
- All endpoints require authentication (get_current_user)
- Service layer handles business logic
- Models use UUID primary keys
- Responses use Pydantic schemas

## File Structure
- src/api/v1/ - API endpoints
- src/services/ - Business logic
- src/models/ - SQLAlchemy models
- src/schemas/ - Pydantic schemas
- tests/api/ - API tests

## Coding Standards
- Use async/await for all database operations
- Return appropriate HTTP status codes
- Include comprehensive error handling
- Write tests for all new endpoints

When asked to implement features:
1. Follow existing patterns in the codebase
2. Create tests first (TDD approach)
3. Use the 3-tier architecture
4. Include proper validation and error handling
```

### Use Your Custom Agent

```
Using #file:.github/agents/todo-api.agent.md context:

Add a DELETE /api/v1/todos/{id} endpoint that:
- Requires authentication
- Checks ownership
- Returns 204 on success, 404/403 on errors
```

**Reflection:** How does including the agent context improve the output?
```
_______________________________________________
_______________________________________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Agent Creator"

---

## 🧠 Memory Bank - Persistent Project Context

### The Problem

Every new Copilot chat session starts with zero memory:

```
Monday:    "We use FastAPI with async/await and 3-tier..."
Tuesday:   "Remember, we use FastAPI with async/await..."
Wednesday: "I already told you, FastAPI..."
Thursday:  "...I give up explaining."
```

### The Solution

A `memory-bank/` folder with structured markdown files that Copilot reads at the start of every conversation.

```
your-project/
├── .github/
│   └── copilot-instructions.md    ← Tell Copilot about Memory Bank
├── memory-bank/                    ← Persistent context lives here
│   ├── projectbrief.md            ← What is this project?
│   ├── productContext.md          ← Why does it exist?
│   ├── techContext.md             ← What tech do we use?
│   ├── systemPatterns.md         ← How do we build things?
│   ├── activeContext.md           ← What's happening NOW? ⚡
│   └── progress.md                ← Where do we stand?
└── src/
```

### Build Your Memory Bank: Step by Step

#### Step 1: Create the folder and files

```bash
mkdir memory-bank
touch memory-bank/projectbrief.md
touch memory-bank/productContext.md
touch memory-bank/techContext.md
touch memory-bank/systemPatterns.md
touch memory-bank/activeContext.md
touch memory-bank/progress.md
```

#### Step 2: Fill in each file

**projectbrief.md** — The foundation
```markdown
# Project Brief

## Project Name
Todo API Workshop App

## Goals
- Build a REST API for managing todos
- Learn AI-assisted development patterns
- Practice TDD with Copilot

## Scope
- CRUD operations for todos
- User ownership model
- Tagging system (many-to-many)
- Authentication (simplified for workshop)

## Success Criteria
- All endpoints return correct responses
- Ownership validation on all mutations
- Tests pass for core functionality
```

**productContext.md** — The why
```markdown
# Product Context

## Problem
Developers need a structured todo management API
with user isolation and organizational features.

## Users
- Developers learning AI-augmented development
- Teams needing a lightweight task API

## User Experience Goals
- RESTful, predictable API design
- Clear error messages
- Fast response times
```

**techContext.md** — The stack
```markdown
# Tech Context

## Stack
- Python 3.11+
- FastAPI (async)
- SQLAlchemy (async sessions)
- Pydantic v2 (validation)
- Pytest (testing)
- SQLite (development)

## Setup
- Poetry for dependency management
- uvicorn for local server
- pyproject.toml for configuration

## Constraints
- All operations must be async
- UUID primary keys (string format)
- Simplified auth (fixed "default-user")
```

**systemPatterns.md** — How we build
```markdown
# System Patterns

## Architecture
3-tier: API (routers) → Services (business logic) → Models (data)

## File Structure
- src/api/v1/ → FastAPI routers
- src/services/ → Business logic layer
- src/models/ → SQLAlchemy ORM models
- src/schemas/ → Pydantic request/response schemas
- tests/ → Pytest test files

## Key Patterns
- Service layer handles all business logic
- Routers only handle HTTP concerns
- Pydantic schemas for all request/response
- HTTPException for error responses
- Ownership validation before mutations

## Conventions
- Async/await everywhere
- Type hints on all functions
- Docstrings on public methods
- PEP 8 style
```

**activeContext.md** — Right now (most important!)
```markdown
# Active Context

## Current Focus
Completing Session 4 Boss Fight - building tagging feature

## Recent Changes
- Session 3: Built POST, GET, PUT endpoints for todos
- Implemented TDD approach for all features
- Service layer pattern established

## Active Decisions
- Tags are case-insensitive (stored lowercase)
- Tag names unique per user
- Many-to-many via association table

## Next Steps
- Implement Tag model and association table
- Build tag endpoints (POST, GET filter, DELETE)
- Add ownership validation for tags
- Run code review on completed features
```

**progress.md** — Status tracker
```markdown
# Progress

## What Works
- [x] Todo model with SQLAlchemy
- [x] POST /api/v1/todos (create)
- [x] GET /api/v1/todos (list)
- [x] PUT /api/v1/todos/{id} (update)
- [x] Pydantic schemas for todos
- [x] Service layer pattern
- [x] Basic test suite

## What's Left
- [ ] Tag model and association table
- [ ] POST /api/v1/todos/{id}/tags
- [ ] GET /api/v1/todos?tag=name
- [ ] DELETE /api/v1/todos/{id}/tags/{tag_id}
- [ ] Ownership validation for tags
- [ ] Complete test coverage

## Known Issues
- Authentication is simplified (hardcoded user)
- No pagination on list endpoints
- No rate limiting
```

#### Step 3: Update copilot-instructions.md

Add this to your existing `.github/copilot-instructions.md`:

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
  Copilot reads memory-bank/ → Full context restored
  No more re-explaining your project

DURING WORK:
  Better suggestions because Copilot knows your patterns
  Reference #file:memory-bank/activeContext.md for focus

END OF DAY:
  Say: "update memory bank"
  Copilot updates activeContext.md and progress.md

NEXT DAY:
  Zero context lost. Pick up exactly where you left off.
```

### How It Connects to What You Learned

| Workshop Concept | Memory Bank Equivalent |
|------------------|----------------------|
| copilot-instructions.md (Session 1) | Tells Copilot to read Memory Bank |
| PRD.md (Session 2) | projectbrief.md + productContext.md |
| 6-Element Framework (Session 2) | Context is pre-loaded from files |
| Custom Agents (Session 4) | systemPatterns.md + techContext.md |

**Key Insight:** Custom Agents tell Copilot HOW you work. The Memory Bank tells Copilot WHERE you are.

### Reflection

How would a Memory Bank help in YOUR daily work?
```
Project I'd use it on: ______________________________
Most valuable file for me: __________________________
What I'd put in activeContext.md: ___________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Memory Architect"

---

## ⚠️ The 70% Problem - Critical Understanding

### The Reality Check

```
THE 70/30 SPLIT

AI Delivers Fast (70%):
┌────────────────────────────────────┐
│ ✅ Boilerplate code                │
│ ✅ Standard CRUD operations        │
│ ✅ Happy path implementation       │
│ ✅ Basic structure                 │
│ ✅ Common patterns                 │
└────────────────────────────────────┘

YOU Must Add (30%):
┌────────────────────────────────────┐
│ 🎯 Edge cases AI missed            │
│ 🎯 Ownership validation            │
│ 🎯 Security hardening              │
│ 🎯 Error message quality           │
│ 🎯 Production-ready error handling │
│ 🎯 Business logic nuances          │
└────────────────────────────────────┘
```

### Why This Matters

- Organizations that understand this: **26% productivity gains**
- Organizations that don't: **Accumulating technical debt**

**Your Professional Value:**
The 30% is why companies hire professionals. AI handles the routine. YOU handle the critical.

**Reflection:** Think of a time when "done" code wasn't production-ready:
```
What was missing? ____________________________
Who caught it? ______________________________
What could have gone wrong? __________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "70/30 Understander"

---

## 🎮 BOSS FIGHT - The Ultimate Challenge

### The Challenge

Build a **complete TODO TAGGING feature** with many-to-many relationships using ALL techniques from Sessions 1-3.

### Requirements

```
ENDPOINTS:
- POST /api/v1/todos/{id}/tags - Add tag to todo
- GET /api/v1/todos?tag=name - Filter todos by tag
- DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag

DATABASE:
- Tag model: id, name, user_id, created_at
- todo_tags association table (many-to-many)

CONSTRAINTS:
- Ownership validation required
- Case-insensitive tags (store lowercase)
- Proper error handling (404, 403, 400)
- 3-tier architecture (models, services, API)
```

### Scoring

| Time | Level | Description |
|------|-------|-------------|
| ≤6 min | 🏆 PLATINUM | Top 1% - Elite |
| ≤8 min | 🥇 GOLD | Top 10% - Expert |
| ≤10 min | 🥈 SILVER | Top 25% - Skilled |
| Completed | ✅ CERTIFIED | Passed! |

**Bonus:** +1 level for each technique used:
- [ ] think hard for planning
- [ ] Plan Mode (/plan)
- [ ] TDD approach
- [ ] Custom Agent

---

### Your Boss Fight Tracker

**Start Time:** _____________

#### Phase 1: Planning (30 seconds)
```
I used: [ ] think hard  [ ] Plan Mode

My plan:
_______________________________________________
_______________________________________________
```

#### Phase 2: Implementation (3 minutes)
```
Files created/modified:
[ ] models/tag.py
[ ] schemas/tag.py
[ ] services/todo_service.py
[ ] api/v1/todos.py
```

#### Phase 3: The Critical 30% (1.5 minutes)
```
I verified:
[ ] Ownership validation works
[ ] Tags are case-insensitive
[ ] Error handling is complete
[ ] Edge cases covered
```

#### Phase 4: Testing (1 minute)
```
Tests I ran:
[ ] Create todo
[ ] Add tag to todo
[ ] Filter by tag
[ ] Remove tag
```

**End Time:** _____________

**Total Time:** _____________ minutes

---

### My Score

```
BASE LEVEL (by time):
[ ] ≤6 min = PLATINUM
[ ] ≤8 min = GOLD
[ ] ≤10 min = SILVER
[ ] Completed = CERTIFIED

BONUSES EARNED:
[ ] Used think hard (+1)
[ ] Used Plan Mode (+1)
[ ] Used TDD (+1)
[ ] Used Custom Agent (+1)

FINAL LEVEL: _________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Boss Fighter"

---

## 🏆 Power User Certification

Congratulations! You've completed the GitHub Copilot Power User Workshop!

### Skills Mastered

```
SESSION 1: FOUNDATION
✅ Security-first development
✅ Copilot modes (Ask, Edit, Agent, Plan)
✅ #file and #folder mentions
✅ .copilotignore configuration

SESSION 2: CONTEXT MASTERY
✅ Thinking modes (think hard)
✅ Explore → Plan → Code workflow
✅ 6-element framework
✅ PRD-driven development

SESSION 3: BUILD SPRINT
✅ Test-Driven Development
✅ Subagents for parallel work
✅ Plan Mode for visibility
✅ Three features in 30 minutes

SESSION 4: MASTERY
✅ Code Review
✅ Custom Agents
✅ The 70/30 Problem
✅ Boss Fight completion
```

### Your Certification

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
_______________________________________________
```

**Biggest mindset shift:**
```
_______________________________________________
```

**What I'll use Monday morning:**
```
_______________________________________________
```

### My Action Plan

**This week, I will:**
```
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
```

**In 30 days, I want to:**
```
_______________________________________________
_______________________________________________
```

---

## Key Takeaways

1. **Security First** - Never expose secrets to AI
2. **Context is King** - Better context = better results
3. **Plan Before Code** - Explore → Plan → Code
4. **Trust but Verify** - Review ALL AI output
5. **Know Your 30%** - YOU add the critical value

---

## Session 4 Achievement Summary

| Achievement | Earned |
|-------------|--------|
| 🔍 Review Master | [ ] |
| 🤖 Agent Creator | [ ] |
| 🧠 Memory Architect | [ ] |
| ⚠️ 70/30 Understander | [ ] |
| 🎮 Boss Fighter | [ ] |
| 🏆 COPILOT CHAMPION | [ ] |

---

## 📚 Continue Learning

### GitHub Awesome Copilot - Your Next Stop

**Your next stop for boosting Copilot skills:**
👉 **https://github.com/github/awesome-copilot**

This curated collection includes:
- 💡 Advanced tips and tricks
- 📖 Community best practices
- 🎯 Use case examples
- 🔧 Tool integrations
- ✨ Latest updates and features

⭐ **Star this repo and check it regularly** - it's actively maintained by the community!

### Official Documentation

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot Chat Documentation](https://docs.github.com/en/copilot/github-copilot-chat)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

**End of Student Packet: Session 4** 🎓

**🎉 CONGRATULATIONS - You're a Copilot Power User! 🎉**
