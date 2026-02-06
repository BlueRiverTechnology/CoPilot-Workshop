# Student Reference: Micro Session 1
## Security & Superpowers - Technical Deep Dive

**📖 Source References:**
- GitHub Copilot Documentation: docs.github.com/en/copilot
- VS Code Copilot Documentation: code.visualstudio.com/docs/copilot

---

## 1. .copilotignore - Complete Security Guide

### Why It Matters

**Scenario without .copilotignore:**
```
1. You have .env with DATABASE_URL="postgres://user:pass@prod-db"
2. AI reads .env to help debug connection issue
3. AI's context now contains your production credentials
4. You take screenshot of chat to share with colleague
5. Your production database password is now in an image file
```

**Result:** Security incident, potential data breach

### Comprehensive Pattern Library

```bash
# ==========================================
# SECURITY (CRITICAL)
# ==========================================

# Environment files
.env
.env.*
*.env
.env.local
.env.production
.env.development

# API Keys and Tokens (any file with these in name)
*_TOKEN
*_SECRET
*_API_KEY
*_PASSWORD
*_CREDENTIALS

# Secret files and directories
secrets/
secrets.json
credentials.json
.credentials
*.key
*.pem
*.p12
*.pfx

# Cloud provider credentials
.aws/credentials
.aws/config
.gcloud/
.azure/

# SSH keys
id_rsa
id_dsa
*.ppk

# Database files with potential sensitive data
*.db
*.sqlite
*.sqlite3
database.yml
database.json

# ==========================================
# PERFORMANCE (REDUCES INDEXING TIME)
# ==========================================

# Node
node_modules/
npm-debug.log
yarn-error.log
.npm/
.yarn/

# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.tox/
.venv/
venv/
env/
ENV/

# Build artifacts
dist/
build/
*.egg-info/
.eggs/

# IDE
.idea/
*.swp
*.swo
*~

# Large data files
*.csv
*.log
*.dat
data/
logs/
tmp/

# ==========================================
# PRIVACY
# ==========================================

# User data
user_data/
uploads/
media/
*.dump
*.sql
backups/
```

### Testing Your Configuration

```bash
# Method 1: File test
echo "SECRET_KEY=test123" > .env
# In Copilot Chat: "#file:.env"
# Expected: File not found or ignored

# Method 2: Check what's included
# Try referencing a file you expect to be ignored
# Copilot should not have access to its contents
```

---

## 2. Terminal Command Safety - GitHub Copilot Approach

### Copilot's Confirmation Model

GitHub Copilot uses a **confirmation-first approach** for terminal commands:

**How it works:**
```
Agent Mode wants to run: pip install fastapi
[Continue] [Cancel]

You review → Click Continue → Command runs
You review → Click Cancel → Agent tries another approach
```

**Why this is safe:**
- You see exactly what will run before it executes
- You can reject dangerous commands
- No automatic execution without your approval

### Safe Commands to Approve

```bash
# Read-only commands (safe)
ls
pwd
cat
echo
which
whoami

# Version checks (safe)
python --version
node --version
npm --version
git --version

# Package management (review first)
pip install           # Check what packages
npm install           # Check what packages
poetry install

# Testing (safe in dev)
pytest
npm test
npm run test
jest

# Git read operations (safe)
git status
git log
git diff
git show
git branch

# Build commands (safe)
npm run build
npm run dev
python setup.py build

# Linting/formatting (safe)
black .
flake8
eslint
prettier
```

### Commands to ALWAYS Reject or Review Carefully

```bash
# File deletion
rm -rf *
rmdir

# System changes
sudo *
chmod
chown

# Data operations
DROP *
DELETE *
TRUNCATE *

# Network operations with unknown destinations
curl * (unknown URLs)
wget * (unknown URLs)

# Destructive git
git reset --hard
git clean -fd
git push --force
```

### The Golden Rule

**Never approve commands you don't understand.**

If Copilot suggests a command and you're unsure:
1. Ask Copilot to explain the command first
2. Research what it does
3. Only then approve or reject

---

## 3. Creating Practice Projects Quickly

### Why Generate Practice Code?

