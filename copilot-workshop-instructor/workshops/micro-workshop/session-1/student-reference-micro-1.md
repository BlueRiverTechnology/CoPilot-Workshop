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

## 9. Writing Effective AI Rules - Complete Guide

### What Are Custom Instructions?

Custom instructions are **always-on context** that tells Copilot HOW you want code written. They're automatically included in every interaction, multiplying your productivity by eliminating the need to repeat guidelines in every prompt.

**This is one of the most transferable skills—every project benefits from well-written AI rules.**

---

### The Complete Rules Ecosystem

There are now **multiple layers** of instruction files. Understanding this hierarchy is crucial:

```
📁 Your Project
├── .github/
│   ├── copilot-instructions.md          ← REPO-WIDE (always active)
│   ├── instructions/
│   │   ├── testing.instructions.md      ← PATH-SPECIFIC (tests/** only)
│   │   ├── api.instructions.md          ← PATH-SPECIFIC (api/** only)
│   │   └── services.instructions.md     ← PATH-SPECIFIC (services/** only)
│   └── agents/
│       └── code-reviewer.agent.md       ← CUSTOM AGENT (Session 4)
├── AGENTS.md                             ← CROSS-TOOL (Copilot, Claude, Cursor)
└── VS Code Settings
    ├── Code generation instructions
    ├── Test generation instructions
    ├── Review instructions
    └── Commit message instructions
```

**The hierarchy:**

1. **`.github/copilot-instructions.md`** - Repository-wide, always active. Works in Chat, Agent Mode, and Code Review.
2. **`.github/instructions/*.instructions.md`** - Path-specific rules with `applyTo` glob frontmatter. Only active when working on matching files.
3. **`.github/agents/*.agent.md`** - Custom agent definitions (covered in Session 4).
4. **`AGENTS.md`** - Emerging open standard from Linux Foundation. Works across Copilot, Claude Code, Cursor, and other AI tools.
5. **VS Code settings** - Per-operation instructions (code generation, test generation, review, commit messages).

**The skill you learn for one layer applies to ALL layers.**

---

### Research-Backed Principles - What Makes Rules Work

Not all rules are equal. Research from GitHub, Anthropic, and the AI engineering community shows clear patterns for what works.

---

#### Principle 1: Short, Imperative, Self-Contained Statements

**Source:** GitHub's official documentation

GitHub's own docs say instructions should be "short, self-contained statements that add context." Not paragraphs. Not essays.

**BAD:**
```markdown
We generally try to follow industry best practices for code quality and
maintainability, so please write code that is clean and well-tested. We
also prefer using modern Python features when appropriate and avoiding
deprecated patterns.
```

**GOOD:**
```markdown
- Use type hints on all function signatures
- Write pytest tests for every service method
- Use Python 3.11+ features (match/case, type unions with |)
```

**Why it works:**
- Specific, actionable, scannable
- AI can quickly parse discrete rules
- Each statement stands alone

---

#### Principle 2: Tell the AI What TO DO, Not What to Avoid

**Source:** AI engineering community best practices

LLMs are poor at negations. Positive directives work better than negative prohibitions.

**BAD:**
```markdown
- Don't use print statements for debugging
- Avoid using global variables
- Don't hardcode configuration values
```

**GOOD:**
```markdown
- Use `logging` module at DEBUG level for diagnostic output
- Pass configuration through dependency injection
- Load configuration from environment variables via python-dotenv
```

**Why it works:**
- The GOOD version tells AI the correct alternative
- Provides a pattern to follow, not just something to avoid
- Reduces ambiguity about what to do instead

---

#### Principle 3: Be Specific and Actionable

**Source:** GitHub documentation and practical experience

Vague aspirational goals don't work. Concrete patterns do.

**BAD:**
```markdown
- Follow good naming conventions
- Make sure code is well-tested
- Use proper error handling
```

**GOOD:**
```markdown
- Use camelCase for JavaScript variables and functions. Use PascalCase for classes.
- Every service method must have a corresponding test file in tests/services/
- Use HTTPException for API errors with proper status codes (400/401/403/404/500)
```

