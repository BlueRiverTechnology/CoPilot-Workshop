# Todo API - GitHub Copilot Workshop Starter Project

**GitHub Copilot Power User Workshop**

## Overview

This is the starter project for the GitHub Copilot Power User Workshop. Students will use this as their starting point to learn AI-augmented development techniques.

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

## How to Use (For Instructors)

### Before Session 2:

1. **Share this project with students** (zip file or Git repo)
2. **Students extract/clone** to their local machine
3. **Students open in VS Code with GitHub Copilot**


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

## What Students Will Build

In Sessions 2-3, students create:
- GET /todos - List all todos
- POST /todos - Create todo
- PUT /todos/{id} - Update todo
- DELETE /todos/{id} - Delete todo

All following the 3-tier pattern (API → Service → Model).

## What's Pre-Built

✅ **Complete Models** (User and Todo with SQLAlchemy, UUID, relationships)  
✅ **Empty Schemas** (Students create Pydantic schemas)  
✅ **Empty Services** (Students create business logic)  
✅ **Empty API Routes** (Students create FastAPI endpoints)  
✅ **Basic FastAPI App** (main.py with health check)

## Copilot Features You'll Learn

- **Ask Mode** - Questions, explanations
- **Edit Mode** - Cmd/Ctrl+I inline edits
- **Agent Mode** - Multi-file autonomous work
- **Plan Mode** - /plan for visibility before execution
- **#mentions** - #file:, #folder:, #problems
- **Thinking Modes** - think, think hard, think harder

## Credits

Created for the GitHub Copilot Power User Workshop
