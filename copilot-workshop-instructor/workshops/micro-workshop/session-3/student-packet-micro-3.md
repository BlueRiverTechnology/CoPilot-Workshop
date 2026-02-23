# Student Packet: Micro Session 3
## Build Sprint - TDD Edition 🚀🧪

**Name:** _________________________
**Date:** _________________________
**Achievement Goal:** 🏆 "Build Master"

---

## Learning Objectives

- [ ] Start with working code (checkpoint safety net)
- [ ] Watch professional TDD workflow with DELETE endpoint
- [ ] Build ONE feature hands-on using full context
- [ ] Compare TDD vs full context approaches
- [ ] Know when to use each approach
- [ ] Experience the safety of checkpoint-based development

---

## From Session 2 to Session 3

**Session 2 - You learned PROFESSIONAL PROMPTING:**
- ✅ 6-element framework (Context + Task + Constraints + Format + Persona + Examples)
- ✅ Advanced #mentions for context
- ✅ PRD creation and planning
- ✅ Thinking modes for complex decisions

**Session 3 - You BUILD with those skills.**
- Starting with WORKING infrastructure (session-3-start checkpoint)
- This is DIFFERENT from building from scratch!
- Focus on learning workflows, not debugging setup

---

## The Checkpoint Approach

**The Foundation:**
You're starting with WORKING code, not empty scaffolding.

**Why this matters:**
- In the original workshop, too many things could fail at once
- Database setup, async SQLAlchemy, test fixtures - each failure ate 5+ minutes
- Students spent time debugging infrastructure, not learning AI workflows

**NEW approach:**
- Start with working infrastructure
- Learn by watching professional TDD
- Build ONE feature with support
- Safety net: `git reset --hard session-3-start` brings you back anytime

**Today:** Master professional workflows with a safety net!

---

## 🛡️ Checkpoint Verification (3 minutes)

### Step 1: Checkout Session 3 Start Branch

**Commands to run:**
```bash
git checkout session-3-start
```

**What this branch includes:**
- ✅ POST /todos endpoint (create)
- ✅ GET /todos endpoint (list with filtering)
- ✅ PUT /todos/{id} endpoint (update)
- ✅ Database setup (create_db.py)
- ✅ Test fixtures (tests/conftest.py)
- ✅ All schemas, services, routes
- ✅ 8 passing tests

**Everything works. Let's verify it!**

---

### Step 2: Verify Checkpoint Works

**Run these commands:**

```bash
# 1. Create the database
python create_db.py

# 2. Run all tests
pytest tests/api/test_todos.py -v
```

**Expected output: All 8 tests passing**
```
✅ test_create_todo
✅ test_create_todo_minimal
✅ test_get_todos_empty
✅ test_get_todos
✅ test_update_todo
✅ test_update_todo_partial
✅ test_update_todo_not_found
✅ test_create_todo_validation
```

**Status:** [ ] My checkpoint is working (8/8 tests passing)

**If tests fail:**
```bash
git reset --hard session-3-start
# Try again - that's the safety net in action!
```

---

🏆 **Achievement:** [ ] "Checkpoint Master" (verified working infrastructure)

---

## 🧪 Instructor Demo: DELETE Endpoint with TDD (10 minutes)

**What you're learning:**
Watch professional Test-Driven Development workflow.

**The TDD Process:**
1. Write tests FIRST (they'll fail - that's expected!)
2. Run tests and see them fail (RED)
3. Implement code to make tests pass (GREEN)
4. Verify success (all tests pass)

**Your job:** WATCH and take notes. You'll practice the full context approach next!

---

### TDD Step 1: Write Tests First

