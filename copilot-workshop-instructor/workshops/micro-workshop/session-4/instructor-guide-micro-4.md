# Instructor Guide: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Duration:** 33 minutes  
**Achievement:** 🏆 "Copilot Champion"  
**Prerequisites:** Sessions 1-3 completed

---

## Session Overview

### Learning Objectives
- ✅ Use Copilot Code Review for PR feedback
- ✅ Create Custom Agents (.agent.md files)
- ✅ Understand the 70% Problem and your critical 30%
- ✅ Complete Boss Fight using ALL techniques from Sessions 1-3
- ✅ Earn Power User Certification

---

## Teaching Script

### [0:00-0:02] HOOK - The Final Challenge

**ENERGY:** Epic finale energy

**SAY:**
> "Welcome to the finale! 🎮
>
> So far you've learned:
> - Security, all AI modes, and #mentions ✅
> - Context mastery & project planning ✅
> - Built 3 features with TDD and Subagents ✅
>
> Today: The ultimate test.
>
> **In 33 minutes:**
> - Master Copilot Code Review
> - Create Custom Agents
> - Understand where YOU add value (The 70/30 Problem)
> - **BOSS FIGHT:** Build complex many-to-many feature using EVERYTHING
>
> Pass the Boss Fight = Power User Certified! 🏆
>
> Let's finish strong! 💪"

**CHECKPOINT:** Everyone pumped for the finale?

---

### [0:02-0:08] 🔍 Copilot Code Review (6 min)

**ENERGY:** Professional, quality-focused

**SAY:**
> "GitHub Copilot has a powerful Code Review feature!
>
> When you create a Pull Request on GitHub, Copilot can:
> - Automatically review your code
> - Suggest improvements
> - Find bugs and security issues
> - Ensure consistency with your codebase
>
> Let me show you how it works..."

---

#### [0:02-0:05] Understanding Copilot Code Review (3 min)

**SHOW ON SCREEN:**
```
COPILOT CODE REVIEW

Where: GitHub.com Pull Requests
How: Request review from "Copilot"

What it checks:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns

Output:
- Inline comments on specific lines
- Suggestions for improvements
- Identification of issues
```

**SAY:**
> "To use Copilot Code Review:
>
> 1. Create a Pull Request on GitHub
> 2. Request review from 'copilot' as a reviewer
> 3. Copilot analyzes your changes
> 4. You get inline comments and suggestions
>
> It's like having a tireless code reviewer on every PR!"

---

#### [0:05-0:08] In-Editor Review with Chat (3 min)

**SAY:**
> "You can also use Copilot Chat for code review directly in your editor!"

**DO - Demonstrate in Copilot Chat:**

```
Review my recent changes in #file:src/api/v1/todos.py.

Check for:
1. Security issues (auth, validation)
2. Error handling completeness
3. Performance concerns
4. Best practice violations

Be thorough and critical.
```

**SAY:**
> "This gives you the same rigorous review without creating a PR.
>
> Use this for:
> - Self-review before committing
> - Quick sanity check on changes
> - Learning from AI feedback"

🏆 **ACHIEVEMENT:** "Review Master"

---

### [0:08-0:14] 🤖 Custom Agents (.agent.md) (6 min)

**ENERGY:** Power-user excitement

**SAY:**
> "Now for a Copilot POWER feature: Custom Agents!
>
> You can create specialized AI agents that know your project's specific context, patterns, and requirements."

---

#### [0:08-0:11] What Are Custom Agents? (3 min)

**SHOW ON SCREEN:**
```
CUSTOM AGENTS (.agent.md files)

Location: .github/agents/*.agent.md

What they do:
- Define specialized AI personas
- Include project-specific knowledge
- Set constraints and patterns
- Reusable across conversations

Examples:
- FastAPI Expert Agent
- Testing Specialist Agent
- Security Review Agent
```

**SAY:**
> "Think of Custom Agents as pre-configured AI specialists for your project.
>
> Instead of explaining your project every time, the agent KNOWS:
> - Your architecture patterns
> - Your coding standards
> - Your common tasks"

---

#### [0:11-0:14] Creating a Custom Agent (3 min)

**DO - Create agent file:**

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

