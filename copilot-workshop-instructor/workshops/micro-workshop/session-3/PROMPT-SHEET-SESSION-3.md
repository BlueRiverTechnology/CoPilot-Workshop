# Session 3 Prompt Sheet: Build Sprint - TDD Edition 🚀🧪

**Copy-paste materials for students**

---

## 🛡️ Checkpoint Verification Commands

### Initial Setup
```bash
# Checkout session 3 start branch
git checkout session-3-start

# Create database
python create_db.py

# Run all tests to verify checkpoint works
pytest tests/api/test_todos.py -v

# Expected: 8/8 tests passing
```

### Safety Net Commands
```bash
# If something breaks, reset to checkpoint
git reset --hard session-3-start

# Then recreate database and verify
python create_db.py
pytest tests/api/test_todos.py -v
```

---

## 🧪 DELETE Endpoint Tests (Instructor Demo Reference)

**This is what the instructor demonstrated. For reference only.**

### Step 1: Write Tests First (TDD)

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

### Step 2: Run Tests (Should Fail)
```bash
pytest tests/api/test_todos.py::test_delete_todo -v
pytest tests/api/test_todos.py::test_delete_todo_not_found -v
```

### Step 3: Implement DELETE Endpoint

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

### Step 4: Verify Tests Pass
```bash
pytest tests/api/test_todos.py -v
# Expected: 10/10 tests passing (8 original + 2 new DELETE tests)
```

---

## 🎯 Priority Feature Prompt (Student Hands-On)

**YOUR turn! Use this as a template for building the priority field feature.**

### Recommended Approach: Full Context Single Prompt

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

### Alternative: Simpler Prompt (If You Prefer)

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

---

## 🆘 Emergency "Stuck Student" Prompt

**If you're completely stuck or confused, use this:**

```
[CONTEXT]
#folder:src/ shows the existing todo API structure

I'm trying to add a priority field (Integer: 1, 2, or 3) to the Todo model and update all necessary files.

[TASK]
Guide me through adding the priority field step by step

[CONSTRAINTS]
- I need to update the model, schemas, service, and API layers
- Priority should default to 2 (medium)
- GET endpoint should support filtering by priority
- Keep existing functionality working

[FORMAT]
Show me which files to update and what changes to make in each
```

---

## 📋 Testing Commands

### Test Your Priority Feature

```bash
# 1. Run existing tests to ensure nothing broke
pytest tests/api/test_todos.py -v

# 2. Start the server
uvicorn src.main:app --reload

# 3. Test creating todo with priority
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "High priority task", "priority": 1}'

# 4. Test creating todo without priority (should default to 2)
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Normal task"}'

# 5. Test filtering by priority
curl "http://localhost:8000/api/v1/todos?priority=1"

# 6. Test updating priority
# (Replace {todo_id} with actual ID from create response)
curl -X PUT http://localhost:8000/api/v1/todos/{todo_id} \
  -H "Content-Type: application/json" \
  -d '{"priority": 3}'
```

---

## 🔧 Common Issues & Solutions

### Issue 1: Tests Fail After Adding Priority

**Solution:**
Check if you need to recreate the database:
```bash
# Remove old database
rm todos.db

# Recreate with new schema
python create_db.py

# Run tests again
pytest tests/api/test_todos.py -v
```

### Issue 2: Import Errors

**Solution:**
Make sure you import Optional from typing in schemas:
```python
from typing import Optional
```

### Issue 3: Filter Not Working

**Solution:**
Check the service layer get_all() method:
```python
async def get_all(
    self,
    user_id: str,
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    priority: Optional[int] = None  # Add this parameter
):
    query = select(Todo).where(Todo.owner_id == user_id)

    if completed is not None:
        query = query.where(Todo.completed == completed)

    if priority is not None:  # Add this filter
        query = query.where(Todo.priority == priority)

    query = query.offset(skip).limit(limit)
    result = await self.db.execute(query)
    return result.scalars().all()
```

### Issue 4: Completely Broken - Need Fresh Start

**Solution:**
Use the safety net:
```bash
# Reset to checkpoint
git reset --hard session-3-start

# Recreate database
python create_db.py

# Verify it works
pytest tests/api/test_todos.py -v

# Start over with your priority feature
```

---

## 🎯 Quick Decision Guide

### Which Approach Should I Use?

**Use the DETAILED prompt if:**
- You want to be very explicit
- You're new to this type of feature
- You want to minimize iterations
- You prefer step-by-step guidance

**Use the SIMPLER prompt if:**
- You're confident with the 6-element framework
- You want to practice concise prompting
- You trust AI to infer details from context
- You want to move faster

**Use the EMERGENCY prompt if:**
- You're stuck and confused
- Previous prompts didn't work
- You need step-by-step guidance
- You want to understand the process better

---

## 🏆 Success Criteria Checklist

**Before you consider the priority feature "done", verify:**

- [ ] Can create todo with priority=1, 2, or 3
- [ ] Can create todo without priority (defaults to 2)
- [ ] Can update todo's priority
- [ ] Can filter todos by priority with GET /todos?priority=1
- [ ] All 8 original tests still pass
- [ ] No errors in terminal or pytest output
- [ ] Code follows existing patterns in codebase

---

## 📊 Performance Tracking Template

**Track your results:**

```markdown
## Priority Feature Implementation

**My approach:**
- [ ] Used detailed prompt
- [ ] Used simpler prompt
- [ ] Used emergency prompt
- [ ] Created my own prompt

**My prompt:**
[Paste your prompt here]

**Results:**
- Time taken: _____ minutes
- Iterations needed: _____
- First attempt success: [ ] Yes [ ] No
- Got stuck on: _____
- What helped: _____

**Comparison to DELETE demo:**
- DELETE (TDD): ~10 minutes, instructor demo
- Priority (Full Context): _____ minutes, my implementation
- Which felt easier: _____
- Which gave better code: _____
- Which would I use for next feature: _____
```

---

## 💡 Pro Tips

1. **Read existing code first**: Use #file mentions to show AI the patterns
2. **Be specific about layers**: Mention model, schema, service, API explicitly
3. **Reference architecture**: Remind AI about 3-tier pattern
4. **Test incrementally**: Run tests after implementation to catch issues early
5. **Use the safety net**: Don't be afraid to reset if things break
6. **One good prompt**: Better than multiple vague ones

---

## 🎮 Preview: Session 4

**Next session you'll use these skills in the BOSS FIGHT!**

Similar challenge, but with:
- Tags (many-to-many relationship)
- Time pressure (10 minutes)
- Everything you learned (TDD, Full Context, 6-element framework)
- Certification on the line!

**Practice now, dominate later!** 💪

---

**End of Prompt Sheet: Session 3** 🎓
