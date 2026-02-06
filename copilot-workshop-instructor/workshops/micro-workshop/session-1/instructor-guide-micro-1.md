# Instructor Guide: Micro Session 1
## Security & Superpowers 🛡️⚡

**Duration:** 60 minutes  
**Prerequisites:** VS Code and GitHub Copilot installed, GitHub account with Copilot access

---

## Session Overview

### Learning Objectives
- ✅ Configure security-first environment (.copilotignore, terminal controls)
- ✅ Master all AI interaction modes (Ask, Edit, Agent, Plan)
- ✅ Use all #mention types for context management
- ✅ Understand Custom Instructions
- ✅ Create first .github/copilot-instructions.md file


### [0:02-0:10] 🛡️ Security First - The Foundation

**ENERGY:** Serious but empowering

**SAY:**
> "Before we move fast, we need to move safely. Three security foundations - we'll set these up in 8 minutes."

---

#### [0:02-0:05] .copilotignore Configuration (3 min)

**DO - Show on screen:**

**SAY:**
> "First rule: Your secrets stay secret. Create `.copilotignore` in your project root."

**SHOW FILE:**
```bash
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

**SAY:**
> "Why this matters: If AI reads your `.env` file or shares it, your keys are compromised. This prevents that."


**VERIFICATION:**
```bash
# Test it works
echo "test-secret-key" > .env
# Open Copilot Chat and type: "#file .env"
# It should show: "This file is ignored" or not find the file
```

**SAY:**
> "✅ If you see 'file is ignored' - you're protected! 🛡️"

---

#### [0:05-0:08] Terminal Command Controls (3 min)

**SAY:**
> "AI can run terminal commands in Agent Mode. That's powerful... and requires your approval. Let's understand the safety model."

**DO - Explain Copilot's Approach:**

**SAY:**
> "GitHub Copilot takes a **confirmation-first approach**. When Agent Mode wants to run a terminal command, it shows you exactly what it plans to run and waits for your approval.
>
> You'll see:
> - The exact command it wants to run
> - A 'Continue' button to approve
> - The option to reject and try something else
>
> This is your safety net. Always review commands before approving!"

**SHOW EXAMPLE WORKFLOW:**
```
Agent Mode suggests: pip install fastapi uvicorn
[Continue] [Cancel]

You click Continue → Command runs
You click Cancel → Agent tries another approach
```

**SAY:**
> "Key safety rule: **Never approve commands you don't understand.**
>
> Example: AI wants to run `rm -rf /` → You see preview → You reject it.
> Example: AI wants to run `pytest` → You understand it → Approve it.
>
> You're always in control!"

---

### [0:10-0:13] 🎮 All AI Modes - Overview (3 min)

**SHOW VISUAL:**
```
❓ Ask Mode = "The Wise Advisor"
   - Thinks WITH you
   - Explores options
   - Answers questions
   - No code changes

✏️ Edit Mode = "The Precise Editor"  
   - Controlled edits to specific files
   - You choose the working set
   - Review each change before applying

🤖 Agent Mode = "The Builder"
   - Implements FOR you autonomously
   - Creates files
   - Runs terminal commands
   - Iterates until task complete

📋 Plan Mode = "The Architect" (Preview)
   - Creates detailed implementation plans
   - Research before implementation
   - Click "Start Implementation" to hand off to Agent
