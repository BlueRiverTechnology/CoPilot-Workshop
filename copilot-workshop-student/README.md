# Todo API - GitHub Copilot Workshop Starter Project

**GitHub Copilot Power User Workshop**

## Overview

This is the starter project for the GitHub Copilot Power User Workshop. Students will use this as their starting point to learn AI-augmented development techniques.

**NEW: This workshop uses checkpoint branches as a safety net.** If you encounter issues during the workshop, you can switch to pre-built checkpoints to get back on track. See the [Checkpoint Branches](#checkpoint-branches-your-safety-net) section below.

## Checkpoint Branches: Your Safety Net

This repository includes **three branches** designed to ensure you never fall behind during the workshop:

### Branch Overview

| Branch | Purpose | What's Included |
|--------|---------|----------------|
| **`main`** | Starting point (Session 1-2) | Scaffolded project with models, empty services/schemas/routes |
| **`session-3-start`** | Session 3 checkpoint | Fully working API with POST, GET, PUT endpoints + tests |
| **`session-4-start`** | Session 4 checkpoint | Everything from Session 3 + DELETE endpoint + Tag model |

### How to Use Checkpoints

#### During Session 3:
If your API isn't working or you're stuck:
```bash
# Switch to the working Session 3 checkpoint
git checkout session-3-start

# Verify it works
pytest -v  # Should show all tests passing
uvicorn src.main:app --reload  # API should run without errors
```

#### During Session 4:
Start fresh with the Boss Fight checkpoint:
```bash
# Switch to Session 4 checkpoint
git checkout session-4-start

# This includes:
# - All CRUD operations from Session 3
# - DELETE endpoint
# - Tag model and association table (ready for you to build tag endpoints)
```

#### Returning to Your Work:
```bash
# See all available branches
git branch -a

# Return to your main branch
git checkout main
```

### The Safety Net Philosophy

**Don't let technical issues derail your learning.** The checkpoint system means:
- You can experiment without fear of breaking everything
- If something goes wrong, you have a working baseline to return to
- You focus on learning AI-assisted development, not debugging infrastructure
- Everyone can participate in later sessions even if they had issues earlier

---

## What's Included

### Security Setup (from Session 1)
- ✅ `.copilotignore` - Protects sensitive files
- ✅ `.github/copilot-instructions.md` - Coding standards and preferences

### Project Structure
```
copilot-workshop-student/
├── .copilotignore           # Security (from Session 1)
├── .github/
│   └── copilot-instructions.md  # Coding standards (from Session 1)
├── pyproject.toml           # Dependencies
├── PRD.md                   # Product requirements
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py              # Basic FastAPI app
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py          # SQLAlchemy Base
│   │   ├── user.py          # Complete User model (UUID, relationships)
│   │   └── todo.py          # Complete Todo model (UUID, relationships)
│   ├── schemas/
│   │   └── __init__.py      # Empty - students fill in Session 2
│   ├── services/
│   │   └── __init__.py      # Empty - students fill in Session 2
│   └── api/
│       └── v1/
│           └── __init__.py  # Empty - students fill in Session 3
└── tests/
    └── __init__.py
```

## Getting Started

### Before the Workshop:

1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd copilot-workshop-student
   ```

2. **Verify all branches are available:**
   ```bash
   git branch -a
   # You should see: main, session-3-start, session-4-start
   ```

3. **Make sure you're on the main branch:**
   ```bash
   git checkout main
   ```

4. **Open in VS Code with GitHub Copilot extension installed**


## Installation

**Using pip:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install from pyproject.toml
pip install -e .
```

**Using poetry:**
```bash
poetry install
```

## Running the App

```bash
# From the project root
uvicorn src.main:app --reload

# Access at: http://localhost:8000
# Docs at: http://localhost:8000/docs
```

## What You'll Build

### Session 1: Security & Writing Effective Rules (60 min)
- Configure `.copilotignore` for security
- Learn all Copilot modes (Ask, Edit, Agent, Plan)
- **Write your own custom Copilot instructions** and test them
- Master context provision with #mentions
- Set up professional AI development environment

### Session 2: Context Mastery & Planning (30 min)
- Learn the professional workflow: Explore → Plan → Code → Commit
- Master the prompting formula: Context + Task + Constraints + Format
- Use thinking modes for complex decisions
- Create PRDs with Plan mode

### Session 3: Checkpoint-Based Build Sprint (30 min)
- **Start from `session-3-start` checkpoint** (fully working API provided)
- Watch instructor demonstrate TDD with DELETE endpoint
- Build one additional feature using AI
- Learn recovery techniques with Git checkpoints

### Session 4: Advanced Tools & Boss Fight (30 min)
- **Start from `session-4-start` checkpoint** (includes Tag model)
- Learn Copilot Code Review, custom agents, Memory Bank
- **Boss Fight Challenge:** Build one tag-related endpoint (e.g., POST /todos/{id}/tags)
- Earn certification: Platinum/Gold/Silver/Certified

### Final API Features:
By the end of the workshop, your API will have:
- POST /todos - Create todo
- GET /todos - List all todos
- PUT /todos/{id} - Update todo
- DELETE /todos/{id} - Delete todo
- One tag-related endpoint (your Boss Fight implementation)

All following the 3-tier pattern (API → Service → Model).

## What's Pre-Built

✅ **Complete Models** (User and Todo with SQLAlchemy, UUID, relationships)  
✅ **Empty Schemas** (Students create Pydantic schemas)  
✅ **Empty Services** (Students create business logic)  
✅ **Empty API Routes** (Students create FastAPI endpoints)  
✅ **Basic FastAPI App** (main.py with health check)

## Copilot Features You'll Learn

### Core Modes
- **Ask Mode** - Questions, explanations, understanding code
- **Edit Mode** - Cmd/Ctrl+I inline edits to working set
- **Agent Mode** - Multi-file autonomous implementation
- **Plan Mode** - /plan for visibility before execution

### Context Mastery
- **#mentions** - #file, #folder, #codebase, #problems, #terminalSelection, #fetch
- **Custom Instructions** - `.github/copilot-instructions.md` for project-wide rules
- **Path-Specific Instructions** - `.github/instructions/*.instructions.md` with `applyTo` frontmatter
- **Rules Writing** - How to write effective instructions that shape AI behavior

### Advanced Techniques
- **Thinking Modes** - think, think hard, think harder, ultrathink
- **Subagents** - Delegate tasks to isolated agents
- **Code Review** - AI-powered PR reviews
- **Custom Agents** - `.agent.md` files for specialized personas
- **Memory Bank** - Persistent project context via markdown files

### The Prompting Formula
**Context + Task + Constraints + Format** (scaled by complexity)

## Troubleshooting & Recovery

### Common Issues

#### "My code isn't working in Session 3"
**Solution:** Switch to the checkpoint branch
```bash
git checkout session-3-start
pytest -v  # Verify everything works
```

#### "I want to start Session 4 fresh"
**Solution:** Use the Session 4 checkpoint
```bash
git checkout session-4-start
```

#### "I want to see what's different between branches"
**Solution:** Compare branches
```bash
# See what files changed between main and session-3-start
git diff main session-3-start --name-only

# See the actual differences
git diff main session-3-start
```

#### "I accidentally committed to the checkpoint branch"
**Solution:** Checkpoints are read-only learning tools. Just switch to a different branch:
```bash
git checkout main  # or session-4-start
```

### Best Practices

1. **Use checkpoints as reference, not starting points for your own work**
   - Checkpoints show you what working code looks like
   - Learn from them, then implement your own version on `main`

2. **Don't be afraid to experiment**
   - You can always return to a checkpoint
   - Break things, try new approaches, learn by doing

3. **If you fall behind, catch up with checkpoints**
   - The goal is learning AI-assisted development, not debugging infrastructure
   - Use checkpoints to stay engaged with later sessions

## Credits

Created for the GitHub Copilot Power User Workshop

**Workshop Focus:** Context mastery, effective rules writing, and professional AI-assisted development workflows

**Philosophy:** Learning through doing, with safety nets to ensure everyone succeeds
