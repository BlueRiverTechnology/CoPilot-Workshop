# Student Packet: Micro Session 2
## Context Mastery & Project Planning 🎯📋

**Name:** _________________________  
**Date:** _________________________  
**Achievement Goal:** 🏆 "Context Master"

---

## Learning Objectives

- [ ] Use thinking modes for extended reasoning
- [ ] Apply Explore → Plan → Code workflow
- [ ] Create and reference PRDs (Product Requirements Documents)
- [ ] Master the 6-element professional prompt framework
- [ ] Use advanced #mention patterns for context

---

## 🔄 Important: Project Transition

**Session 1 Recap:** You built a PRACTICE project to learn Agent Mode and mentions. That was temporary learning material.

**Starting Session 2:** We're switching to the REAL workshop project!

### Action Required Before Starting:
1. ✅ Close any files from Session 1 practice project
2. ✅ Open the `copilot-workshop-student` folder in VS Code (if not already open)
3. ✅ Verify you see these folders:
   - `src/` (with models/, schemas/, services/, api/)
   - `tests/` (for pytest)
   - `session-1/`, `session-2/`, `session-3/`, `session-4/`
   - `PRD.md` at the root
4. ✅ The Session 1 practice project can be deleted or ignored - we won't use it again

**This is your workshop project folder for Sessions 2, 3, and 4!**

---

## From Session 1 to Session 2

**Session 1 - You learned the TOOLS:**
- ✅ 4 Copilot modes (Ask, Edit, Agent, Plan)
- ✅ #mentions for context
- ✅ Custom Instructions for standards
- ✅ Security setup with .copilotignore
- ✅ Built a PRACTICE project (throwaway)

**Session 2 - You learn to USE those tools like a PRO:**
- Working with the PRE-BUILT todo app in `/src` and `/tests`
- This is DIFFERENT from your Session 1 practice project!

---

## The Context Principle

**The Foundation:**
AI is only as smart as the context you give it.

**Bad context:**
```
"create a todo endpoint"
```
→ AI asks 10 questions
→ Multiple revisions needed
→ 15 minutes, many credits

**Good context:**
```
[Context] #folder:src/ shows existing patterns
[Task] Create POST /todos endpoint
[Constraints] async, auth required, error handling
[Format] route + service + test
```
→ AI nails it first try
→ 3 minutes, minimal credits

**Today:** Master giving AI PERFECT context!

---

## 🧠 Thinking Modes - Extended Reasoning

**What they are:**
Keywords that give AI more time to think through complex problems.

**💡 Important:** These are LLM MODEL features, not Copilot-specific. The AI models understand these keywords.

**The modes:**
```
normal          → Instant response
"think"         → +5-10 seconds (basic)
"think hard"    → +10-20 seconds (thorough)
"think harder"  → +20-30 seconds (deep)
"ultrathink"    → +30+ seconds (maximum)
```

**When to use:** Architecture decisions, complex planning, trade-off analysis

**Cost:** Same credits, just more compute time

**I'll use this for:**
_____________________________________________________________________

---

## 🧠 Requirements Planning with Chat Mode

### The Explore Phase

**My exploration prompt:**
```
I want to add a tagging feature to our existing todo API -
allowing many-to-many relationships between todos and tags.

Before we write code, help me think through:
1. What are essential features vs nice-to-have?
2. What technical decisions need to be made upfront
   (schema design, queries)?
3. What challenges should I consider (duplicate tags,
   case sensitivity)?
4. What's the simplest viable implementation?

Don't write code yet - just help me explore this idea.

think about this carefully
```

**Key insights from AI:**
_____________________________________________________________________
_____________________________________________________________________

**Why "think" helps:**
_____________________________________________________________________

---

### The Plan Phase - PRD

**Created:** [ ] PRD-Tags.md

**Core features we're building (Tags for Todo API):**
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________

**Out of scope (NOT building):**
_________________________________________________________________

