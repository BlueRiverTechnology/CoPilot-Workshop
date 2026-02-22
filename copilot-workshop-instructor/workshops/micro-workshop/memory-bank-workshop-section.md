# Memory Bank Workshop Section
## Where to Include & What to Add to Each File

---

# 📍 WHERE IT GOES

**Insert as a new section in Session 4**, between **Custom Agents** [0:08-0:14] and **The 70% Problem** [0:14-0:18].

This shifts the timing slightly:
- Code Review: [0:02-0:08] (unchanged)
- Custom Agents: [0:08-0:14] (unchanged)
- **Memory Bank: [0:14-0:20] (NEW — 6 min)**
- The 70% Problem: [0:20-0:24] (was 0:14-0:18)
- Boss Fight: [0:24-0:34] (was 0:18-0:28, still 10 min)
- Victory Lap: [0:34-0:38] (was 0:28-0:33)

Total session grows from 33 min to ~38 min. If you need to keep it at 33, you can trim Code Review to 4 min and 70% Problem to 3 min.

---

# 📋 FILE 1: INSTRUCTOR GUIDE (instructor-guide-micro-4.md)

**Insert after the "Agent Creator" achievement at the end of the Custom Agents section [0:11-0:14], before "The 70% Problem" section.**

```markdown
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
```

---

# 📋 FILE 2: STUDENT PACKET (student-packet-micro-4.md)

**Insert after the "Agent Creator" achievement section, before "The 70% Problem" section.**

```markdown
---

## 🧠 Memory Bank - Persistent Project Context

### The Problem

Every new Copilot chat session starts with zero memory:

```
Monday:    "We use FastAPI with async/await and 3-tier..."
Tuesday:   "Remember, we use FastAPI with async/await..."
Wednesday: "I already told you, FastAPI..."
Thursday:  "...I give up explaining."
```

### The Solution

A `memory-bank/` folder with structured markdown files that Copilot reads at the start of every conversation.

```
your-project/
├── .github/
│   └── copilot-instructions.md    ← Tell Copilot about Memory Bank
├── memory-bank/                    ← Persistent context lives here
│   ├── projectbrief.md            ← What is this project?
│   ├── productContext.md          ← Why does it exist?
│   ├── techContext.md             ← What tech do we use?
│   ├── systemPatterns.md         ← How do we build things?
│   ├── activeContext.md           ← What's happening NOW? ⚡
│   └── progress.md                ← Where do we stand?
└── src/
```

### Build Your Memory Bank: Step by Step

#### Step 1: Create the folder and files

```bash
mkdir memory-bank
touch memory-bank/projectbrief.md
touch memory-bank/productContext.md
touch memory-bank/techContext.md
touch memory-bank/systemPatterns.md
touch memory-bank/activeContext.md
touch memory-bank/progress.md
```

#### Step 2: Fill in each file

**projectbrief.md** — The foundation
```markdown
# Project Brief

## Project Name
Todo API Workshop App

## Goals
- Build a REST API for managing todos
- Learn AI-assisted development patterns
- Practice TDD with Copilot

## Scope
- CRUD operations for todos
- User ownership model
- Tagging system (many-to-many)
- Authentication (simplified for workshop)

## Success Criteria
- All endpoints return correct responses
- Ownership validation on all mutations
- Tests pass for core functionality
```

**productContext.md** — The why
```markdown
# Product Context

## Problem
Developers need a structured todo management API
with user isolation and organizational features.

## Users
- Developers learning AI-augmented development
- Teams needing a lightweight task API

## User Experience Goals
- RESTful, predictable API design
- Clear error messages
- Fast response times
```

**techContext.md** — The stack
```markdown
# Tech Context

## Stack
- Python 3.11+
- FastAPI (async)
- SQLAlchemy (async sessions)
- Pydantic v2 (validation)
- Pytest (testing)
- SQLite (development)

## Setup
- Poetry for dependency management
- uvicorn for local server
- pyproject.toml for configuration

## Constraints
- All operations must be async
- UUID primary keys (string format)
- Simplified auth (fixed "default-user")
```

**systemPatterns.md** — How we build
```markdown
# System Patterns

## Architecture
3-tier: API (routers) → Services (business logic) → Models (data)