**Prompt the instructor used:**
```
[CONTEXT]
#file:tests/api/test_todos.py shows existing test patterns
#file:src/models/todo.py defines the Todo model
#file:src/api/v1/todos.py has existing endpoints (POST, GET, PUT)

Working on todo API following 3-tier architecture.
Tests use pytest-asyncio with AsyncClient fixture.

[TASK]
Add tests for DELETE /api/v1/todos/{todo_id} endpoint to tests/api/test_todos.py

[CONSTRAINTS]
Test cases to include:
1. test_delete_todo - Successfully delete owned todo (returns 204)
2. test_delete_todo_not_found - Delete non-existent todo (returns 404)

Follow existing test patterns:
- Use client fixture from conftest.py
- Use default_user fixture for ownership
- Create test todo using POST first, then delete it
- Verify deletion with follow-up GET request

DON'T implement the endpoint yet - ONLY add the test functions

[FORMAT]
Add 2 new test functions to existing tests/api/test_todos.py file
```

**Key observations:**
- [ ] Used #file mentions to reference existing patterns
- [ ] Explicit constraint: DON'T implement yet, tests only
- [ ] Clear test case descriptions
- [ ] Follows 6-element framework from Session 2

**Tests created:** _______________________________________________________

---

### TDD Step 2: Run Tests and Watch Them Fail

**Command:**
```bash
pytest tests/api/test_todos.py::test_delete_todo -v
pytest tests/api/test_todos.py::test_delete_todo_not_found -v
```

