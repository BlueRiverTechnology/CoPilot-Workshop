# Instructor Guide: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Duration:** 30 minutes
**Achievement:** 🏆 "Copilot Champion"
**Prerequisites:** Sessions 1-3 completed

---

## Session Overview

### Learning Objectives
- ✅ Use Copilot Code Review for PR feedback
- ✅ Create Custom Agents (.agent.md files)
- ✅ Build a Memory Bank for persistent context
- ✅ Understand the 70% Problem and your critical 30%
- ✅ Complete Boss Fight using ALL techniques from Sessions 1-3
- ✅ Earn Power User Certification

---

## Teaching Script

### [0:00-0:02] HOOK - The Final Challenge & Checkpoint Verification

**ENERGY:** Epic finale energy

**SAY:**
> "Welcome to the finale! 🎮
>
> So far you've learned:
> - Security, all AI modes, and #mentions ✅
> - Context mastery & project planning ✅
> - Built features with TDD and Subagents ✅
>
> Today: The ultimate test.
>
> **In 30 minutes:**
> - Master Copilot Code Review
> - Create Custom Agents
> - Build a Memory Bank
> - Understand where YOU add value (The 70/30 Problem)
> - **BOSS FIGHT:** Build tag endpoint using EVERYTHING
>
> Pass the Boss Fight = Power User Certified! 🏆
>
> But first, let's make sure everyone's starting from the same place..."

**DO - Checkpoint Verification:**

```bash
# Switch to session-4-start checkpoint
git checkout session-4-start

# Verify database
python create_db.py

# Run tests (should have 10 passing)
pytest tests/api/test_todos.py -v

# Expected output:
# test_create_todo PASSED
# test_create_todo_minimal PASSED
# test_get_todos_empty PASSED
# test_get_todos PASSED
# test_update_todo PASSED
# test_update_todo_partial PASSED
# test_update_todo_not_found PASSED
# test_create_todo_validation PASSED
# test_delete_todo PASSED
# test_delete_todo_not_found PASSED
# ========== 10 passed ==========
```

**SAY:**
> "✅ Everyone see 10 tests passing?
>
> This checkpoint gives you:
> - Complete POST, GET, PUT, DELETE /todos endpoints
> - Tag model with many-to-many relationship ALREADY BUILT
> - Association table ready
>
> Your Boss Fight won't be building infrastructure - it'll be building ONE powerful API endpoint using what already exists!
>
> Let's finish strong! 💪"

**CHECKPOINT:** Everyone on session-4-start with passing tests?

---

### [0:02-0:08] 🔍 Copilot Code Review (6 min)

**ENERGY:** Professional, quality-focused

**SAY:**
> "GitHub Copilot has a powerful Code Review feature!
>
> Two ways to use it:
> 1. **On GitHub Pull Requests** - automated review
> 2. **In VS Code Chat** - instant feedback
>
> Let me show you both..."

---

#### [0:02-0:05] GitHub PR Review (3 min)

**SHOW ON SCREEN:**
```
COPILOT CODE REVIEW ON GITHUB

Where: GitHub.com Pull Requests
How: Request review from "Copilot"

What it checks:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns

Output:
- Inline comments on specific lines
- Suggestions for improvements
- Identification of issues
```

**SAY:**
> "To use Copilot Code Review on GitHub:
>
> 1. Create a Pull Request on GitHub
> 2. Request review from 'copilot' as a reviewer
> 3. Copilot analyzes your changes
> 4. You get inline comments and suggestions
>
> It's like having a tireless code reviewer on every PR!
>
> In production teams, this catches issues BEFORE human review - saving senior devs time for the complex stuff."

---

#### [0:05-0:08] In-Editor Review with Chat (3 min)

**SAY:**
> "Even more powerful: Review code WITHOUT creating a PR!
>
> Use Copilot Chat directly in VS Code for instant feedback."

**DO - Demonstrate in Copilot Chat:**

```
Review my implementation in #file:src/api/v1/todos.py

Check for:
1. Security issues (auth, validation, ownership checks)
2. Error handling completeness
3. Performance concerns (N+1 queries, missing indexes)
4. Best practice violations

Be thorough and critical. Point out specific line numbers.
```

**SHOW:** Copilot provides detailed feedback with line numbers

**SAY:**
> "See how specific it is? Line numbers, exact issues, suggestions for fixes!
>
> Use this for:
> - Self-review before committing
> - Quick sanity check on changes
> - Learning from AI feedback
> - Finding edge cases you missed
>
> This is YOUR 30% work - AI generates fast, YOU ensure quality!"

🏆 **ACHIEVEMENT:** "Review Master"

