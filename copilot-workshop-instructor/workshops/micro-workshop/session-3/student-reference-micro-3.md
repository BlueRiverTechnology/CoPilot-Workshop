# Student Reference: Micro Session 3
## Build Sprint - TDD Edition - Technical Deep Dive

**📖 Source References:**
- GitHub Copilot Documentation
- Test-Driven Development Best Practices
- Checkpoint-Based Learning Methodology

---

## 1. Checkpoint-Based Development

### What Are Checkpoints?

**Definition:**
Checkpoints are pre-built, verified states of a codebase that provide:
- Working infrastructure (database, tests, fixtures)
- Complete examples to reference
- Safety net for experimentation
- Fast recovery from errors

**In Session 3:**
The `session-3-start` branch contains a fully working Todo API with 8 passing tests.

### Why Checkpoints Matter

**Traditional approach problems:**
```
Empty scaffolding
  ↓
Student implements feature
  ↓
Database setup fails
  ↓
5 minutes debugging
  ↓
Async fixture configuration fails
  ↓
Another 5 minutes debugging
  ↓
Student falls behind, misses learning
```

**Checkpoint approach:**
```
Working code (checkpoint)
  ↓
Student verifies it works (30 seconds)
  ↓
Student learns by watching demo
  ↓
Student builds ONE feature
  ↓
If breaks: git reset --hard (5 seconds)
  ↓
Focus on learning workflows, not debugging setup
```

### The Safety Net

**Command to remember:**
```bash
git reset --hard session-3-start
```

**What this does:**
- Discards ALL changes since checkpoint
- Returns to verified working state
- Takes 5 seconds
- No permanent damage possible

**When to use:**
- Tests won't pass
- Database schema broken
- Import errors everywhere
- Completely stuck
- Want to start over

**The mindset:**
You can't break anything permanently. Experiment freely!

---

## 2. Test-Driven Development (TDD) with AI

### The TDD Cycle

```
1. Write Test (Red)
   ↓
2. Run Test → Fails (RED)
   ↓
3. Implement Code (Green)
   ↓
4. Run Test → Passes (GREEN)
   ↓
5. Refactor (optional)
   ↓
Repeat for next feature
```

### Why TDD Works with AI

**Without TDD:**
```
You: "Create a todo endpoint"
AI: "What should it do? What validation? What errors?"
You: "Oh, it should..." [back and forth]
Result: Multiple iterations, ambiguity
Time: 15+ minutes, many revisions
```

**With TDD:**
```
You: "Here are the test cases #file:tests/test_todos.py"
AI: [Sees exactly what success looks like]
AI: [Implements to pass tests]
Result: Clear target, fewer iterations
Time: 5-8 minutes, usually first try
```

**Key insight:** Tests ARE the specification. They remove ambiguity.

---

### TDD Phase 1: Write Tests First

