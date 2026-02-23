# Student Reference: Micro Session 4
## Code Review, Custom Agents & Boss Fight - Technical Deep Dive 🎮🏆

**Session Duration:** 30 minutes
**Topics:** Checkpoints, Code Review, Custom Agents, Memory Bank, 70/30 Problem, Boss Fight

---

## Table of Contents

1. [Checkpoint System](#checkpoint-system)
2. [Copilot Code Review](#copilot-code-review)
3. [Custom Agents (.agent.md)](#custom-agents)
4. [Memory Bank Pattern](#memory-bank-pattern)
5. [The 70% Problem](#the-70-problem)
6. [Many-to-Many Relationships](#many-to-many-relationships)
7. [Boss Fight Strategy](#boss-fight-strategy)
8. [Complete Workshop Summary](#complete-workshop-summary)

---

## Checkpoint System

### What Are Checkpoints?

Checkpoints are pre-configured git branches with working code at specific points in the workshop. They provide "safety nets" so everyone can start a session from the same working state.

```
main                 ← Empty scaffolding
  ↓
session-3-start     ← POST, GET, PUT endpoints working
  ↓
session-4-start     ← + DELETE endpoint + Tag model
```

---

### Session 4 Checkpoint Details

**Branch:** `session-4-start`

**What's Included:**

```
COMPLETE CRUD ENDPOINTS:
✅ POST /api/v1/todos - Create todo
✅ GET /api/v1/todos - List todos (with pagination)
✅ PUT /api/v1/todos/{id} - Update todo
✅ DELETE /api/v1/todos/{id} - Delete todo

TAG INFRASTRUCTURE (PRE-BUILT):
✅ Tag model (src/models/tag.py)
   - id: UUID string
   - name: string (max 50 chars)
   - created_at: datetime

✅ todo_tags association table
   - todo_id: FK to todos
   - tag_id: FK to tags
   - Composite primary key

✅ Relationship configured
   - Todo.tags → many-to-many → Tag.todos

COMPLETE TEST SUITE:
✅ 10 passing tests covering all CRUD operations
```

---

### Why Checkpoints Matter

**Problem:** Traditional workshops fail if earlier sessions struggle.

```
WITHOUT CHECKPOINTS:
Session 1: 10% struggle
Session 2: 25% behind (compounding)
Session 3: 40% can't participate
Session 4: 60% lost

WITH CHECKPOINTS:
Session 1: 10% struggle
Session 2: 10% struggle (fresh start available)
Session 3: Everyone on session-3-start checkpoint ✓
Session 4: Everyone on session-4-start checkpoint ✓
```

**Benefit:** Everyone can complete the Boss Fight regardless of earlier struggles.

---

### Checkpoint Verification Process

```bash
# 1. Switch to checkpoint
git checkout session-4-start

# 2. Initialize database
python create_db.py

# 3. Verify tests
pytest tests/api/test_todos.py -v

# Expected: 10 passed
# - test_create_todo
# - test_create_todo_minimal
# - test_get_todos_empty
# - test_get_todos
# - test_update_todo
# - test_update_todo_partial
# - test_update_todo_not_found
# - test_create_todo_validation
# - test_delete_todo
# - test_delete_todo_not_found

# 4. Start server
uvicorn src.main:app --reload

# 5. Quick functional test
curl -X POST http://localhost:8000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Test"}'
```

---

## Copilot Code Review

### Two Review Methods

#### 1. GitHub Pull Request Review

```
WHEN TO USE:
- Formal code review process
- Team collaboration
- Pre-merge quality checks

HOW IT WORKS:
1. Create Pull Request on GitHub
2. Add "Copilot" as a reviewer
3. Copilot analyzes the diff
4. Inline comments appear on specific lines
5. Suggestions for improvements

WHAT IT CHECKS:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns
```

---

#### 2. In-Editor Review (VS Code Chat)

```
WHEN TO USE:
- Self-review before committing
- Quick sanity check
- Learning from AI feedback
- Finding edge cases

HOW IT WORKS:
Use Copilot Chat with specific review prompts
```

**Basic Review:**
```
Review #file:src/api/v1/todos.py for issues.
```

**Thorough Review:**
```
Review #file:src/api/v1/todos.py checking:
1. Security (auth, validation, injection)
2. Error handling (all paths covered?)
3. Performance (N+1 queries, efficiency)
4. Best practices (naming, patterns)

Be thorough and list issues by severity.
```

**Andrew's Comprehensive Pattern:**
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

### When to Use Each Method

| Situation | Method |
|-----------|--------|
| Before committing | In-editor review |
| Pre-PR self-check | In-editor review |
| Team code review | GitHub PR review |
| After AI generation | Andrew's pattern |
| Quick sanity check | Basic in-editor |
| Pre-deployment | Thorough review |

---

## Custom Agents

### What Are Custom Agents?

Custom Agents are `.agent.md` files that pre-load Copilot with specialized knowledge about your project.

```
PURPOSE:
Define AI personas with domain expertise

LOCATION:
.github/agents/*.agent.md

BENEFITS:
- Persistent project knowledge
- Consistent code patterns
- Reduced context repetition
- Specialized domain experts
```

---

### Agent File Structure

```markdown
# .github/agents/[name].agent.md

# [Agent Name]

[Brief description of expertise]

## Architecture Knowledge
[System architecture this agent understands]

## Key Patterns
[Coding patterns to follow]

## File Structure
[Project organization]

## Coding Standards
[Standards and conventions]

## Behavior Instructions
[How to respond to requests]
```

---

### Example: Todo API Expert Agent

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

### Using Custom Agents

**Method 1: Reference in Prompt**
```
Using #file:.github/agents/todo-api-expert.agent.md context:

Add pagination to the GET /api/v1/todos endpoint.
```

**Method 2: Start of Session**
```
I'm working with context from #file:.github/agents/todo-api-expert.agent.md.

Today I need to add a priority field to todos.
```

---

### Agent Best Practices

```
DO:
✅ Keep agents focused on specific domains
✅ Include concrete examples
✅ Update as project evolves
✅ Create multiple specialized agents

DON'T:
❌ Make agents too generic
❌ Include sensitive information
❌ Forget to update when patterns change
❌ Create one massive "knows everything" agent
```

---

### Agent Ideas for Different Projects

| Agent Type | Purpose | Example Knowledge |
|------------|---------|-------------------|
| API Expert | API patterns | REST conventions, error handling |
| Test Specialist | Testing standards | Fixture patterns, coverage goals |
| Security Reviewer | Security checks | Auth patterns, validation rules |
| DB Expert | Database optimization | Query patterns, indexing strategy |
| Frontend Lead | UI patterns | Component structure, state management |
| DevOps Helper | Infrastructure | Deployment process, CI/CD patterns |

---

## Memory Bank Pattern

### The Problem

Every new Copilot chat session starts with ZERO context:

```
Day 1: "We use FastAPI with async/await, 3-tier architecture..."
Day 2: "Remember, FastAPI async, 3-tier..."
Day 3: "I already told you twice..."
Day 4: *gives up*
```

---

### The Solution

A `memory-bank/` folder with structured markdown files that Copilot reads at the start of every conversation.

```
your-project/
├── .github/
│   └── copilot-instructions.md    ← Tell Copilot to read Memory Bank
├── memory-bank/                    ← 6 context files
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── techContext.md
│   ├── systemPatterns.md
│   ├── activeContext.md           ⚡ MOST IMPORTANT
│   └── progress.md
└── src/
```

---

### The 6 Core Files

| File | Updates | Purpose |
|------|---------|---------|
| `projectbrief.md` | Rarely | Foundation: goals, scope, success criteria |
| `productContext.md` | Rarely | Why it exists, users, UX goals |
| `techContext.md` | Occasionally | Stack, setup, technical constraints |
| `systemPatterns.md` | Occasionally | Architecture, file structure, conventions |
| `activeContext.md` | **Every session** | Current focus, recent changes, next steps |
| `progress.md` | **Every session** | Status: what works, what's left, issues |

**Architecture:**
```
Files build hierarchically:
projectbrief (foundation)
├── productContext (why)
└── techContext (what)
    └── systemPatterns (how)
        ├── activeContext (now) ← Changes daily
        └── progress (status)   ← Changes daily
```

---

### copilot-instructions.md Addition

Add this to `.github/copilot-instructions.md`:

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

### Template: activeContext.md

This is the **most frequently updated file**:

```markdown
# Active Context

## Current Focus
[What you're working on right now]

## Recent Changes
- [What changed in the last session]
- [Key decisions made]
- [Files modified]

## Active Decisions
- [Decisions affecting current work]
- [Trade-offs chosen]
- [Patterns established]

## Next Steps
- [Immediate tasks]
- [What to work on next session]

## Open Questions
- [Unresolved decisions]
- [Things to investigate]
```

**Example for Session 4:**
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
- Tags are case-insensitive (stored lowercase)

## Next Steps
- Build POST /todos/{id}/tags endpoint
- Verify ownership validation
- Test tag functionality
- Complete Boss Fight

## Open Questions
- Should tags be unique per user or globally?
- How to handle tag deletion when todos still reference it?
```

---

### Template: progress.md

```markdown
# Progress

## What Works
- [x] [Completed feature 1]
- [x] [Completed feature 2]

## What's Left
- [ ] [Remaining feature 1]
- [ ] [Remaining feature 2]

## Known Issues
- [Bug or limitation 1]
- [Bug or limitation 2]

## Recently Completed
- [Date]: [What was finished]
```

---

### The Daily Workflow

```
MORNING:
1. Start Copilot Chat
2. Copilot automatically reads memory-bank/
3. Full context restored → Zero re-explaining

DURING WORK:
- Better suggestions (Copilot knows your patterns)
- Reference #file:memory-bank/activeContext.md for current focus
- Less iteration needed

END OF DAY:
- Say: "update memory bank"
- Copilot updates activeContext.md and progress.md
- Context preserved for tomorrow

NEXT DAY:
- Zero context lost
- Pick up exactly where you left off
```

---

### Memory Bank vs. Other Tools

| Tool | Scope | Persistence | Best For |
|------|-------|-------------|----------|
| `.copilot-instructions.md` | Rules & standards | Always loaded | HOW you work |
| Custom Agents (`.agent.md`) | Specialized roles | Referenced manually | Domain expertise |
| Memory Bank (`memory-bank/`) | Project state | Always loaded | WHERE you are |
| PRD files | Feature specs | Referenced manually | WHAT to build |

**They work together:**
```
copilot-instructions.md → Sets the rules
Memory Bank → Provides current state
Custom Agents → Add domain expertise
PRD → Defines features to build
```

---

### Best Practices

```
DO:
✅ Update activeContext.md at end of every session
✅ Keep files concise - bullet points, not essays
✅ Commit memory-bank changes with your code
✅ Use "update memory bank" command regularly
✅ Let Copilot suggest updates during conversation

DON'T:
❌ Put sensitive data in memory bank files
❌ Write long paragraphs - Copilot needs scannable content
❌ Forget to update after major decisions
❌ Skip the copilot-instructions.md integration
```

---

## The 70% Problem

### Understanding the Split

Research shows AI-assisted development follows a predictable pattern:

```
THE 70/30 SPLIT

╔═══════════════════════════════════════════╗
║                                           ║
║   AI DELIVERS FAST (70%)                  ║
║   ────────────────────────                ║
║   • Boilerplate code                      ║
║   • Standard CRUD operations              ║
║   • Happy path implementation             ║
║   • Common patterns                       ║
║   • Basic structure                       ║
║   • Repetitive tasks                      ║
║                                           ║
╠═══════════════════════════════════════════╣
║                                           ║
║   YOU MUST ADD (30%)                      ║
║   ────────────────────                    ║
║   • Edge cases AI missed                  ║
║   • Ownership validation                  ║
║   • Security hardening                    ║
║   • Error message quality                 ║
║   • Production error handling             ║
║   • Business logic nuances                ║
║   • Performance optimization              ║
║   • Domain-specific rules                 ║
║                                           ║
╚═══════════════════════════════════════════╝
```

---

### The Business Impact

**Organizations that understand the 70/30:**
- 26% measured productivity gains
- Faster delivery with maintained quality
- Sustainable AI-augmented workflows
- Developer satisfaction increases

**Organizations that don't:**
- Accumulating technical debt
- "AI-generated" bugs in production
- Security vulnerabilities
- Decreased trust in AI tools
- Wasted AI investment

---

### The Critical 30% Checklist

Use after EVERY AI-generated code:

```
SECURITY
[ ] Authentication required on protected endpoints?
[ ] Authorization checks (ownership, roles)?
[ ] Input validation complete?
[ ] SQL injection protected?
[ ] Secrets properly handled?

ERROR HANDLING
[ ] All error paths return appropriate status codes?
[ ] Error messages helpful but not leaky?
[ ] Edge cases handled (empty, null, duplicate)?
[ ] Validation errors specific?

BUSINESS LOGIC
[ ] Business rules correctly implemented?
[ ] Domain-specific edge cases covered?
[ ] Matches requirements exactly?
[ ] Integration with existing features correct?

QUALITY
[ ] Code follows project patterns?
[ ] Naming clear and consistent?
[ ] No magic numbers/strings?
[ ] Comments where needed?
[ ] Tests cover edge cases?
```

---

### Common 30% Fixes: Examples

#### 1. Ownership Validation

```python
# AI's 70% (missing ownership check):
@router.delete("/todos/{id}")
async def delete_todo(id: UUID, db: Session):
    todo = db.query(Todo).get(id)
    if not todo:
        raise HTTPException(404)
    db.delete(todo)
    return {"status": "deleted"}

# YOUR 30% (adds ownership validation):
@router.delete("/todos/{id}")
async def delete_todo(
    id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).get(id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    if todo.owner_id != current_user.id:  # ← YOUR 30%
        raise HTTPException(403, "Access denied")
    db.delete(todo)
    return {"status": "deleted"}
```

---

#### 2. Case Sensitivity

```python
# AI's 70% (case-sensitive):
def get_tag_by_name(tag_name: str, db: Session):
    return db.query(Tag).filter(Tag.name == tag_name).first()

# YOUR 30% (case-insensitive):
def get_tag_by_name(tag_name: str, db: Session):
    return db.query(Tag).filter(
        Tag.name == tag_name.lower()  # ← YOUR 30%
    ).first()
```

---

#### 3. Idempotency

```python
# AI's 70% (creates duplicate):
def add_tag_to_todo(todo: Todo, tag_name: str, db: Session):
    tag = Tag(name=tag_name)
    todo.tags.append(tag)
    db.commit()
    return todo

# YOUR 30% (handles duplicates):
def add_tag_to_todo(todo: Todo, tag_name: str, db: Session):
    # Get or create tag
    tag = get_tag_by_name(tag_name, db)
    if not tag:
        tag = Tag(name=tag_name.lower())
        db.add(tag)

    # Check if already tagged (idempotent)
    if tag in todo.tags:  # ← YOUR 30%
        return todo  # Already tagged, no-op

    todo.tags.append(tag)
    db.commit()
    return todo
```

---

#### 4. Error Message Quality

```python
# AI's 70% (generic error):
if not todo:
    raise HTTPException(404)

# YOUR 30% (helpful error):
if not todo:
    raise HTTPException(
        status_code=404,
        detail=f"Todo with id {todo_id} not found"  # ← YOUR 30%
    )
```

---

### Your Professional Value = The 30%

**Think about it this way:**

```
AI handles the 70% boring stuff:
- Writing boilerplate
- Standard patterns
- Repetitive code

YOU handle the 30% valuable stuff:
- "What could go wrong?"
- "What did AI assume?"
- "Is this production-ready?"
- "What edge cases exist?"

The 30% is why companies hire PROFESSIONALS.
```

---

## Many-to-Many Relationships

### Understanding the Pattern

Many-to-many relationships connect two entities where:
- One entity can relate to multiple of another
- The other entity can relate to multiple of the first

**Example:** Todos and Tags
- One Todo can have multiple Tags
- One Tag can be on multiple Todos

---

### Database Structure

```sql
-- Entity 1: Todos
CREATE TABLE todos (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(200),
    description TEXT,
    completed BOOLEAN,
    owner_id VARCHAR(36)
);

-- Entity 2: Tags
CREATE TABLE tags (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(50),
    created_at TIMESTAMP
);

-- Association Table (Join Table)
CREATE TABLE todo_tags (
    todo_id VARCHAR(36) REFERENCES todos(id),
    tag_id VARCHAR(36) REFERENCES tags(id),
    PRIMARY KEY (todo_id, tag_id)  -- Composite key prevents duplicates
);
```

---

### SQLAlchemy Implementation

**Association Table:**
```python
# src/models/tag.py
from sqlalchemy import Table, Column, String, ForeignKey
from src.models.base import Base

todo_tags = Table(
    'todo_tags',
    Base.metadata,
    Column('todo_id', String(36), ForeignKey('todos.id'), primary_key=True),
    Column('tag_id', String(36), ForeignKey('tags.id'), primary_key=True),
)
```

**Tag Model:**
```python
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Many-to-many relationship
    todos = relationship('Todo', secondary=todo_tags, back_populates='tags')
```

**Todo Model (updated):**
```python
class Todo(Base):
    __tablename__ = 'todos'

    # ... existing fields ...

    # Many-to-many relationship
    tags = relationship('Tag', secondary=todo_tags, back_populates='todos')
```

---

### Working with Many-to-Many

**Add a tag to a todo:**
```python
async def add_tag_to_todo(todo_id: str, tag_name: str, user_id: str, db: AsyncSession):
    # Get todo
    todo = await db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(404, "Todo not found")
    if todo.owner_id != user_id:
        raise HTTPException(403, "Access denied")

    # Get or create tag
    result = await db.execute(
        select(Tag).where(Tag.name == tag_name.lower())
    )
    tag = result.scalar_one_or_none()

    if not tag:
        tag = Tag(name=tag_name.lower())
        db.add(tag)

    # Add to relationship (if not already present)
    if tag not in todo.tags:
        todo.tags.append(tag)  # SQLAlchemy handles the join table

    await db.commit()
    await db.refresh(todo)
    return todo
```

**Query todos by tag:**
```python
async def get_todos_by_tag(tag_name: str, user_id: str, db: AsyncSession):
    result = await db.execute(
        select(Todo)
        .join(Todo.tags)  # Join through the relationship
        .where(Tag.name == tag_name.lower())
        .where(Todo.owner_id == user_id)
    )
    return result.scalars().all()
```

---

### Pydantic Schemas for Many-to-Many

```python
# src/schemas/tag.py
from pydantic import BaseModel, Field
from datetime import datetime

class TagCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class TagResponse(BaseModel):
    id: str
    name: str
    created_at: datetime

    model_config = {"from_attributes": True}

# src/schemas/todo.py (updated)
from typing import List
from .tag import TagResponse

class TodoResponse(BaseModel):
    id: str
    title: str
    description: str | None
    completed: bool
    owner_id: str
    tags: List[TagResponse] = []  # ← Include related tags

    model_config = {"from_attributes": True}
```

---

### Common Pitfalls

**1. N+1 Query Problem**
```python
# BAD: Queries database for each todo's tags
todos = await db.execute(select(Todo))
for todo in todos.scalars():
    print(todo.tags)  # Separate query for EACH todo

# GOOD: Eager load tags with one query
todos = await db.execute(
    select(Todo).options(selectinload(Todo.tags))
)
for todo in todos.scalars():
    print(todo.tags)  # Tags already loaded
```

**2. Forgetting Ownership**
```python
# BAD: Any user can tag any todo
todo.tags.append(tag)

# GOOD: Verify ownership first
if todo.owner_id != current_user.id:
    raise HTTPException(403, "Cannot tag todo you don't own")
todo.tags.append(tag)
```

**3. Not Handling Duplicates**
```python
# BAD: Adds duplicate tags
todo.tags.append(tag)  # Might already exist

# GOOD: Check first (idempotent)
if tag not in todo.tags:
    todo.tags.append(tag)
```

---

## Boss Fight Strategy

### Challenge Recap

**Build:** POST /api/v1/todos/{todo_id}/tags

**Pre-built (session-4-start):**
- ✅ Tag model
- ✅ todo_tags association table
- ✅ Todo.tags relationship

**You build:**
- TagCreate and TagResponse schemas
- add_tag_to_todo service method
- POST /todos/{todo_id}/tags endpoint
- Update TodoResponse to include tags

---

### Winning Strategy: 5-Minute Speed Run

**Phase 1: Planning (30 seconds)**

Use `think hard` for focused planning:
```
#file:.github/agents/todo-api-expert.agent.md #file:src/models/tag.py

think hard about implementing POST /api/v1/todos/{todo_id}/tags

Requirements:
- Add tag to todo (create if doesn't exist)
- Case-insensitive
- Return updated TodoResponse with tags
- Handle 404, 403

Give me implementation plan.
```

**Expected output:**
- File-by-file breakdown
- Implementation order
- Key considerations

---

**Phase 2: Implementation (3 minutes)**

**Option A: Single comprehensive prompt (FASTEST)**
```
#file:.github/agents/todo-api-expert.agent.md #file:PRD.md #file:src/models/tag.py

[Context]
Tag model exists. todo_tags association table exists.
Following 3-tier architecture.

[Task]
Add POST /api/v1/todos/{todo_id}/tags endpoint

[Constraints]
1. TagCreate schema: { "name": str } (1-50 chars)
2. Service method add_tag_to_todo:
   - Verify ownership (404/403)
   - Normalize to lowercase
   - Get or create tag
   - Add to todo.tags
3. POST endpoint returns TodoResponse with tags
4. Update TodoResponse to include tags field

[Format]
Create: src/schemas/tag.py, update: todo.py, todo_service.py, todos.py
```

**Option B: TDD approach (if time permits)**
```
Step 1: Write test first
Step 2: Implement to pass test
```

---

**Phase 3: Critical 30% (1 minute)**

Quick verification:
```
Review the implementation:
1. Ownership validation works?
2. Tags case-insensitive?
3. Idempotency handled?
4. Error messages clear?

Fix any issues.
```

---

**Phase 4: Testing (30 seconds)**

```bash
# Quick functional test
curl -X POST .../todos -d '{"title":"test"}'
curl -X POST .../todos/{id}/tags -d '{"name":"Urgent"}'
curl .../todos/{id}  # Verify tags appear
curl -X POST .../todos/{id}/tags -d '{"name":"urgent"}'  # Test case-insensitive
```

---

### Scoring Optimization

```
TARGET: PLATINUM (≤3 min)

TIME SAVERS:
✓ Use 'think hard' (30 sec planning saves 1 min iteration)
✓ Single comprehensive prompt (faster than sequential)
✓ Skip TDD (test manually at end)
✓ Use Custom Agent (less context to explain)

BONUS POINTS (+1 level each):
✓ Used 'think hard'
✓ Used Custom Agent
✓ Verified ownership (the 30%)
□ Used TDD (skip if time-constrained)

POTENTIAL FINAL SCORE:
Base: PLATINUM (3 min)
+3 bonuses = PLATINUM +3 levels
```

---

### Common Mistakes to Avoid

```
❌ Forgetting to update TodoResponse schema with tags field
❌ Not normalizing tag names to lowercase
❌ Missing ownership validation
❌ Creating duplicate tags instead of get-or-create
❌ Not handling idempotency (tag already on todo)
❌ Poor error messages
❌ Not testing case-insensitivity
```

---

## Complete Workshop Summary

### Session 1: Foundation (60 min)

```
CORE SKILLS:
✅ Security-first mindset (.copilotignore, .env)
✅ Copilot modes (Ask, Edit, Agent, Plan)
✅ #mentions (#file, #folder, #problems)
✅ copilot-instructions.md

KEY TAKEAWAY:
Never expose secrets. Structure determines success.
```

---

### Session 2: Context Mastery (30 min)

```
CORE SKILLS:
✅ Thinking modes (think, think hard, think harder, ultrathink)
✅ Explore → Plan → Code workflow
✅ 6-element framework (Context, Task, Constraints, Format, Tone, Examples)
✅ PRD-driven development

KEY TAKEAWAY:
Context is king. Better context = exponentially better results.
```

---

### Session 3: Build Sprint (30 min)

```
CORE SKILLS:
✅ Test-Driven Development with AI
✅ Subagents for parallel work
✅ Plan Mode for visibility
✅ Rapid feature development
✅ Performance tracking

KEY TAKEAWAY:
Plan once, execute with precision. TDD catches AI mistakes.
```

---

### Session 4: Mastery (30 min)

```
CORE SKILLS:
✅ Checkpoint system for reliability
✅ Copilot Code Review
✅ Custom Agents (.agent.md)
✅ Memory Bank pattern
✅ The 70/30 Problem
✅ Boss Fight (all techniques combined)

KEY TAKEAWAY:
AI delivers 70% fast. YOUR 30% is professional value.
```

---

## Professional Workflow

### Daily AI-Augmented Development

```
MORNING:
1. Copilot reads memory-bank/ → Full context
2. Review PRs with Code Review
3. Plan day with 'think hard'

FEATURE DEVELOPMENT:
1. Explore codebase (semantic search)
2. Plan with 6-element framework
3. Code with TDD + Agent Mode
4. Review with Andrew's pattern
5. Apply your 30% fixes
6. Test edge cases

CODE REVIEW:
1. Self-review before commit
2. Copilot review on PR
3. Human review for business logic

END OF DAY:
1. Update Memory Bank
2. Commit changes
3. Update Custom Agents if patterns changed
```

---

## Certification Checklist

### Skills Verification

```
FOUNDATION ✓
[ ] Configure .copilotignore
[ ] Use all Copilot modes
[ ] Use #mentions effectively
[ ] Never expose secrets

CONTEXT MASTERY ✓
[ ] Use thinking modes appropriately
[ ] Follow Explore → Plan → Code
[ ] Apply 6-element framework
[ ] Create effective PRDs

BUILD SKILLS ✓
[ ] Practice TDD with AI
[ ] Use subagents for parallel work
[ ] Leverage Plan Mode
[ ] Develop features rapidly

MASTERY ✓
[ ] Use checkpoints effectively
[ ] Use Code Review
[ ] Create Custom Agents
[ ] Build Memory Bank
[ ] Understand 70/30 split
[ ] Complete Boss Fight
```

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
│   Name: _____________________               │
│   Level: ____________________               │
│   Date: _____________________               │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Quick Reference Card

```
COPILOT MODES:
• Ask - Questions, explanations
• Edit - Cmd/Ctrl+I inline edits
• Agent - Multi-file autonomous work
• Plan - /plan for visibility before execution

CONTEXT MENTIONS:
• #file:path - Include specific file
• #folder:path - Include folder context
• #file:.github/agents/name.agent.md - Include custom agent
• #file:memory-bank/activeContext.md - Current context
• #problems - Include errors

THINKING MODES:
• think - Basic analysis
• think hard - Complex problems ⚡
• think harder - Very complex
• ultrathink - Maximum reasoning

WORKFLOW:
Explore → Plan → Code → Review → Ship

THE 70/30 RULE:
AI delivers 70% fast. YOU add the critical 30%.
```

---

## Resources

### Official Documentation
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [Copilot Chat Guide](https://docs.github.com/en/copilot/github-copilot-chat)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

### Community
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot)
- Advanced patterns and use cases
- Community best practices

---

**End of Student Reference: Session 4** 🎓

---

## 🎉 CONGRATULATIONS! 🎉

You've completed the GitHub Copilot Power User Workshop!

**You are now equipped to:**
- Work 26% more productively
- Write more secure code
- Leverage AI while adding professional value
- Lead your team in AI-augmented development

**You're not a beginner anymore.**
**You're a POWER USER.**
**You're an AI-AUGMENTED PROFESSIONAL.**

**Go transform how your team codes! 💪🚀**
