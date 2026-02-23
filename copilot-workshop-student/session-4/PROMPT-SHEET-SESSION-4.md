# Prompt Sheet: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Copy-paste materials for students**

---

## 🚦 Checkpoint Verification Commands

### Switch to Checkpoint
```bash
git checkout session-4-start
```

### Initialize Database
```bash
python create_db.py
```

### Verify Tests (Should see 10 passing)
```bash
pytest tests/api/test_todos.py -v
```

### Start Server
```bash
uvicorn src.main:app --reload
```

---

## 🔍 Code Review Prompts

### Basic In-Editor Review

```
Review my implementation in #file:src/api/v1/todos.py

Check for:
1. Security issues (auth, validation, ownership checks)
2. Error handling completeness
3. Performance concerns (N+1 queries, missing indexes)
4. Best practice violations

Be thorough and critical. Point out specific line numbers.
```

---

### Comprehensive Code Review (Andrew's Pattern)

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

### .github/agents/todo-api-expert.agent.md

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

---

### Using the Custom Agent

```
Using context from #file:.github/agents/todo-api-expert.agent.md:

Add a GET /api/v1/tags endpoint that:
- Lists all tags for the current user
- Returns List[TagResponse]
- Follows existing patterns
```

---

## 🧠 Memory Bank Setup

### Add to .github/copilot-instructions.md

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

---

### activeContext.md Template

```markdown
# Active Context

## Current Focus
Session 4 Boss Fight - implementing tag endpoint

## Recent Changes
- Session 3: Built full CRUD for todos
- Checkpoint provides Tag model pre-built
- DELETE endpoint already exists

## Active Decisions
- Tags stored in existing Tag model
- Many-to-many via todo_tags association table
- Using simplified auth (default-user)

## Next Steps
- Build POST /todos/{id}/tags endpoint
- Verify ownership validation
- Test tag functionality
```

---

### Update Memory Bank Command

At the end of any work session, simply say:

```
update memory bank
```

Or be more specific:

```
Update memory-bank/activeContext.md and memory-bank/progress.md
to reflect what we accomplished in this session.
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

### Challenge: Build POST /todos/{id}/tags Endpoint

**What's PRE-BUILT in session-4-start:**
- ✅ Tag model (id, name, created_at)
- ✅ todo_tags association table
- ✅ Relationship in Todo model
- ✅ All CRUD endpoints for todos

**What YOU BUILD:**
- POST /api/v1/todos/{todo_id}/tags
- Request: `{ "name": "urgent" }`
- Create tag if doesn't exist (case-insensitive)
- Associate with todo
- Return updated TodoResponse with tags
- Handle 404 (todo not found), 403 (not owned)

---

### Scoring

| Time | Level | Bonus |
|------|-------|-------|
| ≤3 min | 🏆 PLATINUM | +1 level per bonus |
| ≤4 min | 🥇 GOLD | +1 level per bonus |
| ≤5 min | 🥈 SILVER | +1 level per bonus |
| Completed | ✅ CERTIFIED | +1 level per bonus |

**Bonus Points (+1 level each):**
- Used 'think hard' for planning
- Used TDD approach
- Used Custom Agent
- Verified ownership validation (the 30%)

---

### STEP 1: Planning Prompt (think hard) - 30 seconds

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

---

### STEP 2: Single Comprehensive Prompt - 3 minutes

**Option A: Complete Implementation (Recommended for Speed)**

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

---

**Option B: TDD Approach (If Time Allows)**

First create test:
```
#file:tests/api/test_todos.py #file:src/models/tag.py

[Context]
Tag model exists. Need to test POST /todos/{id}/tags endpoint.

[Task]
Create test_add_tag_to_todo in tests/api/test_todos.py

[Constraints]
- Test successful tag addition
- Test 404 if todo not found
- Test 403 if not owned
- Test case-insensitive tag creation

[Format]
Add test to existing test file, follow pytest-asyncio patterns
```

Then implement to pass tests:
```
#file:tests/api/test_todos.py #file:.github/agents/todo-api-expert.agent.md

Implement POST /todos/{id}/tags endpoint to make the test pass.
Follow the 3-tier architecture pattern.
```

---

### STEP 3: Critical 30% Review - 30 seconds

```
Review the tag implementation for production readiness:

1. Ownership validation - Verified?
2. Case sensitivity - Tags normalized to lowercase?
3. Idempotency - What if tag already on todo?
4. Error messages - Clear and helpful?
5. Edge cases covered?

Fix any issues found.
```

---

### STEP 4: Quick Testing - 30 seconds

```bash
# Start server (if not running)
uvicorn src.main:app --reload

# Create a todo
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Todo"}'

# Copy the todo_id from response, then add tag
curl -X POST http://localhost:8000/api/v1/todos/<todo_id>/tags \
  -H "Content-Type: application/json" \
  -d '{"name":"urgent"}'

# Verify tags appear in todo
curl http://localhost:8000/api/v1/todos/<todo_id>

# Test case-insensitivity (should return same todo)
curl -X POST http://localhost:8000/api/v1/todos/<todo_id>/tags \
  -H "Content-Type: application/json" \
  -d '{"name":"URGENT"}'
```

---

## 📚 Quick Reference

### Copilot Modes

| Mode | How to Use | Best For |
|------|-----------|----------|
| **Ask** | Open Chat | Questions, exploration |
| **Edit** | Cmd/Ctrl+I | Inline edits |
| **Agent** | Chat dropdown | Multi-file features |
| **Plan** | /plan command | Implementation planning |

---

### Context Mentions

```
#file:path/to/file.py        - Include specific file
#folder:path/to/folder        - Include folder context
#file:.github/agents/name.agent.md - Include custom agent
#file:memory-bank/activeContext.md - Include current context
#problems                      - Include current errors
```

---

### Thinking Modes

```
think         - Basic analysis
think hard    - Complex problems (USE THIS for Boss Fight planning!)
think harder  - Very complex problems
ultrathink    - Maximum reasoning
```

---

### Workflow

```
1. Explore → Understand what exists
2. Plan → Use 'think hard' or /plan
3. Code → Use Agent Mode with context
4. Review → Use Code Review
5. Verify → Test the critical 30%
6. Ship → Deploy with confidence
```

---

## 🏆 Session 4 Achievements

- 🚦 **Checkpoint Master** - Verified session-4-start checkpoint
- 🔍 **Review Master** - Used Copilot Code Review
- 🤖 **Agent Creator** - Created Custom Agent
- 🧠 **Memory Architect** - Built Memory Bank
- ⚠️ **70/30 Understander** - Knows where to add value
- 🎮 **Boss Fighter** - Completed final challenge
- 🏆 **COPILOT CHAMPION** - Full workshop complete!

---

## Power User Certification

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

**End of Prompt Sheet: Session 4** 🎓

**🎉 CONGRATULATIONS - Workshop Complete! 🎉**
