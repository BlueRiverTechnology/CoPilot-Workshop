# Session 2 Prompt Sheet: Context Mastery & Project Planning 🎯📋

**Copy-paste materials for students**

---

## 1️⃣ Thinking Modes Keywords

Add these to your prompts for extended reasoning:

```
"think"         → Basic extended thinking (~5-10 sec)
"think hard"    → Thorough analysis (~10-20 sec)
"think harder"  → Deep evaluation (~20-30 sec)
"ultrathink"    → Maximum thinking budget (~30+ sec)
```

**💡 Note:** These are LLM MODEL features, not tool-specific. Same credits, more compute time.

**Use for:** Architecture decisions, complex planning, trade-off analysis

---

## 2️⃣ Requirements Planning Prompt (Explore Phase)

**Copy into Copilot Chat (Ask Mode):**

```
I want to add a tagging feature to our existing todo API -
allowing many-to-many relationships between todos and tags.

Before we write any code, help me think through:
1. What are the essential features vs nice-to-have?
2. What technical decisions need to be made upfront
   (schema design, queries)?
3. What are potential challenges I should consider
   (duplicate tags, case sensitivity)?
4. What's the simplest viable implementation?

Don't write code or create documents yet - just help me explore this idea.

think about this carefully
```

---

## 3️⃣ PRD Generation Prompt (Plan Phase)

**Copy into Copilot Chat (Agent Mode):**

```
Based on our planning discussion, create a Product Requirements Document (PRD)
for adding Tags to our existing Todo API.

Include:
1. Feature Overview (what we're adding and why)
2. Core Features (MVP only - detailed descriptions)
3. User Stories
4. Technical Requirements (schema, endpoints, many-to-many relationships)
5. Success Criteria
6. Out of Scope (what we're NOT building in v1)

Save as PRD-Tags.md in the project root.
```

### Using Your PRD During Development

**Reference it when implementing features:**

```
#file:PRD-Tags.md

Implement POST /api/v1/todos/{id}/tags endpoint following PRD requirements.

Include:
- Features from PRD Core Features section
- Technical requirements (many-to-many, case-insensitive)
- User authorization (only tag own todos)
- Error handling and validation
```

**PRD Best Practices:**
- ✅ Reference with #file:PRD-Tags.md when implementing features
- ✅ Use for code review validation
- ✅ Check scope before adding new features
- ✅ Update PRD as requirements evolve (living document!)

---

## 4️⃣ The 6-Element Prompt Framework

**Use what you need, not all elements every time!**

```
[PERSONA] ← Who should AI be? (optional for simple tasks)
"You're a senior FastAPI developer specializing in async APIs..."

[CONTEXT] ← What's the situation? (ALWAYS use)
What am I working on? What's the background? Use #mentions here.

[TASK] ← What needs to be done? (ALWAYS use)
Be specific. One clear objective.

[CONSTRAINTS] ← What are the rules? (use when needed)
- Must follow X
- Use Y pattern
- Include Z
- Avoid A

[FORMAT] ← What's the expected output? (use when needed)
Files to create/update, structure, format

[EXAMPLES] ← Show patterns to follow (use when patterns exist)
"Like #file:example.py lines X-Y..."
```

---

## 5️⃣ Advanced #mentions for [CONTEXT] Element

**Why these matter:**
The [CONTEXT] element is the most important part of your prompt.
These patterns make it powerful.

### File and Folder References
**Use in [CONTEXT] element:**
```
[CONTEXT] #folder:src/api/ shows all API endpoints
[TASK] Review for consistency in error handling
```

**Common patterns:**
```
#file:src/main.py           # Specific file
#folder:src/api/            # All files in folder
#folder:tests/              # All test files
#folder:src/                # All source files
```

### Combining #mentions
**Use in [CONTEXT] element:**
```
[CONTEXT] #folder:src/api/ shows existing patterns, #problems shows current errors
[TASK] Fix all errors in API folder while maintaining consistency
[CONSTRAINTS] Don't break existing tests
```

### #problems for Debugging
**Use in [CONTEXT] element:**
```
[CONTEXT] #problems shows current errors
[TASK] Fix all errors shown in the problems panel
```

**Other useful references:**
- `#terminalSelection` - Selected terminal output
- `@workspace` - Search entire workspace
- `#file:path#L10-L30` - Specific lines in a file

---

## 6️⃣ Prompt Examples by Complexity

### Simple Task (2 elements)
```
[CONTEXT] Python FastAPI project
[TASK] Create .gitignore file for venv/, .env, __pycache__
```

### Medium Task (4 elements)
```
[CONTEXT] #file:src/api/v1/todos.py has POST /todos endpoint
[TASK] Add validation to ensure title is 1-200 chars
[CONSTRAINTS] Return 400 with clear error message, don't break existing tests
[FORMAT] Update the endpoint function only
```

### Complex Task (ALL 6 elements)
```
[PERSONA] You're a senior SQLAlchemy developer specializing in complex relationships and FastAPI integration.

[CONTEXT] #folder:src/models/ has User and Todo models. #folder:src/api/v1/ shows existing routing patterns. #file:src/services/todo_service.py demonstrates service layer architecture. #file:PRD-Tags.md defines the tagging feature requirements.

[TASK] Add Tag model with many-to-many relationship to Todo, plus endpoints to add/remove tags

[CONSTRAINTS]
- Tag names unique, case-insensitive (auto-normalize to lowercase)
- Users only tag their own todos (verify ownership)
- POST /api/v1/todos/{id}/tags to add tag
- DELETE /api/v1/todos/{id}/tags/{tag_id} to remove
- Include tags in TodoResponse schema
- Follow 3-tier architecture (model→service→route)
- Use async/await patterns from #file:.github/copilot-instructions.md
- Follow requirements from #file:PRD-Tags.md

[FORMAT]
1. Migration file (alembic) for new tables
2. src/models/tag.py - Tag model + TodoTag association table
3. src/services/tag_service.py - business logic
4. src/api/v1/tags.py - route handlers
5. src/schemas/tag.py - Pydantic schemas
6. tests/api/test_tags.py - comprehensive tests

[EXAMPLES]
Look at #file:src/models/user.py lines 15-30 for relationship pattern example
Follow error handling from #file:src/api/v1/todos.py lines 45-60
```

---

## 7️⃣ GitHub Copilot Modes Quick Reference

| Mode | Keyboard | Best For |
|------|----------|----------|
| **Ask** | Open Chat | Exploration, questions, learning |
| **Edit** | Cmd+I | Quick inline changes |
| **Agent** | Chat dropdown | Multi-file features, building |
| **Plan** | /plan in chat | Complex implementation planning |

---

## 8️⃣ Session 2 #mentions Cheat Sheet

| Reference | Syntax | Use Case |
|-----------|--------|----------|
| Single file | `#file:path/file.py` | Specific file context |
| Folder | `#folder:path/` | All files in directory |
| Problems | `#problems` | Current IDE errors |
| Terminal | `#terminalSelection` | Terminal output |
| Workspace | `@workspace` | Search entire project |
| Line range | `#file:path.py#L10-L30` | Specific code section |

---

## 🏆 Session 2 Achievements

- [ ] 🧠 **Deep Thinker** - Used thinking modes
- [ ] 📋 **Strategic Planner** - Created a PRD
- [ ] 🎯 **Context Ninja** - Used advanced #mentions
- [ ] 🏆 **Context Master** - Completed Session 2
