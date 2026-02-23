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

### [0:08-0:13] 🔧 Controlling Copilot's Capabilities (5 min)

**SAY:**
> "Beyond .copilotignore, you control WHAT Copilot can DO through VS Code settings.
>
> Think of it as: .copilotignore = what it SEES, settings = what it CAN DO."

**DEMO - Show Settings:**
1. Open Command Palette → "Preferences: Open User Settings (JSON)"
2. Search for "copilot"
3. Show `chat.tools.terminal.autoApprove: false`

**SAY:**
> "This setting means Copilot must ASK before running terminal commands. Important for safety!
>
> You decide: Speed vs. Control. I recommend starting with autoApprove FALSE, then relax as you get comfortable."

**DEMO - Show Configure Tools:**
1. Open Chat view
2. Select Agent mode
3. Click "Configure Tools" (wrench icon)
4. Show the list of tools

**SAY:**
> "These are the CAPABILITIES Copilot has in Agent mode. You can toggle them on/off.
>
> **Pro tip:** When working on critical systems, limit tools to only what you need!"

**CHECKPOINT:** Everyone sees the Configure Tools dialog?

**TIME CHECK:** 5 minutes (keep it brief, this is awareness, not deep dive)

---

### [0:13-0:16] 🎮 All AI Modes - Overview (3 min)

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

### [0:16-0:21] 🏗️ Agent Mode + Practice Project Generation (5 min)

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

**5. Advanced Mentions (Quick Overview - 1 min)**

**SAY:**
> "Two more mentions you might see:
>
> **#codebase** - Includes ALL code in your workspace (use sparingly - lots of tokens!)
> **#fetch:url** - Fetches content from a web URL
>
> We won't use these today, but they're available when needed. Usually #file and #folder are more precise!"

**DO:** Show in chat dropdown briefly, don't demo

**NOTE:** Focus remains on #file, #folder, #terminalSelection, #problems

---

### [0:32-0:42] 📋 Writing Effective AI Rules - The Context Multiplier

**Purpose:**

Custom instructions are **always-on context** that multiplies your AI productivity. Instead of repeating guidelines in every prompt, you write them once and Copilot follows them automatically. This is one of the most transferable skills—every project benefits from well-written AI rules.

**ENERGY:** This is a game-changer, teach with conviction

**SAY:**
> "Next 10 minutes - the skill that separates AI amateurs from AI professionals. We're learning how to write rules that actually shape AI behavior."

---

#### [0:32-0:34] The Rules Ecosystem - Where Instructions Live (2 min)

**SAY:**
> "There's not just one place for AI rules. There's an entire ecosystem. Let me show you the full picture."

**SHOW VISUAL:**
```
📁 Your Project
├── .github/
│   ├── copilot-instructions.md          ← REPO-WIDE (always active)
│   ├── instructions/
│   │   ├── testing.instructions.md      ← PATH-SPECIFIC (tests/** only)
│   │   └── api.instructions.md          ← PATH-SPECIFIC (api/** only)
│   └── agents/
│       └── code-reviewer.agent.md       ← CUSTOM AGENT (Session 4)
├── AGENTS.md                             ← CROSS-TOOL (Copilot, Claude, Cursor)
└── VS Code Settings
    ├── Code generation instructions
    ├── Test generation instructions
    ├── Review instructions
    └── Commit message instructions
```

