# Instructor Guide: Micro Session 3
## Build Sprint - Context Edition 🚀⚡

**Duration:** 30 minutes  
**Achievement:** 🏆 "Build Master"  
**Prerequisites:** Session 2 completed (context mastery learned)

---

## Session Overview

### Learning Objectives
- ✅ Build complete CRUD features using professional AI workflow
- ✅ Experience efficiency gains from good context management
- ✅ Master Test-Driven Development (TDD) with AI
- ✅ Compare: minimal context vs full context approach
- ✅ Use Subagents for parallel verification
- ✅ Track results: prove context quality matters

---

## Teaching Script

### [0:00-0:02] HOOK - The Build Challenge

**ENERGY:** Super high, competitive spirit

**SAY:**
> "Welcome to Build Sprint! This is where you PROVE context mastery works.
>
> **The Experiment:**
> Next 30 minutes, build 3 complete CRUD features.
>
> **Feature 1:** TDD approach (tests first, then code)
> **Feature 2:** Full context formula from Session 2
> **Feature 3:** Speed challenge - can you do it in 3 minutes?
>
> **YOU'LL track:**
> - Time spent
> - Iterations needed
> - First-attempt success rate
>
> Get your MY-CONTEXT-EXPERIMENT.md open. We're tracking everything live! 📊
>
> Ready to prove what good context can do? LET'S BUILD! 🚀"

**DO:** Ensure everyone has MY-CONTEXT-EXPERIMENT.md open

**CHECKPOINT:** Everyone ready with tracker?

**SETUP - Before starting:**
```bash
# First, ensure dependencies are installed (if not done in Session 1)
pip install -r requirements.txt

# Then start the development server in a separate terminal
uvicorn src.main:app --reload
```

**SAY:**
> "Make sure dependencies are installed and your dev server is running at http://localhost:8000. You'll need it for testing endpoints later!"

---

### [0:02-0:12] 🧪 Feature 1: Create Todo - TDD Approach

**ENERGY:** Methodical, professional, teaching mode