**SAY:**
> "Now when you reference this agent, Copilot has ALL this context automatically!
>
> You can invoke it by referencing the file or using the agent in your prompts."

**SHOW usage example:**
```
Using #file:.github/agents/todo-api.agent.md context:

Add a DELETE /api/v1/todos/{id} endpoint that:
- Requires authentication
- Checks ownership
- Returns 204 on success, 404/403 on errors
```

**SAY:**
> "The agent KNOWS your patterns. Less explaining, better results!"

🏆 **ACHIEVEMENT:** "Agent Creator"

---

### [0:14-0:20] 🧠 Memory Bank - Persistent Project Context (6 min)

**ENERGY:** Mind-blown, "this changes everything"

**SAY:**
> "Custom Agents are powerful. But here's the problem:
>
> Every time you start a new Copilot chat session... it FORGETS everything.
>
> Your architecture decisions? Gone.
> What you worked on yesterday? Gone.
> What you decided about the database? Gone.
>
> **The Memory Bank solves this.**
>
> It gives Copilot a structured set of markdown files to read at the start of every conversation — so it always knows your project."

---

#### [0:14-0:16] Why Memory Bank Matters (2 min)

**SHOW ON SCREEN:**
```
THE PROBLEM:
┌──────────────────────────────────────┐
│  Monday: "We use FastAPI with async" │
│  Tuesday: "Remember, we use FastAPI" │
│  Wednesday: "I told you, FastAPI..." │
│  Thursday: "...FastAPI. AGAIN."      │
└──────────────────────────────────────┘

THE SOLUTION: Memory Bank
┌──────────────────────────────────────┐
│  memory-bank/                        │
│  ├── projectbrief.md     (goals)     │
│  ├── productContext.md   (the why)   │
│  ├── techContext.md      (stack)     │
│  ├── systemPatterns.md   (patterns)  │
│  ├── activeContext.md    (right now) │
│  └── progress.md         (status)   │
│                                      │
│  Copilot reads these EVERY session   │
└──────────────────────────────────────┘
```

**SAY:**
> "The Memory Bank is a `memory-bank/` folder in your project root with structured markdown files.
>
> Each file serves a specific purpose — from the big picture project brief down to what you're actively working on right now.
>
> The magic? Your `.github/copilot-instructions.md` tells Copilot to read these files first. So every new chat session starts with full project context."

---

#### [0:16-0:19] Building a Memory Bank from Scratch (3 min)

**SAY:**
> "Let me show you how to build a Memory Bank from scratch. There are two parts:
>
> **Part 1:** Create the memory-bank folder with 6 core files.
> **Part 2:** Update your copilot-instructions.md to tell Copilot how to use them.
>
> Let's start with the files."

**DO - Show the 6 core files and their purpose:**

**SHOW ON SCREEN:**
```
STEP 1: Create the folder structure

your-project/
├── .github/
│   └── copilot-instructions.md    ← UPDATE this
├── memory-bank/                    ← CREATE this
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── techContext.md
│   ├── systemPatterns.md
│   ├── activeContext.md
│   └── progress.md
└── src/
    └── ... your code
```

**SAY:**
> "Six files. Each one answers a specific question Copilot needs to know."

**SHOW ON SCREEN:**
```
STEP 2: What goes in each file

projectbrief.md — "What is this project?"
  → Project name, goals, scope, requirements
  → The foundation everything else builds on

productContext.md — "Why does this project exist?"
  → Problems it solves, who it's for
  → User experience goals
  → How it fits in the bigger picture

techContext.md — "What are we building with?"
  → Languages, frameworks, libraries
  → Dev environment setup
  → Technical constraints and decisions

systemPatterns.md — "How do we build things here?"
  → Architecture (e.g., 3-tier, microservices)
  → Design patterns in use
  → Naming conventions, file structure

activeContext.md — "What's happening RIGHT NOW?"
  → Current sprint/focus area
  → Recent changes and decisions
  → Immediate next steps
  → ⚡ This is the most important file

progress.md — "Where do we stand?"
  → What's working
  → What's left to build
  → Known issues and blockers
  → Overall project status
```

**SAY:**
> "Notice how these build on each other. The project brief feeds into product context and tech context, which feed into system patterns, which all feed into active context and progress.
>
> `activeContext.md` is the most important file — it's what Copilot checks first to understand where you left off."