---

### [0:08-0:14] 🤖 Custom Agents (.agent.md) (6 min)

**ENERGY:** Power-user excitement

**SAY:**
> "Now for a Copilot POWER feature: Custom Agents!
>
> You can create specialized AI agents that know your project's specific context, patterns, and requirements.
>
> Think of it as creating a senior developer persona who KNOWS your codebase."

---

#### [0:08-0:11] What Are Custom Agents? (3 min)

**SHOW ON SCREEN:**
```
CUSTOM AGENTS (.agent.md files)

Location: .github/agents/*.agent.md

What they do:
- Define specialized AI personas
- Include project-specific knowledge
- Set constraints and patterns
- Reusable across conversations

The Hierarchy:
.github/copilot-instructions.md → Repo-wide, always active
.github/instructions/*.instructions.md → Path-specific rules
.github/agents/*.agent.md → Custom agent definitions

Examples:
- FastAPI Expert Agent
- Testing Specialist Agent
- Security Review Agent
- Database Migration Agent
```

**SAY:**
> "Custom Agents are pre-configured AI specialists.
>
> Instead of explaining your project every time, the agent KNOWS:
> - Your architecture patterns
> - Your coding standards
> - Your common tasks
> - Your file structure
>
> It's persistent expertise you can invoke on demand!"

---

#### [0:11-0:14] Creating a Custom Agent (3 min)

**SAY:**
> "Let's create a Todo API Expert Agent for our project!"

**DO - Create agent file (.github/agents/todo-api-expert.agent.md):**

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

**SAY:**
> "Now when you reference this agent, Copilot has ALL this context automatically!"

**SHOW usage example:**
```
Using context from #file:.github/agents/todo-api-expert.agent.md:

Add a GET /api/v1/tags endpoint that:
- Lists all tags for the current user
- Returns List[TagResponse]
- Follows existing patterns
```

**SAY:**
> "The agent KNOWS:
> - Your 3-tier architecture
> - Your file structure
> - Your coding patterns
> - Your database models
>
> Less explaining, better results, consistent code!
>
> Create agents for different domains:
> - Testing agent (knows test patterns)
> - Security agent (focuses on vulnerabilities)
> - Performance agent (optimizes queries)
>
> Each one is a specialist!"

🏆 **ACHIEVEMENT:** "Agent Creator"

---

### [0:14-0:20] 🧠 Memory Bank - Persistent Project Context (6 min)

**ENERGY:** Mind-blown, "this changes everything"

**SAY:**
> "Custom Agents are powerful. But here's the problem:
>
> Every time you start a new Copilot chat session... it FORGETS everything.
>
> Your architecture decisions? Gone.
> What you worked on yesterday? Gone.
> What you decided about the database? Gone.
>
> **The Memory Bank solves this.**
>
> It gives Copilot a structured set of markdown files to read at the start of every conversation — so it always knows your project state."

---

#### [0:14-0:17] Building a Memory Bank (3 min)

**SAY:**
> "A Memory Bank is simple: 6 markdown files that answer key questions about your project.
>
> Let me show you the structure..."

**SHOW ON SCREEN:**
```
MEMORY BANK STRUCTURE

your-project/
├── .github/
│   └── copilot-instructions.md    ← UPDATE: Tell Copilot to read memory bank
├── memory-bank/                    ← CREATE: 6 context files
│   ├── projectbrief.md            (What is this project?)
│   ├── productContext.md          (Why does it exist?)
│   ├── techContext.md             (What are we building with?)
│   ├── systemPatterns.md          (How do we build things?)
│   ├── activeContext.md           (What's happening RIGHT NOW?)
│   └── progress.md                (Where do we stand?)
└── src/
    └── ... your code
```

**SAY:**
> "Each file has a purpose..."

**SHOW ON SCREEN:**
```
THE 6 FILES

projectbrief.md — "What is this project?"
  → Project name, goals, scope, requirements
  → The foundation everything else builds on

productContext.md — "Why does this project exist?"
  → Problems it solves, who it's for
  → User experience goals
  → How it fits in the bigger picture

techContext.md — "What are we building with?"
  → Languages, frameworks, libraries
  → Dev environment setup
  → Technical constraints and decisions

systemPatterns.md — "How do we build things here?"
  → Architecture (e.g., 3-tier, microservices)
  → Design patterns in use
  → Naming conventions, file structure

activeContext.md — "What's happening RIGHT NOW?"
  → Current sprint/focus area
  → Recent changes and decisions
  → Immediate next steps
  → ⚡ MOST IMPORTANT FILE - update daily

progress.md — "Where do we stand?"
  → What's working
  → What's left to build
  → Known issues and blockers
```

