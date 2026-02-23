# Instructor Guide: Micro Session 3
## Build Sprint - TDD Edition 🚀🧪

**Duration:** 30 minutes
**Achievement:** 🏆 "Build Master"
**Prerequisites:** Session 2 completed (context mastery learned)

---

## Session Overview

### Learning Objectives
- ✅ Start with working code (checkpoint safety net)
- ✅ Watch professional TDD workflow with DELETE endpoint
- ✅ Build ONE feature hands-on with full context
- ✅ Compare TDD vs full context approaches
- ✅ Know when to use each approach
- ✅ Experience the safety of checkpoint-based development

---

## CRITICAL: New Checkpoint-Based Approach

**THIS SESSION IS COMPLETELY DIFFERENT FROM THE ORIGINAL.**

**OLD approach:** Students build API from empty scaffolding, everything can break.

**NEW approach:** Students start with WORKING code, learn by watching then doing ONE thing well.

**Instructor mindset:** You're teaching TDD patterns and professional workflows, NOT debugging async SQLAlchemy setup for 20 students simultaneously.

**Safety net:** If anything breaks, students can `git reset --hard session-3-start` and they're back to working code.

---

## Pre-Session Checklist

- [ ] Students have completed Session 2
- [ ] Students have the `copilot-workshop-student` repo
- [ ] Students can checkout branches (`git checkout session-3-start`)
- [ ] Verify YOUR demo environment has the checkpoint code working
- [ ] Have the DELETE endpoint prompt ready (see PROMPT SHEET)
- [ ] Timer ready for student exercise

---

## 🧠 SESSION 3 SCRIPT

### [0:00-0:03] Checkpoint Verification & Safety Net (3 min)

**ENERGY:** Clear, reassuring, setting up success

**SAY:**
> "Welcome to Session 3 - Build Sprint! This is where you actually BUILD features using what you learned.
>
> But first - **the most important 3 minutes of the session.**
>
> We're using a CHECKPOINT approach. You're starting with WORKING code, not empty scaffolding.
>
> Why? Because in the original workshop, too many things could fail at once. Database setup, async SQLAlchemy, test fixtures - each failure ate 5 minutes per student.
>
> **NEW approach:** Start with working infrastructure. Learn by watching, then build ONE feature with support.
>
> Let's verify your checkpoint is working! 🛡️"

---

#### [0:00-0:02] Checkout Session 3 Start Branch (2 min)

**DO - Guide students step-by-step:**

**SAY:**
> "Everyone, open your terminal in the `copilot-workshop-student` folder.
>
> Type this command:"

```bash
git checkout session-3-start
```

**SHOW on your screen while they do it.**

**SAY:**
> "This branch has:
> - ✅ POST /todos endpoint (create)
> - ✅ GET /todos endpoint (list with filtering)
> - ✅ PUT /todos/{id} endpoint (update)
> - ✅ Database setup (`create_db.py`)
> - ✅ Test fixtures (`tests/conftest.py`)
> - ✅ All schemas, services, routes
> - ✅ 8 passing tests
>
> Everything works. Let's verify it!"

---

#### [0:02-0:03] Verify Checkpoint Works (1 min)

**DO - Run verification commands together:**

**SAY:**
> "Run these commands with me. Everyone type along:"

```bash
# 1. Create the database
python create_db.py

# 2. Run all tests
pytest tests/api/test_todos.py -v
```

**SHOW YOUR SCREEN:** All 8 tests passing:
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

**SAY:**
> "Everyone see 8 tests passing? 🙋
>
> If yes: ✅ Your API works! You have a safety net!
>
> If no: Don't panic! Just run `git reset --hard session-3-start` and try again. That's the safety net in action."

**CHECKPOINT:** Everyone has working tests?

**SAY:**
> "Perfect! ✅ You now have working infrastructure.
>
> **The safety net:** Anytime something breaks today, you can reset to this checkpoint:
> ```bash
> git reset --hard session-3-start
> ```
>
> You're never more than 5 seconds away from working code.
>
> That's the power of checkpoint-based learning! 🛡️"

---

### [0:03-0:13] 🧪 Instructor Demo: DELETE Endpoint with TDD (10 min)

**ENERGY:** Teaching, methodical, professional