**Learning benefits:**
- Something to search through
- Examples to analyze
- Code to reference with #mentions
- Patterns to understand

**Agent Mode is perfect for this:**
- Generates complete structure
- Includes best practices
- Working code examples
- Takes seconds, not hours

### The Practice Project Structure

```
project/
├── routes/          # API endpoints (3 files)
│   ├── hello.py    # Basic endpoint examples
│   ├── users.py    # Authentication patterns
│   └── items.py    # CRUD operations
│
├── helpers/         # Utility functions (2 files)
│   ├── auth.py     # Authentication logic
│   └── validate.py # Input validation
│
└── main.py          # Entry point (1 file)
```

**Why this structure?**
- **3 layers** demonstrate organization
- **6 files** make workspace search useful
- **Simple enough** to understand quickly
- **Real patterns** to learn from

### What's in Each File

**routes/hello.py:**
- Basic FastAPI endpoint
- Error handling example
- Docstrings and type hints

**routes/users.py:**
- User endpoints
- Authentication required
- Dependency injection pattern

**routes/items.py:**
- CRUD operations
- Validation examples
- Status codes

**helpers/auth.py:**
- Token verification
- User authentication
- Dependency for routes

**helpers/validate.py:**
- Email validation
- Password strength
- Input sanitization

**main.py:**
- FastAPI app initialization
- Router registration
- Basic configuration

### Using This for Practice

**For @workspace search:**
```
"@workspace authentication logic" → finds auth.py patterns
"@workspace validation" → finds validate.py functions
"@workspace error handling" → finds try/except blocks
```

**For #mentions:**
```
#file:routes/users.py → reference specific file
#folder:helpers → reference entire directory
#file:main.py → reference entry point
```

**This structure is your playground for Session 1!**

---

## 4. AI Modes - Complete Usage Guide

### Learning Flow

**In the workshop, you:**
1. **Learned** all modes conceptually (overview)
2. **Experienced** Agent Mode by generating your practice project
3. **Saw** quick demos of Ask, Edit, and Plan modes
4. **Practiced** switching between modes

**Why this order?**
- Understanding WHAT each mode does (before using it)
- Experiencing the most impressive mode first (Agent Mode)
- Building something useful immediately (practice project)
- Reinforcing through practice (mode switching exercise)

**Now let's dive deep into each mode...**

---

### Ask Mode ❓ - The Wise Advisor

**Purpose:** Think before you act, explore options

**Best for:**
- Planning architecture
- Understanding existing code
- Exploring alternatives
- Learning new concepts
- Discussing trade-offs

**Example prompts:**
```
Good:
"What's the best way to structure a FastAPI app with:
- User authentication
- Role-based permissions
- Database migrations
- Testing setup

Show me 3 approaches with pros/cons."

Bad:
"Create a FastAPI app" [too vague, use Agent Mode]
```

**How to access:**
- Select "Ask" from the agents dropdown in Copilot Chat

---

### Edit Mode ✏️ - The Precise Editor

**Purpose:** Make controlled edits to specific files

**Best for:**
- Modifying existing code
- Multi-file coordinated changes
- When you want to control exactly which files change
- Reviewing changes before applying

**Example prompts:**
```
Good:
"Add error handling to all endpoints in the routes folder"
[Add routes/hello.py, routes/users.py, routes/items.py to working set]

"Refactor these files to use async/await"
[Select specific files in working set]
```

**How to access:**
- Select "Edit" from the agents dropdown
- Add files to the working set

**Key feature:** You control the working set of files

---

### Agent Mode 🤖 - The Builder

**Purpose:** Autonomous implementation

**Best for:**
- Creating new features
- Multi-step tasks
- When you want Copilot to figure out what files to create/modify
- Complex implementations

**Example prompts:**
```
Good:
"Create a FastAPI endpoint for user registration:
- POST /api/users/register
- Input: email, password, full_name
- Validate email format
- Hash password with bcrypt
- Return user ID and token
- Handle duplicate email error"

Bad:
"What should a registration endpoint look like?" 
[use Ask Mode for this]
```

**How to access:**
- Select "Agent" from the agents dropdown

**Key feature:** Copilot autonomously determines what files to create/modify and can run terminal commands