**SAY:**
> "The magic happens in `.github/copilot-instructions.md`..."

**DO - Show what to add:**

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

**SAY:**
> "That's it. Now Copilot reads your context EVERY session.
>
> The 'update memory bank' command is magic - at the end of your day, just say those three words and Copilot updates all context files based on what you accomplished!"

---

#### [0:17-0:20] Memory Bank in Practice (3 min)

**SAY:**
> "Here's the daily workflow..."

**SHOW ON SCREEN:**
```
THE DAILY WORKFLOW

Morning:   Copilot reads memory-bank/ → Full context
           "I see you're working on the tagging feature.
            Last session you built the Tag model and
            association table. Next is the API layer."

Coding:    Better suggestions because of context
           No more repeating yourself
           Copilot knows your patterns and where you are

End of day: "update memory bank"
           → activeContext.md updated with today's work
           → progress.md updated with status

Next day:  Copilot reads updated files → Continuity
           Zero context lost
```

**SAY:**
> "Think of it this way:
>
> **Custom Agents** tell Copilot HOW you work (patterns, rules)
> **Memory Bank** tells Copilot WHERE you are (current state)
>
> Together, they create persistent AI knowledge of your project!
>
> Your workshop project has `.github/copilot-instructions.md` and `PRD.md` - that's the foundation.
>
> The Memory Bank pattern takes it to the next level for real-world, multi-day projects.
>
> This separates someone who USES Copilot from someone with a true AI-augmented workflow!"

🏆 **ACHIEVEMENT:** "Memory Architect"

---

### [0:20-0:23] ⚠️ The 70% Problem - Critical Understanding (3 min)

**ENERGY:** Serious, professional, setting expectations

**SAY:**
> "Before the Boss Fight, one critical lesson from industry research:
>
> **THE 70% PROBLEM**
>
> AI delivers rapid initial progress - gets you 70% of the way FAST.
> But the final 30%? That's where YOU add value.
>
> Organizations that understand this see 26% productivity gains.
> Those that don't? They face accumulating technical debt and bugs in production."

**SHOW ON SCREEN:**
```
THE 70% PROBLEM

AI Delivers Fast (70%):
✅ Boilerplate code
✅ Standard patterns
✅ Happy path implementation
✅ Basic structure
✅ Common use cases

YOU Must Add (30%):
🎯 Edge cases AI missed
🎯 Ownership validation
🎯 Performance optimization
🎯 Security hardening
🎯 Production-readiness
🎯 Business logic nuances
🎯 Real-world error handling
🎯 "What if" scenarios
```

**SAY:**
> "Concrete example from our Todo API:
>
> **AI's 70%:**
> - Creates the endpoint structure
> - Connects to the database
> - Returns data
> - Basic validation
>
> **YOUR 30%:**
> - Checks: Can user only tag THEIR OWN todos?
> - Handles: What if the todo doesn't exist?
> - Optimizes: Is there an N+1 query problem?
> - Secures: Could this leak another user's data?
>
> In the Boss Fight:
> - AI will get you 70% there quickly
> - YOUR job is to finish the final 30%
>
> This is where professionals shine. This is where YOU prove mastery! 💪
>
> Ask yourself: 'What could go wrong? What did AI assume?'"

🏆 **ACHIEVEMENT:** "70/30 Understander"

---

### [0:23-0:28] 🎮 BOSS FIGHT - The Ultimate Challenge (5 min)

**ENERGY:** EPIC FINALE, game show excitement

**SAY:**
> "This is it. THE BOSS FIGHT. 🎮
>
> Everything you've learned. All techniques. One challenge.
>
> **THE CHALLENGE:**
> Build a POST endpoint to add tags to todos using the many-to-many relationship.
>
> **What's ALREADY BUILT (in session-4-start):**
> - ✅ Tag model (id, name, created_at)
> - ✅ todo_tags association table
> - ✅ Relationship defined in Todo model
>
> **WHAT YOU BUILD:**
> - POST /api/v1/todos/{todo_id}/tags
> - Request body: { "name": "urgent" }
> - Creates tag if doesn't exist (case-insensitive)
> - Associates tag with todo
> - Returns updated TodoResponse with tags included
> - Proper error handling (404 if todo not found, 403 if not owned)
> - THE 30%: Ownership validation, edge cases, error messages
>
> **TECHNIQUES TO USE:**
> - ✅ Custom Agent context (just created!)
> - ✅ 'think hard' for planning (Session 2)
> - ✅ Context+Task+Constraints+Format prompts (Session 2)
> - ✅ Advanced #mentions (Session 2)
> - ✅ TDD approach (Session 3)
> - ✅ Code Review when done (just learned!)
>
> **SCORING:**
> - Complete in 3 min: 🏆 PLATINUM (top 1%)
> - Complete in 4 min: 🥇 GOLD (top 10%)
> - Complete in 5 min: 🥈 SILVER (top 25%)
> - Complete at all: ✅ CERTIFIED
>
> **BONUS POINTS:**
> - Used 'think hard' for planning: +1 level
> - Used TDD approach: +1 level
> - Used Custom Agent: +1 level
> - Verified ownership validation (the 30%): +1 level
>
> **BOSS FIGHT STARTS... NOW! ⏱️🎮**"