---

**DO - Show what to add to copilot-instructions.md:**

**SAY:**
> "Now the critical part. You need to tell Copilot the Memory Bank exists and how to use it. Add this to your `.github/copilot-instructions.md`:"

**SHOW ON SCREEN:**
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

**SAY:**
> "That's it. Now Copilot knows to read your memory bank and stay in context.
>
> The 'update memory bank' command is especially powerful — at the end of a session, just say those three words and Copilot will update all your context files based on what you accomplished."

---

#### [0:19-0:20] Memory Bank in Practice (1 min)

**SAY:**
> "Here's the daily workflow with a Memory Bank:
>
> **Start of day:** Copilot reads the Memory Bank automatically. It knows your project, your patterns, and where you left off.
>
> **During work:** Code normally. Copilot's responses are more accurate because it has full context.
>
> **End of day:** Say 'update memory bank'. Copilot updates activeContext.md and progress.md with what you accomplished and what's next.
>
> **Next morning:** Copilot reads the updated files. Zero context lost.
>
> Think of it this way: Custom Agents tell Copilot HOW you work. The Memory Bank tells Copilot WHERE you are."

**SHOW ON SCREEN:**
```
THE DAILY WORKFLOW

Morning:   Copilot reads memory-bank/ → Full context
           "I see you're working on the auth module.
            Last session you finished the login endpoint
            and planned to start password reset next."

Coding:    Better suggestions because of context
           No more repeating yourself

End of day: "update memory bank"
           → activeContext.md updated
           → progress.md updated

Next day:  Copilot reads updated files → Continuity
```

**SAY:**
> "Your workshop project already has `.github/copilot-instructions.md` and `PRD.md` — that's the foundation. The Memory Bank pattern takes it to the next level for real-world, multi-day projects.
>
> This is what separates someone who USES Copilot from someone who has a true AI-augmented workflow."

🏆 **ACHIEVEMENT:** "Memory Architect"

---

### [0:20-0:24] ⚠️ The 70% Problem - Critical Understanding (4 min)

**ENERGY:** Serious, professional, setting expectations

**SAY:**
> "Before the Boss Fight, one critical lesson from industry research:
>
> **THE 70% PROBLEM**
>
> AI delivers rapid initial progress - gets you 70% of the way FAST.
> But the final 30%? That's where YOU add value.
>
> Organizations that understand this see 26% productivity gains.
> Those that don't? They face accumulating technical debt."

**SHOW ON SCREEN:**
```
THE 70% PROBLEM

AI Delivers Fast (70%):
✅ Boilerplate code
✅ Standard patterns
✅ Happy path implementation
✅ Basic structure

YOU Must Add (30%):
🎯 Edge cases AI missed
🎯 Performance optimization
🎯 Security hardening
🎯 Production-readiness
🎯 Business logic nuances
🎯 Real-world error handling
```

**SAY:**
> "In the Boss Fight:
> - AI will get you 70% there quickly
> - YOUR job is to finish the final 30%
>
> This is where professionals shine. This is where YOU prove mastery! 💪"

🏆 **ACHIEVEMENT:** "70/30 Understander"

---

### [0:18-0:28] 🎮 BOSS FIGHT - The Ultimate Challenge (10 min)

**ENERGY:** EPIC FINALE, game show excitement

**SAY:**
> "This is it. THE BOSS FIGHT. 🎮
>
> Everything you've learned. All techniques. One challenge.
>
> **THE CHALLENGE:**
> Build a complete TODO TAGGING feature with many-to-many relationships.
>
> Remember: AI gives you fast 70%. YOUR value is the final 30%!
>
> **Requirements:**
> - Many-to-many relationship (Todo ↔ Tag)
> - POST /api/v1/todos/{id}/tags - Add tag
> - GET /api/v1/todos?tag=name - Filter by tag
> - DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag
> - Full 3-tier architecture (schemas, services, routes)
> - Proper error handling (404, 403, 400)
> - Ownership validation (THE 30%!)
>
> **TECHNIQUES TO USE:**
> - ✅ 'think hard' for planning (Session 2)
> - ✅ Context+Task+Constraints+Format prompts (Session 2)
> - ✅ Advanced #mentions (Session 2)
> - ✅ Plan Mode or Subagents (Session 3)
> - ✅ TDD approach (Session 3)
> - ✅ Code Review (just learned!)
>
> **SCORING:**
> - Complete in 6 min: 🏆 PLATINUM (top 1%)
> - Complete in 8 min: 🥇 GOLD (top 10%)
> - Complete in 10 min: 🥈 SILVER (top 25%)
> - Complete at all: ✅ CERTIFIED
>
> **BONUS POINTS:**
> - Used 'think hard' for planning: +1 level
> - Used Plan Mode: +1 level
> - Used TDD approach: +1 level
> - Used Custom Agent: +1 level
>
> **BOSS FIGHT STARTS... NOW! ⏱️🎮**"

