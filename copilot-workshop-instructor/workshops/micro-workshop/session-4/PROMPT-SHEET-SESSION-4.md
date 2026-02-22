# Prompt Sheet: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Duration:** 33 minutes  
**Achievement:** 🏆 "Copilot Champion"

---

## Quick Reference

| Copilot Feature | How to Use |
|-----------------|------------|
| Code Review | Request "Copilot" as reviewer on GitHub PR |
| In-Editor Review | Ask for review in Copilot Chat |
| Custom Agents | Create `.github/agents/*.agent.md` files |
| Plan Mode | Start prompt with `/plan` |

---

## 🔍 Code Review Prompts

### In-Editor Review Request

```
Review my recent changes in #file:src/api/v1/todos.py.

Check for:
1. Security issues (auth, validation)
2. Error handling completeness
3. Performance concerns
4. Best practice violations

Be thorough and critical.
```

---

### Andrew's Code Review Pattern

Use this after any AI-generated code:

```
Review this implementation with a critical eye:

## Code Quality
- Are there any code smells?
- Is error handling complete?
- Are edge cases covered?

## Security
- Any injection vulnerabilities?
- Is authentication/authorization correct?
- Input validation complete?

## Performance
- Any N+1 query issues?
- Unnecessary database calls?
- Memory efficiency concerns?

## Maintainability
- Is the code clear and readable?
- Does it follow existing patterns?
- Is it properly documented?

List issues in priority order with specific fixes.
```

---

## 🤖 Custom Agent Template

### .github/agents/todo-api.agent.md

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

---

### Using the Custom Agent

```
Using #file:.github/agents/todo-api.agent.md context:

Add a DELETE /api/v1/todos/{id} endpoint that:
- Requires authentication
- Checks ownership
- Returns 204 on success, 404/403 on errors
```

---

## 🧠 Memory Bank Prompts

### Initialize Memory Bank

Ask Copilot to create your Memory Bank:

```
Create a memory-bank/ folder for this project with these files:
- projectbrief.md
- productContext.md
- techContext.md
- systemPatterns.md
- activeContext.md
- progress.md

Use context from #file:.github/copilot-instructions.md
and #file:PRD.md to populate them.

Each file should be concise with bullet points,
not long paragraphs.
```

### Update Memory Bank

Say this at the end of any work session:

```
update memory bank
```

Or be more specific:

```
Update memory-bank/activeContext.md and memory-bank/progress.md
to reflect what we accomplished in this session.
```

### Reference Memory Bank in Prompts

```
#file:memory-bank/activeContext.md #file:memory-bank/systemPatterns.md

Based on my current context and patterns,
implement the next feature on my list.
```

---

## ⚠️ The 70% Problem Explained

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

Your 30% is why companies hire professionals!
```

---

## 🎮 BOSS FIGHT - Complete Prompts

### Scoring

| Time | Level | Description |
|------|-------|-------------|
| ≤6 min | 🏆 PLATINUM | Top 1% - Elite |
| ≤8 min | 🥇 GOLD | Top 10% - Expert |
| ≤10 min | 🥈 SILVER | Top 25% - Skilled |
| Completed | ✅ CERTIFIED | Passed! |

**Bonus:** +1 level for each: think hard, Plan Mode, TDD, Custom Agent

---

### Requirements Recap

```
TODO TAGGING FEATURE

Endpoints:
- POST /api/v1/todos/{id}/tags - Add tag to todo
- GET /api/v1/todos?tag=name - Filter todos by tag  
- DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag

Database:
- Tag model: id, name, user_id, created_at
- todo_tags association table (many-to-many)

Constraints:
- Ownership validation required
- Case-insensitive tags (store lowercase)
- Proper error handling (404, 403, 400)
- 3-tier architecture (models, services, API)
```

---

### STEP 1: Planning Prompt (think hard)

```
#file:PRD-Tags.md #file:src/models/todo.py

think hard about implementing a many-to-many tagging system for todos.

Requirements:
- POST /api/v1/todos/{id}/tags (add tag to todo)
- GET /api/v1/todos?tag=name (filter todos by tag)
- DELETE /api/v1/todos/{id}/tags/{tag_id} (remove tag)
- Must follow existing 3-tier architecture
- Ownership validation required
- Handle 404, 403, 400 errors

Consider:
- Database schema (Tag model, join table)
- Case sensitivity for tag names
- API design (RESTful endpoints)
- Service layer methods needed