**TIMER:** 5 minutes (strict)

---

## Boss Fight Winning Strategy

### Recommended Approach (share if asked)

**STEP 1: Plan with Think Hard (30 seconds)**

```
#file:.github/agents/todo-api-expert.agent.md #file:src/models/tag.py #file:src/models/todo.py

think hard about implementing POST /api/v1/todos/{todo_id}/tags

Requirements:
- Add tag to todo (create tag if doesn't exist)
- Case-insensitive tag lookup
- Return updated TodoResponse with tags
- Handle 404 (todo not found), 403 (not owned)

Give me the implementation plan.
```

**STEP 2: Implement (3-4 min)**

Option A: Single comprehensive prompt
```
#file:.github/agents/todo-api-expert.agent.md #file:PRD.md #file:src/models/tag.py #folder:src/api/v1/

[Context]
Tag model and todo_tags association table already exist in src/models/tag.py.
Todo model has tags relationship defined.
Following 3-tier architecture per agent instructions.

[Task]
Add POST /api/v1/todos/{todo_id}/tags endpoint to associate tags with todos.

[Constraints]
1. TagCreate schema: { "name": str } (1-50 chars)
2. Service method add_tag_to_todo(todo_id, tag_name, user_id, db):
   - Check todo exists and is owned by user (404/403)
   - Normalize tag name to lowercase
   - Create tag if doesn't exist (get or create pattern)
   - Add tag to todo.tags relationship
   - Return updated Todo object
3. POST endpoint:
   - Path param: todo_id (UUID string)
   - Request body: TagCreate
   - Require authentication (default-user)
   - Return TodoResponse with tags included
4. Update TodoResponse schema to include tags: List[TagResponse]
5. Error handling: 404 if todo not found, 403 if not owned

[Format]
Create:
- src/schemas/tag.py (TagCreate, TagResponse)
- Add method to src/services/todo_service.py
- Add endpoint to src/api/v1/todos.py
- Update src/schemas/todo.py (add tags to TodoResponse)
```

Option B: TDD approach (if time allows)
```
First create test, then implement to pass it.
```

**STEP 3: The Critical 30% (30 seconds)**

```
Review the tag implementation for production readiness:

1. Ownership validation - Verified?
2. Case sensitivity - Tags normalized to lowercase?
3. Idempotency - What if tag already on todo?
4. Error messages - Clear and helpful?
5. Edge cases covered?

Fix any issues.
```

**STEP 4: Quick Test (30 seconds)**

```bash
# Test the endpoint
curl -X POST http://localhost:8000/api/v1/todos/<todo_id>/tags \
  -H "Content-Type: application/json" \
  -d '{"name": "urgent"}'

# Verify tags appear
curl http://localhost:8000/api/v1/todos/<todo_id>
```

---

### [0:28-0:30] 🎉 Victory Lap & Certification (2 min)

**ENERGY:** Celebration mode

**SAY:**
> "TIME! ✋
>
> Who finished? 🙋
> Who got it working? 🙋
> Who verified ownership validation (the 30%)? 🙋
>
> **Certification levels achieved:**
> - Platinum (≤3 min)? 🏆
> - Gold (≤4 min)? 🥇
> - Silver (≤5 min)? 🥈
> - Certified (completed)? ✅"

**CELEBRATE:**
> "🎉 CONGRATULATIONS! 🎉
>
> You've completed the GitHub Copilot Power User Workshop!
>
> In 3 hours total, you learned:
>
> **Session 1:**
> - Security-first development (.copilotignore, approval models)
> - All Copilot modes (Ask, Edit, Agent, Plan)
> - Writing effective rules and instructions
>
> **Session 2:**
> - Context mastery with #mentions
> - Professional workflows (Explore → Plan → Code)
> - 6-Element Prompt Framework
>
> **Session 3:**
> - TDD with AI
> - Subagents and parallel work
> - Building features FAST
>
> **Session 4:**
> - Code Review and Custom Agents
> - Memory Bank pattern
> - The critical 70/30 understanding
> - Boss Fight completion!
>
> You're not beginners anymore.
> You're POWER USERS.
> You're AI-AUGMENTED PROFESSIONALS.
>
> Go transform how your team codes! 💪🚀"

