# Student Reference: Micro Session 2
## Context Mastery & Project Planning - Technical Deep Dive

**📖 Reference:** GitHub Copilot Documentation, Best Practices Guide

---

## Session 2 Overview: From Tools to Mastery

**Session 1 Foundation:**
You learned the tools - 4 Copilot modes, #mentions, Custom Instructions, security setup.
You built a PRACTICE project.

**Session 2 Focus:**
You learn to USE those tools like a professional through context mastery.
You work with the PRE-BUILT todo app in `/src` and `/tests` - DIFFERENT from Session 1 practice!

**The Core Principle:**
AI output quality = Context quality

---

## 1. The Context Principle - Deep Understanding

### Why Context Matters

**The Core Truth:**
AI output quality directly correlates with context quality.

```
Weak context → Ambiguous → Multiple iterations → Slow
Strong context → Clear → First-attempt success → Fast
```

**Professional developers know:** The time spent crafting a good prompt is ALWAYS less than the time spent fixing bad output.

### The Context Quality Spectrum

**Level 1: Beginner** (Vague)
```
"create an endpoint"
```
AI must guess: What kind? What HTTP method? What does it do? Authentication?

**Level 2: Intermediate** (Some details)
```
"create a POST endpoint for todos"
```
Better, but still missing: Error handling? Validation? Response format?

**Level 3: Advanced** (Specific)
```
"Create POST /api/v1/todos endpoint with TodoCreate input, 
auth required, return 201 with TodoResponse, handle 400/500 errors"
```
Much better! But could be clearer about where to put code.

**Level 4: Professional** (Complete)
```
[Context] #folder:src/api/ shows existing patterns
[Task] Create POST /api/v1/todos endpoint
[Constraints]
- Use TodoCreate schema for input validation
- Require authentication (get_current_user)
- Associate todo with current user
- Return 201 status with TodoResponse
- Handle ValueError→400, Exception→500
- Follow async patterns from #file:.github/copilot-instructions.md
[Format]
- Update src/api/v1/todos.py (create if needed)
- Use TodoService.create() method
- Add proper error handling
```
**Result:** AI has zero ambiguity. Perfect output, first try.

---

## 2. Thinking Modes - Extended Reasoning

### What They Are

**💡 Important:** Thinking modes are LLM MODEL features, not Copilot-specific. The AI models that power Copilot understand these keywords for extended reasoning.

**The Modes:**
```
normal          → Instant response (default)
"think"         → +5-10 seconds (basic extended thinking)
"think hard"    → +10-20 seconds (thorough analysis)
"think harder"  → +20-30 seconds (deep evaluation)
"ultrathink"    → +30+ seconds (maximum thinking budget)
```

### When to Use

**Use thinking modes for:**
- Architecture decisions
- Complex planning
- Trade-off analysis
- Technical design choices
- Exploring multiple approaches

**Skip for:**
- Simple tasks (file creation, basic edits)
- Well-defined straightforward operations
- Tasks with clear single solutions

### Cost

**Same credits** - just more compute time. Worth it for important decisions where quality matters more than speed.

### Examples

**Without thinking mode:**
```
What's the best database for a todo app?

Response: "PostgreSQL is a good choice..."
```

**With "think hard":**
```
think hard about the best database choice for a todo app.
Consider: scale, complexity, team skills, hosting.

Response: [Takes 15 seconds]
"Let me analyze the trade-offs:

PostgreSQL:
  Pros: Robust, ACID compliant, JSON support
  Cons: Heavier, requires more setup
  Best for: Production apps with growth potential

SQLite:
  Pros: Zero config, fast for reads, embedded
  Cons: Limited concurrency, no network access
  Best for: Development, small deployments

Given a todo app context..."
```

**The difference:** More thorough analysis, considers trade-offs, provides reasoning.

---

## 3. Professional Workflow: Explore → Plan → Code

### The Complete Pattern

```
1. EXPLORE (Ask Mode + "think")
   ↓
2. PLAN (Document or PRD)
   ↓
3. CODE (Agent Mode + structured prompts)
```