```

**SAY:**
> "That's the overview. Now let's experience the most powerful one - Agent Mode - by building something REAL!"

---

### [0:13-0:18] 🏗️ Agent Mode + Practice Project Generation (5 min)

**ENERGY:** Exciting, "watch this magic" energy

**SAY:**
> "Agent Mode is your builder. It creates entire files, complete features, working code.
>
> Let me show you. We need a practice project. Watch me generate one in 30 seconds with Agent Mode..."

---

#### [0:13-0:14] Instructor Demo (1 min)

**DO - Demonstrate in Agent Mode:**

1. **Open Copilot Chat** (click Copilot icon in title bar or Cmd+Shift+I)
2. **Select Agent from the agents dropdown** at bottom of chat
3. **SAY:** "I'm going to ask Agent Mode to build an entire project structure"
4. **Type this prompt** (show on screen):

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

5. **Press Enter**

**SAY while generating:**
> "Watch... it's creating all 6 files... complete working code... docstrings... error handling... authentication patterns...
>
> [Files appear]
>
> Done! 30 seconds. 6 files. Complete project. THAT'S Agent Mode power! 🚀"

**SHOW:** File explorer with all generated files

---

#### [0:14-0:17] Students Generate Their Project (3 min)

**SAY:**
> "Your turn! Everyone copy that prompt into Agent Mode and generate YOUR practice project.
>
> This is your first Agent Mode experience. Let's go!"

---

### [0:18-0:20] 🛡️ Copilot Safety Features (2 min)

**ENERGY:** Reassuring, practical

**SAY:**
> "Before we dive deeper, let me show you safety features.
>
> Because you'll experiment, try things, sometimes code won't work out.
>
> Copilot + VS Code have your back!"

---

#### [0:18-0:19] Undo and Git Integration (1 min)

**SAY:**
> "Multiple ways to recover from AI changes:"

**DO - Demo:**
```
1. Standard Undo: Cmd+Z (Mac) / Ctrl+Z (Windows) 
   - Works for individual file changes
   
2. Git Integration:
   - Stage changes you like
   - Discard changes you don't (right-click → Discard Changes)
   - Commit at checkpoints
   
3. Accept/Reject in Edit Mode:
   - Edit Mode shows diffs BEFORE applying
   - Accept or Discard each change
