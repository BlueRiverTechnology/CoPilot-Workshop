# Session 3 Prompt Sheet: Build Sprint - Context Edition 🚀⚡

**Copy-paste materials for students**

---

## 1️⃣ Feature 1: Create Todo - TDD Approach

### Step 1: Write Tests First (Copilot Chat - Agent Mode)

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

### Step 2: Run Tests (Terminal)
```bash
pytest tests/api/test_todos.py -v
```

### Step 3: Implement to Make Tests Pass (Copilot Chat - Agent Mode)

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

---

## 2️⃣ Feature 2: List Todos - Full Context Power

### Single Comprehensive Prompt (Copilot Chat - Agent Mode)

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

### Quick Test Commands
```bash
# Create database
python create_db.py

# Start server (if not running)
uvicorn src.main:app --reload

# Test POST endpoint
curl -X POST http://localhost:8000/api/v1/todos -H "Content-Type: application/json" -d '{"title":"Test todo","description":"Test description"}'

# Test GET endpoint
curl http://localhost:8000/api/v1/todos

# Test with filtering
curl "http://localhost:8000/api/v1/todos?completed=false&limit=10"
```

---

## 3️⃣ Feature 3: Update Todo - SPEED CHALLENGE

**YOU decide the approach! Complete in 3 MINUTES!**

### Requirements:
- PUT endpoint (full update) or PATCH (partial)
- Path parameter: todo_id (UUID)
- Update title, description, completed status
- Only if user owns the todo (403 if not, 404 if doesn't exist)
- Return updated TodoResponse

### Example Prompt (if you need guidance):

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

### Alternative: More Detailed Prompt

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

---

## 4️⃣ Subagents - Parallel Verification

### Spawn a Subagent for Code Review

```
Launch a subagent to review all the code we just created in src/api/v1/todos.py and src/services/todo_service.py for:
- Error handling completeness
- Async/await correctness
- Potential security issues

While that runs, I'll continue with the next task.
```

### When to Use Subagents

**Perfect for:**
- Code review while building
- Running tests in parallel
- Documentation generation
- Multiple independent tasks
- Verification while you continue working

---

## 5️⃣ Plan Mode - Complex Implementation

### Using /plan for Visibility

```
/plan Add a DELETE /api/v1/todos/{id} endpoint that removes a todo, returns 404 if not found, 403 if not owned by user, 204 on success. Create tests first using TDD approach.
```

### When to Use Plan Mode

**Perfect for:**
- Complex multi-file changes
- Architectural decisions
- When you want to verify approach first
- Learning what Copilot will do
- Team code reviews

---

## 6️⃣ Performance Tracking Template

**Update this as you build each feature:**

```markdown
## Feature 1: POST /todos (TDD Approach)

**Phase 1: Write Tests**
- Time: ____ minutes
- Tests created: ✓
- Tests status: FAILING (expected) ✓

**Phase 2: Implement**
- Time: ____ minutes
- Iterations needed: ____
- Tests status: PASSING ✓

**Total Feature 1:**
- Total time: ____ minutes
- Approach: TDD (tests first)
- First attempt success?: ____

---

## Feature 2: GET /todos (Full Context Approach)

**My Prompt:**
[paste your prompt here]

- Time: ____ minutes
- Iterations needed: ____
- First attempt success?: ____

**Compared to Feature 1:**
- Faster?: ____
- Easier?: ____
- Better code?: ____

---

## Feature 3: PUT /todos/{id} (Speed Challenge - 3 min)

**My Approach:**
- [ ] TDD (tests first)
- [ ] Full context prompt
- [ ] Hybrid

**My Prompt:**
[paste here]

- Time: ____ minutes (goal: <3)
- Made the goal?: ____
- Iterations needed: ____

---

## My Build Sprint Results

**What Made the Biggest Difference?**
☐ Better #mentions
☐ Clear constraints in prompts
☐ More context upfront
☐ Structured requests (Context+Task+Constraints+Format)
☐ TDD approach
☐ Subagents
☐ Plan Mode
☐ Other: _____

**My Pattern Discovery**
Feature with BEST results: ____
Why it worked: _____

**Most valuable lesson:**
_____
```

---

## 7️⃣ Quick Commands Reference

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start dev server
uvicorn src.main:app --reload
```

### Testing
```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/api/test_todos.py -v

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run tests with output
pytest -v -s
```

### API Testing
```bash
# Create todo
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Todo", "description": "Test"}'

# List todos
curl http://localhost:8000/api/v1/todos 

# Update todo
curl -X PUT http://localhost:8000/api/v1/todos/{id} \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated", "completed": true}'
```

---

## 8️⃣ GitHub Copilot Modes Quick Reference

| Mode | Keyboard | Session 3 Use |
|------|----------|---------------|
| **Ask** | Open Chat | Questions, thinking |
| **Edit** | Cmd+I | Quick inline fixes |
| **Agent** | Chat dropdown | Building features (primary) |
| **Plan** | /plan | Complex implementation planning |

---

## 🏆 Session 3 Achievements

- [ ] ⚡ **TDD Practitioner** - Used Test-Driven Development
- [ ] 🎯 **Context Master** - Applied full context formula
- [ ] 🏃 **Speed Demon** - Completed 3-minute challenge
- [ ] 📊 **Results Tracker** - Tracked and analyzed performance
- [ ] 🤖 **Parallel Worker** - Used Subagents
- [ ] 📋 **Strategic Planner** - Used Plan Mode
- [ ] 🏆 **Build Master** - Complete session!

---

## 💡 Pro Tips from Session 3

1. **TDD clarifies requirements:** Tests define what success looks like
2. **Context quality matters:** More/better context = fewer iterations
3. **Structure helps:** Context+Task+Constraints+Format consistently works
4. **Subagents enable parallelism:** AI can work on multiple things at once
5. **Plan Mode gives visibility:** See the plan before execution
6. **Track your results:** Data proves what works for YOU

---

**Next Session:** Advanced Tools & Boss Fight! 🎮