### Phase 1: EXPLORE

**Purpose:** Think WITH the AI before coding

**When to use:**
- Complex features
- Unclear requirements
- Multiple possible approaches
- Learning new domain

**How to do it (Copilot Chat - Ask Mode):**
```
I want to add a tagging feature to our existing todo API -
allowing many-to-many relationships between todos and tags.

Before we write code, help me think through:
1. What are essential vs nice-to-have features?
2. What technical decisions need to be made upfront
   (schema design, queries)?
3. What challenges should I consider (duplicate tags,
   case sensitivity)?
4. What's the simplest viable implementation?

Don't write code yet - just help me explore this idea.

think about this carefully
```

**Why "think" matters:**
- `think` → Basic extended reasoning (5-10 sec more)
- `think hard` → More computation (10-20 sec more)
- `think harder` → Deep analysis (20-30 sec more)
- `ultrathink` → Maximum thinking budget (30+ sec)

**Cost:** Same credits, just more compute time. Worth it for important decisions!

**Example conversation:**
```
You: "think hard about the best way to implement many-to-many
     relationship between todos and tags for our existing todo API"

AI: [Takes 15 seconds thinking...]
    "Let me evaluate several approaches:

    Approach 1: Single join table (todo_tags)
    Pros: Simple, standard pattern, clean separation
    Cons: No metadata on tag associations
    Best for: MVP with basic tagging

    Approach 2: Join table with metadata
    Pros: Can add created_at, created_by, ordering
    Cons: More complex queries
    Best for: If you need tag history/audit

    Approach 3: JSON array in todos table
    Pros: Fast for reading single todo
    Cons: Poor query performance (can't filter todos by tag),
          no referential integrity, denormalized
    Best for: Read-heavy, no tag-based queries needed

    Recommendation for todo API: Approach 1 because..."
```

**Key insight:** Professionals don't jump to code. They explore with AI first.

---

### Phase 2: PLAN

**Purpose:** Document intentions before implementation

**Two types of planning:**

**A. Product Requirements Document (PRD)**

What to build, for whom, and why.

```markdown
# PRD-Tags.md - Tagging Feature for Todo API

## Overview
Add tagging functionality to existing todo API to enable categorization
and filtering of todos by user-defined tags.

## Core Features (MVP)
1. Create Tags
   - Tag name (required, unique, case-insensitive, max 50 chars)
   - Auto-normalize to lowercase
   - User-specific tags

2. Add/Remove Tags from Todos
   - POST /api/v1/todos/{id}/tags to add tag
   - DELETE /api/v1/todos/{id}/tags/{tag_id} to remove
   - Users can only tag their own todos

3. List Todos by Tag
   - GET /api/v1/todos?tag=work
   - Filter todos by one or more tags
   - Existing pagination support

4. View Tags on Todo
   - Include tags in TodoResponse
   - Show all tags for a todo

## Technical Requirements
- Many-to-many: Todo ↔ TodoTag ↔ Tag (3 tables)
- Prevent duplicate tags (case-insensitive uniqueness)
- Cascade delete: Remove todo_tags entries when todo deleted
- 3-tier architecture: models → services → API

## User Stories
- As a user, I want to tag todos to organize by category
- As a user, I want to filter todos by tag to see related items
- As a user, I want tags to be case-insensitive (work = Work = WORK)

## Non-Goals (NOT Building in v1)
- Tag sharing between users
- Tag hierarchies/nesting
- Tag colors or icons
- Tag analytics or trending
```

**Why write PRDs:**
- Prevents scope creep
- Clear success criteria
- Reference during development
- Helps AI understand full context

**How to use PRDs in development:**
```
#file:PRD-Tags.md

Implement POST /api/v1/todos/{id}/tags endpoint following PRD requirements.

Include:
- Features from PRD Core Features section
- Technical requirements (many-to-many, case-insensitive)
- User authorization (only tag own todos)
- Error handling and validation
```

