# Instructor Guide: Micro Session 2
## Context Mastery & Project Planning 🎯📋

**Duration:** 30 minutes (Minutes 0:33-1:03)
**Goal:** Transform students from tool users into AI strategy professionals

---

## Session Flow Overview

| Time | Section | Focus |
|------|---------|-------|
| 0:00-0:03 | Thinking Modes | Extended reasoning capabilities |
| 0:03-0:10 | Planning Workflow | Explore → Plan → Code with PRDs |
| 0:10-0:17 | 6-Element Framework | Professional prompting toolbox |
| 0:17-0:23 | Advanced #mentions | Context patterns for [CONTEXT] element |
| 0:23-0:27 | Framework Practice | Apply 6-element framework |
| 0:27-0:30 | Toolkit Review | Complete mental model |

---

## Key Teaching Objectives

By end of session, students will:
1. ✅ Understand thinking modes for extended reasoning
2. ✅ Use Explore → Plan → Code workflow
3. ✅ Create and reference PRDs in development
4. ✅ Apply 6-element framework (scaled by complexity)
5. ✅ Use advanced #mention patterns

---

## Pre-Session Checklist

- [ ] Students have completed Session 1
- [ ] Copilot Chat panel visible
- [ ] PRD-Tags.md ready for demo (create during session)
- [ ] Browser open for quick context if needed
- [ ] Prompt Sheet Session 2 distributed

---

## 🧠 SESSION 2 SCRIPT

### [0:00-0:03] Thinking Modes Introduction

**ENERGY:** Engaged, building momentum

**SAY:**
> "Welcome to Session 2! You mastered the tools in Session 1. Now you'll learn to use them like a PROFESSIONAL.
>
> First - a powerful technique for complex decisions: THINKING MODES.
>
> These are NOT GitHub Copilot features - they're LLM MODEL features. The AI models that power Copilot understand these keywords."

**SHOW ON SCREEN:**
```
THINKING MODES - Extended Reasoning Keywords

"think"         → Basic extended thinking (~5-10 sec)
"think hard"    → Thorough analysis (~10-20 sec)
"think harder"  → Deep evaluation (~20-30 sec)
"ultrathink"    → Maximum thinking budget (~30+ sec)

💡 These are MODEL features, not tool features
💡 Same credits, just more compute time
💡 Worth it for architecture decisions & complex planning
```

**SAY:**
> "When you add 'think hard' to a prompt, you're telling the AI to take MORE TIME before responding.
>
> Normal response = instant.
> 'think hard' = AI takes 15-20 seconds to really analyze.
>
> **Use these for:** Architecture decisions, complex planning, trade-off analysis.
>
> **Skip for:** Simple tasks like file creation or basic edits."

**DEMO: Quick Thinking Mode Example**

**SAY:**
> "Let me show you the difference."

**Without thinking mode:**
```
What's the best database for a todo app?
```

**Response:** Quick, surface-level answer

**With thinking mode:**
```
think hard about the best database for a todo app.
Consider: scale, complexity, team skills, hosting costs.
```

**Response:** [Takes 15 seconds] Detailed analysis with trade-offs, multiple options compared, clear reasoning.

**SAY:**
> "See the difference? The second response analyzes trade-offs, compares options, and shows reasoning.
>
> Same cost. More thinking time. Better decisions."

🏆 **MICRO-ACHIEVEMENT:** "Deep Thinker" (earned by understanding thinking modes)

---

### [0:03-0:10] Professional Planning Workflow

**ENERGY:** Strategic, professional

---

#### [0:03-0:05] The Explore → Plan → Code Workflow (2 min)

**SAY:**
> "Now for the PROFESSIONAL workflow. This is what separates AI amateurs from AI professionals.
>
> Most developers do this: IDEA → CODE → PROBLEMS → FIX → MORE PROBLEMS
>
> Professionals do this: EXPLORE → PLAN → CODE
>
> Three phases. Let me show you each one."

**SHOW ON SCREEN:**
```
PROFESSIONAL AI WORKFLOW

Phase 1: EXPLORE (Chat Mode)
→ Think WITH AI before coding
→ Use "think" keywords for analysis
→ Identify challenges early

Phase 2: PLAN (Document)
→ Create PRD (Product Requirements Document)
→ Define scope, constraints, success criteria
→ This becomes your AI context reference

Phase 3: CODE (Agent Mode)
→ Reference your PRD
→ Use structured prompts
→ AI has full context from planning
```