```

**SAY:**
> "Key workflow: Work in small increments. Commit often.
>
> Agent Mode making too many changes? Stop it, undo, try a more specific prompt.
>
> Edit Mode shows diffs first - review before accepting!
>
> You're in control!"

---

#### [0:19-0:20] Review Before Accepting (1 min)

**SAY:**
> "In Edit Mode and Agent Mode, you see changes before they're final."

**SHOW:**
- Edit Mode: Diff preview with Accept/Discard buttons
- Agent Mode: Files in working set, option to review each

**SAY:**
> "Golden rule: **Review before you accept.**
>
> AI is powerful but not perfect. You're the final quality gate!"

---

### [0:20-0:25] ⚡ Inline AI Tools & Other Modes (5 min)

**ENERGY:** Fast-paced, show the superpowers

**SAY:**
> "Agent Mode: mastered! ✅ Now I'll show you the INLINE superpowers that work as you code!"

---

#### [0:21-0:22] Inline Chat - Quick Edits (1 min)

**SAY:**
> "Superpower: Inline Chat (Cmd+I) - edit code inline, no chat panel needed!"

**DO - Demo:**
```
1. Open routes/hello.py
2. Select the get_greeting function
3. Press Cmd+I (Mac) or Ctrl+I (Windows/Linux)
4. Type: "add type hints and docstring"
5. Shows DIFF PREVIEW
6. Accept or reject
```

**SAY:**
> "See that? AI shows you the DIFF before applying.
>
> Perfect for:
> - Quick refactoring
> - Adding docstrings
> - Converting code (sync→async)
> - Extracting methods
>
> Fast, inline, no chat needed. Lightning quick!"

---

#### [0:22-0:23] Ghost Text / Inline Completions (1 min)

**SAY:**
> "As you type, Copilot suggests completions in gray 'ghost text'. Press Tab to accept."

**DO - Demo:**
```
1. Open a Python file
2. Start typing: def calculate_
3. See ghost text suggestion appear
4. Press Tab to accept
5. Continue typing, more suggestions appear
```

**SAY:**
> "This is the original Copilot superpower - it's always there, always helping as you code!"

---

#### [0:24-0:25] Other Modes Quick Demo (1 min)

**SAY:**
> "Plus the other modes you've seen:"

**1. Ask Mode (15 sec):**
```
Select Ask from agents dropdown
Type: "What's the best way to add rate limiting?"
```
**SAY:** "THINKS with you. Planning, exploring. No code changes."

**2. Plan Mode (15 sec):**
```
Select Plan from agents dropdown
Type: "Create a plan to add user authentication"
```
**SAY:** "Creates detailed implementation plan. Click 'Start Implementation' to hand off to Agent Mode!"

**3. @workspace Search (15 sec):**
```
In chat: "@workspace authentication logic"
```
**SAY:** "Finds code by MEANING across your entire codebase!"

---

### [0:25-0:27] 🔄 Mode Switching Practice (2 min)

**SAY:**
> "Now YOU'LL practice switching between modes with two quick tasks.
>
> Task 1: Ask Mode - Ask about email validation
> - Select Ask from agents dropdown
> - Ask: 'How should I validate emails in Python?'
> - Read the response, understand the approach
>
> Task 2: Agent Mode - Implement the validation
> - Switch to Agent in agents dropdown
> - Prompt: 'Create email validation function in helpers/validate.py'
> - Watch it generate the code
>
> 1 minute for BOTH tasks - Experience the difference! ⏱️"

**TIMER:** 1 minute

**AT 1:00:**
> "Now reverse it! Start with AGENT, then understand with ASK.
>
> Task 3: Agent Mode FIRST - Add error handling
> - Agent Mode: 'Add error handling to routes/hello.py'
> - Watch it generate
>
> Task 4: Ask Mode - Understand what was added
> - Ask Mode: 'Explain the error handling in routes/hello.py'
> - See the difference in responses
>
> 1 minute - GO! ⏱️"

**AT 2:00:**
> "Stop! What did you notice? Ask Mode explains and discusses.
> Agent Mode builds and implements. Both powerful, different purposes!
> You just experienced BOTH workflows!"

**SAY:**
> "Key insight: 
> - Planning/Questions → Ask Mode
> - Building/Implementation → Agent Mode
> - Quick fixes → Inline Chat (Cmd+I)
> - Finding code → @workspace
>
> Right tool = 2x faster!"

🏆 **MICRO-ACHIEVEMENT:** "Mode Master" - Mastered mode switching!

---

### [0:27-0:32] 🎯 #mentions - Context Superpowers

**ENERGY:** Gamified and playful

**SAY:**
> "AI is only as good as the context you give it. #mentions are how you give AI x-ray vision into your project.
>
> Time for MENTION BINGO! 🎮"

**SHOW BINGO CARD (on screen or print):**
```
┌─────────────────────────────────┐
│  🎮 MENTION BINGO               │
├─────────────────────────────────┤
│  [ ] #file                      │
│  [ ] #codebase                  │
│  [ ] #folder                    │
│  [ ] #terminalSelection         │
│  [ ] #problems                  │
│  [ ] #fetch (web content)       │
└─────────────────────────────────┘
```

---

#### [0:27-0:32] Teach Each #mention (1 min each)

**1. #file - Specific File Context**

**SAY:**
> "#file tells AI: Look at THIS specific file."

**DEMO:**
```
Agent Mode:
"Looking at #file:routes/hello.py, add logging statements to track each greeting request"
```

**SHOW:** AI adds import logging, configures logger, adds log statements

---

**2. #folder - Directory Context**

**SAY:**
> "#folder shows AI everything in a directory."

**DEMO:**
```
Ask Mode:
"What patterns do you see in #folder:routes ?"
```

**SHOW:** AI analyzes all 3 route files (hello.py, users.py, items.py), describes:
- Endpoint patterns
- Authentication usage
- Error handling approaches
- Common structure

**SAY:**
> "See? It analyzed all 3 files at once and found the patterns!"

**STUDENT TRY:** "Try #folder:helpers or #folder:routes on your project. Check it off!"

---

**3. #terminalSelection - Include Command Output**

**SAY:**
> "#terminalSelection includes selected terminal output. Perfect for debugging!"

**DEMO:**

1. Create a simple file with runtime error:

```python
# test_calc.py
def divide(a, b):
    return a / b

result = divide(10, 0)
print(f"Result: {result}")
```

2. Run it in terminal:
```bash
python test_calc.py
```

3. Error appears: `ZeroDivisionError: division by zero`

4. Select the error in terminal, then in Ask Mode:
```
"Fix this error: #terminalSelection"
```

**SHOW:** AI sees the ZeroDivisionError from terminal, suggests adding error handling:
```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

---

**4. #problems - Fix IDE Errors**