**Best practices:**
- Reference with `#file:PRD-Tags.md` when implementing features
- Use for code review validation ("Does this match PRD?")
- Check scope before adding features ("Is this in PRD?")
- Update PRD as requirements evolve (living document)

---

**B. Architecture Decision Records (ADR)**

Why you chose specific approaches.

```markdown
# ADR 001: Why FastAPI for Todo API?

## Status
Accepted

## Context
Need Python web framework for REST API.
Team knows Python. Need async support.

## Decision
Use FastAPI

## Rationale
**Pros:**
- Native async/await support (fast I/O)
- Auto-generated OpenAPI docs
- Type hints = better validation
- Modern Python 3.11+ features
- Excellent for APIs specifically

**Cons:**
- Newer than Django/Flask (smaller community)
- Team learning curve (2-3 hours)

**Alternatives Considered:**
- Django: Too heavy for simple API, slower
- Flask: Missing async, no auto-docs, more boilerplate

## Consequences
- Team must learn FastAPI (acceptable - 2 hour investment)
- Excellent documentation available
- Fast development speed
- Performance benefits from async
```

**When to write ADRs:**
- Major technology choices
- Architecture patterns
- Database decisions
- Authentication strategies

---

### Phase 3: CODE

**Purpose:** Implement with high-quality prompts

**Use the 6-Element Professional Framework:**

**IMPORTANT:** This is a TOOLBOX, not a checklist!
- Simple tasks: Use 2-3 elements
- Medium tasks: Use 4 elements  
- Complex tasks: Use 5-6 elements

```
1. [PERSONA] ← Optional: Define AI's expertise
   "You're a senior FastAPI developer specializing in async APIs..."
   Use when: Complex domain knowledge needed
   Skip when: Simple tasks, file operations

2. [CONTEXT] ← ALWAYS include!
   - What code exists? (#mentions)
   - What patterns to follow?
   - What's the architecture?
   
3. [TASK] ← ALWAYS include!
   - ONE clear objective
   - Specific, not vague

4. [CONSTRAINTS] ← Use when requirements exist
   - Must include X
   - Must use Y
   - Must avoid Z
   - Status codes
   - Error handling
   Skip when: Task is self-explanatory

5. [FORMAT] ← Use when structure matters
   - Which files to create/update
   - Expected structure
   - Return type
   Skip when: Format is obvious

6. [EXAMPLES] ← Optional: Show patterns
   "Like #file:example.py lines X-Y..."
   Use when: Project-specific patterns exist
   Skip when: Standard patterns sufficient
```

**Scaling Guide:**

```
SIMPLE TASK (2 elements):
[CONTEXT] + [TASK]
Example: "Create .gitignore file"

MEDIUM TASK (4 elements):  
[CONTEXT] + [TASK] + [CONSTRAINTS] + [FORMAT]
Example: "Add validation to endpoint"

COMPLEX TASK (5-6 elements):
[PERSONA] + [CONTEXT] + [TASK] + [CONSTRAINTS] + [FORMAT] + [EXAMPLES]
Example: "Implement many-to-many relationship with endpoints"
```

**Example:**
```
[Context]
Working on todo API with tagging feature. #folder:src/api/v1/ shows existing endpoint patterns.
#file:src/models/todo.py has Todo model defined.
#file:PRD-Tags.md defines tagging requirements.
Following 3-tier architecture from #folder:src/

[Task]
Create POST /api/v1/todos/{id}/tags endpoint to add tags to a todo

[Constraints]
- Tag name required (max 50 chars, case-insensitive)
- Auto-normalize tag names to lowercase
- Create tag if doesn't exist, reuse if exists
- Only allow users to tag their own todos (verify ownership)
- Return 201 with updated TodoResponse including tags
- Return 400 for validation errors (empty name, too long)
- Return 403 if user doesn't own todo
- Return 404 if todo not found
- Must use async/await (#file:.github/copilot-instructions.md pattern)
- Follow 3-tier architecture pattern

[Format]
Update these files:
1. src/models/tag.py - Tag model with many-to-many relationship
   * Tag model: id, name (unique, lowercase)
   * TodoTag association table
2. src/services/tag_service.py - add_tag_to_todo() method
   * Takes todo_id, tag_name, user_id
   * Verify todo ownership
   * Create or fetch tag (case-insensitive)
   * Create todo_tag association
3. src/api/v1/todos.py - add POST "/{id}/tags" endpoint
   * Path param: todo_id (UUID)
   * Body: TagCreate (name field)
   * Use get_current_user and get_db dependencies
   * Call service.add_tag_to_todo()
   * Return TodoResponse with tags included
```