## File Structure
- src/api/v1/ → FastAPI routers
- src/services/ → Business logic layer
- src/models/ → SQLAlchemy ORM models
- src/schemas/ → Pydantic request/response schemas
- tests/ → Pytest test files

## Key Patterns
- Service layer handles all business logic
- Routers only handle HTTP concerns
- Pydantic schemas for all request/response
- HTTPException for error responses
- Ownership validation before mutations

## Conventions
- Async/await everywhere
- Type hints on all functions
- Docstrings on public methods
- PEP 8 style
```

**activeContext.md** — Right now (most important!)
```markdown
# Active Context

## Current Focus
Completing Session 4 Boss Fight - building tagging feature

## Recent Changes
- Session 3: Built POST, GET, PUT endpoints for todos
- Implemented TDD approach for all features
- Service layer pattern established

## Active Decisions
- Tags are case-insensitive (stored lowercase)
- Tag names unique per user
- Many-to-many via association table

## Next Steps
- Implement Tag model and association table
- Build tag endpoints (POST, GET filter, DELETE)
- Add ownership validation for tags
- Run code review on completed features
```

**progress.md** — Status tracker
```markdown
# Progress

## What Works
- [x] Todo model with SQLAlchemy
- [x] POST /api/v1/todos (create)
- [x] GET /api/v1/todos (list)
- [x] PUT /api/v1/todos/{id} (update)
- [x] Pydantic schemas for todos
- [x] Service layer pattern
- [x] Basic test suite

## What's Left
- [ ] Tag model and association table
- [ ] POST /api/v1/todos/{id}/tags
- [ ] GET /api/v1/todos?tag=name
- [ ] DELETE /api/v1/todos/{id}/tags/{tag_id}
- [ ] Ownership validation for tags
- [ ] Complete test coverage

## Known Issues
- Authentication is simplified (hardcoded user)
- No pagination on list endpoints
- No rate limiting
```

#### Step 3: Update copilot-instructions.md

Add this to your existing `.github/copilot-instructions.md`:

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

### The Daily Workflow

```
MORNING:
  Copilot reads memory-bank/ → Full context restored
  No more re-explaining your project

DURING WORK:
  Better suggestions because Copilot knows your patterns
  Reference #file:memory-bank/activeContext.md for focus

END OF DAY:
  Say: "update memory bank"
  Copilot updates activeContext.md and progress.md

NEXT DAY:
  Zero context lost. Pick up exactly where you left off.
```

### How It Connects to What You Learned

| Workshop Concept | Memory Bank Equivalent |
|------------------|----------------------|
| copilot-instructions.md (Session 1) | Tells Copilot to read Memory Bank |
| PRD.md (Session 2) | projectbrief.md + productContext.md |
| 6-Element Framework (Session 2) | Context is pre-loaded from files |
| Custom Agents (Session 4) | systemPatterns.md + techContext.md |

**Key Insight:** Custom Agents tell Copilot HOW you work. The Memory Bank tells Copilot WHERE you are.

### Reflection

How would a Memory Bank help in YOUR daily work?
```
Project I'd use it on: ______________________________
Most valuable file for me: __________________________
What I'd put in activeContext.md: ___________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Memory Architect"

---
```

---

# 📋 FILE 3: STUDENT REFERENCE (student-reference-micro-4.md)

**Insert a new section after "Custom Agents" and before "The 70% Problem".**

```markdown
---

## Memory Bank - Persistent Project Context

### Overview

The Memory Bank gives Copilot persistent memory across chat sessions using structured markdown files in a `memory-bank/` directory.

### Architecture

```
memory-bank/
├── projectbrief.md      Foundation: goals, scope, requirements
│   ├── productContext.md    Why it exists, who it's for
│   ├── systemPatterns.md    Architecture, patterns, conventions
│   └── techContext.md       Stack, setup, constraints
│       ├── activeContext.md     Current focus, recent changes ⚡
│       └── progress.md         Status, what works, what's left
```

Files build on each other hierarchically. The project brief informs everything below it. Active context and progress change most frequently.

### The 6 Core Files