**SAY:**
> Create a dummy file with syntax errors, then use #problems to fix them.

```python
# test_syntax.py
def hello(name)
    return f"Hello, {name}
```

> "#problems gives AI all your IDE warnings/errors at once."

**DEMO:**
```
Agent Mode:
"Fix all issues in #problems"
```

**SHOW:** AI fixes all linting errors, type issues, etc.

---

### [0:32-0:35] 📋 Custom Instructions - Your AI's Personality

**Purpose:**

Custom instructions let you define persistent guidelines that shape how Copilot behaves in your project. Instead of repeating context in every prompt, you set it once and Copilot follows it automatically.

**ENERGY:** Conceptual but crucial

**SAY:**
> "Last 5 minutes - the customization that changes everything."

---

#### [0:32-0:34] Custom Instructions File (2 min)

**SHOW VISUAL:**
```
.github/copilot-instructions.md

This file is automatically included in every Copilot interaction!

Contents:
- Project overview
- Coding standards
- Naming conventions
- Architectural guidelines
- Technology preferences
```

**SAY:**
> "Custom instructions tell Copilot HOW you want code written.
>
> Create once, applied everywhere. No more repeating 'use type hints' in every prompt!"

---

#### [0:34-0:35] Create First Custom Instructions File (1 min)

**SAY:**
> "Let's create your first custom instructions file."

**DO - Create the file:**

1. **Create folder:** `.github/` in project root
2. **Create file:** `copilot-instructions.md`
3. **Add content:**

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

**SAY:**
> "See? Clear sections for different guidelines.
>
> This file is automatically read by Copilot for every interaction!
>
> Because it's in `.github/`, it's project-specific. Perfect for team standards."

**STUDENT PRACTICE:**
> "Everyone create this file now. Customize the project overview for your style. 1 minute!"

**TIMER:** 1 minute

**AT 1:00:**
> "Done! ✅ You've got Custom Instructions. Copilot now knows your preferences!"

🎯 **CHECKPOINT:** Everyone has created their custom instructions file

---

**BONUS: Path-Specific Instructions**

**SAY:**
> "Want different rules for different parts of your code? Use path-specific instructions!"

```
.github/instructions/
├── api.instructions.md      # For routes/
├── tests.instructions.md    # For tests/
└── docs.instructions.md     # For documentation
```

**SAY:**
> "Each file can specify which paths it applies to. Advanced topic for later!"

---

## Session 1 Wrap-Up

### [0:30] Victory Lap & Achievement Summary

**SAY:**
> "Session 1 complete! 🎉 Let's see what you built in 30 minutes..."

**ACHIEVEMENTS UNLOCKED:**
- 🏆 **Fortress Builder** - Completed security setup
- 🏗️ **Project Generator** - Created practice project
- 🔐 **Secret Keeper** - .copilotignore configured
- ⚡ **Command Guardian** - Understand terminal approval
- 🎮 **Mode Master** - All AI modes practiced
- 🎯 **Context Master** - #mentions mastered
- 📋 **Instruction Writer** - Custom instructions created

**CAPABILITIES GAINED:**
- ✅ Secure AI development environment
- ✅ Generated complete project with Agent Mode
- ✅ Know which mode to use when
- ✅ Give AI perfect context with #mentions
- ✅ Custom instructions configured

**PREVIEW SESSION 2:**
> "Next up: Context Mastery! We'll learn the professional prompting formula and plan our Todo app.
> Plus: Thinking modes for complex decisions. Get ready to level up! 🚀"

**BREAK:** 2 minutes, then Session 2

---

**NUGGETS OF WISDOM:**
1. **AI drift** - the phenomenon where AI-generated code gradually deviates from specifications over extended sessions. Technical causes include:
    - Token limits
    - Recency weighting
    - Context compression
    
    Strategies to deal with drift:
    - Start new chat session
    - Use Plan mode for complex features
    - Break work into smaller chunks

2. **Prompt Files** - Create reusable prompts as `.prompt.md` files (covered in Session 3)

3. **Custom Agents** - Create specialized AI personas as `.agent.md` files (covered in Session 4)

---

**End of Instructor Guide: Micro Session 1**