---

### Plan Mode 📋 - The Architect

**Purpose:** Create detailed implementation plans before coding

**Best for:**
- Complex features that need thinking through
- When you want to review the approach before implementing
- Architecture decisions
- Multi-step implementations

**Example prompts:**
```
Good:
"Create a plan for adding user authentication with:
- JWT tokens
- Refresh token rotation
- Password reset flow
- Email verification"

Result: Detailed step-by-step plan
Then: Click "Start Implementation" to hand off to Agent Mode
```

**How to access:**
- Select "Plan" from the agents dropdown

**Key feature:** Research and planning without code changes, then hand off to Agent Mode

---

### Inline Chat ⚡ - The Quick Fix

**Purpose:** Inline edits without opening chat

**How to use:**
1. Select code (or place cursor)
2. Press `Cmd+I` (Mac) or `Ctrl+I` (Windows/Linux)
3. Type instruction
4. Press Enter
5. Review diff and accept/reject

**Best for:**
- Adding type hints
- Adding docstrings
- Renaming variables
- Quick refactors
- Fixing single issues

**Example usage:**
```python
# Before (cursor on this function)
def calculate(a, b):
    return a + b

# Inline Chat: "add type hints and docstring"

# After
def calculate(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b
```

---

## 5. Recovery and Safety Features

### Overview: Your Safety Net

VS Code + Git provide multiple layers of protection:

1. **Undo (Cmd+Z)** - Immediate undo of changes
2. **Git Integration** - Stage/discard changes, commit checkpoints
3. **Accept/Reject** - Review changes before applying

---

### 1. Standard Undo

**Purpose:** Instantly undo recent changes

**How to use:**
- `Cmd+Z` (Mac) or `Ctrl+Z` (Windows)
- Multiple times to go back further

**Best for:** Quick mistakes, unwanted AI additions

---

### 2. Git Integration

**Purpose:** Version control and checkpoint management

**How to use:**
```
1. Stage changes you want to keep:
   - Click + next to changed files in Source Control
   
2. Discard changes you don't want:
   - Right-click file → Discard Changes
   
3. Commit at checkpoints:
   - Write message → Commit
   - Now you can always return to this state
```

**Professional workflow:**
```
1. Commit working state
2. Start new feature with Agent Mode
3. Review changes
4. Like it? → Stage and commit
5. Don't like it? → Discard changes
```

---

### 3. Accept/Reject in Edit Mode

**Purpose:** Review before applying

**How it works:**
1. Edit Mode shows proposed changes as diffs
2. For each file, you see:
   - Current code (left)
   - Proposed changes (right)
3. Click Accept or Discard for each change

**Why this is powerful:**
- No surprise changes
- Review each modification
- Partial acceptance possible

---

### Recovery Strategy

| Situation | Solution |
|-----------|----------|
| Just made a mistake | Cmd+Z (Undo) |
| Don't like AI's changes | Discard Changes in Source Control |
| Want to try different approach | Discard, then try again |
| Multiple file changes to review | Edit Mode → Accept/Reject each |
| Need to return to earlier state | Git reset to previous commit |
| Major experiment about to start | Git commit first as checkpoint |

**Golden rule:** Commit often, discard freely, experiment boldly!

---

## 6. Inline AI Tools - The Superpowers

### Ghost Text / Inline Completions

**What it is:**
AI-powered code completion that suggests code as you type.

**How it works:**
- Analyzes your codebase and coding patterns
- Predicts what you'll write next
- Shows gray "ghost text" suggestion

**Controls:**
- **Tab:** Accept suggestion
- **Esc:** Reject suggestion
- **Keep typing:** Refine/change suggestion

**Best practices:**
1. **Start typing function name** → Get full implementation
   ```python
   # Type: def calculate_total
   # Ghost text suggests:
   def calculate_total(items: list[dict]) -> float:
       """Calculate total price from list of items."""
       return sum(item['price'] * item['quantity'] for item in items)
   ```

2. **Write docstring** → Get function body
   ```python
   def process_payment():
       """Process a payment and return transaction ID."""
       # Ghost text suggests the implementation
   ```

