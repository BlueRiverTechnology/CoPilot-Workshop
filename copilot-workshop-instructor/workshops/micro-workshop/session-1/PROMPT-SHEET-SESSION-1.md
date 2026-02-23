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
# Open Copilot Chat and type: "#file:.env"
# It should show: "This file is ignored" or not find the file
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

## 6️⃣ Writing Effective Rules - Examples

### Good Rules vs Bad Rules

**BAD EXAMPLES (Don't copy these!):**

```markdown
# ❌ Too vague
- Follow good naming conventions
- Make sure code is well-tested
- Don't use print statements

# ❌ Too negative (LLMs are poor at negations)
- Don't use raw SQL
- Avoid using global variables
- Never expose secrets
```

**GOOD EXAMPLES (Copy these patterns!):**

```markdown
# ✅ Specific and actionable
- Use type hints on all function signatures
- Every service method must have a corresponding test file in tests/services/
- Use `logging` module at DEBUG level for diagnostic output

# ✅ Positive directives (what TO do)
- Use SQLAlchemy ORM for all database operations
- Define constants in UPPER_SNAKE_CASE at module level
- Store secrets in environment variables, access via python-dotenv

# ✅ With code examples
## Error Handling Pattern

Use HTTPException for API errors:

```python
# GOOD - Do this
async def get_user(user_id: str) -> User:
    try:
        return await db.get(User, user_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
```
```

---

## 7️⃣ Custom Instructions Template - Fill This In!

**Create `.github/copilot-instructions.md` in your project root:**

**Copy this template and fill in YOUR project's rules:**

```markdown
# Project: [YOUR PROJECT NAME]

## Overview
[Brief description - 1-2 sentences about what this project does]
[Tech stack: Python 3.11+, FastAPI, SQLAlchemy, etc.]

## Coding Standards
- Use type hints on all function signatures
- Write docstrings in Google style
- Use async/await for all I/O operations
- Follow PEP 8
- Max line length: 100 characters

## Architecture Patterns
- 3-tier structure: API routes → Service layer → Models
- All database operations in service layer
- Pydantic v2 for all request/response schemas

## Naming Conventions
- Files: snake_case
- Classes: PascalCase
- Functions: snake_case
- Constants: UPPER_SNAKE_CASE

## Error Handling
- Use HTTPException for API errors with proper status codes
- Log all errors before raising
- Never expose internal error details to clients

## Testing
- Every service method must have a corresponding test
- Use pytest fixtures for database setup
- Use AAA pattern: Arrange, Act, Assert
```

---

## 8️⃣ XML Tags for Claude-Based Tools

**If you're using Claude Code, Cursor, or other Claude-based tools, use XML tags:**

```markdown
<role>Senior Python developer specializing in FastAPI</role>

<architecture>
  - 3-tier: API routes → Service layer → Models
  - All database operations use async/await
  - Pydantic v2 for all request/response schemas
</architecture>

<coding_standards>
  - Use type hints on every function signature
  - Write Google-style docstrings
  - Follow PEP 8, max line length 100
  - Use async/await for all I/O operations
</coding_standards>

<constraints>
  - Never use raw SQL — always use SQLAlchemy ORM
  - All endpoints return proper HTTP status codes (400/401/403/404/500)
  - Log all errors before raising exceptions
  - Never expose internal error details to clients
</constraints>

<testing>
  - Every service method must have a test in tests/services/
  - Use pytest fixtures for database setup
  - AAA pattern: Arrange, Act, Assert
  - Mock external API calls
</testing>
```

**Why XML tags?** They create clear boundaries that prevent AI from mixing up context, instructions, and examples.

---

## 9️⃣ Path-Specific Instructions Example

**Create `.github/instructions/testing.instructions.md`:**

```yaml
---
applyTo: "**/tests/**"
---

# Testing Guidelines

## Test Structure
- Every test function name starts with `test_`
- Use AAA pattern: Arrange, Act, Assert
- One assertion per test when possible

## Fixtures
- Use pytest fixtures for database setup
- Define fixtures in conftest.py
- Use scope="function" for isolation

## Mocking
- Mock external API calls
- Use pytest-mock for all mocking
- Never make real external API calls in tests

## Coverage
- Aim for 80%+ code coverage
- Test happy path and error cases
- Include edge cases
```

**How to use different rules for different paths:**

```
.github/instructions/
├── api.instructions.md          (applyTo: "src/api/**")
├── testing.instructions.md      (applyTo: "**/tests/**")
├── services.instructions.md     (applyTo: "src/services/**")
└── documentation.instructions.md (applyTo: "**/*.md")
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
- [ ] 📋 **Rules Writer** - Custom rules written using research-backed principles
- [ ] 🔄 **Context Multiplier** - Understand how rules connect to everything

---

## 💡 Pro Tips from Session 1

1. **Security First:** Always add .env to .copilotignore before anything else
2. **Mode Selection:** Ask = think, Agent = build, Edit = precise changes, Inline = quick fix
3. **Context Stacking:** Combine multiple #mentions for precision
4. **Rules Writing:** Start with 5-10 rules, test them, iterate based on what works
5. **Positive Directives:** Tell AI what TO do, not what to avoid (LLMs are poor at negations)
6. **Structured Content:** Use clear Markdown headings or XML tags for better AI parsing
7. **Code Examples in Rules:** Show the pattern you want, don't just describe it
8. **Review Before Accept:** Always check diffs before accepting changes
9. **Git Integration:** Commit often, discard changes you don't like
10. **Verify Rules Work:** Check References section in Copilot Chat to see if your rules are being used

---

**Next Session:** Context Mastery & Project Planning! 🚀