Give me the complete implementation plan.
```

---

### STEP 2: Plan Mode Implementation

```
/plan Implement the tagging feature for todos:
1. Create Tag model and todo_tags association table
2. Create TagCreate and TagResponse schemas
3. Add service methods (add_tag_to_todo, remove_tag_from_todo, get_todos_by_tag)
4. Add API endpoints (POST, DELETE, GET with filter)
5. Include ownership validation and error handling

Follow existing patterns in #folder:src/
```

---

### Alternative: Sequential Prompts

**Models:**
```
#file:src/models/todo.py #file:src/models/base.py

[Context]
Existing Todo model structure. Using SQLAlchemy async with UUID keys.

[Task]
Create Tag model and todo_tags association table for many-to-many relationship.

[Constraints]
- Tag: id (UUID), name (str, 50 chars), user_id (FK), created_at
- Unique constraint: (user_id, name)
- todo_tags: todo_id (FK), tag_id (FK), composite PK
- Add tags relationship to Todo model

[Format]
Create src/models/tag.py, update src/models/todo.py
```

**Schemas:**
```
#file:src/schemas/todo.py

[Context]
Existing Pydantic schema patterns.

[Task]
Create Pydantic schemas for Tag operations.

[Constraints]
- TagCreate: name (required, 1-50 chars)
- TagResponse: id, name, user_id, created_at
- Update TodoResponse to include tags: List[TagResponse]

[Format]
Create src/schemas/tag.py, update src/schemas/todo.py
```

**Services:**
```
#file:src/services/todo_service.py

[Context]
Existing service patterns. Using async/await with AsyncSession.

[Task]
Add tag methods to TodoService:
1. add_tag_to_todo(todo_id, tag_name, user_id, db)
2. remove_tag_from_todo(todo_id, tag_id, user_id, db)
3. get_todos_by_tag(tag_name, user_id, db)

[Constraints]
- Ownership validation: user must own the todo
- Tag auto-creation: if tag doesn't exist, create it
- Case-insensitive tag lookup (store lowercase)
- Return 404 if todo not found, 403 if not owner

[Format]
Add methods to src/services/todo_service.py
```

**API Endpoints:**
```
#file:src/api/v1/todos.py #file:.github/copilot-instructions.md

[Context]
Existing endpoint patterns. FastAPI with async, dependencies.

[Task]
Add tag endpoints to todos router.

[Constraints]
- POST /api/v1/todos/{todo_id}/tags - Add tag, return TodoResponse
- DELETE /api/v1/todos/{todo_id}/tags/{tag_id} - Remove tag, return 204
- GET /api/v1/todos - Add ?tag=name query param for filtering
- Require authentication
- Proper error handling (404, 403, 400)

[Format]
Update src/api/v1/todos.py
```

---

### STEP 3: Critical 30% Review

```
Review the tagging implementation for the critical 30%:

1. Ownership validation - Can users only tag THEIR OWN todos?
2. Case sensitivity - Are tags normalized to lowercase?
3. Error messages - Are they clear and helpful?
4. Edge cases:
   - What if todo doesn't exist?
   - What if tag already on todo (idempotent)?
   - What if removing tag that isn't on todo?
5. Security - Any SQL injection risks?

Fix any issues found.
```

---

### Testing Commands

```bash
# Start server
uvicorn src.main:app --reload

# Create todo
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Test tagging"}'

# Add tag
curl -X POST http://localhost:8000/api/v1/todos/<todo_id>/tags \
  -H "Content-Type: application/json" \
  -d '{"name": "urgent"}'

# Filter by tag
curl "http://localhost:8000/api/v1/todos?tag=urgent"

# Remove tag
curl -X DELETE http://localhost:8000/api/v1/todos/<todo_id>/tags/<tag_id>
```

---

## 🏆 Power User Certification

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
│   Level: _______________                    │
│   Date: _______________                     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Session 4 Achievements

- 🔍 **Review Master** - Used Copilot Code Review
- 🤖 **Agent Creator** - Created Custom Agent
- 🧠 **Memory Architect** - Built a Memory Bank for persistent context
- ⚠️ **70/30 Understander** - Knows where to add value
- 🎮 **Boss Fighter** - Completed final challenge
- 🏆 **COPILOT CHAMPION** - Full workshop complete!

---

**End of Prompt Sheet: Session 4** 🎓

**🎉 CONGRATULATIONS - Workshop Complete! 🎉**
