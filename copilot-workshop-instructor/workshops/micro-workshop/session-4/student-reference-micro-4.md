# Student Reference: Micro Session 4
## Code Review, Custom Agents & Boss Fight - Technical Deep Dive 🎮🏆

**Session Duration:** 33 minutes  
**Topics:** Code Review, Custom Agents, 70/30 Problem, Boss Fight

---

## Table of Contents

1. [Copilot Code Review](#copilot-code-review)
2. [Custom Agents (.agent.md)](#custom-agents)
3. [The 70% Problem](#the-70-problem)
4. [Boss Fight Strategy](#boss-fight-strategy)
5. [Complete Workshop Summary](#complete-workshop-summary)

---

## Copilot Code Review

### GitHub Pull Request Review

Copilot can review your Pull Requests directly on GitHub:

```
WHERE: GitHub.com → Pull Request → Reviewers

HOW TO USE:
1. Create/open a Pull Request
2. Click "Reviewers" in sidebar
3. Add "Copilot" as a reviewer
4. Copilot analyzes and comments

WHAT IT REVIEWS:
✅ Code quality and best practices
✅ Potential bugs
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase
```

### In-Editor Code Review

Use Copilot Chat for instant reviews without creating a PR:

```
BASIC REVIEW:
Review #file:src/api/v1/todos.py for issues.

THOROUGH REVIEW:
Review #file:src/api/v1/todos.py checking:
1. Security (auth, validation, injection)
2. Error handling (all paths covered?)
3. Performance (N+1 queries, efficiency)
4. Best practices (naming, patterns)

Be thorough and list issues by severity.
```

### Andrew's Code Review Pattern

A comprehensive review template for AI-generated code:

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

### When to Use Code Review

| Situation | Review Method |
|-----------|---------------|
| Before PR | In-editor review |
| During PR | GitHub Copilot reviewer |
| After AI generation | Andrew's pattern |
| Quick sanity check | Basic review prompt |
| Pre-deployment | Thorough review |

---

## Custom Agents

### What Are Custom Agents?

Custom Agents are pre-configured AI specialists defined in `.agent.md` files:

```
PURPOSE:
- Define specialized AI personas
- Pre-load project-specific context
- Set coding standards and patterns
- Create reusable conversation context

LOCATION:
.github/agents/*.agent.md

EXAMPLES:
- api-expert.agent.md
- testing-specialist.agent.md
- security-reviewer.agent.md
```

### Agent File Structure

```markdown
# .github/agents/[name].agent.md

# [Agent Name]

[Brief description of the agent's expertise]

## Architecture Knowledge
[What the agent knows about your system architecture]

## Key Patterns
[Coding patterns the agent should follow]

## File Structure
[Project organization the agent understands]

## Coding Standards
[Standards and conventions to enforce]

## Behavior Instructions
[How the agent should respond to requests]
```

### Example: Todo API Expert Agent

```markdown
# .github/agents/todo-api.agent.md

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

### Using Custom Agents

**Method 1: Reference in Prompt**
```
Using #file:.github/agents/todo-api.agent.md context:

Add pagination to the GET /api/v1/todos endpoint.
```

**Method 2: Include at Start of Session**
```
I'm working with the context from #file:.github/agents/todo-api.agent.md.

Today I need to add a new feature for todo priorities.
```

### Agent Best Practices

```
DO:
✅ Keep agents focused on specific domains
✅ Include concrete examples in agent files
✅ Update agents as project evolves
✅ Create multiple specialized agents

DON'T:
❌ Make agents too generic
❌ Include sensitive information
❌ Forget to update when patterns change
❌ Create one massive "knows everything" agent
```

### Agent Ideas for Your Projects

| Agent Type | Purpose |
|------------|---------|
| API Expert | Knows your API patterns |
| Test Writer | Follows your test conventions |
| Security Reviewer | Checks security patterns |
| DB Expert | Database optimization |
| Frontend Lead | UI patterns and components |
| DevOps Helper | Deployment and infra |

---

## The 70% Problem

### Understanding the Split

AI-assisted development creates a predictable productivity pattern:

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

### The Business Impact

**Organizations that understand the 70/30:**
- 26% measured productivity gains
- Faster delivery with maintained quality
- Sustainable AI-augmented workflows
- Professional development teams thriving

**Organizations that don't:**
- Accumulating technical debt
- "AI-generated" bugs in production
- Decreased trust in AI tools
- Wasted potential

### The Critical 30% Checklist

Use this checklist after EVERY AI-generated code:

```
SECURITY (Check all that apply)
[ ] Authentication required on all protected endpoints?
[ ] Authorization checks (ownership, roles)?
[ ] Input validation complete?
[ ] SQL injection protected?
[ ] Secrets properly handled?

ERROR HANDLING
[ ] All error paths return appropriate status codes?
[ ] Error messages are helpful but not leaky?
[ ] Edge cases handled (empty, null, duplicate)?
[ ] Validation errors are specific?

BUSINESS LOGIC
[ ] Business rules correctly implemented?
[ ] Edge cases for your domain covered?
[ ] Matches requirements exactly?
[ ] Integration with existing features correct?

QUALITY
[ ] Code follows project patterns?
[ ] Naming is clear and consistent?
[ ] No magic numbers/strings?
[ ] Comments where needed?
```

### Common 30% Fixes

**Authentication/Authorization:**
```python
# AI might generate:
@router.get("/todos/{id}")
async def get_todo(id: UUID, db: Session):
    return db.query(Todo).get(id)

# YOUR 30% adds:
@router.get("/todos/{id}")
async def get_todo(
    id: UUID, 
    current_user: User = Depends(get_current_user),  # Auth
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).get(id)
    if not todo:
        raise HTTPException(404, "Todo not found")  # Not found
    if todo.user_id != current_user.id:
        raise HTTPException(403, "Access denied")   # Ownership
    return todo
```

**Case Sensitivity:**
```python
# AI might generate:
def get_todos_by_tag(tag_name: str):
    return query.filter(Tag.name == tag_name)

# YOUR 30% adds:
def get_todos_by_tag(tag_name: str):
    return query.filter(Tag.name == tag_name.lower())  # Normalize
```

**Idempotency:**
```python
# AI might generate:
def add_tag_to_todo(todo_id, tag_name):
    tag = Tag(name=tag_name)
    todo.tags.append(tag)

# YOUR 30% adds:
def add_tag_to_todo(todo_id, tag_name):
    existing = get_tag_by_name(tag_name)
    if existing and existing in todo.tags:
        return todo  # Already tagged - idempotent
    tag = existing or Tag(name=tag_name.lower())
    todo.tags.append(tag)
```

---

## Boss Fight Strategy

### The Challenge Recap

```
BUILD: Complete TODO TAGGING feature

ENDPOINTS:
• POST /api/v1/todos/{id}/tags - Add tag
• GET /api/v1/todos?tag=name - Filter by tag
• DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag

DATABASE:
• Tag model (id, name, user_id, created_at)
• todo_tags association table (many-to-many)

REQUIREMENTS:
• Ownership validation
• Case-insensitive tags
• 404/403/400 error handling
• 3-tier architecture
```

### Winning Strategy: Speed Run

**Phase 1: Planning (30 seconds)**

Use `think hard` to plan architecture:
```
think hard about implementing many-to-many tagging for todos.

Need: Tag model, association table, 3 endpoints, ownership validation.
Give me file-by-file implementation order.
```

**Phase 2: Implementation (3 minutes)**

Use Plan Mode for visibility and efficiency:
```
/plan Implement todo tagging:
1. Tag model + association table
2. Tag schemas
3. Tag service methods
4. Tag API endpoints

Follow patterns in #folder:src/
```

**Phase 3: Critical 30% (1.5 minutes)**

Quick verification:
```
Verify the tagging implementation:
1. Does ownership validation work?
2. Are tags case-insensitive?
3. Are error messages clear?
4. Is idempotency handled?

Fix any issues.
```

**Phase 4: Testing (1 minute)**

```bash
# Quick functional test
curl -X POST .../todos -d '{"title":"test"}'
curl -X POST .../todos/{id}/tags -d '{"name":"Urgent"}'
curl ".../todos?tag=urgent"  # Case insensitive
```

### Parallel Work with Subagents

For maximum speed, use subagents:

**Main Chat:** Database layer
```
Create Tag model and todo_tags association table.
#file:src/models/todo.py #file:src/models/base.py
```

**Subagent 1:** Schema layer
```
Create TagCreate and TagResponse schemas.
#file:src/schemas/todo.py
```

**Subagent 2:** Plan API layer
```
/plan Add tag endpoints to todos router.
Include POST, DELETE, and GET with ?tag filter.
```

### Scoring Strategy

```
TARGET: PLATINUM (≤6 min)

TECHNIQUE              TIME SAVED
think hard planning    30 seconds (focused plan)
Plan Mode             1 minute (batch implementation)
Skip TDD              1 minute (testing at end)
Focused prompts       30 seconds (less iteration)

BONUS POINTS (+1 level each):
• Use think hard ✓
• Use Plan Mode ✓
• Use TDD (if time allows)
• Use Custom Agent ✓
```

---

## Complete Workshop Summary

### Session 1: Foundation (60 min)

```
CORE SKILLS:
✅ Security-first mindset (.copilotignore, .env handling)
✅ Copilot modes (Ask, Edit, Agent, Plan)
✅ #mentions (#file:, #folder:, #problems)
✅ Basic prompting techniques

KEY TAKEAWAY:
Never expose secrets to AI. Structure determines success.
```

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

### Session 3: Build Sprint (30 min)

```
CORE SKILLS:
✅ Test-Driven Development with AI
✅ Subagents for parallel work
✅ Plan Mode for visibility
✅ Rapid feature development

KEY TAKEAWAY:
Plan once, execute with precision. TDD catches AI mistakes.
```

### Session 4: Mastery (33 min)

```
CORE SKILLS:
✅ Copilot Code Review
✅ Custom Agents (.agent.md)
✅ The 70/30 Problem
✅ Boss Fight (all techniques combined)

KEY TAKEAWAY:
AI delivers 70% fast. YOUR 30% is professional value.
```

---

## Professional Workflow Summary

### Daily AI-Augmented Development

```
MORNING STANDUP:
1. Review PRs with Copilot Code Review
2. Plan day's work with think hard

FEATURE DEVELOPMENT:
1. Explore codebase with semantic search
2. Plan with 6-element framework
3. Code with TDD + Agent Mode
4. Review with Andrew's pattern
5. Apply your 30% fixes

CODE REVIEW:
1. Self-review before commit
2. Copilot review on PR
3. Human review for business logic

CONTINUOUS IMPROVEMENT:
1. Update Custom Agents with new patterns
2. Refine .copilot-instructions.md
3. Share prompts with team
```

### Prompt Template Library

**Quick Feature:**
```
#file:[relevant file]

Add [feature] that:
- [Requirement 1]
- [Requirement 2]

Follow existing patterns.
```

**Comprehensive Feature:**
```
#folder:[relevant folder]

think hard about implementing [feature].

[Context]
[Current state description]

[Task]
[Specific implementation needed]

[Constraints]
- [Constraint 1]
- [Constraint 2]

[Format]
[Desired output structure]
```

**Code Review:**
```
Review #file:[file] for:
1. Security issues
2. Error handling
3. Performance
4. Best practices

Be thorough. List issues by severity.
```

**Debug:**
```
#file:[error file] #problems

This error occurs: [error message]

Expected: [expected behavior]
Actual: [actual behavior]

think hard about the root cause and fix.
```

---

## Certification Checklist

### Skills Verification

```
FOUNDATION ✓
[ ] Can configure .copilotignore
[ ] Knows all Copilot modes
[ ] Uses #mentions effectively
[ ] Never exposes secrets

CONTEXT MASTERY ✓
[ ] Uses thinking modes appropriately
[ ] Follows Explore → Plan → Code
[ ] Applies 6-element framework
[ ] Creates effective PRDs

BUILD SKILLS ✓
[ ] Practices TDD with AI
[ ] Uses subagents for parallel work
[ ] Leverages Plan Mode
[ ] Develops features rapidly

MASTERY ✓
[ ] Uses Code Review effectively
[ ] Creates Custom Agents
[ ] Understands 70/30 split
[ ] Completed Boss Fight
```

### Power User Certification

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
• Ask Mode - Questions, explanations
• Edit Mode - Cmd/Ctrl+I inline edits
• Agent Mode - Multi-file autonomous work
• Plan Mode - /plan for visibility before execution

CONTEXT MENTIONS:
• #file:path - Include specific file
• #folder:path - Include folder context
• #problems - Include current errors
• #terminalSelection - Include terminal output

THINKING MODES:
• think - Basic analysis
• think hard - Complex problems
• think harder - Very complex problems
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
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

### Advanced Topics
- [Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot)
- [Copilot for Business](https://docs.github.com/en/copilot/copilot-business)
- [Copilot Enterprise](https://docs.github.com/en/copilot/github-copilot-enterprise)

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

**Go transform how your team codes! 💪🚀**