**Why it's powerful:**
- Context-aware (learns from YOUR code)
- Multi-line predictions
- Always available as you type

---

### Inline Chat (Cmd+I) - Quick Edits

**What it is:**
Inline AI edits without opening Copilot Chat panel.

**How to use:**
1. **Select code** (or place cursor)
2. **Press `Cmd+I`** (Mac) or `Ctrl+I` (Windows/Linux)
3. **Type instruction** (e.g., "add type hints")
4. **Review DIFF PREVIEW** (shows before/after)
5. **Accept or reject** the changes

**Use cases:**

**1. Quick Refactoring**
```python
# Select this code, Cmd+I: "extract to separate function"
result = sum(item['price'] * item['quantity'] for item in items)

# Becomes:
def calculate_total(items):
    return sum(item['price'] * item['quantity'] for item in items)

result = calculate_total(items)
```

**2. Adding Documentation**
```python
# Cmd+I on function: "add comprehensive docstring"
def process_order(order_id: str, user_id: str):
    pass

# Becomes:
def process_order(order_id: str, user_id: str):
    """Process an order for a user.
    
    Args:
        order_id: Unique identifier for the order
        user_id: User making the order
        
    Returns:
        Processed order object
    """
    pass
```

**3. Converting Code**
```python
# Cmd+I: "convert to async"
def get_user(user_id):
    return db.query(User).filter(User.id == user_id).first()

# Becomes:
async def get_user(user_id):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

**Benefits:**
- No context switching (stays inline)
- See diff before accepting (safe)
- Faster than Agent Mode for small changes
- Perfect for focused edits

---

### Inline Tools Summary

| Tool | Activation | Purpose |
|------|------------|---------|
| **Ghost Text** | Automatic as you type | Code prediction/completion |
| **Inline Chat** | Cmd+I / Ctrl+I | Quick inline edits with diff |

**Pro workflow:**
1. **Type** (ghost text suggests)
2. **Tab** (accept suggestion)
3. **Cmd+I** (quick refinements when needed)

**Result:** Lightning-fast coding with AI assistance!

---

## 7. Choosing the Right Mode - Decision Framework

**The key to faster development: Pick the right mode!**

```
What do I need to do?

├─ Planning / Exploring / Questions?
│  └─ Ask Mode ❓
│
├─ Creating detailed implementation plan?
│  └─ Plan Mode 📋
│
├─ Implementing new features autonomously?
│  └─ Agent Mode 🤖
│
├─ Controlled edits to specific files?
│  └─ Edit Mode ✏️
│
├─ Quick inline edit to existing code?
│  └─ Inline Chat ⚡ (Cmd+I)
│
└─ Finding where something is?
   └─ @workspace search
```

**Real-world examples:**

| Scenario | Wrong Mode | Right Mode | Why |
|----------|------------|------------|-----|
| "Should I use REST or GraphQL?" | Agent | **Ask** | Need to explore options |
| "Create user authentication" | Ask | **Agent** | Need implementation |
| "Add type hint to this function" | Agent | **Inline Chat** | Quick inline fix |
| "Where is authentication logic?" | Ask | **@workspace** | Finding existing code |
| "Plan a new feature" | Agent | **Plan** | Think before building |

---

## 8. #mentions - Complete Context Guide

### #file - Specific File Context

**Syntax:** `#file:path/to/file.ext`

**Use when:**
- Modifying specific file
- Asking about file's purpose
- Adding to existing code

**Example prompts:**
```
Good:
"Looking at #file:routes/hello.py, add logging to track greetings"
"Refactor #file:helpers/auth.py to use async token verification"
"Add rate limiting to #file:routes/users.py endpoints"
```

**Pro tip:** Works with any file in workspace

---

### #folder - Directory Context

**Syntax:** `#folder:path/to/folder`

**Use when:**
- Analyzing patterns across files
- Creating files following existing patterns
- Understanding module structure

**Examples:**
```
"What patterns do you see in #folder:routes?"
"Create a new route in #folder:routes following the same structure"
"Analyze #folder:helpers and suggest improvements"
```

**Pro tip:** Great for consistency

---

### #terminalSelection - Command Output Context