**Expected result:** Tests FAIL (endpoint doesn't exist)

**Why this is good:**
- Proves tests are actually testing something
- When we implement and tests pass, we KNOW it works
- This is RED in the TDD Red-Green-Refactor cycle

**Observation:** Tests failed as expected [ ]

---

### TDD Step 3: Implement to Make Tests Pass

**Prompt the instructor used:**
```
[CONTEXT]
#file:tests/api/test_todos.py defines success criteria for DELETE endpoint (test_delete_todo and test_delete_todo_not_found)
#file:src/api/v1/todos.py has existing endpoints (POST, GET, PUT) showing routing patterns
#file:src/services/todo_service.py has TodoService class with create, get_all, get_by_id, update methods
#file:src/models/todo.py defines the Todo model
#file:.github/copilot-instructions.md has architecture and coding standards

Following 3-tier architecture: API → Service → Models

[TASK]
Implement DELETE /api/v1/todos/{todo_id} endpoint to make the new tests pass

[CONSTRAINTS]
Implementation requirements:
1. Add delete_todo() method to TodoService class:
   - Parameters: todo_id (str), user_id (str)
   - Fetch todo by ID
   - Check ownership (owner_id must match user_id)
   - If not found or not owned: return None
   - If owned: delete from database, commit, return True
   - Use async/await patterns

2. Add DELETE "/{todo_id}" endpoint to todos router:
   - Path parameter: todo_id (str)
   - Get database session with Depends(get_db)
   - Use fixed user_id = "default-user" (matches POST/PUT endpoints)
   - Call service.delete_todo()
   - Return 404 if None, 204 No Content if successful
   - Include proper HTTPException error handling

Must satisfy both test cases:
- test_delete_todo: Returns 204 when deleting owned todo
- test_delete_todo_not_found: Returns 404 when todo doesn't exist

Follow existing endpoint patterns for consistency

[FORMAT]
Update these files:
1. src/services/todo_service.py - add delete_todo method to TodoService class
2. src/api/v1/todos.py - add DELETE endpoint
```

**Key observations:**
- [ ] Referenced the TESTS as context (AI knows what success looks like)
- [ ] Detailed constraints for both service and API layers
- [ ] Must satisfy specific test cases
- [ ] Follows 3-tier architecture pattern

**Implementation notes:** _________________________________________________

---

### TDD Step 4: Run Tests and Celebrate Green

**Command:**
```bash
pytest tests/api/test_todos.py -v
```

**Expected result:** ALL 10 tests pass (8 original + 2 new DELETE tests)

**Why TDD works with AI:**
1. Tests give AI clear success criteria
2. Less ambiguity = better first-try code
3. Automatic verification - no manual testing needed
4. Professional workflow from day one

**Final result:** All tests passing [ ]

---

🏆 **Achievement:** [ ] "TDD Observer" (watched complete TDD workflow)

---

## 🎯 Student Hands-On: Build ONE Feature (12 minutes)

**Now YOUR turn!**

You'll build ONE feature yourself using the FULL CONTEXT approach from Session 2.

**Your challenge: Add a 'priority' field to todos**

Simple feature. Clear requirements. Working infrastructure.

---

### Feature Requirements & Strategy (2 minutes)

**What you're building:**

```
FEATURE: Add Priority Field to Todos

REQUIREMENTS:
1. Add 'priority' field to Todo model
   - Type: Integer
   - Values: 1 (high), 2 (medium), 3 (low)
   - Default: 2 (medium)
   - Optional in creation

2. Update schemas:
   - TodoCreate: priority is optional (defaults to 2)
   - TodoResponse: include priority
   - TodoUpdate: allow updating priority

3. Update existing endpoints:
   - POST /todos: Accept priority in request
   - GET /todos: Return priority in response
   - PUT /todos/{id}: Allow updating priority

4. Add filtering:
   - GET /todos?priority=1 should filter by priority

SUCCESS CRITERIA:
✅ Can create todo with priority
✅ Can create todo without priority (defaults to 2)
✅ Can update priority
✅ Can filter by priority
✅ All existing tests still pass
```

---

### Plan Your Approach (30 seconds)

**Questions to think about:**
1. What complexity level? (Simple/Medium/Complex)
2. Which elements of the 6-element framework do you need?
3. What #mentions should you include?
4. One prompt or multiple steps?

**My strategy:**
- Complexity: ____________
- Elements I'll use: ____________
- Key #mentions: ____________
- Approach: ____________

---

### Building Time (8 minutes)

**Tips:**
- Start with ONE good prompt
- Use #file to reference existing code
- Be specific in constraints
- Test after implementation

**If you get stuck:**
- Raise your hand for help
- Check the prompt sheet (PROMPT-SHEET-SESSION-3.md)
- Remember: Safety net is `git reset --hard session-3-start`

**My prompt:**
```
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________
```

**Testing commands:**
```bash
# Run existing tests to ensure nothing broke
pytest tests/api/test_todos.py -v

# Start server to test manually
uvicorn src.main:app --reload

# Test creating todo with priority
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "High priority task", "priority": 1}'

# Test filtering by priority
curl "http://localhost:8000/api/v1/todos?priority=1"
```

**Results:**
- Time taken: _____ minutes
- First attempt success: [ ] Yes [ ] No
- Iterations needed: _____
- Final status: [ ] Working [ ] In progress [ ] Stuck

---

🏆 **Achievement:** [ ] "Feature Builder" (built complete feature with full context)

---

## 🧠 Reflection & Comparison (3 minutes)

### Two Approaches Comparison

**🧪 TDD APPROACH (Instructor Demo - DELETE endpoint)**

Process: Tests First → Fail → Implement → Pass

Strengths I observed:
- _________________________________________________________________
- _________________________________________________________________
- _________________________________________________________________

Best for: _____________________________________________________________

---

**⚡ FULL CONTEXT APPROACH (Your Priority Field)**

Process: Plan → One Comprehensive Prompt → Implement

Strengths I experienced:
- _________________________________________________________________
- _________________________________________________________________
- _________________________________________________________________

Best for: _____________________________________________________________

---

### When to Use Each Approach

**Use TDD when:**
- [ ] Requirements are complex or unclear
- [ ] Learning a new pattern
- [ ] Testing is critical (security, payments, data integrity)
- [ ] Establishing patterns for AI to follow

**Use Full Context when:**
- [ ] Requirements are crystal clear
- [ ] Existing patterns to follow
- [ ] Speed matters
- [ ] Infrastructure already working (like today!)

**The Pro Move:**
Combine them! Start with TDD for first feature (establishes patterns), switch to Full Context for similar features (follows patterns), back to TDD when adding something genuinely new.

**My takeaway:**
_____________________________________________________________________
_____________________________________________________________________

---

🏆 **Achievement:** [ ] "Strategic Thinker" (understands when to use each approach)

---

## Session 3 Victory Lap

**Look at what you accomplished in 30 minutes:**

✅ Started with working API (checkpoint verified)
✅ Watched professional TDD workflow (DELETE endpoint)
✅ Built a complete feature hands-on (priority field)
✅ Learned when to use TDD vs Full Context
✅ Experienced checkpoint safety net
✅ Used 6-element framework in practice
✅ Professional AI development skills

**Capabilities gained:**
- 🧪 Test-Driven Development with AI
- ⚡ Full Context implementation
- 🎯 Strategic approach selection (TDD vs Full Context)
- 🛡️ Checkpoint-based development safety
- 📋 Professional prompt structure in action

---

## 🏆 Session 3 Achievements Checklist

- [ ] 🛡️ **Checkpoint Master** - Successfully used checkpoint safety net
- [ ] 👀 **TDD Observer** - Watched complete TDD workflow
- [ ] 🏗️ **Feature Builder** - Built a complete feature with full context
- [ ] 🧠 **Strategic Thinker** - Understands when to use each approach
- [ ] 🏆 **Build Master** - Completed Session 3!

**Total Achievements Earned:** _____ / 5

---

## What Made Today's Session Work?

**The checkpoint safety net:**
- ✅ Working database setup
- ✅ Async fixtures configured
- ✅ 8 passing tests proving it works
- ✅ Complete examples to reference

**This let you focus on:**
- Learning workflows instead of debugging infrastructure
- Comparing approaches instead of fixing setup
- Building features instead of troubleshooting async issues

**The power of `git reset --hard session-3-start`:**
Anytime you broke something, one command brought you back.

**That's checkpoint-based learning!** 🛡️

---

## Looking Ahead: Session 4 Preview

**What's next - the FINALE!** 🎮

**Session 4: Code Review, Custom Agents & Boss Fight**

You'll learn:
- Code Review with Copilot (automated quality checks)
- Custom Agents (.agent.md files for specialized tasks)
- Memory Bank (persistent project context)
- The 70% Problem (AI gets you 70%, you add the critical 30%)

Then: **THE BOSS FIGHT!** 💪
- 10-minute challenge
- Build ONE tag-related endpoint
- Tag model already provided (another checkpoint!)
- Apply EVERYTHING you learned
- Earn Power User Certification!

**Preparation:**
- [ ] Session 3 completed
- [ ] Understand TDD vs Full Context trade-offs
- [ ] Confident with 6-element framework
- [ ] Ready for the finale!

---

## Quick Reference Card

### Checkpoint Commands
```bash
# Checkout session 3 start
git checkout session-3-start

# Reset if something breaks
git reset --hard session-3-start

# Verify checkpoint works
python create_db.py
pytest tests/api/test_todos.py -v
```

### TDD Cycle
```
1. Write Tests First (RED)
   ↓
2. Run Tests → Fail
   ↓
3. Implement Code (GREEN)
   ↓
4. Run Tests → Pass
   ↓
5. Refactor (optional)
```

### 6-Element Framework (from Session 2)
```
[PERSONA] + [CONTEXT] + [TASK] + [CONSTRAINTS] + [FORMAT] + [EXAMPLES]
           ↑ Always!    ↑ Always!
```

### When to Use What
```
TDD: Complex features, unclear requirements, critical testing
Full Context: Clear requirements, existing patterns, speed matters
Hybrid: Best of both - TDD for patterns, Full Context to follow them
```

---

**End of Student Packet: Micro Session 3** 🎓