**SAY:**
> "Today you'll learn Phases 1 and 2. In Sessions 3-4, you'll do Phase 3 - actually building features from your PRD."

---

#### [0:05-0:07] Phase 1: EXPLORE Demo (2 min)

**SAY:**
> "Let's add a TAGS feature to our todo API. Many-to-many relationship.
>
> Amateur approach: Jump into code mode, start coding.
>
> Professional approach: EXPLORE first. Think with AI.
>
> Watch me use Ask Mode - I'm NOT asking for code. I'm asking for THINKING."

**OPEN COPILOT CHAT (Ask Mode)** and type:

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

**WAIT for response, then highlight key insights:**

**SAY:**
> "Look at what we got! We didn't write ANY code, but we:
> - Identified essential vs nice-to-have features
> - Surfaced technical decisions (schema design)
> - Found challenges we'd have missed (case sensitivity!)
> - Have a clear scope for MVP
>
> This 2-minute conversation just saved us hours of rework.
>
> Now watch how we CAPTURE this in Phase 2."

---

#### [0:07-0:09] Phase 2: PLAN with PRD (2 min)

**SAY:**
> "Now we document our plan. This creates a REFERENCE that AI can use during coding."

**SWITCH TO Agent Mode:**

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

**SHOW the generated PRD-Tags.md:**

```markdown
# PRD-Tags.md - Tagging Feature for Todo API

## 1. Feature Overview
Add tagging functionality to our todo API to enable categorization
and filtering of todos by user-defined tags.

## 2. Core Features (MVP)
1. Create Tags - Tag name (required, unique per user, case-insensitive)
2. Add/Remove Tags from Todos - POST/DELETE endpoints
3. List Todos by Tag - GET /api/v1/todos?tag={tag_name}
4. View Tags on Todo - Include tags in TodoResponse

## 3. User Stories
- As a user, I want to tag todos to organize by category
- As a user, I want to filter todos by tag
- As a user, I want tags to be case-insensitive

## 4. Technical Requirements
### Schema
- Tag model: id, name, user_id, created_at
- TodoTag association table: todo_id, tag_id

### API Endpoints
- POST /api/v1/todos/{todo_id}/tags - Add tag to todo
- DELETE /api/v1/todos/{todo_id}/tags/{tag_id} - Remove tag from todo
- GET /api/v1/tags - List user's tags with counts
- GET /api/v1/todos?tag={tag_name} - Filter todos by tag

### Technical Stack
- SQLAlchemy async relationships
- Eager loading to prevent N+1 queries
- FastAPI validation with Pydantic schemas

## 5. Success Criteria
- Users can create and assign tags
- Filtering by tag works correctly
- Case-insensitive tag names ("Work" = "work")
- No duplicate tags per user
- Response time < 200ms for tag operations

## 6. Out of Scope (NOT Building)
- Tag colors or icons
- Sharing tags between users
- Tag hierarchies or nested tags
- Tag suggestions/autocomplete
- Bulk tag operations
```