**SAY:**
> "Now watch me build the DELETE endpoint using Test-Driven Development.
>
> You're going to WATCH, not code. This is a live demo.
>
> I'll show you the complete TDD workflow:
> 1. Write tests FIRST (they'll fail)
> 2. Run tests and see them fail (red)
> 3. Implement code to make tests pass (green)
> 4. Verify success
>
> This is how professionals build with AI. Watch every step! 🧪"

**IMPORTANT:** Students are WATCHING, not coding along. This prevents 20 different implementations and keeps everyone together.

---

#### [0:03-0:05] Step 1: Write the Tests First (2 min)

**SAY:**
> "Step 1 in TDD: Write tests BEFORE any implementation exists.
>
> This feels backward, but it forces you to define WHAT success looks like before HOW to build it."

**DO - Open Copilot Chat (Agent Mode) on your screen, type this prompt:**

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

**SAY while typing:**
> "Notice what I'm doing:
> - **#file references** to existing tests so AI sees the patterns
> - **Context from Session 2** - the 6-element framework
> - **Explicit constraint:** DON'T implement yet, tests only
>
> This is professional prompting!"

**PRESS ENTER, wait for generation**

**SAY while it generates:**
> "Watch... AI is reading our existing tests... learning the patterns... creating test functions that match our style..."

**SHOW the generated test code:**

```python
async def test_delete_todo(client: AsyncClient, default_user: User):
    # Create a todo first
    create_response = await client.post(
        "/api/v1/todos",
        json={"title": "Test Todo", "completed": False}
    )
    assert create_response.status_code == 201
    todo_id = create_response.json()["id"]

    # Delete it
    delete_response = await client.delete(f"/api/v1/todos/{todo_id}")
    assert delete_response.status_code == 204

    # Verify it's gone
    get_response = await client.get(f"/api/v1/todos/{todo_id}")
    assert get_response.status_code == 404


async def test_delete_todo_not_found(client: AsyncClient):
    # Try to delete non-existent todo
    response = await client.delete("/api/v1/todos/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
```

**SAY:**
> "✅ Perfect! Tests created. Notice:
> - They follow our existing patterns
> - They define exactly what success looks like
> - They WILL fail right now (endpoint doesn't exist)
>
> That's the point of TDD!"

---

#### [0:05-0:06] Step 2: Run Tests and Watch Them Fail (1 min)

**SAY:**
> "Step 2: Run tests and confirm they FAIL. This proves our tests are testing something real!"

**DO - Run tests in terminal:**

```bash
pytest tests/api/test_todos.py::test_delete_todo -v
pytest tests/api/test_todos.py::test_delete_todo_not_found -v
```

**SHOW the failures:**
```
FAILED tests/api/test_todos.py::test_delete_todo - 404 Not Found
FAILED tests/api/test_todos.py::test_delete_todo_not_found - 404 Not Found
```

**SAY:**
> "✅ Tests FAIL! Perfect!
>
> This is RED in the TDD Red-Green-Refactor cycle.
>
> Failures prove:
> - Our tests are actually testing something
> - The endpoint doesn't exist yet
> - When we implement it and tests pass, we KNOW it works
>
> Now let's make them GREEN! 🟢"

---

#### [0:06-0:11] Step 3: Implement to Make Tests Pass (5 min)

**SAY:**
> "Step 3: Implement the feature to make tests pass.
>
> Watch how I give AI the TESTS as context. AI can see exactly what success looks like!"

**DO - Copilot Chat (Agent Mode), type this prompt:**

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

**SAY while typing:**
> "See what I'm doing?
> - **#file:tests/api/test_todos.py** - AI knows what success looks like
> - **Referenced existing code** - AI sees our patterns
> - **Explicit architecture** - 3-tier pattern
> - **Detailed constraints** - exactly what to build
> - **Test requirements** - must satisfy both test cases
>
> Zero ambiguity. AI has everything it needs!"

**PRESS ENTER, wait for generation**

**SAY while it generates:**
> "Watch... AI is reading the tests... learning our patterns... implementing the service method... creating the endpoint..."

**SHOW the generated code:**

**Service layer (src/services/todo_service.py):**
```python
async def delete_todo(self, todo_id: str, user_id: str) -> bool | None:
    """Delete a todo if owned by user. Returns True if deleted, None if not found/not owned."""
    result = await self.db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == user_id)
    )
    todo = result.scalar_one_or_none()

    if not todo:
        return None

    await self.db.delete(todo)
    await self.db.commit()
    return True
```

**API layer (src/api/v1/todos.py):**
```python
@router.delete("/{todo_id}", status_code=204)
async def delete_todo(
    todo_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Delete a todo by ID."""
    service = TodoService(db)
    result = await service.delete_todo(todo_id, user_id="default-user")

    if result is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    return Response(status_code=204)
```

**SAY:**
> "✅ Implementation complete! Notice:
> - Service layer handles business logic
> - API layer handles HTTP concerns
> - Follows our existing patterns
> - Handles both success and error cases
>
> Now the moment of truth... do the tests pass?"

---

#### [0:11-0:13] Step 4: Run Tests and Celebrate Green (2 min)

**DO - Run ALL tests:**

```bash
pytest tests/api/test_todos.py -v
```

**SHOW the results:**
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

10 passed in 0.87s
```

**SAY:**
> "🎉 ALL TESTS PASS! Including our 2 new DELETE tests!
>
> That's TDD in action:
> - ✅ RED: Tests failed (endpoint didn't exist)
> - ✅ GREEN: Tests pass (endpoint works)
> - ✅ REFACTOR: Could improve if needed (but it's clean!)
>
> **Why this works with AI:**
> - Tests give AI clear success criteria
> - Less ambiguity = better first-try code
> - Automatic verification - no manual testing needed
> - Professional workflow from day one
>
> You just watched professional TDD! 🧪✨"

**SAY:**
> "Key takeaways from this demo:
> 1. **Tests first** - Define success before implementation
> 2. **Watch them fail** - Proves tests are real
> 3. **Give AI the tests** - They're the best context
> 4. **Verify success** - Automated verification
>
> This is how you build features that WORK the first time! 💪"

---

### [0:13-0:25] 🎯 Student Hands-On: Build ONE Feature (12 min)

**ENERGY:** Supportive, encouraging, hands-on coaching

**SAY:**
> "Now YOUR turn! You'll build ONE feature yourself.
>
> I just showed you TDD with DELETE. Now you'll practice the FULL CONTEXT approach from Session 2.
>
> **Your challenge: Add a 'priority' field to todos**
>
> Simple feature. Clear requirements. Working infrastructure.
>
> You'll use everything from Session 2:
> - 6-element framework
> - #mentions for context
> - Professional prompt structure
>
> I'll give you the requirements, you write the prompt! 📝"

---

#### [0:13-0:15] Feature Requirements & Strategy (2 min)

**SAY:**
> "Here's what you're building:"

**SHOW ON SCREEN:**
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

**SAY:**
> "Before you code, PLAN your approach:
>
> **Questions to think about:**
> 1. What complexity level? (Simple/Medium/Complex)
> 2. Which elements of the 6-element framework do you need?
> 3. What #mentions should you include?
> 4. One prompt or multiple steps?
>
> Take 30 seconds - plan your strategy! ⏱️"

**TIMER:** 30 seconds

**AT 0:30:**
> "Okay! Here's my suggestion:
>
> **Complexity:** Medium (4-5 elements)
> - CONTEXT: #file references to models, schemas, services, routes
> - TASK: Clear - add priority field
> - CONSTRAINTS: Field specs, default value, filtering
> - FORMAT: Which files to update
> - Skip PERSONA (straightforward), skip EXAMPLES (have patterns)
>
> **Approach:** ONE comprehensive prompt
> - You have working infrastructure
> - Requirements are clear
> - AI can see all patterns with #mentions
>
> Ready to build? Let's go! 🚀"

---

#### [0:15-0:23] Student Building Time (8 min)

**SAY:**
> "You have 8 minutes to implement the priority feature.
>
> **Tips:**
> - Start with ONE good prompt
> - Use #file to reference existing code
> - Be specific in constraints
> - Test after implementation
>
> **If you get stuck:**
> - Raise your hand, I'll help
> - Check the prompt sheet
> - Remember: Safety net is `git reset --hard session-3-start`
>
> Timer starts NOW! ⏱️"

**TIMER:** 8 minutes

---

**WHILE STUDENTS WORK:**

**Walk around, monitor progress, provide guidance:**

**Common issues to watch for:**

**Issue 1: Prompt too vague**
**Help:** "What #files should AI look at? What exactly should the priority field do?"

**Issue 2: Not using #mentions**
**Help:** "Reference #file:src/models/todo.py so AI sees the existing model!"

**Issue 3: Trying to do too much at once**
**Help:** "Start with JUST the model and schemas. Then update the endpoints."

**Issue 4: Tests failing**
**Help:** "Run pytest -v to see which test is failing. What's the error message?"

**Issue 5: Completely stuck**
**Provide the example prompt:**

```
[CONTEXT]
#file:src/models/todo.py defines the Todo model
#file:src/schemas/todo.py has TodoCreate, TodoResponse, TodoUpdate schemas
#file:src/services/todo_service.py has TodoService with get_all method (for filtering)
#file:src/api/v1/todos.py has all endpoints

Working on todo API with 3-tier architecture

[TASK]
Add 'priority' field to todos with values 1 (high), 2 (medium), 3 (low)

[CONSTRAINTS]
1. Model layer (src/models/todo.py):
   - Add priority: Integer column to Todo model
   - Default value: 2 (medium)
   - Not nullable

2. Schema layer (src/schemas/todo.py):
   - TodoCreate: priority is Optional[int] = 2
   - TodoResponse: include priority field
   - TodoUpdate: priority is Optional[int] (can update it)

3. Service layer (src/services/todo_service.py):
   - Update get_all() method to accept priority filter parameter
   - Filter by priority if provided: .where(Todo.priority == priority)

4. API layer (src/api/v1/todos.py):
   - GET endpoint: add priority query parameter (Optional[int])
   - Pass priority filter to service.get_all()
   - POST and PUT automatically handle priority (Pydantic schemas)

[FORMAT]
Update all 4 files:
1. src/models/todo.py
2. src/schemas/todo.py
3. src/services/todo_service.py
4. src/api/v1/todos.py
```

---

**AT 6 MINUTES:**
> "2 minutes left! If you're done, test it:
> ```bash
> pytest tests/api/test_todos.py -v
> uvicorn src.main:app --reload
> # Test in browser or curl
> ```

**AT 8 MINUTES:**
> "TIME! ✋ Fingers off keyboards!
>
> **Quick poll:**
> - Who got it working? 🙋
> - Who's close? 🙋
> - Who tried it and learned something? 🙋
>
> All three count as success! This was about LEARNING the workflow! 💪"

---

#### [0:23-0:25] Quick Demo & Debrief (2 min)

**SAY:**
> "Let me show the solution quickly..."

**DO - Show your implementation (either live-code the prompt or show pre-built):**

**SHOW the prompt you'd use:**
```
[CONTEXT]
#file:src/models/todo.py #file:src/schemas/todo.py #file:src/services/todo_service.py #file:src/api/v1/todos.py

Todo API with 3-tier architecture. Adding priority field to todos.

[TASK]
Add priority field (Integer: 1=high, 2=medium, 3=low, default=2) to all layers

[CONSTRAINTS]
- Model: Integer column, default=2, not nullable
- Schemas: TodoCreate (optional, default 2), TodoResponse (include), TodoUpdate (optional)
- Service: Add priority parameter to get_all() for filtering
- API: Add priority query param to GET endpoint
- Maintain backward compatibility

[FORMAT]
Update: src/models/todo.py, src/schemas/todo.py, src/services/todo_service.py, src/api/v1/todos.py
```

**SHOW the result working:**
```bash
# Create todo with priority
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "High priority task", "priority": 1}'

# Filter by priority
curl "http://localhost:8000/api/v1/todos?priority=1"
```

**SAY:**
> "✅ Done! What made this work?
> - Started with working infrastructure (checkpoint!)
> - Used clear context (#file mentions)
> - Specific constraints (field type, default value, filtering)
> - Professional prompt structure
>
> **Key insight:** One good prompt beats ten vague ones! 🎯"

---

### [0:25-0:28] 🧠 Reflection & Comparison (3 min)

**ENERGY:** Reflective, insightful, connecting the dots

**SAY:**
> "Let's compare the two approaches you experienced today..."

**SHOW ON SCREEN:**
```
TWO APPROACHES COMPARISON

🧪 TDD APPROACH (Instructor Demo - DELETE endpoint)
Process: Tests First → Fail → Implement → Pass
Strengths:
  ✅ Clear success criteria upfront
  ✅ Automatic verification
  ✅ Forces you to think before coding
  ✅ Great for complex/unclear features
  ✅ Professional standard

Timing: ~10 minutes for full cycle
Best for: Complex features, unclear requirements, learning new patterns

---

⚡ FULL CONTEXT APPROACH (Your Priority Field)
Process: Plan → One Comprehensive Prompt → Implement
Strengths:
  ✅ Fast when requirements are clear
  ✅ Leverages existing patterns
  ✅ One prompt gets multiple layers
  ✅ Great for straightforward features
  ✅ Builds on working infrastructure

Timing: ~8 minutes with good context
Best for: Clear requirements, extending existing patterns, speed
```

**SAY:**
> "**When to use each approach:**
>
> **Use TDD when:**
> - Requirements are complex or unclear
> - You're learning a new pattern
> - Testing is critical (security, payments, data integrity)
> - You want to establish patterns for AI to follow
>
> **Use Full Context when:**
> - Requirements are crystal clear
> - You have existing patterns to follow
> - Speed matters
> - Infrastructure is already working (like today!)
>
> **The Pro Move:** Combine them!
> - Start with TDD for the first feature (establishes patterns)
> - Switch to Full Context for similar features (follows patterns)
> - Back to TDD when adding something genuinely new
>
> Both are professional workflows. Choose based on the situation! 🎯"

**SAY:**
> "**What made today's session work?**
>
> You started with the `session-3-start` checkpoint:
> - ✅ Working database setup
> - ✅ Async fixtures configured
> - ✅ 8 passing tests proving it works
> - ✅ Complete examples to reference
>
> This let you focus on LEARNING workflows instead of debugging infrastructure.
>
> **The safety net:** Anytime you broke something, `git reset --hard session-3-start` brought you back.
>
> That's the power of checkpoint-based learning! 🛡️"

---

### [0:28-0:30] 🎉 Victory Lap & Preview Session 4 (2 min)

**ENERGY:** Celebration, high energy, proud

**SAY:**
> "Look at what you accomplished in 30 minutes! 📊"

**SHOW ON SCREEN:**
```
SESSION 3 ACHIEVEMENTS

✅ Started with working API (checkpoint verified)
✅ Watched professional TDD workflow (DELETE endpoint)
✅ Built a complete feature hands-on (priority field)
✅ Learned when to use TDD vs Full Context
✅ Experienced checkpoint safety net
✅ Used 6-element framework in practice
✅ Professional AI development skills

CAPABILITIES GAINED:
🧪 Test-Driven Development with AI
⚡ Full Context implementation
🎯 Strategic approach selection (TDD vs Full Context)
🛡️ Checkpoint-based development safety
📋 Professional prompt structure in action
```

**SAY:**
> "Who feels more confident building with AI now? 🙋
> Who sees the value of TDD? 🙋
> Who appreciated the checkpoint safety net? 🙋
>
> YOU'RE BUILDING LIKE PROFESSIONALS NOW! 🏆"

**ACHIEVEMENTS UNLOCKED:**
- 🛡️ **Checkpoint Master** - Successfully used checkpoint safety net
- 👀 **TDD Observer** - Watched complete TDD workflow
- 🏗️ **Feature Builder** - Built a complete feature with full context
- 🧠 **Strategic Thinker** - Understands when to use each approach
- 🏆 **Build Master** - Completed Session 3!

---

**PREVIEW SESSION 4:**

**SAY:**
> "Next session - the FINALE! 🎮
>
> **Session 4: Code Review, Custom Agents & Boss Fight**
>
> You'll learn:
> - Code Review with Copilot (automated quality checks)
> - Custom Agents (.agent.md files for specialized tasks)
> - Memory Bank (persistent project context)
> - The 70% Problem (AI gets you 70%, you add the critical 30%)
>
> Then: **THE BOSS FIGHT!** 💪
> - 10-minute challenge
> - Build ONE tag-related endpoint
> - Tag model already provided (another checkpoint!)
> - Apply EVERYTHING you learned
> - Earn Power User Certification!
>
> The finale awaits! See you there! 🚀"

**BREAK:** 2 minutes, then Session 4

---

## Instructor Notes

### Critical Success Factors

**1. Checkpoint Verification is NON-NEGOTIABLE**
- DO NOT proceed until all students have 8 passing tests
- If someone's checkpoint is broken, have them `git reset --hard session-3-start`
- This 3-minute investment saves 20 minutes of debugging later

**2. Students WATCH the TDD Demo**
- They should NOT code along during the DELETE demo
- This prevents 20 different implementations and keeps the class together
- They'll get hands-on practice with the priority feature

**3. The Priority Feature is Intentionally Simple**
- Goal: Apply the framework successfully, not solve a hard problem
- Success = using good context and seeing it work
- Even partial completion is learning success

### Common Issues & Solutions

**Issue:** Student's checkpoint doesn't have all 8 tests passing
**Solution:** `git reset --hard session-3-start` then `python create_db.py` and `pytest -v`

**Issue:** Student skips ahead and tries DELETE instead of priority
**Solution:** "Great initiative! But let's do priority first - it's designed for you to apply the full context formula."

**Issue:** Priority feature prompt is too vague
**Solution:** Show the 6-element framework on screen, have them identify which elements they're missing

**Issue:** Student breaks their working code during priority feature
**Solution:** Remind them of the safety net: `git reset --hard session-3-start` - that's what it's for!

**Issue:** Tests failing after implementation
**Solution:** Check the error message. Usually it's a schema validation issue or database migration needed. Guide them to read the pytest output.

**Issue:** Student wants to add tests for priority feature
**Solution:** "Great instinct! That's optional today - focus on implementation. But if you finish early, absolutely write tests!"

### Time Flexibility

**If running behind (cut to 25 min):**
- Shorten checkpoint verification to 2 min (if everyone's fast)
- Reduce TDD demo to 8 min (skip some explanation during coding)
- Give students 6 min instead of 8 min for priority feature
- Skip detailed debrief, just show solution quickly

**If ahead (expand to 33 min):**
- Have students write tests for their priority feature (TDD practice)
- Add a second feature: "favorite" boolean toggle
- Let students try the DELETE endpoint themselves
- Deeper discussion on TDD vs Full Context trade-offs

**If WAY behind (emergency 20 min version):**
- Checkpoint verification: 2 min
- TDD demo DELETE: Just SHOW the code, don't live-code it (3 min)
- Skip student hands-on, just demo priority feature (5 min)
- Quick comparison and victory lap (2 min)
- **NOTE:** This loses the hands-on practice which is valuable. Only use if critical time constraint.

### Energy Management

- **Reassuring:** Checkpoint verification (0:00-0:03)
- **Teaching/Methodical:** TDD demo (0:03-0:13)
- **Encouraging/Supportive:** Student hands-on (0:13-0:25)
- **Reflective:** Comparison and insights (0:25-0:28)
- **Celebration:** Victory lap (0:28-0:30)

### Key Teaching Points

1. **Checkpoints are safety nets** - You're never more than `git reset` away from working code
2. **TDD defines success first** - Tests are the contract AI fulfills
3. **Full context works when requirements are clear** - One good prompt beats ten vague ones
4. **Both approaches are professional** - Choose based on situation, not dogma
5. **Starting with working code** - Lets you focus on learning workflows, not debugging setup

### What Changed From Original Session 3

**OLD Session 3 Problems:**
- Zero time buffer (28 min content in 30 min session)
- Built from empty scaffolding (too many failure points)
- 3 features in 28 minutes (too ambitious)
- Students who failed fell behind for Session 4

**NEW Session 3 Solutions:**
- ✅ Checkpoint verification builds in buffer time
- ✅ Start with working code (session-3-start branch)
- ✅ One demo + one hands-on feature (focused learning)
- ✅ Safety net ensures everyone can succeed
- ✅ Students learn workflows, not debug async SQLAlchemy

**Result:** More students succeed, learn professional patterns, and arrive at Session 4 ready for the Boss Fight.

---

**End of Instructor Guide: Micro Session 3** 🎓
