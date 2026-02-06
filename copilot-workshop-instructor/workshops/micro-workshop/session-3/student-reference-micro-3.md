# Student Reference: Micro Session 3
## Build Sprint - Context Edition - Technical Deep Dive

**📖 Source References:**
- GitHub Copilot Documentation
- Best Practices for AI-Assisted Development

---

## 1. Test-Driven Development (TDD) with AI

### The TDD Cycle

```
1. Write Test (Red)
   ↓
2. Run Test → Fails
   ↓
3. Implement Code (Green)
   ↓
4. Run Test → Passes
   ↓
5. Refactor (optional)
```

### Why TDD Works with AI

**Without TDD:**
```
You: "Create a todo endpoint"
AI: "What should it do? What validation? What errors?"
You: "Oh, it should..." [back and forth]
Result: Multiple iterations, ambiguity
```

**With TDD:**
```
You: "Here are the test cases #file:tests/test_todos.py"
AI: [Sees exactly what success looks like]
AI: [Implements to pass tests]
Result: Clear target, fewer iterations
```

**Key insight:** Tests ARE the specification. They remove ambiguity.

---

### TDD Phase 1: Write Tests First

**Professional test structure:**

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_todo_success(
    client: AsyncClient
):
    """Test successful todo creation."""
    response = await client.post(
        "/api/v1/todos",
        json={
            "title": "Test Todo",
            "description": "Test Description"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Test Description"
    assert "id" in data
    assert "created_at" in data
    assert data["completed"] == False

@pytest.mark.asyncio
async def test_create_todo_empty_title(
    client: AsyncClient
):
    """Test validation error for empty title."""
    response = await client.post(
        "/api/v1/todos",
        json={"title": "   ", "description": "Test"}
    )
    
    assert response.status_code == 400
    assert "title" in response.json()["detail"].lower()
```

**What makes these tests good:**
- Clear test names (explain what they test)
- One assertion per concept
- Cover happy path + edge cases
- Include expected status codes
- Test both success and failure scenarios

---

### TDD Phase 2: Implement to Pass Tests

**Prompt structure for TDD implementation:**

```
[Context]
#file:tests/api/test_todos.py shows the tests I need to pass.
#file:src/models/todo.py has the Todo model.
Following 3-tier architecture from #folder:src/

[Task]
Implement POST /api/v1/todos endpoint to make ALL tests pass

[Constraints]
- Create TodoCreate and TodoResponse schemas (src/schemas/todo.py)
- Create TodoService.create method (src/services/todo_service.py)
- Create POST endpoint (src/api/v1/todos.py)
- Must pass ALL test cases:
  * Success: 201 with created todo
  * Empty title: 400 validation error
- Use async/await from #file:.github/copilot-instructions.md

[Format]
Create/update these files:
1. src/schemas/todo.py
2. src/services/todo_service.py
3. src/api/v1/todos.py
4. src/main.py (register router)
```

**Why this works:**
- AI sees exact requirements in tests
- No ambiguity about success criteria
- Error cases are explicit
- Can verify with test run

---

## 2. The 6-Element Professional Framework in Action

### Framework Recap (from Session 2)

**Remember: It's a TOOLBOX, not a checklist!**

```
1. [PERSONA] ← Optional: Complex domain expertise
2. [CONTEXT] ← ALWAYS: What exists, what to reference
3. [TASK] ← ALWAYS: One clear objective
4. [CONSTRAINTS] ← When needed: Specific requirements
5. [FORMAT] ← When needed: Expected output structure
6. [EXAMPLES] ← Optional: Project-specific patterns
```

**For Session 3 Features (Medium Complexity):**
We're using 4 elements: Context + Task + Constraints + Format

**Why skip Persona and Examples?**
- These are standard CRUD features (no specialized domain knowledge needed)
- Following well-established patterns (no custom examples required)
- Medium complexity = 4 elements is right amount!

### Real-World Example: GET Endpoint

**Weak prompt (beginner):**
```
"create endpoint to get todos"
```

**Strong prompt (professional):**
```
[Context]
Working on todo API. #folder:src/api/v1/ shows existing endpoint patterns.
#file:src/models/todo.py has Todo model.
#file:src/schemas/todo.py has TodoResponse schema (from Feature 1).
#file:src/services/todo_service.py has TodoService class.
Following 3-tier architecture.

[Task]
Add GET /api/v1/todos endpoint to list all todos

[Constraints]
Must support:
1. Pagination: skip (int, default 0), limit (int, default 100) query params
2. Filtering: completed (Optional[bool]) query param
3. Return List[TodoResponse]
4. Status code: 200 OK

Implementation:
- Add get_all() method to TodoService
  * Takes: skip (int), limit (int), completed (Optional[bool])
  * Use SQLAlchemy async query with .offset(), .limit()
  * If completed param provided, filter by completed status
  * Return List[Todo]
- Add GET "/" endpoint to todos router
  * Query params: skip, limit, completed (all optional)
  * Use get_db dependency
  * Call service.get_all()
  * Return List[TodoResponse]
- Follow async patterns from #file:.github/copilot-instructions.md
- Include try/except error handling

[Format]
Update these files:
1. src/services/todo_service.py - add get_all method to TodoService class
2. src/api/v1/todos.py - add GET "/" endpoint

Don't modify: schemas (TodoResponse already exists)
```

**Difference:**
- Weak: AI must guess everything → multiple iterations
- Strong: Zero ambiguity → first-attempt success

---

## 3. Context Quality Impact Analysis

### Measuring Context Quality

**Track these metrics:**
- Time spent per feature
- Number of iterations needed
- First-attempt success rate

**Typical results:**

**Weak context:**
```
Initial prompt: Vague
AI response: Has questions
Your followup: Answer questions
AI response: Still not quite right
Your followup: Fix specific issues
...repeat 3-5 times
Total: 15+ minutes, 5+ iterations
```

**Strong context:**
```
Initial prompt: Context+Task+Constraints+Format
AI response: Exactly what you need
Your action: Test it, works
Total: 3-5 minutes, 1 iteration
```

**The pattern:** Better context = fewer iterations = faster results

---

### Context Optimization Checklist

**Before submitting prompt, verify:**

✅ **Context section includes:**
- [ ] Relevant files with #mentions
- [ ] Existing patterns to follow (#folder)
- [ ] Architecture understanding
- [ ] Tech stack (FastAPI, async, PostgreSQL)

✅ **Task section is:**
- [ ] One clear objective
- [ ] Specific (not vague)
- [ ] Actionable

✅ **Constraints section lists:**
- [ ] All functional requirements
- [ ] Validation rules
- [ ] Error handling requirements
- [ ] Status codes
- [ ] Response formats

✅ **Format section specifies:**
- [ ] Which files to create/update
- [ ] Expected structure
- [ ] What NOT to change

**Missing any? Add it before submitting!**

---

## 4. Subagents - Parallel AI Work

### What Are Subagents?

Subagents are isolated AI agents that Copilot can spawn to handle tasks in parallel. They:
- Run independently of your main conversation
- Can work on different aspects simultaneously
- Report back when complete
- Don't interfere with your current work

### When to Use Subagents

**Perfect for:**
- Code review while you continue building
- Running tests in parallel
- Documentation generation
- Multiple independent tasks
- Verification without interrupting flow

### How Subagents Work

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

### Example: Spawning a Subagent

```
Launch a subagent to review all the code we just created in 
src/api/v1/todos.py and src/services/todo_service.py for:
- Error handling completeness
- Async/await correctness
- Potential security issues

While that runs, I'll continue with the next task.
```

### Subagent Benefits

1. **Parallel work** - AI multitasks for you
2. **Non-blocking** - Continue working while subagent runs
3. **Specialized tasks** - Subagent focuses on one thing
4. **Better verification** - Dedicated review without context switching

---

## 5. Plan Mode - Visibility Before Execution

### What is Plan Mode?

Plan Mode lets you see what Copilot will do BEFORE it does it. Use `/plan` to:
- Get a step-by-step implementation plan
- Review the approach
- Modify steps if needed
- Then execute with confidence

### When to Use Plan Mode

**Perfect for:**
- Complex multi-file changes
- Architectural decisions
- When you want to verify approach first
- Learning what Copilot will do
- Team code reviews (share the plan)

### Example: Using /plan

```
/plan Add a DELETE /api/v1/todos/{id} endpoint that removes a todo, 
returns 404 if not found, 403 if not owned by user, 204 on success. 
Create tests first using TDD approach.
```

**Plan output:**
```
Plan:
1. Create tests/api/test_delete_todo.py with test cases:
   - Test successful deletion (204)
   - Test not found (404)
   - Test not owned (403)
   
2. Add delete() method to TodoService:
   - Check todo exists
   - Check ownership
   - Delete from database
   
3. Add DELETE endpoint to todos router:
   - Path parameter: todo_id
   - Call service.delete()
   - Return appropriate status codes

4. Run tests to verify
```

### Plan Mode Benefits

1. **Visibility** - See the plan before execution
2. **Control** - Modify steps before running
3. **Learning** - Understand what Copilot will do
4. **Confidence** - Know the approach is right
5. **Communication** - Share plans with team

---

## 6. Comparing Approaches: TDD vs Full Context

### When to Use TDD

**Best for:**
- Complex features with many edge cases
- Features where requirements are unclear
- Critical features that need thorough testing
- Learning new domains
- Features that will be modified frequently

**Benefits:**
- Clear success criteria
- Catches edge cases early
- Forces thinking about requirements
- Automatic regression testing
- Confidence in correctness

**Cost:**
- Slightly more time upfront (writing tests)
- More files to manage

---

### When to Use Full Context

**Best for:**
- Well-understood features
- Following established patterns
- Speed is priority
- Features with simple requirements
- Prototyping

**Benefits:**
- Faster initial implementation
- Less ceremony
- Good for straightforward cases

**Cost:**
- Less verification
- Might miss edge cases
- Need manual testing
- Less confidence

---

### Hybrid Approach (Best)

**The professional pattern:**

```
1. Use FULL CONTEXT for initial implementation
   (Fast, gets 90% there)

2. Then ADD TESTS for verification
   (Catches the edge cases, adds confidence)

3. Use TDD for future changes
   (Tests exist, can use TDD cycle)
```

**This gives you:**
- Speed of full context
- Confidence of TDD
- Best of both worlds

---

## 7. AI Code Review Checklist - Critical Verification

### Why AI-Generated Code Needs Special Review

**AI-Specific Issues:**
1. **Hallucinations** - Functions/APIs that don't exist
2. **Outdated patterns** - Deprecated libraries/methods
3. **Subtle bugs** - Logic errors that look correct
4. **Security gaps** - Missing authentication/validation
5. **Performance issues** - Inefficient algorithms

**The Problem:** AI code often "looks right" but has hidden issues.

---

### The Complete AI Code Review Checklist

**After AI generates code, ALWAYS check:**

#### 1. Reality Check ✅
- [ ] Does the code actually RUN?
- [ ] All imports valid?
- [ ] All functions/methods exist in the imported libraries?
- [ ] Library versions current?

#### 2. Hallucination Detection 🚨
- [ ] No "magic" functions that don't exist?
- [ ] Imports reference real packages?
- [ ] APIs match actual library documentation?

#### 3. Security & Quality 🔒
- [ ] Input validation present?
- [ ] Error handling comprehensive?
- [ ] No hardcoded secrets?
- [ ] SQL injection protection?

#### 4. Logic & Performance 🎯
- [ ] Edge cases handled?
- [ ] Efficient algorithm?
- [ ] No N+1 query problems?
- [ ] Resource cleanup?

#### 5. Integration & Style 📐
- [ ] Fits existing codebase patterns?
- [ ] Tests included?
- [ ] Proper type hints?

---

### Real-World Examples

**Example 1: Missing Error Handling**
```python
# ❌ AI Generated (NO ERROR HANDLING):
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)  # ⚠️ What if todo is None?
    db.commit()
    return {"message": "Deleted"}

# ✅ Correct:
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:  # ✅ Check if exists
        raise HTTPException(404, "Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
```

**Example 2: Performance Issue**
```python
# ❌ AI Generated (N+1 QUERY PROBLEM):
@router.get("/todos")
async def get_todos_with_tags(db: Session):
    todos = db.query(Todo).all()
    
    # ⚠️ This queries database for each todo!
    return [
        {
            "title": todo.title,
            "tags": db.query(Tag).filter(Tag.todo_id == todo.id).all()
        }
        for todo in todos
    ]

# ✅ Better:
@router.get("/todos")
async def get_todos_with_tags(db: Session):
    # One query with join - much faster!
    todos = db.query(Todo).options(
        joinedload(Todo.tags)
    ).all()
    
    return [
        {"title": todo.title, "tags": todo.tags}
        for todo in todos
    ]
```

---

## 8. Professional Patterns

### Pattern 1: Think Before Code

```
BAD: Jump straight to implementation
GOOD: "think about..." before coding
BETTER: "think hard about..." for complexity
```

### Pattern 2: Iterative Reference

```
DON'T: Write everything from scratch
DO: Reference existing code

"Look at patterns in #folder:src/api/v1/ for consistency.
Then create new endpoint following those patterns."
```

### Pattern 3: Explicit Constraints

```
VAGUE: "handle errors"
SPECIFIC: "Handle errors:
- ValueError → 400 with message
- NotFoundError → 404
- PermissionError → 403
- Other exceptions → 500 without details"
```

---

## 9. GitHub Copilot Modes for Session 3

| Mode | Use Case | Session 3 Application |
|------|----------|----------------------|
| **Ask** | Questions, thinking | Planning test cases |
| **Edit** | Quick fixes | Small adjustments |
| **Agent** | Multi-file building | Main development mode |
| **Plan** | Complex planning | Before big features |

---

## 10. Self-Assessment Quiz

**1. What's the TDD cycle?**
Answer: Write test → Run (fails) → Implement → Run (passes)

**2. Why does TDD work well with AI?**
Answer: Tests remove ambiguity, show exactly what success looks like

**3. What are Subagents?**
Answer: Isolated AI agents that run in parallel for tasks like code review

**4. When to use Plan Mode?**
Answer: Complex features, when you want to verify approach before execution

**5. How do you verify AI code quality?**
Answer: Review checklist, test thoroughly, check for hallucinations

**6. When to use TDD vs full context?**
Answer: TDD for complex/critical features, full context for simple/fast cases

**7. Why reference existing code with #mentions?**
Answer: Ensures consistency, AI learns your patterns

**8. What makes a constraint "specific"?**
Answer: Exact requirements (status codes, error cases, validation rules)

---

## 11. Next Session Preview

**Session 4: Advanced Tools & Boss Fight - You'll learn:**
- Advanced prompting (thinking modes, specificity patterns)
- Code Review with Copilot
- Custom Agents (.agent.md files)
- Professional patterns from industry
- **BOSS FIGHT:** Apply everything for certification

**The finale where theory, practice, and mastery come together!** 🚀

---

**End of Student Reference: Micro Session 3** 🎓