**Why this works:**
- Zero ambiguity
- References existing code
- Explicit requirements
- Clear deliverables

---

## 4. Advanced #mention Patterns

### Pattern 1: File and Folder References

**Basic patterns:**
```
#file:src/main.py              ← Single specific file
#folder:src/api/               ← All files in folder
#folder:tests/                 ← All test files
#folder:src/                   ← All source files
```

**Use when:**
- Need to show AI multiple related files
- Want AI to see patterns across files
- Establishing consistency

**Example:**
```
#folder:src/api/

Review all API endpoints for consistency:
- Are error codes standardized?
- Do all use the same auth pattern?
- Are response formats consistent?
```

---

### Pattern 2: Folder Context

**Syntax:**
```
#folder:src/services/    ← Include entire directory
#folder:tests/           ← All test context
```

**Use when:**
- AI needs broad context
- Understanding architecture
- Finding patterns

**Example:**
```
#folder:src/services/

Analyze the service layer pattern used across all services.
Then create tag_service.py following the same pattern.
```

---

### Pattern 3: #problems for Error Fixing

**The #problems mention:**

**#problems** - Current IDE errors
```
Use for: Fixing errors in bulk
Example: "#problems Fix all linting and type errors"
```

**Why focus on #problems?**
- Already learned #terminalSelection and @workspace in Session 1
- #problems is powerful when combined with other #mentions
- Session 2 focuses on layering contexts (see Pattern 4 below)

---

### Pattern 4: Combining #mentions (The Power Move)

**The power move:** Layer multiple contexts

**Example 1: Context + Errors**
```
#folder:src/api/ #problems

Fix all errors in the API layer while maintaining 
consistency with existing patterns.
```

**Example 2: Multiple files for context**
```
#file:src/services/todo_service.py #file:src/models/todo.py

Review the service layer and its interaction with the model.
Are there any potential issues with the data flow?
```

**Example 3: Multiple files for pattern matching**
```
#file:src/api/v1/todos.py #file:src/api/v1/users.py

Both endpoints follow similar patterns. Create items.py 
endpoint following the exact same structure.
```

**Why layer contexts:**
- AI gets complete picture
- More accurate output
- Fewer followup questions

---

## 5. The 6-Element Framework (Deep Dive)

### Part 1: [Context]