**Why it works:**
- Zero ambiguity = better compliance
- AI knows exactly what pattern to follow
- Reduces variation in generated code

---

#### Principle 4: Use Structured Markdown (or XML for Claude-based tools)

**Source:** GitHub and Anthropic best practices

Copilot parses structured content better than prose. Use distinct headings, bullet points, code examples.

**For GitHub Copilot (Markdown structure):**

```markdown
# Project: Todo API

## Architecture Patterns
- 3-tier structure: API routes → Service layer → Models
- All database operations in service layer
- Pydantic v2 for all request/response schemas

## Coding Standards
- Use type hints on every function signature
- Write Google-style docstrings
- Follow PEP 8, max line length 100

## Error Handling
- Use HTTPException for API errors
- Log all errors before raising
- Never expose internal error details to clients
```

**For Claude-based tools (XML tags):**

Anthropic specifically recommends using XML tags to structure instructions. XML tags create clear boundaries that prevent the AI from mixing up context, instructions, and examples.

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

**Key principle:** Whether you use XML tags or Markdown headings depends on the tool—Copilot prefers Markdown structure, Claude prefers XML—but the principle is the same: **Create clear, labeled compartments for different types of information.**

**Why it works:**
- AI can quickly locate relevant sections
- Clear separation between different concerns
- Reduces context bleed between topics

---

#### Principle 5: Include Code Examples Where They Clarify Intent

**Source:** Practical experience and prompt engineering best practices

A before/after code snippet removes ambiguity. Show the pattern, don't just describe it.

**Instead of:** "Use proper error handling"

**Show this:**