**Professional test structure:**

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_delete_todo(client: AsyncClient, default_user: User):
    """Test successful todo deletion."""
    # Arrange: Create a todo
    create_response = await client.post(
        "/api/v1/todos",
        json={"title": "Test Todo", "completed": False}
    )
    assert create_response.status_code == 201
    todo_id = create_response.json()["id"]

    # Act: Delete it
    delete_response = await client.delete(f"/api/v1/todos/{todo_id}")

    # Assert: Verify deletion
    assert delete_response.status_code == 204

    # Verify it's gone
    get_response = await client.get(f"/api/v1/todos/{todo_id}")
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_delete_todo_not_found(client: AsyncClient):
    """Test deleting non-existent todo returns 404."""
    # Try to delete non-existent todo
    response = await client.delete("/api/v1/todos/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
```

**What makes these tests good:**
- Clear test names (explain what they test)
- Arrange-Act-Assert pattern
- Cover happy path + edge cases
- Include expected status codes
- Test both success and failure scenarios
- Independent (don't depend on each other)

**Prompt for creating tests:**
```
[CONTEXT]
#file:tests/api/test_todos.py shows existing test patterns
#file:src/models/todo.py defines the Todo model

[TASK]
Add tests for DELETE /api/v1/todos/{todo_id} endpoint

[CONSTRAINTS]
- Test successful deletion (204)
- Test not found (404)
- Use existing test patterns
- DON'T implement endpoint yet

[FORMAT]
Add test functions to tests/api/test_todos.py
```

---

### TDD Phase 2: Run Tests and See Red

**Command:**
```bash
pytest tests/api/test_todos.py::test_delete_todo -v
```

**Expected output:**
```
FAILED tests/api/test_todos.py::test_delete_todo - 404 Not Found
```

**Why this is GOOD:**
- Proves tests are actually testing something
- Confirms endpoint doesn't exist yet
- When tests pass after implementation, we KNOW it works
- This is the RED in Red-Green-Refactor

**If tests PASS at this stage:**
Something is wrong! Either:
- Endpoint already exists
- Test isn't testing what you think
- Need to review test logic

---

### TDD Phase 3: Implement to Make Tests Pass

**Prompt structure for TDD implementation:**

```
[CONTEXT]
#file:tests/api/test_todos.py defines success criteria (test_delete_todo, test_delete_todo_not_found)
#file:src/api/v1/todos.py has existing endpoints showing patterns
#file:src/services/todo_service.py has TodoService class
#file:src/models/todo.py defines the Todo model

Following 3-tier architecture: API → Service → Models

[TASK]
Implement DELETE /api/v1/todos/{todo_id} endpoint to make tests pass

[CONSTRAINTS]
Service layer:
- Add delete_todo() method to TodoService
- Check ownership before deletion
- Return None if not found/not owned
- Return True if successfully deleted

API layer:
- DELETE "/{todo_id}" endpoint
- Return 404 if None
- Return 204 if successful
- Use async/await patterns

Must satisfy test cases:
- test_delete_todo: Returns 204 when deleting owned todo
- test_delete_todo_not_found: Returns 404 when todo doesn't exist

[FORMAT]
Update:
1. src/services/todo_service.py - add delete_todo method
2. src/api/v1/todos.py - add DELETE endpoint
```

**Why this works:**
- AI sees exact requirements in tests
- No ambiguity about success criteria
- Error cases are explicit
- Can verify with test run
- Faster than explaining requirements in prose

---

### TDD Phase 4: Run Tests and See Green

**Command:**
```bash
pytest tests/api/test_todos.py -v
```

**Expected output:**
```
✅ test_create_todo
✅ test_create_todo_minimal
✅ test_get_todos_empty
✅ test_get_todos
✅ test_update_todo
✅ test_update_todo_partial
✅ test_update_todo_not_found
✅ test_create_todo_validation
✅ test_delete_todo          ← NEW
✅ test_delete_todo_not_found ← NEW

10 passed in 0.87s
```

**What this means:**
- Implementation satisfies all requirements
- New tests pass (feature works)
- Old tests still pass (didn't break anything)
- Ready to ship!

---

## 3. Full Context Approach (Alternative to TDD)

### What Is Full Context?

**Definition:**
A development approach where you provide comprehensive context in ONE prompt to implement a feature completely.

**When to use:**
- Requirements are crystal clear
- Existing patterns to follow
- Speed matters more than test-first approach
- Infrastructure already working

**The Session 3 example:**
Adding priority field to todos - simple, clear requirements, existing patterns.

---

### Full Context Prompt Structure

**For Session 3 priority feature:**

```
[CONTEXT]
#file:src/models/todo.py defines the Todo model
#file:src/schemas/todo.py has TodoCreate, TodoResponse, TodoUpdate schemas
#file:src/services/todo_service.py has TodoService with get_all method
#file:src/api/v1/todos.py has all endpoints

Working on todo API with 3-tier architecture

[TASK]
Add 'priority' field to todos with values 1 (high), 2 (medium), 3 (low)

[CONSTRAINTS]
Model layer: Integer column, default=2, not nullable
Schema layer: TodoCreate (optional, default 2), TodoResponse (include), TodoUpdate (optional)
Service layer: Add priority parameter to get_all() for filtering
API layer: Add priority query param to GET endpoint

[FORMAT]
Update: src/models/todo.py, src/schemas/todo.py, src/services/todo_service.py, src/api/v1/todos.py
```

**Why this works:**
- All layers covered in one prompt
- Clear specifications for each layer
- AI can see existing patterns via #file
- Faster than TDD for simple features

---

## 4. TDD vs Full Context: When to Use What

### Comparison Table

| Aspect | TDD Approach | Full Context Approach |
|--------|--------------|----------------------|
| **Speed** | Slower initially (write tests first) | Faster for simple features |
| **Clarity** | Tests define exact requirements | Requirements in constraints |
| **Verification** | Automatic (run tests) | Manual testing needed |
| **Learning curve** | Steeper (need to write tests) | Easier (familiar if following patterns) |
| **Best for** | Complex features, critical code | Simple features, clear requirements |
| **Edge cases** | Forces you to think about them | Easy to miss |
| **Regression protection** | Built-in | Need to add tests later |
| **Time investment** | More upfront, saves later | Less upfront, risk later |

---

### Decision Framework

**Use TDD when:**
- ✅ Requirements are complex or unclear
- ✅ Feature is critical (payments, auth, data integrity)
- ✅ Learning a new domain or pattern
- ✅ Establishing patterns for team/AI to follow
- ✅ Feature will be modified frequently
- ✅ Edge cases are important

**Use Full Context when:**
- ✅ Requirements are crystal clear
- ✅ Strong existing patterns to follow
- ✅ Speed is priority (prototyping, demos)
- ✅ Feature is straightforward CRUD
- ✅ Infrastructure already working
- ✅ Low risk of breaking things

**The Hybrid Approach (BEST):**
```
1. Use Full Context for initial implementation
   → Fast, gets 90% there

2. Add tests afterward for verification
   → Catches edge cases, adds confidence

3. Use TDD for future changes
   → Tests exist, can use TDD cycle

Result: Speed of Full Context + Confidence of TDD
```

---

## 5. Professional Development Workflows

### Workflow 1: Checkpoint-Based Feature Development

**Process:**
1. Checkout checkpoint branch
2. Verify it works (run tests)
3. Watch demo or learn pattern
4. Implement ONE feature
5. Test thoroughly
6. If breaks: reset to checkpoint
7. If works: commit and continue

**Benefits:**
- Never more than 5 seconds from working code
- Focus on learning, not debugging setup
- Safe experimentation environment
- Professional safety net habit

---

### Workflow 2: TDD with AI Pair Programming

**Process:**
1. Discuss requirements with AI
2. AI generates tests based on requirements
3. Run tests (should fail - RED)
4. AI implements feature
5. Run tests (should pass - GREEN)
6. Review code, refactor if needed
7. Commit

**Benefits:**
- Clear success criteria
- Less iteration
- Automatic verification
- Professional standard

---

### Workflow 3: Full Context Feature Sprint

**Process:**
1. Gather all context (#file mentions)
2. Write comprehensive prompt (Context + Task + Constraints + Format)
3. AI implements across all layers
4. Test manually
5. Fix any issues
6. Add tests for confidence
7. Commit

**Benefits:**
- Fast implementation
- Good for clear requirements
- Leverages existing patterns
- Efficient for simple features

---

## 6. Git Safety Net Commands

### Essential Commands

**Reset to checkpoint (SAFE):**
```bash
git reset --hard session-3-start
```
Discards ALL changes, returns to checkpoint. Non-destructive if you haven't committed.

**Check what's changed:**
```bash
git status
git diff
```
See what you've modified before resetting.

**Save work before resetting (if you want to keep it):**
```bash
git stash
# Later, if you want it back:
git stash pop
```

**See checkpoint history:**
```bash
git log --oneline
```

**Compare current state to checkpoint:**
```bash
git diff session-3-start
```

### Best Practices

**Before making changes:**
```bash
# Verify you're on the right branch
git branch

# Verify tests pass
pytest -v

# Now you have a known good state
```

**After implementation:**
```bash
# Run tests
pytest -v

# If pass: Commit
git add .
git commit -m "Add priority field to todos"

# If fail: Debug or reset
git reset --hard session-3-start
```

**Safety habit:**
- Commit working code frequently
- Test before committing
- Reset fearlessly if stuck
- Checkpoints are your friend

---

## 7. The 6-Element Framework in Practice

### Framework Recap (from Session 2)

```
[PERSONA] ← Optional: Who should AI be?
[CONTEXT] ← ALWAYS: What's the situation?
[TASK] ← ALWAYS: What needs to be done?
[CONSTRAINTS] ← When needed: What are the rules?
[FORMAT] ← When needed: What's the expected output?
[EXAMPLES] ← Optional: Show patterns to follow
```

### Session 3 Usage Patterns

**For TDD tests (3-4 elements):**
```
[CONTEXT] #file mentions to existing tests
[TASK] Create tests for DELETE endpoint
[CONSTRAINTS] Test cases to include
[FORMAT] Where to add tests
```
Skip: Persona (not needed), Examples (have patterns)

**For TDD implementation (4-5 elements):**
```
[CONTEXT] #file mentions to tests + existing code
[TASK] Implement to make tests pass
[CONSTRAINTS] Service + API requirements
[FORMAT] Which files to update
```
Skip: Persona (straightforward), Examples (have patterns)

**For Full Context feature (4 elements):**
```
[CONTEXT] #file mentions to all relevant files
[TASK] Add priority field
[CONSTRAINTS] Requirements for each layer
[FORMAT] Files to update
```
Skip: Persona, Examples (clear from context)

**Key insight:**
Use 3-5 elements for Session 3 features. They're medium complexity - not simple enough for 2, not complex enough for 6.

---

## 8. Common Pitfalls and Solutions

### Pitfall 1: Forgetting to Recreate Database

**Problem:**
Added field to model, but tests fail with "column doesn't exist".

**Solution:**
```bash
# Remove old database
rm todos.db

# Recreate with new schema
python create_db.py

# Run tests again
pytest -v
```

**Prevention:**
Recreate database whenever you modify models.

---

### Pitfall 2: Tests Pass But Feature Doesn't Work

**Problem:**
Tests say everything is fine, but manual testing shows bugs.

**Solution:**
Tests might not cover all cases. Add more test cases:
```python
@pytest.mark.asyncio
async def test_priority_defaults_to_medium(client: AsyncClient):
    """Test that priority defaults to 2 when not specified."""
    response = await client.post(
        "/api/v1/todos",
        json={"title": "Test Todo"}  # No priority specified
    )

    assert response.status_code == 201
    assert response.json()["priority"] == 2  # Should default
```

**Prevention:**
Think about edge cases when writing tests.

---

### Pitfall 3: Breaking Existing Tests

**Problem:**
Added new feature, now old tests fail.

**Solution:**
Check what changed:
```bash
git diff

# See which tests fail
pytest -v

# Common issue: Schema changes
# Make sure old fields still work
```

**Prevention:**
- Run ALL tests after changes
- Keep backward compatibility
- Use optional fields when adding new ones

---

### Pitfall 4: Vague Prompts Lead to Many Iterations

**Problem:**
"Add priority to todos" → AI asks many questions

**Solution:**
Be specific in constraints:
```
BAD:  "Add priority field"
GOOD: "Add priority: Integer column, values 1-3, default 2, not nullable"
```

**Prevention:**
Use the 6-element framework. Specific constraints = fewer iterations.

---

## 9. Advanced Techniques

### Technique 1: Incremental Testing

**Instead of:**
Build entire feature → test everything at once → debug mess

**Do this:**
```bash
# Add model field
pytest -v  # See what breaks

# Add schema field
pytest -v  # See what breaks

# Add service method
pytest -v  # See what breaks

# Add API endpoint
pytest -v  # Final verification
```

**Benefit:** Catch issues early, know exactly what broke.

---

### Technique 2: Reference-Driven Development

**Pattern:**
Always reference existing code when building similar features.

```
[CONTEXT]
#file:src/api/v1/todos.py shows completed field filtering
#file:src/services/todo_service.py shows how completed filter works

[TASK]
Add priority filtering following the same pattern as completed filtering
```

**Benefit:** Consistent code style, fewer explanations needed.

---

### Technique 3: Constraint Stacking

**Pattern:**
Layer constraints from general to specific.

```
[CONSTRAINTS]
Architecture: Follow 3-tier pattern (API → Service → Model)
Data type: Integer field, values 1-3
Default: 2 (medium priority)
Validation: Reject values outside 1-3
API: Accept as query param for filtering
Schema: Optional in create, required in response
```

**Benefit:** Nothing left ambiguous, AI has complete picture.

---

## 10. Session 3 Learning Outcomes

### What You Learned

**Technical Skills:**
- ✅ Test-Driven Development workflow
- ✅ Full Context feature implementation
- ✅ Checkpoint-based development
- ✅ Git safety net commands
- ✅ Professional testing patterns

**Prompt Engineering:**
- ✅ When to use which elements of 6-element framework
- ✅ How to reference tests for TDD
- ✅ How to structure constraints for clarity
- ✅ Balance between detail and brevity

**Strategic Thinking:**
- ✅ When to use TDD vs Full Context
- ✅ How to choose approach based on requirements
- ✅ Risk management (checkpoints as safety nets)
- ✅ Incremental vs comprehensive approaches

**Professional Habits:**
- ✅ Test before committing
- ✅ Reset fearlessly when stuck
- ✅ Reference existing patterns
- ✅ Layer changes incrementally

---

### Applying to Real Projects

**Scenario 1: New feature in existing codebase**
```
Use: Full Context approach
Why: Existing patterns to follow, clear requirements
Safety: Create feature branch, can always revert
```

**Scenario 2: Critical security feature**
```
Use: TDD approach
Why: Must get it right, edge cases matter
Safety: Tests prove correctness
```

**Scenario 3: Exploratory prototype**
```
Use: Full Context for speed
Add: Tests afterward for features you keep
Why: Speed matters, can iterate quickly
```

**Scenario 4: Team onboarding**
```
Use: Checkpoint approach
Why: Team learns patterns without breaking things
Safety: Everyone can reset to known good state
```

---

## 11. Quick Reference

### Checkpoint Commands
```bash
git checkout session-3-start    # Get checkpoint
git reset --hard session-3-start # Reset to checkpoint
python create_db.py              # Recreate database
pytest -v                        # Verify tests
```

### TDD Cycle
```
1. Write tests → 2. See RED → 3. Implement → 4. See GREEN → 5. Refactor
```

### Full Context Elements
```
CONTEXT (always) + TASK (always) + CONSTRAINTS (usually) + FORMAT (usually)
```

### Decision Guide
```
Complex/Critical → TDD
Simple/Clear → Full Context
Unsure → Start with tests (safer)
```

---

## 12. Self-Assessment Quiz

**1. What is a checkpoint in development?**
Answer: Pre-built, verified state of a codebase that provides working infrastructure and safety net for experimentation.

**2. What's the command to reset to the Session 3 checkpoint?**
Answer: `git reset --hard session-3-start`

**3. What are the 4 steps of TDD?**
Answer: 1) Write tests first, 2) Run and see RED, 3) Implement code, 4) Run and see GREEN

**4. When should you use TDD vs Full Context?**
Answer: TDD for complex/critical features; Full Context for clear/simple requirements

**5. Why do tests written before implementation help AI?**
Answer: Tests define exact success criteria, removing ambiguity about what to build

**6. What's the hybrid approach?**
Answer: Use Full Context for speed, add tests afterward for confidence, use TDD for future changes

**7. When should you recreate the database?**
Answer: Whenever you modify model schema (add/change fields)

**8. What's the benefit of checkpoints?**
Answer: Focus on learning workflows instead of debugging setup; fast recovery from errors

---

## 13. Next Steps: Session 4 Preview

**What's coming:**
- Code Review with Copilot (automated quality checks)
- Custom Agents (.agent.md files)
- Memory Bank (persistent context)
- The 70% Problem (AI gets you 70%, you add critical 30%)
- **BOSS FIGHT:** Tag-related endpoint in 10 minutes

**How Session 3 prepares you:**
- TDD skills → Apply in Boss Fight
- Full Context → Fast implementation under pressure
- Checkpoints → session-4-start has Tag model ready
- 6-element framework → Professional prompts in Boss Fight

**You're ready!** 💪

---

**End of Student Reference: Micro Session 3** 🎓