**What to include:**
- Relevant files (#mentions)
- Architecture patterns
- Existing code to reference
- Project constraints
- Tech stack

**Examples:**

**Weak context:**
```
Working on a todo app
```

**Strong context:**
```
Working on FastAPI todo API.
#folder:src/ shows 3-tier architecture (api/services/models).
#file:src/models/todo.py has Todo model with title, description, completed fields.
Following async patterns from #file:.github/copilot-instructions.md.
PostgreSQL database via SQLAlchemy async.
```

---

### Part 2: [Task]

**Rules for good tasks:**
- ONE clear objective
- Specific, not vague
- Actionable verb (create, update, fix, analyze)
- Include what, not how (unless specific approach needed)

**Examples:**

**❌ Vague:**
```
"make it better"
"fix the code"
"add features"
```

**✅ Specific:**
```
"Create POST /api/v1/todos endpoint"
"Fix the N+1 query problem in get_all_todos()"
"Add pagination support to the list endpoint"
```

---

### Part 3: [Constraints]

**Types of constraints:**

**Functional requirements:**
- Must authenticate users
- Must validate input
- Must handle errors

**Technical requirements:**
- Use async/await
- Follow existing patterns
- Max X seconds response time

**Quality requirements:**
- Include type hints
- Write docstrings
- Add error handling

**What NOT to do:**
- Don't use mocks (use real DB)
- Don't expose internal errors
- Don't skip validation

**Example constraint section:**
```
[Constraints]
- Require authentication via get_current_user dependency
- Validate: title not empty, max 200 chars
- Validate: description optional, max 1000 chars
- Return 201 status on success
- Return 400 for validation errors with clear message
- Return 500 for unexpected errors (don't expose internals)
- Associate todo with current user (owner_id)
- Follow async patterns from #file:.github/copilot-instructions.md
- Include proper type hints
- Write docstring explaining endpoint
```

---

### Part 4: [Format]

**What to specify:**
- Which files to create/modify
- Expected structure
- Response format
- Return types

**Example format section:**
```
[Format]
Create or update these files:
1. src/schemas/todo.py
   - TodoCreate schema (title, description)
   - TodoResponse schema (all fields + id, owner_id, created_at)
   
2. src/services/todo_service.py
   - TodoService class
   - create() method taking TodoCreate and user_id
   - Returns Todo model instance
   
3. src/api/v1/todos.py
   - POST "/" endpoint
   - Returns TodoResponse
   - Status code 201

4. src/main.py
   - Import and include todos router

Don't modify: tests (will add separately)
```

---

## 6. Thinking Modes - When and How

### The Thinking Levels

| Mode | Compute Time | Use For |
|------|--------------|---------|
| (normal) | Instant | Simple tasks, clear requirements |
| `think` | +5-10 sec | Planning, exploring options |
| `think hard` | +10-20 sec | Complex decisions, architecture |
| `think harder` | +20-30 sec | Deep analysis, optimization |
| `ultrathink` | +30+ sec | Critical decisions, security |

### When to Use Each

**Normal (no keyword):**
- Straightforward implementation
- Clear requirements
- Following established patterns

**"think":**
- Initial feature planning
- Understanding new codebase
- Exploring trade-offs

**"think hard":**
- Architecture decisions
- Complex refactoring plans
- Performance optimization strategies
- Security considerations

**"think harder":**
- Mission-critical code
- Complex algorithm design
- System-wide changes

**"ultrathink":**
- Rarely needed
- Production security audit
- Complex distributed systems
- Critical business logic

### Examples

**Planning with "think":**
```
think about how to structure the tagging feature for our existing todo API.

Should it be:
- Option A: Tags as separate table with many-to-many (Todo ↔ TodoTag ↔ Tag)?
- Option B: Tags as JSON array in todos table?
- Option C: Tags as comma-separated string in todos?

Consider:
- Query performance (filter todos by tag)
- Flexibility (tag reuse, tag management)
- Database complexity and maintenance
- Case-insensitive uniqueness requirements
```

**Architecture with "think hard":**
```
think hard about the best caching strategy for this API.

Consider:
- Where to cache (Redis? In-memory? CDN?)
- What to cache (responses? query results? rendered data?)
- Invalidation strategy (TTL? Event-based? Manual?)
- Cache miss handling
- Multi-instance consistency

We have 100k daily active users, 1M API calls/day, 
P99 latency target <200ms.
```

---

## 7. Custom Instructions vs Prompt Files

### What They Actually Are

**Custom Instructions** (.github/copilot-instructions.md)
- HOW AI should behave
- Coding standards
- Team preferences
- Always applied to every interaction
- Examples: "use type hints", "max line 100", "async for I/O"

**Prompt Files** (.github/prompts/*.prompt.md)
- Reusable prompt templates
- Feature-specific instructions
- Referenced with `#file:` when needed
- Examples: API endpoint template, test template

### When to Use Each

**Use Custom Instructions for:**
```
✅ "Always use type hints"
✅ "Write docstrings for all functions"
✅ "Use async/await for I/O"
✅ "Max line length 100 characters"
✅ "Follow PEP 8"
```

**Use Prompt Files for:**
```
✅ Reusable feature templates
✅ Standard code patterns
✅ Onboarding new team members
✅ Consistent prompts across team
```

---

## 8. GitHub Copilot Modes Deep Dive

### Ask Mode
**Best for:** Questions, exploration, learning
**File changes:** No
**When to use:** 
- Exploring ideas
- Learning about code
- Understanding patterns
- "think" sessions

### Edit Mode (Cmd+I)
**Best for:** Quick inline changes
**File changes:** Single file, targeted
**When to use:**
- Small fixes
- Adding a function
- Modifying existing code
- Quick refactors

### Agent Mode
**Best for:** Multi-file features
**File changes:** Multiple files
**When to use:**
- Building features
- Creating PRDs
- Multi-file refactors
- Complex implementations

### Plan Mode (/plan)
**Best for:** Complex implementation planning
**File changes:** Creates plan first, then executes
**When to use:**
- Large features
- Architectural changes
- When you want to review before execution
- Complex multi-step tasks

---

## 9. Context Management Best Practices

### The Professional Checklist

**✅ DO:**
- Reference existing code with #mentions
- Be hyper-specific in requirements
- Use Context+Task+Constraints+Format structure
- Think before coding ("think" keyword)
- Layer multiple #mentions for complete context
- Include status codes and error cases
- Specify files to create/update

**❌ DON'T:**
- Assume AI knows your patterns
- Be vague ("make it good")
- Skip error handling requirements
- Forget to specify response format
- Rush to code without planning
- Use generic prompts

### Quick Reference: Prompt Quality

**Level 1 (Beginner):**
```
"create endpoint"
```

**Level 2 (Intermediate):**
```
"Create POST /todos endpoint with authentication"
```

**Level 3 (Advanced):**
```
"Create POST /todos endpoint. Requires auth. 
Takes title and description. Returns 201 with created todo."
```

**Level 4 (Professional):**
```
[Context] #folder:src/api/ #file:src/models/todo.py
Following 3-tier architecture

[Task] Create POST /api/v1/todos endpoint

[Constraints]
- Auth required (get_current_user)
- Input: TodoCreate (title required max 200, description optional max 1000)
- Validate title not empty
- Associate with current user
- Return 201 with TodoResponse
- Handle 400 validation, 401 auth, 500 errors
- Use async patterns from #file:.github/copilot-instructions.md

[Format]
- src/schemas/todo.py: TodoCreate, TodoResponse
- src/services/todo_service.py: create() method
- src/api/v1/todos.py: POST endpoint
```

**Aim for Level 4 on important features.**

---

## 10. Self-Assessment Quiz

**1. What's the most important factor for AI output quality?**
Answer: Context quality - good context = good output

**2. What are the 6 parts of a professional prompt?**
Answer: Persona, Context, Task, Constraints, Format, Examples

**3. When should you use "think hard"?**
Answer: Complex decisions, architecture planning, critical features

**4. What's the difference between Custom Instructions and Prompt Files?**
Answer: Custom Instructions = always applied, Prompt Files = referenced when needed

**5. What's the professional workflow?**
Answer: Explore → Plan → Code

**6. What are the 4 Copilot modes?**
Answer: Ask, Edit, Agent, Plan

**7. What #mention gives you IDE errors?**
Answer: #problems

**8. When do you use Ask vs Agent mode for planning?**
Answer: Ask for exploring/planning (no changes), Agent for creating documents

**9. What should [Context] include?**
Answer: Relevant files (#mentions), architecture, existing patterns, tech stack

**10. What makes a good [Task]?**
Answer: One clear objective, specific not vague, actionable verb

---

## 11. Next Session Preview

**Session 3: Build Sprint - You'll:**
- Build with TDD approach (tests first)
- Apply the 6-Element Framework formula
- Compare: basic prompts vs optimized prompts
- Track YOUR actual results
- Prove that context quality matters
- Use Subagents for parallel work

**The proof session - where you see it work!** 🚀

---

**End of Student Reference: Micro Session 2** 🎓