---

## Boss Fight Winning Strategy

### [0:00-0:30] Planning with Think Hard

**Prompt:**
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

### [0:30-3:30] Implementation with Plan Mode

**Use /plan for visibility:**

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

### Alternative: Sequential Implementation

**STEP 1: Database Models**

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

**STEP 2: Schemas**

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

**STEP 3: Service Layer**

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

**STEP 4: API Endpoints**

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

### [3:30-5:00] The Critical 30% - Review & Fix

**SAY to students:**
> "Now comes YOUR 30%! AI got you most of the way. Time to make it production-ready!"

**Have them check:**
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

### [5:00-6:00] Quick Test

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

### [0:28-0:33] 🎉 Victory Lap & Certification

**ENERGY:** Celebration mode

**SAY:**
> "TIME! ✋
>
> Who finished? 🙋
> Who got tests passing? 🙋
> Who verified ownership validation (the 30%)? 🙋
>
> **Certification levels achieved?**
> - Platinum (≤6 min)? 🏆
> - Gold (≤8 min)? 🥇
> - Silver (≤10 min)? 🥈
> - Certified (completed)? ✅"

**CELEBRATE:**
> "🎉 CONGRATULATIONS! 🎉
>
> You've completed the GitHub Copilot Power User Workshop!
>
> In 2 hours, you learned:
> - Security-first development
> - All Copilot modes (Ask, Edit, Agent, Plan)
> - Context mastery with #mentions
> - Professional workflows (Explore → Plan → Code)
> - TDD with AI
> - Subagents and parallel work
> - Code Review and Custom Agents
> - The critical 70/30 understanding
>
> You're not beginners anymore.
> You're POWER USERS.
> You're AI-AUGMENTED PROFESSIONALS.
>
> Go transform how your team codes! 💪🚀"

---

## Session 4 Wrap-Up

### Achievements Unlocked

- 🔍 **Review Master** - Used Copilot Code Review
- 🤖 **Agent Creator** - Created Custom Agent
- ⚠️ **70/30 Understander** - Knows where to add value
- 🎮 **Boss Fighter** - Completed final challenge
- 🏆 **COPILOT CHAMPION** - Full workshop complete!

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
│   Level: _______________                    │
│   Date: _______________                     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Instructor Notes

### Common Issues & Solutions

**Issue:** Boss Fight too ambitious  
**Solution:** Focus on core endpoints, skip DELETE if short on time

**Issue:** Custom Agent concept unclear  
**Solution:** Explain as "pre-loaded context for every conversation"

**Issue:** 70/30 concept misunderstood  
**Solution:** Give specific examples (ownership validation, edge cases)

### Time Flexibility

**If running behind:**
- Shorten Code Review to 2 min
- Skip Custom Agent creation (just show concept)
- Give more time on Boss Fight

**If ahead:**
- Have students create their own Custom Agent
- Do full code review of Boss Fight result
- Add bonus features to tagging

### Energy Management

- **Epic:** Opening (0:00-0:02)
- **Professional:** Code Review (0:02-0:08)
- **Excited:** Custom Agents (0:08-0:14)
- **Serious:** 70/30 Problem (0:14-0:18)
- **Game show:** Boss Fight (0:18-0:28)
- **Celebration:** Certification (0:28-0:33)

---

**End of Instructor Guide: Micro Session 4** 🎓

**🎉 COMPLETE WORKSHOP SERIES FINISHED! 🎉**