**Syntax:** `#terminalSelection` (includes selected terminal output)

**Use when:**
- Debugging errors
- Understanding command output
- Fixing test failures

**How to use:**
```
1. Run command that produces output/error
2. Select the relevant output in terminal
3. In Chat: "Fix this error: #terminalSelection"
```

**Pro tip:** Saves copying/pasting errors

---

### #problems - IDE Errors Context

**Syntax:** `#problems`

**Use when:**
- Fixing multiple errors at once
- Addressing linting issues
- Resolving type errors

**Examples:**
```
Agent Mode:
"Fix all issues in #problems"

Ask Mode:
"Why am I getting these errors? #problems"
```

**Pro tip:** Faster than fixing one-by-one

---

### #codebase / @workspace - Full Codebase Search

**Syntax:** `@workspace query` or `#codebase`

**Use when:**
- Finding code by meaning
- Understanding project structure
- Locating implementations

**Examples:**
```
"@workspace where is authentication implemented?"
"@workspace find all database queries"
"@workspace validation logic"
```

**Pro tip:** Semantic search - finds by meaning, not just text

---

### #fetch - Web Content

**Syntax:** `#fetch:URL`

**Use when:**
- Need accurate API reference
- Learning new framework
- Ensuring correct usage

**Examples:**
```
"#fetch:https://fastapi.tiangolo.com - 
How do I add WebSocket support?"
```

**Pro tip:** Gets current documentation

---

## 9. Custom Instructions - Your AI's Personality

### What Are Custom Instructions?

Custom instructions tell Copilot HOW you want code written. They're automatically included in every interaction.

**Location:** `.github/copilot-instructions.md`

**Scope:** Entire repository

### Creating Effective Instructions

**Recommended sections:**

```markdown
# Project Overview
Brief description, tech stack, purpose

# Coding Standards
- Type hints on all functions
- Google-style docstrings
- async/await for I/O operations
- Max line length: 100 chars
- PEP 8 compliant

# Architecture Patterns
- 3-tier: API → Service → Repository
- Dependency injection
- Repository pattern for data access

# Error Handling
- Use HTTPException for API errors
- Log all errors before raising
- Never expose internal errors to clients

# Naming Conventions
- Files: snake_case
- Classes: PascalCase
- Functions: snake_case
- Constants: UPPER_SNAKE_CASE
```

### Path-Specific Instructions

For different rules in different parts of your codebase:

```
.github/instructions/
├── api.instructions.md      # For routes/
├── tests.instructions.md    # For tests/
└── docs.instructions.md     # For documentation
```

Each file uses YAML frontmatter to specify paths:
```yaml
---
applyTo: "routes/**/*.py"
---
# API-specific instructions here
```

---

## 10. Self-Assessment Quiz

**1. What should ALWAYS be in .copilotignore?**
Answer: .env files, API keys, secrets, credentials

**2. How does Copilot handle terminal commands in Agent Mode?**
Answer: Shows preview and asks for confirmation before running

**3. Which AI mode is best for planning?**
Answer: Ask Mode (or Plan Mode for detailed plans)

**4. Which AI mode is fastest for inline edits?**
Answer: Inline Chat (Cmd+I)

**5. What #mention includes terminal output?**
Answer: #terminalSelection

**6. Where do custom instructions go?**
Answer: `.github/copilot-instructions.md`

**7. How do you search your entire codebase?**
Answer: @workspace query

**8. What are the 4 main Copilot modes?**
Answer: Ask, Edit, Agent, Plan

**9. How do you access Inline Chat?**
Answer: Cmd+I (Mac) or Ctrl+I (Windows)

**10. What's the golden rule for terminal commands?**
Answer: Never approve commands you don't understand

---

## 11. Further Reading

**Official Docs:**
- GitHub Copilot: docs.github.com/en/copilot
- VS Code Copilot: code.visualstudio.com/docs/copilot
- Copilot Chat: docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide

**Next Session Preview:**
- Professional workflow: Explore → Plan → Code → Commit
- Context + Task + Constraints + Format formula
- Thinking modes for complex decisions
- Building first feature

---

**End of Student Reference: Micro Session 1** 🎓