**SAY:**
> "Feature 1: We're using Test-Driven Development.
>
> **TDD workflow from best practices:**
> 1. Write tests FIRST (they'll fail)
> 2. Implement code to make tests pass
> 3. Refactor if needed
>
> This is how professionals build with AI. Let's experience it! 🧪"

---

#### [0:02-0:04] Step 1: Write Tests First (2 min)

**SAY:**
> "Step 1: Write the test BEFORE any implementation code exists.
>
> This seems backward, but it forces you to think about WHAT you want before HOW to build it."

**DO - In Copilot Chat (Agent Mode), type:**

```
#file:PRD.md #folder:src/models/

[Context]
Working on todo API following PRD requirements. Models defined in src/models/.
We need to test creating todos via API.

[Task]
Create test file tests/api/test_todos.py with tests for POST /api/v1/todos endpoint

[Constraints]
- Use pytest with async support
- Test cases to include:
  1. Successful todo creation
  2. Validation error (empty title)
  3. Validation error (title too long - max 200 chars)
- Create tests/conftest.py with AsyncClient test client
- Use fixtures from tests/conftest.py
- DON'T implement the endpoint yet - just write the tests
- Tests should FAIL initially (TDD approach)

[Format]
Create tests/api/test_todos.py with all test cases
```

**SAY while generating:**
> "Notice a few things:
> - **#file:PRD.md reference** - AI has full context about our requirements!
> - **Prompt structure** from Session 2 - Context, Task, Constraints, Format
> - **Selective #mentions** - Only what's needed (#folder:src/models/)
>
> Why not all 6 prompt elements? Because this is MEDIUM complexity:
> - Skipped Persona: Test writing is straightforward
> - Skipped Examples: Standard pytest patterns
>
> Using what we NEED, not all we HAVE! This is the scalable framework in action.
>
> And I explicitly said DON'T implement yet - tests only!"

**SAY:**
> "✅ Tests created! Now let's run them and watch them FAIL..."

---

#### [0:04-0:05] Step 2: Run Tests (Confirm Failure) (1 min)

**DO - Terminal:**
```bash
pytest tests/api/test_todos.py -v
```

**SHOW:** Tests fail (endpoint doesn't exist yet)

**SAY:**
> "✅ Perfect! All tests FAILED. That's exactly what we want in TDD!
>
> The tests define WHAT we need. Now we implement to make them pass."

---

#### [0:05-0:10] Step 3: Implement to Make Tests Pass (5 min)

**SAY:**
> "Now we implement. But notice: we give AI the TESTS as context!
>
> AI can see what success looks like. This is powerful!"

**DO - Copilot Chat (Agent Mode):**

```
#file:PRD.md #file:tests/api/test_todos.py #file:src/models/todo.py

[Context]
Tests in test_todos.py define success criteria.
Todo model exists in src/models/.
Following 3-tier architecture per PRD: API → Service → Database

[Task]
Implement POST /api/v1/todos endpoint to make all tests pass

[Prerequisites]
- Create database setup script (create_db.py) that:
  * Creates async engine from DATABASE_URL env var
  * Runs Base.metadata.create_all() to create tables
  * Can be run standalone: python create_db.py
- Ensure DATABASE_URL is set in .env file

[Constraints]
- Create 3 layers in order:
  1. Pydantic schemas (TodoCreate, TodoResponse)
  2. Service layer (TodoService.create method) - MUST persist to database
  3. API route (POST endpoint) - inject db session dependency
- TodoService.__init__ must accept AsyncSession (required, not optional)
- TodoService.create must call db.add(), db.commit(), db.refresh()
- API endpoint must use Depends(get_db) to inject database session
- Create get_db() dependency function if it doesn't exist
- Use fixed owner_id ("default-user") for all todos
- DO NOT implement authentication or get_current_user dependency
- Must handle all test cases:
  * Success case (201 response)
  * Empty title validation (422 Pydantic error)
  * Title length validation (max 200 chars, 422 if exceeded)
- Use async/await patterns from #file:.github/copilot-instructions.md

[Format]
Create all 3 files and register router in src/main.py
```

**SAY while generating:**
> "See how I gave it:
> - The tests (so it knows what to build)
> - The model (so it understands the data)
> - Architecture context (3-tier pattern)
> - Explicit constraints (all the requirements)
>
> This is professional prompting!"

**SHOW:** AI generates all 3 layers

**DO - Quick verification in terminal:**
```bash
pytest tests/api/test_todos.py -v
```

**SHOW:** Tests pass (or mostly pass - fix any remaining issues)

**SAY:**
> "🎉 Tests PASS! That's TDD in action!
>
> Write test → Watch it fail → Implement → Watch it pass
>
> **Why this works with AI:**
> - Tests give AI clear success criteria
> - Less ambiguity = better code
> - You verify correctness automatically"

---

### [0:12-0:19] ⚡ Feature 2: List Todos - Full Context Power

**SAY:**
> "Feature 1: TDD approach, 7 minutes, careful and methodical.
>
> Feature 2: Watch how fast we can go with PERFECT context from Session 2! ⚡"

---

#### [0:12-0:19] Single Comprehensive Prompt (7 min)

**SAY:**
> "This time: ONE prompt. All layers. Watch this..."

**DO - Copilot Chat Agent Mode (students type along):**

```
#file:PRD.md #folder:src/api/ #folder:src/services/

[Context]
Working on todo API following PRD requirements and patterns in src/api/ and src/services/

Existing code:
- #file:src/models/todo.py has Todo model
- #file:src/schemas/todo.py has TodoCreate and TodoResponse (from Feature 1)
- #file:src/services/todo_service.py has TodoService class (from Feature 1)
- #file:src/api/v1/todos.py has POST endpoint (from Feature 1)

[Task]
Add GET /api/v1/todos endpoint to list all todos for user

[Constraints]
Must support:
1. Pagination: skip (int, default 0) and limit (int, default 100) query params
2. Filtering: completed (Optional[bool]) query param to filter by status
3. Only return todos owned by user
4. Return List[TodoResponse]
5. Status code: 200 OK

Implementation requirements:
- Add get_all() method to TodoService class
  * Takes user_id, skip, limit, completed (optional)
  * Use SQLAlchemy async query with .offset(), .limit()
  * Filter by owner_id and optionally by completed status
  * Return list of Todo objects
- Add GET "/" endpoint to todos router
  * Query parameters: skip, limit, completed (optional)
  * Call service.get_all()
  * Return List[TodoResponse]
- Follow async patterns from #file:.github/copilot-instructions.md
- Include proper error handling (try/except with HTTPException)

[Format]
Update these files:
1. src/services/todo_service.py - add get_all method
2. src/api/v1/todos.py - add GET endpoint
Don't modify schemas (TodoResponse already exists)
```

**SAY while generating:**
> "Count the specificity:
> - ✅ Exact files to update
> - ✅ Exact method names
> - ✅ Exact query parameters
> - ✅ Exact business logic (pagination, filtering)
> - ✅ Exact response format
> - ✅ Referenced existing code with #mentions
>
> AI has ZERO ambiguity. Result? Perfect code, first try!"

**SHOW generated code** (verify it's correct)

**DO - Start the server (if not already running):**
```bash
# Create Database
python create_db.py

# In a separate terminal
uvicorn src.main:app --reload
```

**SHOW:** Server starting on `http://localhost:8000`

**SAY:**
> "Server's running! Now let's test our GET endpoint..."

**DO - Quick test:**
```bash
# In terminal or Postman
curl http://localhost:8000/api/v1/todos

curl "http://localhost:8000/api/v1/todos?completed=false&limit=10"
```

**SHOW:** Working endpoint!

**SAY:**
> "✅ DONE! How long did that take?
>
> Compare to Feature 1:
> - Feature 1 (TDD): 7 minutes, multiple steps
> - Feature 2 (Full Context): ____ minutes, ONE prompt
>
> **Key difference:** More context upfront = faster results
>
> Both approaches work. Choose based on situation:
> - Complex/unclear? Use TDD
> - Clear requirements? Use full context"

---

### [0:19-0:22] 🎯 Feature 3: Update Todo - SPEED CHALLENGE

**ENERGY:** Race mode, competitive, exciting

**SAY:**
> "Final feature: YOUR TURN! 🎮
>
> **SPEED CHALLENGE: 3 MINUTES!**
>
> Build PUT /api/v1/todos/{id} endpoint using everything you learned:
> - TDD? (optional but good practice)
> - Full context formula? (Context+Task+Constraints+Format)
> - Advanced #mentions?
>
> **Requirements:**
> - PUT endpoint (full update) or PATCH (partial)
> - Path parameter: todo_id (UUID)
> - Update title, description, completed status
> - Only if user owns the todo (403 if not, 404 if doesn't exist)
> - Return updated TodoResponse
>
> **YOU DECIDE THE APPROACH!**
>
> Pair up - help each other! Fastest pair wins! ⏱️
>
> Timer starts NOW! 3 minutes!"

**TIMER:** 3 minutes (strict)

**WALK AROUND:** Watch approaches, encourage best practices

**HINT if stuck (at 1:30):**
> "Use Context+Task+Constraints+Format! Reference existing code with #mentions!"

**EXAMPLE PROMPT if students need guidance:**
```
#file:PRD.md #folder:src/api/v1/ #file:src/services/todo_service.py #file:src/schemas/todo.py

[Context] Following PRD requirements.

[Task] Add PUT /api/v1/todos/{id} endpoint

[Constraints]
- TodoUpdate schema (all fields optional)
- Service update() method (check ownership, return None if not found/owned)
- PUT endpoint with todo_id path param
- Return 404 if not found, 200 with TodoResponse if success

[Format]
Update src/schemas/todo.py, src/services/todo_service.py, src/api/v1/todos.py
```

**AT 3:00:**
> "TIME! ✋ Who finished? 🎉 Who got it working?"

**QUICK DEMO solution if needed** (Agent Mode):
```
#file:PRD.md #file:src/api/v1/todos.py #file:src/services/todo_service.py

[Context]
Continuing todo API work following PRD requirements.
src/api/v1/todos.py has POST and GET endpoints.
src/services/todo_service.py has TodoService with create and get_all methods.

[Task]
Add PUT /api/v1/todos/{id} endpoint for updating todos

[Constraints]
1. Create TodoUpdate schema in src/schemas/todo.py:
   - All fields optional (title, description, completed)
2. Add update() method to TodoService:
   - Parameters: todo_id (UUID), data (TodoUpdate), user_id (UUID)
   - Check ownership (owner_id == user_id)
   - Return None if not found or not owned by user
   - Update only fields that are provided (exclude_unset=True)
   - Commit and refresh
3. Add PUT "/{todo_id}" endpoint:
   - Path parameter: todo_id (UUID)
   - Call service.update()
   - Return 404 if None, 200 with TodoResponse if success

[Format]
Update src/schemas/todo.py, src/services/todo_service.py, src/api/v1/todos.py
```

**SAY:**
> "✅ Feature 3 complete!
>
> **3-minute challenge results:**
> - Who made it? 🙋
> - Who was close? 🙋
> - What strategy worked? TDD? Full context? Both?
>
> You just built 3 CRUD operations in 20 minutes total! 🎯"

---

### [0:22-0:25] 🤖 Subagents - Parallel Verification (3 min)

**SAY:**
> "Now let's learn a Copilot POWER feature: Subagents!
>
> Subagents are isolated agents that can run in parallel. Perfect for verification tasks!"

**SHOW Subagent concept:**
```
MAIN AGENT (you're working with):
→ Building the feature

SUBAGENT 1 (parallel):
→ Reviewing code quality
→ Running independently
→ Reports back findings

SUBAGENT 2 (parallel):
→ Running tests
→ Checking for issues
→ Reports back results
```

**DO - Demonstrate Subagent Launch:**

**SAY:**
> "Watch me spawn a subagent for code review while we continue building.
>
> In the Copilot Chat, Copilot can automatically spawn subagents when complex tasks need parallel work. You'll see messages like 'Spawning subagent to...'
>
> You can also explicitly request parallel work:"

```
Launch a subagent to review all the code we just created in src/api/v1/todos.py and src/services/todo_service.py for:
- Error handling completeness
- Async/await correctness
- Potential security issues

While that runs, I'll continue with the next task.
```

**SAY:**
> "The subagent runs independently! While it's reviewing, you can:
> - Continue building features
> - Start another task
> - The subagent reports back when done
>
> **This is parallel AI work!** 🚀
>
> Perfect for:
> - Code review while building
> - Running tests in parallel
> - Documentation generation
> - Multiple independent tasks"

🏆 **ACHIEVEMENT:** "Parallel Worker"

---

### [0:25-0:28] Plan Mode - Complex Implementation (3 min)

**SAY:**
> "Let me show you another Copilot power feature: **Plan Mode**!
>
> For complex features, use `/plan` to see the full implementation plan BEFORE execution."

**DO - Demonstrate Plan Mode:**

```
/plan Add a DELETE /api/v1/todos/{id} endpoint that removes a todo, returns 404 if not found, 403 if not owned by user, 204 on success. Create tests first using TDD approach.
```

**SAY:**
> "See what happened? Plan mode:
> 1. Analyzed the request
> 2. Created a step-by-step plan
> 3. Shows you WHAT it will do BEFORE doing it
>
> You can:
> - Review the plan
> - Modify steps
> - Ask for changes
> - Then execute
>
> **Perfect for:**
> - Complex multi-file changes
> - Architectural decisions
> - When you want to verify approach first
> - Learning what Copilot will do"

**SHOW the plan output:**
```
Plan:
1. Create tests/api/test_delete_todo.py with test cases
2. Add delete() method to TodoService
3. Add DELETE endpoint to todos router
4. Verify all tests pass
```

**SAY:**
> "Accept the plan to execute, or modify it first!"

🏆 **ACHIEVEMENT:** "Strategic Planner"

---

### [0:28-0:30] 🎉 Victory Lap & Results Analysis

**ENERGY:** Celebration mode, high energy

**SAY:**
> "Time to analyze YOUR results... 📊"

**DO - GUIDE REFLECTION:**

```markdown
# My Build Sprint Results

## Feature 1: POST /todos (TDD Approach)
- Time: ____ min
- Iterations: ____
- Approach: Tests first, then implementation

## Feature 2: GET /todos (Full Context)
- Time: ____ min
- Iterations: ____
- Approach: One comprehensive prompt

## Feature 3: PUT /todos (Speed Challenge)
- Time: ____ min (goal: <3 min)
- Iterations: ____
- Made goal?: ____

## What Made the Biggest Difference?
☐ Better #mentions
☐ Clear constraints in prompts
☐ More context upfront
☐ Structured requests (Context+Task+Constraints+Format)
☐ TDD approach
☐ Other: _____

## My Pattern Discovery
Feature with BEST results: ____
Why it worked: _____

## What You Built Today
- 3 complete CRUD operations ✅
- Used Subagents for parallel work ✅
- Used Plan Mode for complex planning ✅
- Professional AI development skills ✅

## Most valuable lesson:
_____
```

**SAY:**
> "🎉 LOOK AT WHAT YOU DID!
>
> In 30 minutes:
> - Built 3 complete, tested features
> - Experienced TDD with AI
> - Proved context quality matters
> - Used Subagents and Plan Mode
> - Learned professional workflows
>
> **Key insights:**
> 1. Good context = faster results
> 2. TDD forces clarity
> 3. Specificity reduces iterations
> 4. Subagents enable parallel work
> 5. Plan Mode gives visibility
>
> YOU'RE BUILDING LIKE A PRO NOW! 🏆"

**GROUP CELEBRATION:**
> "Who feels faster with AI now? 🙋 
> Who sees the value of good prompts? 🙋
> Who's going to use TDD? 🙋
> Who's going to use Subagents? 🙋
>
> YOU'RE POWER USERS! 🎉"

---

## Session 3 Wrap-Up

### Achievements Unlocked

**SAY:**
> "Check your achievements..."

- ⚡ **TDD Practitioner** - Used Test-Driven Development
- 🎯 **Context Master** - Applied full context formula
- 🏃 **Speed Demon** - Completed 3-minute challenge
- 📊 **Results Tracker** - Tracked and analyzed performance
- 🤖 **Parallel Worker** - Used Subagents
- 📋 **Strategic Planner** - Used Plan Mode
- 🏆 **Build Master** - Complete session!

**CAPABILITIES GAINED:**
- ✅ Test-Driven Development with AI
- ✅ Professional prompting structure (Context+Task+Constraints+Format)
- ✅ Subagents for parallel work
- ✅ Plan Mode for complex features
- ✅ Performance comparison and analysis

**PREVIEW SESSION 4:**
> "Final session: Advanced Tools & Boss Fight! 🎮
>
> You'll learn:
> - Advanced prompting (thinking modes, specificity)
> - Code Review with Copilot
> - Custom Agents
> - Professional patterns
> 
> Then: BOSS FIGHT!
> - 5-minute challenge
> - Build complex tagging feature
> - Apply EVERYTHING you learned
> - Earn Power User Certification!
>
> The finale! See you there! 🚀"

**BREAK:** 2 minutes, then Session 4

---

## Instructor Notes

### Common Issues & Solutions

**Issue:** Students skip test-writing in TDD  
**Solution:** Emphasize: "Tests first! That's the whole point of TDD. They define success."

**Issue:** Prompts still too vague in Feature 2  
**Solution:** Show the formula on screen, have them structure before typing

**Issue:** Speed challenge too fast for some  
**Solution:** That's okay! It's aspirational. Celebrate who made it, encourage those who didn't.

**Issue:** Subagent concept confuses students  
**Solution:** Explain: "It's like delegating to a junior dev who works in parallel and reports back."

### Time Flexibility

**If running behind:**
- Shorten TDD to just show the concept (don't run full cycle)
- Skip Feature 3 student challenge (demo it quickly)
- Skip Plan Mode demo (mention it exists)

**If ahead:**
- Add DELETE endpoint as practice
- Have students try launching their own subagent
- Explore Plan Mode in more detail

### Energy Management

- **High:** Opening challenge (0:00-0:02)
- **Methodical:** TDD Feature 1 (0:02-0:12)
- **Fast:** Full context Feature 2 (0:12-0:19)
- **Exciting:** Speed challenge (0:19-0:22)
- **Mind-blown:** Subagents & Plan Mode (0:22-0:28)
- **Celebration:** Victory lap (0:28-0:30)

### Key Teaching Points

1. **TDD clarifies requirements** - Forces you to think about success criteria
2. **Context quality matters** - More/better context = fewer iterations
3. **Structure helps** - Context+Task+Constraints+Format is a formula that works
4. **Subagents enable parallel work** - AI can multitask for you
5. **Plan Mode gives visibility** - See before you execute

---

**End of Instructor Guide: Micro Session 3** 🎓