```markdown
## Error Handling Pattern

Use HTTPException for API errors with proper status codes:

```python
# GOOD - Do this
async def get_user(user_id: str) -> User:
    try:
        return await db.get(User, user_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
    except DatabaseError as e:
        logger.error(f"Database error fetching user {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# BAD - Don't do this
async def get_user(user_id: str):
    user = await db.get(User, user_id)  # Can raise unhandled exceptions
    return user
```
```

**Why it works:**
- Concrete example is unambiguous
- Shows exact pattern to follow
- BAD example clarifies what to avoid

---

#### Principle 6: Keep Files Under ~1,000 Lines

**Source:** GitHub official documentation

GitHub explicitly warns: beyond 1,000 lines, quality deteriorates.

**Why it matters:**
- AI models have token limits
- Long files dilute important instructions
- Parsing quality degrades with length

**Best practice:**
- Start with 5-10 rules
- Add iteratively based on actual needs
- If file grows large, split into path-specific instructions

---

#### Principle 7: Iterate Based on What Works

**Source:** Empirical best practice

Rules writing is empirical, not theoretical. You must test and refine.

**The process:**

1. **Start minimal:** Write 5-10 core rules
2. **Test them:** Use Copilot on real tasks
3. **Check compliance:** Does Copilot follow your rules?
4. **Verify usage:** Check References section in Copilot Chat
5. **Refine:** Add rules where Copilot deviates from your preferences
6. **Remove:** Delete rules that Copilot ignores or doesn't need

**This is the most important principle: Rules are a living document.**

---

### How to Verify Copilot is Using Your Rules

**Method 1: Check References Section**

In Copilot Chat responses, look for the References section at the bottom. It will show `.github/copilot-instructions.md` when Copilot reads your rules.

**Method 2: Test Compliance**

Give Copilot a task and check if the output follows your rules:
- Did it use type hints? (if your rule says to)
- Did it use async/await? (if your rule says to)
- Did it follow your naming conventions?

**Method 3: Ask Copilot Directly**

```
@workspace What coding standards should I follow in this project?
```

Copilot should reference your custom instructions.

---

### Path-Specific Instructions - Advanced Rules Scoping

**Why use path-specific instructions?**

Different parts of your codebase have different requirements:
- **API routes:** Need endpoint docs, status codes, validation
- **Tests:** Need AAA pattern, fixtures, mocking
- **Services:** Need business logic patterns, error handling
- **Documentation:** Need clear writing, consistent formatting

**How to create path-specific instructions:**

**File structure:**
```
.github/instructions/
├── api.instructions.md
├── testing.instructions.md
├── services.instructions.md
└── documentation.instructions.md
```

**Example: `.github/instructions/testing.instructions.md`**

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
- Use scope="function" for test isolation

## Mocking
- Mock external API calls
- Use pytest-mock for all mocking
- Never make real external API calls in tests

## Coverage
- Aim for 80%+ code coverage
- Test happy path and error cases
- Include edge cases and boundary conditions
```

**How it works:**

- Path-specific instructions **stack with** repo-wide instructions
- When working on test files, Copilot sees **both** `.github/copilot-instructions.md` **and** `.github/instructions/testing.instructions.md`
- Use glob patterns in `applyTo`: `"**/*.py"`, `"**/tests/**"`, `"src/api/**"`

**Examples of glob patterns:**

```yaml
applyTo: "**/*.py"              # All Python files
applyTo: "**/tests/**"          # All files in tests directories
applyTo: "src/api/**/*.py"      # Python files in src/api
applyTo: "**/*.{ts,tsx}"        # TypeScript files
applyTo: "**/README.md"         # All README files
```

---

### The AGENTS.md Cross-Tool Standard

**What is it?**

An emerging open standard from the Linux Foundation for AI instructions that work across multiple tools.

**Location:** `AGENTS.md` in project root

**Why use it?**

- Works with Copilot, Claude Code, Cursor, and other AI tools
- Team members can use different tools with same context
- Future-proof as AI tooling evolves

**Example AGENTS.md:**

```markdown
# Agents

This project uses AI-assisted development. These guidelines apply to all AI tools.

## Role
Senior Python developer specializing in FastAPI and async web applications.

## Architecture
- 3-tier structure: API routes → Service layer → SQLAlchemy models
- All database operations use async/await with SQLAlchemy
- Pydantic v2 for request/response validation

## Coding Standards
- Type hints required on all function signatures
- Google-style docstrings for all public functions
- PEP 8 compliant, max line length 100
- async/await for all I/O operations

## Error Handling
- Use HTTPException for API errors with proper status codes
- Log all errors before raising
- Never expose internal error details to API clients

## Testing
- pytest for all tests
- AAA pattern: Arrange, Act, Assert
- Fixtures in conftest.py
- Mock external dependencies
```

**When to use AGENTS.md vs .github/copilot-instructions.md:**

- **Use `.github/copilot-instructions.md`** for GitHub Copilot-specific features
- **Use `AGENTS.md`** for cross-tool compatibility
- **Use both** if your team uses multiple AI tools

---

### How Rules Connect to Everything Else

**Rules are the foundation of the professional workflow you'll learn in Session 2:**

**Rules + PRD + Memory Bank = Copilot that truly knows your project**

**The progression:**

1. **Session 1:** Custom instructions (always-on context)
2. **Session 2:** PRD files (feature-specific context)
3. **Session 4:** Memory Bank (project knowledge repository)

**Why this matters:**

- Custom instructions are **always-on context** that saves you from repeating yourself
- Every prompt you write from now on benefits from these rules
- This is context mastery—what separates AI amateurs from AI professionals

**The professional workflow:**

```
1. Write effective rules (Session 1) → AI knows your standards
2. Create PRDs (Session 2) → AI knows your features
3. Build Memory Bank (Session 4) → AI knows your decisions
4. Use #mentions and @workspace → AI has perfect context
5. Write concise prompts → AI delivers exactly what you need
```

**This is the path to 2-5x productivity gains.**

---

### Common Anti-Patterns to Avoid

**1. Writing essays instead of rules**

```markdown
❌ BAD:
We believe that code quality is very important and we generally try to
maintain high standards across the codebase. When writing new code, please
keep in mind that readability matters and future developers will need to
understand what you've written.

✅ GOOD:
- Write self-documenting code with clear variable names
- Add docstrings to all public functions
- Use type hints for function signatures
```

**2. Negative prohibitions without alternatives**

```markdown
❌ BAD:
- Don't use print for debugging
- Avoid global variables
- Don't hardcode values

✅ GOOD:
- Use `logging` module at DEBUG level for diagnostics
- Pass configuration through dependency injection
- Load config from environment variables via python-dotenv
```

**3. Vague aspirational statements**

```markdown
❌ BAD:
- Follow best practices
- Write clean code
- Be consistent

✅ GOOD:
- Use async/await for all I/O operations
- Follow PEP 8 style guide, max line length 100
- Use snake_case for functions, PascalCase for classes
```

**4. Including instructions that AI already knows**

```markdown
❌ BAD:
- Python functions start with def
- Classes use class keyword
- Variables store values

✅ GOOD:
- Use Pydantic v2 BaseModel for all schemas
- Use UUID strings for primary keys (not integers)
- Fixed owner_id = "default-user" for simplified auth
```

**5. Making rules too long**

```markdown
❌ BAD:
A 2,000-line custom instructions file covering every possible scenario

✅ GOOD:
Start with 5-10 core rules, add iteratively based on what Copilot actually needs guidance on
```

---

### Template for Your Project

**Copy this template and adapt it to your project:**

```markdown
# Project: [YOUR PROJECT NAME]

## Overview
[1-2 sentence description of what this project does]
[Tech stack: Python 3.11+, FastAPI, SQLAlchemy, PostgreSQL, etc.]

## Architecture Patterns
- [Your architecture: 3-tier, microservices, monolith, etc.]
- [Key patterns: dependency injection, repository pattern, etc.]
- [Data layer: ORM, raw SQL, etc.]

## Coding Standards
- Use type hints on all function signatures
- Write [docstring style] docstrings for all public functions
- Follow [style guide: PEP 8, Black, etc.]
- Max line length: [80/100/120] characters
- Use [async/sync] for I/O operations

## Naming Conventions
- Files: [snake_case/kebab-case]
- Classes: [PascalCase]
- Functions: [snake_case/camelCase]
- Constants: [UPPER_SNAKE_CASE]

## Error Handling
- [How to handle API errors: HTTPException, custom exceptions, etc.]
- [Logging requirements: log level, format, etc.]
- [What to expose vs hide in error messages]

## Testing
- [Test framework: pytest, unittest, jest, etc.]
- [Test structure: AAA, Given-When-Then, etc.]
- [Coverage requirements: 80%, 90%, etc.]
- [Mocking requirements: mock external APIs, databases, etc.]

## [Project-Specific Section]
- [Add any project-specific rules here]
- [Authentication patterns, caching strategies, etc.]
```

---

### Quick Reference: Rules Writing Checklist

Before finalizing your custom instructions, check:

- [ ] **Short statements** - Each rule is one concise line
- [ ] **Positive directives** - Tell AI what TO do, not what to avoid
- [ ] **Specific and actionable** - Zero ambiguity about what's expected
- [ ] **Structured with headings** - Clear sections for different concerns
- [ ] **Code examples included** - Show patterns where helpful
- [ ] **Under 1,000 lines** - Start minimal, add iteratively
- [ ] **Tested with Copilot** - Verified that Copilot follows them
- [ ] **References visible** - Check that Copilot reads them in chat

**Remember: Rules are a living document. Start small, test, iterate.**

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

**6. Where do repo-wide custom instructions go?**
Answer: `.github/copilot-instructions.md`

**7. What makes a GOOD rule vs a BAD rule?**
Answer: Good = short, specific, positive directive (what TO do). Bad = vague, negative, or too long.

**8. Why use XML tags in rules for Claude-based tools?**
Answer: Creates clear boundaries that prevent AI from mixing up context, instructions, and examples.

**9. How do you verify Copilot is reading your rules?**
Answer: Check the References section in Copilot Chat responses.

**10. What's Principle 2 of effective rules writing?**
Answer: Tell the AI what TO DO, not what to avoid (LLMs are poor at negations).

**11. How do you search your entire codebase?**
Answer: @workspace query

**12. What are the 4 main Copilot modes?**
Answer: Ask, Edit, Agent, Plan

**13. How do you access Inline Chat?**
Answer: Cmd+I (Mac) or Ctrl+I (Windows)

**14. What's the golden rule for terminal commands?**
Answer: Never approve commands you don't understand

**15. What's the recommended max length for custom instructions files?**
Answer: Under ~1,000 lines (GitHub warns quality deteriorates beyond this)

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