**SAY:**
> "The hierarchy:
> 1. **`.github/copilot-instructions.md`** - Repository-wide. Always active. Works in Chat, Agent Mode, and Code Review.
> 2. **`.github/instructions/*.instructions.md`** - Path-specific rules with frontmatter like `applyTo: '**/tests/**'`. Only active when working on matching files.
> 3. **`.github/agents/*.agent.md`** - Custom agent definitions (we'll cover these in Session 4).
> 4. **`AGENTS.md`** - Emerging open standard from Linux Foundation. Works across Copilot, Claude Code, Cursor, and other AI tools.
> 5. **VS Code settings** - Per-operation instructions (code gen, test gen, review, commits).
>
> Today we're focusing on repo-wide instructions. The skill you learn here applies to ALL of these."

🎯 **CHECKPOINT:** Everyone understands there are multiple layers of instructions?

---

#### [0:34-0:38] Research-Backed Principles - What Makes Rules Work (4 min)

**SAY:**
> "Not all rules are equal. Research from GitHub, Anthropic, and the AI engineering community shows clear patterns for what works."

**SHOW ON SCREEN:**

**Principle 1: Short, Imperative, Self-Contained Statements**

**SAY:**
> "GitHub's own docs say instructions should be 'short, self-contained statements that add context.' Not paragraphs. Not essays.
>
> **BAD:** 'We generally try to follow industry best practices for code quality and maintainability, so please write code that is clean and well-tested.'
>
> **GOOD:** 'Use type hints on all function signatures.'
>
> See the difference? Specific, actionable, scannable."

---

**Principle 2: Tell the AI What TO DO, Not What to Avoid**

**SAY:**
> "LLMs are poor at negations. Positive directives work better than negative prohibitions.
>
> **BAD:** 'Don't use print statements for debugging.'
>
> **GOOD:** 'Use `logging` module at DEBUG level for diagnostic output.'
>
> Notice: The GOOD version tells the AI the correct alternative, not just what to avoid."

---

**Principle 3: Be Specific and Actionable**

**SAY:**
> "Vague aspirational goals don't work. Concrete patterns do.
>
> **BAD:** 'Follow good naming conventions.'
>
> **GOOD:** 'Use camelCase for JavaScript variables and functions. Use PascalCase for classes.'
>
> **BAD:** 'Make sure code is well-tested.'
>
> **GOOD:** 'Every service method must have a corresponding test file in tests/services/.'
>
> Zero ambiguity = better compliance."

---

**Principle 4: Use Structured Markdown (or XML for Claude-based tools)**

**SAY:**
> "Copilot parses structured content better than prose. Use distinct headings, bullet points, code examples.
>
> For Claude-based tools like Claude Code, Anthropic recommends XML tags:"

**SHOW EXAMPLE:**
```markdown
<role>Senior Python developer specializing in FastAPI</role>

<architecture>
  - 3-tier: API routes → Service layer → Models
  - All database operations use async/await
  - Pydantic v2 for all request/response schemas
</architecture>

<constraints>
  - Never use raw SQL — always use SQLAlchemy ORM
  - All endpoints return proper HTTP status codes (400/401/403/404/500)
  - Include type hints on every function signature
</constraints>
```

**SAY:**
> "XML tags create clear boundaries that prevent the AI from mixing up context, instructions, and examples. Whether you use XML or Markdown headings depends on the tool, but the principle is the same: **Create clear, labeled compartments for different types of information.**"

---

**Principle 5: Include Code Examples Where They Clarify Intent**

**SAY:**
> "A before/after code snippet removes ambiguity. Show the pattern, don't just describe it.
>
> Example: Instead of 'Use proper error handling,' show:"

```python
# GOOD - Do this
async def get_user(user_id: str) -> User:
    try:
        return await db.get(User, user_id)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
```

---

**Principle 6: Keep Files Under ~1,000 Lines**

**SAY:**
> "GitHub explicitly warns: beyond 1,000 lines, quality deteriorates. Start minimal. Add iteratively based on what you actually need."

---

**Principle 7: Iterate Based on What Works**

**SAY:**
> "Rules writing is empirical. Start with 5-10 rules. Test them. See if Copilot follows them. Refine.
>
> This is the most important principle: **Rules are a living document.**"

🎯 **CHECKPOINT:** These principles make sense? They're grounded in research, not guesswork!

---

#### [0:38-0:40] Live Exercise - Write Your Own Rules (2 min)

**SAY:**
> "Now YOU write rules for the Todo API project. Don't just copy mine—write rules that answer: 'What would a new developer on my team need to know to write code that fits this project?'"

**DO - Guide the exercise:**

**SAY:**
> "Create `.github/copilot-instructions.md` in your practice project. Write 3-5 custom rules. Use the principles we just covered:
> - Short imperative statements
> - Positive directives (what TO do)
> - Specific and actionable
> - Organized with clear Markdown headings
>
> I'll give you 2 minutes. Go!"

**TIMER:** 2 minutes

**AT 2:00:**
> "Done! ✅ You've written your first AI rules using research-backed principles!"

🎯 **CHECKPOINT:** Everyone has created their custom instructions file with their own rules

---

#### [0:40-0:41] Path-Specific Instructions - Rules That Scope (1 min)

**SAY:**
> "Want different rules for different parts of your code? Use path-specific instructions!"

**SHOW VISUAL:**
```
.github/instructions/testing.instructions.md

---
applyTo: "**/tests/**"
---

# Testing Guidelines

- Use pytest fixtures for database setup
- Every test function name starts with test_
- Use AAA pattern: Arrange, Act, Assert
- Mock external API calls
```

**SAY:**
> "Path-specific instructions + repo-wide instructions **stack together**. When working on test files, Copilot sees both!
>
> This is powerful for teams: different rules for API code, test code, documentation, scripts."

---

#### [0:41-0:42] How Rules Connect to Everything Else (1 min)

**SAY:**
> "Rules are the foundation of the professional workflow you'll learn in Session 2:
>
> **Rules + PRD + Memory Bank = Copilot that truly knows your project.**
>
> Custom instructions are **always-on context** that saves you from repeating yourself. Every prompt you write from now on benefits from these rules.
>
> This is context mastery. This is what separates AI amateurs from AI professionals."

🎯 **CHECKPOINT:** Everyone understands how rules fit into the bigger picture?

**SAY:**
> "You can verify rules are being used by checking the **References** section in Copilot Chat responses. It'll show `.github/copilot-instructions.md` when it's reading your rules."

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

**IMPORTANT NOTE ABOUT THE PRACTICE PROJECT:**
> "The practice project you just created was for learning purposes - to experience Agent Mode and #mentions in action.
>
> **In Session 2, we'll switch to the REAL workshop project** - a pre-built Todo API that you'll extend and enhance.
>
> Think of it as: Session 1 = Training wheels. Session 2+ = Real bike! 🚴
>
> You can delete the practice project or keep it for reference - we won't use it again."

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