**How I'll use my PRD:**
- [ ] Reference with #file:PRD-Tags.md when implementing features
- [ ] Use for code review validation
- [ ] Check scope before adding new features
- [ ] Update as requirements evolve

---

🏆 **Achievement:** [ ] "Strategic Planner" (earned by watching professional workflow)

---

## 🎯 The Professional Prompt Framework

### The 6-Element Toolbox

**KEY INSIGHT:** It's NOT a checklist - it's a TOOLBOX!
Use what you need, not all you have.

```
1. [PERSONA] Who should AI be?
   Use when: Complex domain knowledge needed
   Skip when: Simple tasks

2. [CONTEXT] What's the situation?
   Use #mentions here
   Use when: ALWAYS (most important!)

3. [TASK] What needs to be done?
   Use when: ALWAYS

4. [CONSTRAINTS] What are the rules?
   Use when: Specific requirements exist
   Skip when: Task is self-explanatory

5. [FORMAT] Expected output structure
   Use when: Output structure matters
   Skip when: Format is obvious

6. [EXAMPLES] Show patterns to follow
   Use when: Project-specific patterns exist
   Skip when: Standard patterns sufficient
```

### Decision Guide

**Simple Task** (file creation, config):
→ Use: **Context + Task** (2 elements)

**Medium Task** (single feature):
→ Use: **Context + Task + Constraints + Format** (4 elements)

**Complex Task** (multi-part feature):
→ Use: **Context + Task + Constraints + Format + Persona** (5 elements)

**Very Complex** (architecture, many-to-many):
→ Use: **ALL 6 elements**

---

### Scaling Examples

**SIMPLE (2 elements):**
```
[CONTEXT] Python FastAPI project
[TASK] Create .gitignore for venv/, .env, __pycache__

✅ Done! No need for Persona, Constraints, Format, Examples
```

**MEDIUM (4 elements):**
```
[CONTEXT] #file:src/api/v1/todos.py has POST /todos endpoint
[TASK] Add validation for title length 1-200 chars
[CONSTRAINTS] Return 400 with clear message, don't break tests
[FORMAT] Update endpoint function only

✅ Right amount! Skipped Persona and Examples - don't need them
```

**COMPLEX (ALL 6):**
```
[PERSONA] Senior SQLAlchemy developer specializing in relationships

[CONTEXT] #folder:src/models/ has User, Todo models
#folder:src/api/v1/ shows routing patterns
#file:PRD-Tags.md defines the tagging feature requirements

[TASK] Add Tag model with many-to-many to Todo + endpoints

[CONSTRAINTS]
- Tag names unique, case-insensitive
- Users only tag their own todos
- POST /api/v1/todos/{id}/tags to add
- DELETE to remove
- 3-tier architecture
- Follow requirements from #file:PRD-Tags.md

[FORMAT]
1. Migration file
2. src/models/tag.py
3. src/services/tag_service.py
4. src/api/v1/tags.py
5. tests/api/test_tags.py

[EXAMPLES]
#file:src/models/user.py lines 15-30 for relationship pattern
#file:src/api/v1/todos.py lines 45-60 for error handling

✅ ALL 6 - complex task demands it!
```

---

## ⚡ Advanced #mentions for [CONTEXT] Element

**What I learned:**
The [CONTEXT] element is the most important part of prompts.
These patterns make it powerful.

### File and Folder References
**Use in [CONTEXT] element:**
```
[CONTEXT] #folder:src/api/ shows all API endpoints
[TASK] Review for consistency in error handling
```

**Common patterns:**
```
#file:src/main.py          # Specific file
#folder:src/api/           # All files in folder  
#folder:tests/             # All test files
#folder:src/               # All source files
```

**Example I tried:**
_____________________________________________________________________

---

### Combining #mentions
**Use in [CONTEXT] element:**
```
[CONTEXT] #folder:src/api/ shows existing patterns, #problems shows current errors
[TASK] Fix all errors in API folder while maintaining consistency
[CONSTRAINTS] Don't break existing tests
```

