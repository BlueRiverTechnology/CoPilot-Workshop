# Session 1 Prompt Sheet: Security & Superpowers 🛡️⚡

**Copy-paste materials for students**

---

## 1️⃣ .copilotignore File

**Copy this entire content into `.copilotignore` file in your project root:**

```
# Security - NEVER let AI see these
.env
.env.*
*.key
*.pem
secrets/
credentials.json

# API Keys and Tokens
*_TOKEN
*_SECRET
*_API_KEY
*_PASSWORD

# Database
*.db
database.yml

# Build artifacts (performance)
node_modules/
__pycache__/
*.pyc
.pytest_cache/
dist/
build/

# Large files (performance)
*.log
*.csv
*.json
*.sqlite
```

### Verification Command:
```bash
# Test it works
echo "test-secret-key" > .env
# Open Copilot Chat and type: "#file:.env"
# It should show: "This file is ignored" or not find the file
```

---

## Terminal Command Control
** Copy this into Agent Mode:**

```
pip install fastapi uvicorn
```
---

## 2️⃣ Practice Project Generation Prompt

**Copy this into Agent Mode:**

```
Create a minimal FastAPI learning project:

Structure (6 files total):
├── routes/        # 3 files
│   ├── hello.py   (basic endpoint)
│   ├── users.py   (user endpoints with auth)
│   └── items.py   (CRUD operations)
├── helpers/       # 2 files
│   ├── auth.py    (simple authentication)
│   └── validate.py (input validation)
└── main.py        # 1 file (app entry point)

Make each file 20-40 lines with:
- Clear docstrings
- Type hints
- Error handling examples
- Authentication patterns
- Validation logic

Keep it simple but demonstrative.
```

---

## 3️⃣ Mode Switching Practice Prompts

### Task 1: Ask Mode - Ask about email validation
```
How should I validate emails in Python?
```

### Task 2: Agent Mode - Implement the validation
```
Create email validation function in helpers/validate.py
```

### Task 3: Agent Mode FIRST - Add error handling
```
Add error handling to routes/hello.py
```

### Task 4: Ask Mode - Understand what was added
```
Explain the error handling in #file:routes/hello.py
```

---

## 4️⃣ Test Files for #mention Practice

**Create test files to practice #mentions:**

### test_calc.py
```python
# test_calc.py
def divide(a, b):
    return a / b

result = divide(10, 0)
print(f"Result: {result}")
```

### test_syntax.py
```python
# test_syntax.py
def hello(name)
    return f"Hello, {name}
```

---

## 5️⃣ #mention Examples to Try

### #file Example
```
Looking at #file:routes/hello.py, add logging statements to track each greeting request
```

### #folder Example
```
What patterns do you see in #folder:routes ?
```

### #terminalSelection Example
```bash
# First, run this in terminal:
python test_calc.py

# Select the error output in terminal
# Then in Ask Mode:
Fix this error: #terminalSelection
```

### #problems Example
```
# Create test_syntax.py with errors (shown above)
# Then in Agent Mode:
Fix all issues in #problems
```

### #codebase Example
```
@workspace find all authentication-related code
```

---

## 6️⃣ Custom Instructions File

**Create `.github/copilot-instructions.md` in your project root:**

```markdown
# Project: Todo API

## Overview
FastAPI backend for personal task management.
Python 3.11+, SQLAlchemy async, PostgreSQL.

## Coding Standards
- Use type hints on all functions
- Write docstrings in Google style
- Use async/await for all I/O
- Follow PEP 8
- Max line length: 100 characters

## Naming Conventions
- Files: snake_case
- Classes: PascalCase  
- Functions: snake_case
- Constants: UPPER_SNAKE_CASE

## Error Handling
- Always use try/except for I/O operations
- Return meaningful error messages
- Log errors with appropriate severity
```

---

## 🎯 Quick Reference: All AI Modes

```
❓ Ask Mode = "The Wise Advisor"
   - Thinks WITH you
   - Explores options
   - Answers questions
   - No code changes

✏️ Edit Mode = "The Precise Editor"
   - Controlled edits to working set
   - You choose which files
   - Review before accepting

🤖 Agent Mode = "The Builder"  
   - Implements FOR you
   - Creates files
   - Runs terminal commands
   - Iterates until complete

📋 Plan Mode = "The Architect"
   - Creates implementation plans
   - Research before building
   - Hand off to Agent Mode

⚡ Inline Chat (Cmd+I) = "The Quick Fix"
   - Inline edits
   - No chat panel needed
   - Lightning fast
```

---

## 🎯 Quick Reference: #mentions

```
#file:path/to/file.py     → Reference specific file
#folder:path/to/folder    → Reference entire directory
#codebase                 → Search entire codebase
#problems                 → Include IDE errors/warnings
#terminalSelection        → Include selected terminal output
#terminalLastCommand      → Include last command output
#fetch:url                → Fetch web content
@workspace                → Search across workspace
```

---

## 🎮 Speed Challenge Checklist

**Use ALL 5 #mentions in 3 minutes:**

- [ ] Use #file to modify a specific file
- [ ] Use #folder to analyze routes/ or helpers/
- [ ] Run a command, then use #terminalSelection to reference output
- [ ] Use #problems to fix any issues
- [ ] Use @workspace to search your codebase

---

## 🏆 Session 1 Achievements

- [ ] 🏆 **Fortress Builder** - Completed security setup
- [ ] 🏗️ **Project Generator** - Created practice project
- [ ] 🔐 **Secret Keeper** - .copilotignore configured
- [ ] ⚡ **Command Guardian** - Understand terminal approval
- [ ] 🎮 **Mode Master** - All AI modes practiced
- [ ] 🎯 **Context Master** - #mentions mastered
- [ ] 📋 **Instruction Writer** - Custom instructions created

---

## 💡 Pro Tips from Session 1

1. **Security First:** Always add .env to .copilotignore before anything else
2. **Mode Selection:** Ask = think, Agent = build, Edit = precise changes, Inline = quick fix
3. **Context Stacking:** Combine multiple #mentions for precision
4. **Custom Instructions:** Set once in `.github/copilot-instructions.md`, applied everywhere
5. **Review Before Accept:** Always check diffs before accepting changes
6. **Git Integration:** Commit often, discard changes you don't like
7. **Plan Mode:** Use for complex features before implementing

---

**Next Session:** Context Mastery & Project Planning! 🚀