| File | Updates | What Goes In It |
|------|---------|-----------------|
| `projectbrief.md` | Rarely | Project name, goals, scope, success criteria |
| `productContext.md` | Rarely | Problem being solved, users, UX goals |
| `techContext.md` | Occasionally | Stack, setup instructions, constraints |
| `systemPatterns.md` | Occasionally | Architecture, file structure, conventions |
| `activeContext.md` | **Every session** | Current focus, recent changes, next steps |
| `progress.md` | **Every session** | What works, what's left, known issues |

### copilot-instructions.md Addition

Add to your `.github/copilot-instructions.md`:

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

### Key Commands

| Command | What Happens |
|---------|-------------|
| "update memory bank" | Copilot reviews and updates ALL memory-bank files |
| `#file:memory-bank/activeContext.md` | Include current focus as context |
| `#folder:memory-bank` | Include entire memory bank as context |

### Template: activeContext.md

This is the file you'll update most. Template:

```markdown
# Active Context

## Current Focus
[What you're working on right now]

## Recent Changes
- [What changed in the last session]
- [Key decisions made]
- [Files modified]

## Active Decisions
- [Decisions that affect current work]
- [Trade-offs you've chosen]

## Next Steps
- [Immediate tasks]
- [What to work on next session]

## Open Questions
- [Unresolved decisions]
- [Things to investigate]
```

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

### Best Practices

```
DO:
✅ Update activeContext.md at end of every session
✅ Keep files concise — bullet points, not essays
✅ Commit memory-bank changes with your code
✅ Use "update memory bank" when ending a session
✅ Let Copilot suggest updates during conversation

DON'T:
❌ Put sensitive data in memory bank files
❌ Write novels — Copilot needs scannable content
❌ Forget to update after major decisions
❌ Skip the copilot-instructions.md update
```

### Memory Bank vs. Other Context Tools

| Tool | Scope | Persistence | Best For |
|------|-------|-------------|----------|
| copilot-instructions.md | Rules & standards | Always loaded | HOW you work |
| Custom Agents (.agent.md) | Specialized roles | Referenced manually | Domain expertise |
| Memory Bank (memory-bank/) | Project state | Always loaded | WHERE you are |
| PRD files | Feature specs | Referenced manually | WHAT to build |

**They work together:** Instructions set rules → Memory Bank provides context → Agents add expertise → PRDs define features.

---
```

---

# 📋 FILE 4: PROMPT SHEET (PROMPT-SHEET-SESSION-4.md)

**Add a new section after Custom Agents prompts, before Boss Fight prompts.**

```markdown
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
```

---

# 📋 FILE 5: SLIDE DECK GUIDE (SLIDE-DECK-GUIDE.md)

**Insert 3 new slides after the Custom Agents slides, before The 70% Problem slides. This shifts all subsequent slide numbers by 3.**

```markdown
---

## SLIDE XX: The Memory Problem

### Visual
- **Layout:** Split screen — left shows repeated chat messages, right shows frustration
- **Animation:** Messages stacking up on repeat

### Text on Slide
```
🧠 THE PROBLEM: COPILOT FORGETS

Every new chat session starts from zero.

Monday:    "We use FastAPI with async..."
Tuesday:   "Remember, we use FastAPI..."
Wednesday: "I ALREADY TOLD YOU..."
Thursday:  😤

Your context. Your decisions. Your progress.
Gone. Every. Single. Time.

What if Copilot could REMEMBER?
```

### Speaker Notes
> "Custom Agents are great for defining roles. But Copilot still forgets between sessions. You end up repeating your project setup, your decisions, your progress. The Memory Bank fixes this."

---

## SLIDE XX+1: Memory Bank Structure

### Visual
- **Layout:** Folder tree on left, descriptions on right
- **Color coding:** Each file a different color
- **Highlight:** activeContext.md glows (most important)

### Text on Slide
```
🧠 THE MEMORY BANK

memory-bank/
├── projectbrief.md      → What is this project?
├── productContext.md     → Why does it exist?
├── techContext.md        → What tech do we use?
├── systemPatterns.md     → How do we build things?
├── activeContext.md  ⚡  → What's happening NOW?
└── progress.md           → Where do we stand?

+ Update .github/copilot-instructions.md
  to tell Copilot: "Read memory-bank/ first"

✨ Copilot reads these EVERY session
✨ Say "update memory bank" to save state
✨ Zero context lost between sessions
```