**Example I tried:**
_____________________________________________________________________

---

### #problems for Debugging
**Use in [CONTEXT] element:**
```
[CONTEXT] #problems shows current errors
[TASK] Fix all errors shown in the problems panel
```

**Other useful references:**
- `#terminalSelection` - Selected terminal output
- `@workspace` - Search entire workspace
- `#file:path.py#L10-L30` - Specific lines

**Most useful pattern for me:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Context Ninja"

---

## Complete Example: Framework + Advanced #mentions

**Putting it all together:**

```
[PERSONA] Senior FastAPI developer with SQLAlchemy expertise

[CONTEXT]
#folder:src/models/ shows existing data models
#folder:src/api/v1/ shows current endpoint patterns
#file:src/services/todo_service.py demonstrates service layer
#file:PRD-Tags.md contains feature requirements
#problems shows any current errors

[TASK] Implement the Tag feature according to PRD-Tags.md

[CONSTRAINTS]
- Follow existing patterns in codebase
- Use async/await throughout
- Include comprehensive error handling
- Write tests for all new endpoints
- Don't break existing functionality

[FORMAT]
1. New model file: src/models/tag.py
2. New service file: src/services/tag_service.py  
3. New routes file: src/api/v1/tags.py
4. New schemas file: src/schemas/tag.py
5. Test file: tests/api/test_tags.py

[EXAMPLES]
#file:src/models/user.py for model patterns
#file:src/api/v1/todos.py for route patterns
```

**Why this works:**
- [PERSONA] → Expert context for complex task
- [CONTEXT] → Multiple #mentions give full picture
- [TASK] → Clear objective
- [CONSTRAINTS] → Specific rules
- [FORMAT] → Exact deliverables
- [EXAMPLES] → Patterns to follow

---

## GitHub Copilot Modes for Session 2

| Mode | Shortcut | Session 2 Use |
|------|----------|---------------|
| **Ask** | Open Chat | Explore ideas, thinking |
| **Edit** | Cmd+I | Quick fixes |
| **Agent** | Chat dropdown | Create PRD, build features |
| **Plan** | /plan | Complex planning |

**My most-used mode today:**
_____________________________________________________________________

---

## Session 2 Reflection

**The Context Principle in my words:**
_____________________________________________________________________
_____________________________________________________________________

**My most useful technique learned:**
_____________________________________________________________________

**How I'll use PRDs in my work:**
_____________________________________________________________________

**Framework elements I'll use most:**
_____________________________________________________________________

---

## 🏆 Session 2 Achievements Checklist

- [ ] 🧠 **Deep Thinker** - Used thinking modes for complex analysis
- [ ] 📋 **Strategic Planner** - Created PRD-Tags.md  
- [ ] 🎯 **Context Ninja** - Used advanced #mention patterns
- [ ] 🏆 **Context Master** - Completed Session 2

**Total Achievements Earned:** _____ / 4

---

## Looking Ahead: Session 3 Preview

**What's next:**
- Phase 3: CODE - Actually build features from your PRD
- Test-Driven Development (TDD) with Copilot
- Using Plan mode for implementation strategy
- Building the Tags feature

**Preparation:**
- [ ] PRD-Tags.md created and saved
- [ ] Understand 6-element framework
- [ ] Familiar with #mention patterns
- [ ] Ready to write code!

---

## Quick Reference Card

### Thinking Modes
```
think → think hard → think harder → ultrathink
(basic)   (thorough)   (deep)      (maximum)
```

### 6-Element Framework
```
[PERSONA] + [CONTEXT] + [TASK] + [CONSTRAINTS] + [FORMAT] + [EXAMPLES]
           ↑ Always!    ↑ Always!
```

### #mentions
```
#file:path.py        → Single file
#folder:path/        → All files in folder
#problems            → IDE errors
#terminalSelection   → Terminal output
@workspace           → Search all
```

### Professional Workflow
```
EXPLORE (Ask Mode) → PLAN (PRD) → CODE (Agent Mode)
```