**HAND OUT CERTIFICATES:**
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
│   Level: _______________                    │
│   Date: _______________                     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Session 4 Wrap-Up

### Achievements Unlocked

- 🔍 **Review Master** - Used Copilot Code Review
- 🤖 **Agent Creator** - Created Custom Agent
- 🧠 **Memory Architect** - Built Memory Bank
- ⚠️ **70/30 Understander** - Knows where to add value
- 🎮 **Boss Fighter** - Completed final challenge
- 🏆 **COPILOT CHAMPION** - Full workshop complete!

---

## Instructor Notes

### Common Issues & Solutions

**Issue:** Students skip checkpoint verification
**Solution:** Don't start until EVERYONE has 10 passing tests. This is critical.

**Issue:** Boss Fight too ambitious even simplified
**Solution:** Extend to 7 minutes if needed. The time buffer allows this.

**Issue:** Custom Agent concept unclear
**Solution:** Explain as "pre-loaded expert context for every conversation"

**Issue:** Memory Bank seems like overkill
**Solution:** Emphasize: "For this 2-hour workshop, maybe. For real projects spanning weeks? Essential."

**Issue:** 70/30 concept misunderstood
**Solution:** Give specific examples: "AI creates endpoint. YOU add: What if user doesn't own this todo?"

**Issue:** Students don't verify ownership in Boss Fight
**Solution:** During review, explicitly ask: "Can ANY user tag ANY todo? Or just their own?"

### Time Flexibility

**If running behind (use the 5-min buffer):**
- Shorten Code Review to 4 min (skip GitHub PR, focus on in-editor)
- Shorten Custom Agents to 4 min (show concept, don't create live)
- Shorten Memory Bank to 4 min (explain structure, skip daily workflow details)
- Keep 70/30 Problem (3 min) - critical concept
- Keep Boss Fight time (5 min) - core challenge
- 4+4+4+3+5 = 20 min + 2 min intro/wrap = 22 min (8 min buffer!)

**If ahead (rare, but possible):**
- Have students create their own Custom Agent for another domain
- Build a second tag endpoint (GET /todos?tag=name filter)
- Do full code review of Boss Fight results
- Discuss Memory Bank strategies for different project types

### Energy Management

- **Epic:** Opening & checkpoint (0:00-0:02)
- **Professional:** Code Review (0:02-0:08)
- **Excited:** Custom Agents (0:08-0:14)
- **Mind-blown:** Memory Bank (0:14-0:20)
- **Serious:** 70/30 Problem (0:20-0:23)
- **Game show:** Boss Fight (0:23-0:28)
- **Celebration:** Certification (0:28-0:30)

### Key Teaching Points

1. **Checkpoint-based learning is safe** - Everyone starts from working code
2. **Code Review is part of the workflow** - Not an afterthought
3. **Custom Agents reduce repetitive context** - DRY principle for prompts
4. **Memory Bank enables continuity** - Multi-day projects need this
5. **70/30 is critical** - AI speed + human quality = professional results
6. **Boss Fight tests EVERYTHING** - Integration of all techniques

### What Makes This Session Work

1. **Checkpoint removes Session 3 dependency** - Even if Session 3 struggled, everyone starts Session 4 equal
2. **Simplified Boss Fight is achievable** - ONE endpoint vs three means more students succeed
3. **5-minute time buffer** - Room for things to go wrong without panic
4. **70/30 concept reframes success** - "AI got you 70%, now YOU finish it" removes pressure to have AI do everything
5. **Clear success criteria** - Working endpoint with ownership validation = win

### Pre-Session Preparation

**Verify before session:**
- [ ] session-4-start branch exists in student repo
- [ ] Tag model and todo_tags table are in the branch
- [ ] DELETE endpoint exists and works
- [ ] All 10 tests pass on the checkpoint
- [ ] create_db.py script works
- [ ] You've tested the Boss Fight timing yourself

**Have ready:**
- [ ] Custom Agent example file
- [ ] Memory Bank structure diagram
- [ ] Boss Fight success criteria on screen
- [ ] Certificates printed or digital
- [ ] Timer for Boss Fight

---

**End of Instructor Guide: Micro Session 4** 🎓

**🎉 COMPLETE WORKSHOP SERIES FINISHED! 🎉**