**SAY:**
> "Perfect! We have a clear plan for the Tags feature.
>
> **The workflow so far:**
> - ✅ Phase 1: EXPLORE (thinking with AI)
> - ✅ Phase 2: PLAN (documented in PRD)
> - ⏭️ Phase 3: CODE (we'll learn prompting techniques next)
>
> You just learned professional planning with AI!"

---

#### [0:09-0:10] Using Your PRD in Development (1 min)

**SAY:**
> "Great! We have a PRD for Tags. But here's the power move: REFERENCE it when building features.
>
> This keeps AI aligned with your requirements throughout development."

**SHOW EXAMPLE on screen:**
```
#file:PRD-Tags.md

Implement POST /api/v1/todos/{todo_id}/tags endpoint following PRD requirements.

Include:
- Tag schema per PRD (case-insensitive, user-specific)
- Many-to-many relationship per PRD technical requirements
- Authentication required
- Error handling per PRD success criteria
```

**SAY:**
> "See that #file:PRD-Tags.md? Now AI has full context about our tags feature requirements, tech stack, and constraints.
>
> **Three ways to use your PRD:**
>
> 1. **During Implementation** - Reference it with #file:PRD-Tags.md in prompts (Session 3-4)
> 2. **Code Review** - Ask: 'Does this match PRD requirements?'
> 3. **Scope Control** - Check features against PRD before building
>
> You'll see this in action when you build features in Session 3!"

**SHOW ON SCREEN:**
```
PRD BEST PRACTICES:

✅ Reference with #file:PRD-[feature].md when implementing features
✅ Use for code review validation
✅ Check scope before adding new features
✅ Update PRD as requirements evolve (living document!)
```

🏆 **MICRO-ACHIEVEMENT:** "Strategic Planner" (earned by watching professional workflow)

---

### [0:10-0:17] 🎯 Phase 3: CODE - The 6-Element Framework

**ENERGY:** Teaching, focused

**SAY:**
> "This is how you write prompts that BUILD features.
>
> You can give AI context 10 different ways. But there's ONE framework that consistently works best.
>
> The 6-element framework professionals use. Here's the key:
>
> **It's NOT a checklist. It's a TOOLBOX.**
>
> Simple task? Use 2-3 elements.
> Complex task? Use 4-6 elements.
>
> Master this = massive productivity gains.
>
> **Note:** We're learning the CONCEPTS today. You'll USE this framework in Session 3 to actually build features!"

---

#### [0:10-0:13] The 6-Element Framework (3 min)

**SHOW ON SCREEN:**
```
THE PROFESSIONAL PROMPT FRAMEWORK
(Use what you need, not all you have!)

1. [PERSONA] ← Who should AI be?
   "You're a senior FastAPI developer specializing in async APIs..."
   Use when: Complex domain knowledge needed
   Skip when: Simple tasks, file operations

2. [CONTEXT] ← What's the situation?
   What am I working on? What's the background?
   Use #mentions here.
   Use when: ALWAYS (most important!)

3. [TASK] ← What needs to be done?
   Be specific. One clear objective.
   Use when: ALWAYS

4. [CONSTRAINTS] ← What are the rules?
   - Must follow X
   - Use Y pattern
   - Include Z
   - Avoid A
   Use when: Specific requirements exist
   Skip when: Task is self-explanatory

5. [FORMAT] ← What's the expected output?
   Files to create/update, structure, format
   Use when: Output structure matters
   Skip when: Format is obvious

6. [EXAMPLES] ← Show patterns to follow
   "Like #file:example.py lines X-Y..."
   Use when: Project-specific patterns exist
   Skip when: Standard patterns sufficient
```

**DECISION GUIDE:**
```
Simple task (config, file creation):
→ Use: Context + Task
→ Skip: Persona, Examples

Medium task (single feature):
→ Use: Context + Task + Constraints + Format
→ Skip: Persona, Examples (optional)

Complex task (multi-part feature):
→ Use: Context + Task + Constraints + Format + Persona
→ Maybe: Examples (if patterns exist)

Very Complex (architecture, many-to-many):
→ Use: ALL 6 elements!
```

---

#### [0:13-0:16] Framework Scaling Examples (3 min)

**SAY:**
> "Let me show you three examples - watch how we SCALE the framework based on complexity."

**EXAMPLE 1: SIMPLE TASK** (2 elements)
```
Task: Create .gitignore file

[CONTEXT] Python FastAPI project
[TASK] Create .gitignore file for venv/, .env, __pycache__

✅ That's it! Context + Task is enough.
NO NEED for Persona (simple file), Constraints (clear), Format (obvious), Examples.
```

**SAY:**
> "Simple task. 2 elements. Done!"

**EXAMPLE 2: MEDIUM TASK** (4 elements)
```
Task: Add validation to existing endpoint

[CONTEXT] #file:src/api/v1/todos.py has POST /todos endpoint
[TASK] Add validation to ensure title is 1-200 chars
[CONSTRAINTS] Return 400 with clear error message, don't break existing tests
[FORMAT] Update the endpoint function only

✅ 4 elements - right amount!
SKIPPED: Persona (validation is straightforward), Examples (standard pattern)
```

**SAY:**
> "Medium complexity. Added Constraints and Format. Still skipped Persona and Examples - don't need them!"

**EXAMPLE 3: COMPLEX TASK** (ALL 6 elements)
```
Task: Implement many-to-many tagging feature

[PERSONA] You're a senior SQLAlchemy developer specializing in complex relationships and FastAPI integration.

[CONTEXT] #folder:src/models/ has User and Todo models. #folder:src/api/v1/ shows existing routing patterns. #file:src/services/todo_service.py demonstrates service layer architecture.

[TASK] Add Tag model with many-to-many relationship to Todo, plus endpoints to add/remove tags

[CONSTRAINTS]
- Tag names unique, case-insensitive
- Users only tag their own todos
- POST /api/v1/todos/{id}/tags to add tag
- DELETE /api/v1/todos/{id}/tags/{tag_id} to remove
- Include tags in TodoResponse schema
- Follow 3-tier architecture (model→service→route)
- Use async/await patterns from #file:.github/copilot-instructions.md

[FORMAT]
1. Migration file (alembic) for new tables
2. src/models/tag.py - Tag model + association table
3. src/services/tag_service.py - business logic
4. src/api/v1/tags.py - route handlers
5. src/schemas/tag.py - Pydantic schemas
6. tests/api/test_tags.py - comprehensive tests

[EXAMPLES]
Look at #file:src/models/user.py lines 15-30 for relationship pattern example
Follow error handling from #file:src/api/v1/todos.py lines 45-60

✅ ALL 6 elements - complex task demands it!
```

**SAY:**
> "See the pattern?
>
> - Example 1: SIMPLE = 2 elements
> - Example 2: MEDIUM = 4 elements  
> - Example 3: COMPLEX = ALL 6 elements
>
> **This is how professionals think.**
>
> Notice the [CONTEXT] element in each? That's THE most important element.
> Now let me show you how to make it POWERFUL."

---

### [0:17-0:23] ⚡ Advanced #mentions for [CONTEXT] Element

**ENERGY:** Practical, hands-on

---

#### [0:17-0:21] Advanced #mention Patterns (4 min)

**SAY:**
> "The [CONTEXT] element is the foundation of every prompt.
> 
> In Session 1, you learned basic #mentions (#file, #folder).
> 
> Now I'll show you ADVANCED patterns:
> - Glob patterns (multiple files at once)
> - Combining #mentions (layered context)
> - #problems (debugging)
>
> Watch how these fit INTO the [CONTEXT] element of your prompts."

**TEACH each pattern with examples:**

**1. Glob Patterns (1.5 min)**

**SAY:**
> "Instead of adding files one by one, you can reference patterns of files."

**SHOW EXAMPLE IN PROMPT:**
```
[CONTEXT] #folder:src/api/ shows all API endpoints
[TASK] Review for consistency in error handling
```

**Common patterns:**
```
#folder:src/api/          ← All files in src/api/
#folder:tests/            ← All test files
#folder:src/              ← All files in src/ and subdirs
```

**SAY:**
> "See? Folder reference in [CONTEXT] = AI sees all relevant files at once."

**2. Combining #mentions (1.5 min)**

**SAY:**
> "The power move: Layer multiple #mentions in [CONTEXT]."

**SHOW EXAMPLE IN PROMPT:**
```
[CONTEXT] #folder:src/api/ shows existing patterns, #problems shows current errors
[TASK] Fix all errors in API folder while maintaining consistency
[CONSTRAINTS] Don't break existing tests
```

**SAY:**
> "See that? Two #mentions in [CONTEXT]:
> - #folder:src/api/ = what patterns to follow
> - #problems = what's broken
>
> AI gets the complete picture."

**3. #problems for Debugging (1 min)**

**SAY:**
> "#problems gives AI your current IDE errors."

**SHOW EXAMPLE IN PROMPT:**
```
[CONTEXT] #problems shows current errors
[TASK] Fix all errors shown in the problems panel
```

**SAY:**
> "Remember #terminalSelection and @workspace from Session 1? Same idea - special references for specific context."

🏆 **MICRO-ACHIEVEMENT:** "Context Ninja"

---

### [0:23-0:27] Framework Practice

**ENERGY:** Applied, practical

---

#### [0:23-0:25] Student Practice: Prompt Transformation (2 min)

**SAY:**
> "Quick challenge! Transform this weak prompt into a strong one:
>
> **Weak:** 'create an update endpoint'
>
> Use the framework: Which elements do you need? Simple, medium, or complex task?
> 30 seconds in your head - what would you add?"

**TIMER:** 30 seconds

**AT 0:30 - CALL ON SOMEONE:**
> "What would you add for context? ...constraints? ...format?"

**SHOW ANSWER:**
```
✅ Strong version:
[Context] #folder:src/api/ #file:src/models/todo.py
[Task] Create PUT /api/v1/todos/{id} endpoint
[Constraints]
- async, auth required, validate input
- Only allow owner to update their todos
- Handle not found (404) and unauthorized (403)
[Format]
- Update src/api/v1/routes/todos.py
- Add TodoUpdate schema to src/schemas/todo.py
- Add update method to src/services/todo_service.py
- Add tests to tests/api/test_todos.py
```

---

#### [0:25-0:27] Real-World Application (2 min)

**SAY:**
> "Let's see this in Copilot! I'll show you a complete prompt using the framework."

**DEMO in Copilot Chat (Agent Mode):**

```
[CONTEXT] #folder:src/api/v1/ shows current endpoint patterns. #file:src/models/todo.py defines the Todo model. #file:src/services/todo_service.py shows service layer patterns.

[TASK] Create PUT /api/v1/todos/{id} endpoint to update an existing todo

[CONSTRAINTS]
- Require authentication (get_current_user dependency)
- Only allow owner to update their todos (403 if not owner)
- Handle todo not found (404)
- Validate input with Pydantic schema
- Follow existing async patterns

[FORMAT]
- Update src/api/v1/todos.py with new endpoint
- Create TodoUpdate schema in src/schemas/todo.py if needed
- Add update method to TodoService
```

**SAY:**
> "Watch how Copilot creates EXACTLY what we asked for - following our existing patterns because we gave proper context!"

---

### [0:27-0:30] 🧰 Session 2 Toolkit Summary

**ENERGY:** Consolidating, empowering

**SAY:**
> "Let me show you the complete picture of what you've learned today."

**SHOW ON SCREEN:**
```
SESSION 2 COMPLETE TOOLKIT

🧠 THINKING MODES
├── "think" → Basic extended reasoning
├── "think hard" → Thorough analysis
├── "think harder" → Deep evaluation
└── "ultrathink" → Maximum thinking

📋 PROFESSIONAL WORKFLOW
├── Phase 1: EXPLORE → Think with AI (Ask Mode)
├── Phase 2: PLAN → Document in PRD
└── Phase 3: CODE → Build with framework

🎯 6-ELEMENT FRAMEWORK (Toolbox!)
├── [PERSONA] → Who should AI be?
├── [CONTEXT] → #mentions, references (ALWAYS!)
├── [TASK] → What to do (ALWAYS!)
├── [CONSTRAINTS] → Rules and requirements
├── [FORMAT] → Expected output structure
└── [EXAMPLES] → Patterns to follow

⚡ ADVANCED #MENTIONS
├── #folder:path/ → All files in folder
├── #file:path → Specific file
├── #problems → IDE errors/warnings
├── #terminalSelection → Terminal output
└── @workspace → Search entire workspace
```

**SAY:**
> "You now have PROFESSIONAL-LEVEL context skills!
>
> Session 3 Preview: You'll USE these skills to actually BUILD features - TDD style!"

---

## 🏆 Session 2 Achievements

| Achievement | Earned By |
|-------------|-----------|
| 🧠 Deep Thinker | Understanding thinking modes |
| 📋 Strategic Planner | Watching Explore → Plan → Code workflow |
| 🎯 Context Ninja | Mastering advanced #mention patterns |
| 🏆 Context Master | Completing Session 2 |

---

## Instructor Notes

### Common Student Questions

**Q: "Do thinking modes cost more?"**
A: No! Same credits, just more compute time. Worth it for important decisions.

**Q: "When do I use all 6 elements?"**
A: Complex, multi-file tasks. Simple tasks only need 2-3 elements. Match complexity!

**Q: "What's the difference between Ask and Agent mode for planning?"**
A: Ask for exploration (no file changes). Agent for creating documents like PRDs.

### Session Transition

**Before Session 3:**
- Ensure students have created PRD-Tags.md
- Students should understand the 6-element framework
- Verify Copilot is working in Agent mode
- Preview: "Next session, you'll BUILD features using TDD!"