### Speaker Notes
> "Six markdown files, each answering a question Copilot needs. The project brief is the foundation. Active context is what changes most — it's your current focus, recent changes, and next steps. You update copilot-instructions to tell Copilot to read these files. Then say 'update memory bank' at the end of each session."

---

## SLIDE XX+2: Memory Bank Daily Workflow

### Visual
- **Layout:** Circular flow diagram
- **Steps:** Morning → Code → End of Day → Next Morning
- **Key insight:** Custom Agents = HOW, Memory Bank = WHERE

### Text on Slide
```
🧠 THE DAILY WORKFLOW

  ┌─────────────┐
  │   MORNING   │ Copilot reads memory-bank/
  │  Full context restored automatically
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │   CODING    │ Better suggestions
  │  No repeating yourself
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │  END OF DAY │ "update memory bank"
  │  State saved to markdown
  └──────┬──────┘
         │
         └──────→ Next day: zero context lost

KEY INSIGHT:
  Custom Agents → HOW you work
  Memory Bank   → WHERE you are
```

### Speaker Notes
> "This is the workflow. Morning: context is restored. During coding: better results. End of day: update the bank. Next morning: pick up where you left off. Think of it this way — Custom Agents tell Copilot how you work. The Memory Bank tells Copilot where you are. Together, Copilot becomes a true project partner."

---
```

---

# 📋 FILE 6: KNOWLEDGE BASE (knowledge.md)

**Add a new section in the appropriate location (near Custom Instructions or Advanced Features).**

```markdown
---

## Memory Bank - Persistent Project Context

### Concept
The Memory Bank is a community-developed pattern that gives GitHub Copilot persistent memory across chat sessions. It uses structured markdown files in a `memory-bank/` directory, referenced through `.github/copilot-instructions.md`.

### Origin
Inspired by the Cline Memory Bank concept, adapted for GitHub Copilot. Now included in GitHub's official `awesome-copilot` repository as a recommended instructions file.

### Core Files
| File | Purpose | Update Frequency |
|------|---------|-----------------|
| projectbrief.md | Goals, scope, requirements | Rarely |
| productContext.md | Why it exists, users, UX goals | Rarely |
| techContext.md | Stack, setup, constraints | Occasionally |
| systemPatterns.md | Architecture, patterns, conventions | Occasionally |
| activeContext.md | Current focus, recent changes, next steps | Every session |
| progress.md | What works, what's left, known issues | Every session |

### Required copilot-instructions.md Addition

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

### Key Commands
- "update memory bank" — Copilot reviews and updates all files
- `#file:memory-bank/activeContext.md` — Reference current context
- `#folder:memory-bank` — Include entire memory bank

### Relationship to Other Context Tools
- **copilot-instructions.md**: Rules and standards (HOW you work)
- **Custom Agents**: Specialized AI personas (domain expertise)
- **Memory Bank**: Project state and progress (WHERE you are)
- **PRD files**: Feature specifications (WHAT to build)

### Alternative Implementations
- **MCP-based**: `@modelcontextprotocol/server-memory` for JSON storage
- **MemoriPilot extension**: VS Code extension with specialized update tools
- **Copilot Memories**: Official Visual Studio feature (VS 2026 only, not VS Code)

---
```

---

# 📋 FILE 7: ACHIEVEMENTS UPDATE

**Add to the Session 4 achievements list in all files that track achievements:**

```
🧠 **Memory Architect** - Built a Memory Bank for persistent context
```

Updated Session 4 achievement list:
- 🔍 Review Master
- 🤖 Agent Creator
- 🧠 Memory Architect (NEW)
- ⚠️ 70/30 Understander
- 🎮 Boss Fighter
- 🏆 COPILOT CHAMPION

---

# 📋 SUMMARY: The copilot-instructions.md Addition

This is the exact text students add to their existing `.github/copilot-instructions.md` file. It goes at the end, after all existing sections:

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

This is intentionally simple. It:
1. Tells Copilot the Memory Bank exists
2. Specifies the reading order (foundation → specifics → current state)
3. Asks Copilot to suggest updates when it notices stale information
4. Defines the "update memory bank" command for end-of-session saves
