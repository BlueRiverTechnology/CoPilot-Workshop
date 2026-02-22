# GitHub Copilot Workshop - Complete Slide Deck Guide
## Verbatim Text, Imagery, and Exercise Placeholders

**Total Slides:** 72  
**Duration:** 2.5 Hours (4 Sessions)  
**Format:** Each slide includes exact text, visual descriptions, and speaker notes

---

# 📍 PRE-SESSION: TITLE & INTRO (Slides 1-5)

---

## SLIDE 1: Title Slide

### Visual
- **Background:** Dark gradient (GitHub dark theme - #0d1117 to #161b22)
- **Center:** GitHub Copilot logo (large, glowing effect)
- **Below logo:** Workshop title

### Text on Slide
```
GITHUB COPILOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
From First Prompt to Power User

[GitHub Copilot Logo]

🎯 2.5 Hours | 4 Sessions | 1 Complete Project
```

### Speaker Notes
> "Welcome! Today you'll go from your first AI prompt to becoming a Copilot Power User. By the end, you'll have built a complete API with AI assistance and earned your certification."

---

## SLIDE 2: Your Journey Today

### Visual
- **Layout:** 4 connected boxes in horizontal flow with arrows between them
- **Color coding:** Session 1 (blue), Session 2 (purple), Session 3 (green), Session 4 (gold)
- **Icons:** Shield, Brain, Rocket, Trophy

### Text on Slide
```
YOUR JOURNEY TODAY

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  🛡️ SESSION 1 │───▶│  🧠 SESSION 2 │───▶│  🚀 SESSION 3 │───▶│  🏆 SESSION 4 │
│             │    │             │    │             │    │             │
│  Security & │    │   Context   │    │    Build    │    │   Mastery   │
│ Superpowers │    │   Mastery   │    │   Sprint    │    │ Boss Fight  │
│             │    │             │    │             │    │             │
│   30 min    │    │   30 min    │    │   30 min    │    │   30 min    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
        ↓                  ↓                  ↓                  ↓
   Learn the          Think like         Build with         Prove your
     tools           a professional       speed             mastery
```

### Speaker Notes
> "Four sessions, each 30 minutes, each building on the last. Session 1: Learn your tools safely. Session 2: Think like a professional. Session 3: Build at lightning speed. Session 4: Prove your mastery and earn certification."

---

## SLIDE 3: What We're Building

### Visual
- **Left side:** Simple API architecture diagram (boxes: FastAPI → Services → Database)
- **Right side:** Screenshot of working API in browser (Swagger docs)
- **Glow effect:** Around the architecture showing it's AI-assisted

### Text on Slide
```
WHAT WE'RE BUILDING

┌──────────────────────────────────────────────────────────┐
│                    Todo API Project                       │
│                                                          │
│   🔹 FastAPI with async/await                            │
│   🔹 SQLAlchemy database layer                           │
│   🔹 3-tier architecture (API → Services → Models)       │
│   🔹 Complete CRUD operations                            │
│   🔹 Many-to-many relationships (Tags)                   │
│   🔹 Authentication patterns                             │
│   🔹 Test suite with pytest                              │
│                                                          │
│   ⚡ Built with AI assistance               │
└──────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "We'll build a professional-grade Todo API. This isn't a toy - it's production patterns you'll use in real work. The difference? We'll build it Quickly."

---

## SLIDE 4: Prerequisites Check

### Visual
- **Layout:** Checklist with green checkmarks
- **Icons:** VS Code logo, GitHub logo, Copilot logo
- **Style:** Clean, minimal

### Text on Slide
```
PREREQUISITES CHECK ✓

Before we begin, confirm you have:

☑️  VS Code installed and updated
☑️  GitHub Copilot extension installed
☑️  GitHub account with Copilot access
☑️  Copilot Chat extension installed
☑️  Python 3.9+ installed
☑️  Student project folder ready

🔗 Setup Guide: [Your setup link here]

Quick Test: Open Copilot Chat (Cmd+Shift+I)
           See the chat panel? You're ready! ✅
```

### Speaker Notes
> "Quick check - everyone has Copilot working? Open Copilot Chat with Cmd+Shift+I on Mac or Ctrl+Shift+I on Windows. See the chat panel? Perfect. If anyone needs help, raise your hand now."

---

## SLIDE 5: How to Get the Most from Today

### Visual
- **Layout:** 3 columns with icons
- **Style:** Tips card format with subtle shadows

### Text on Slide
```
HOW TO GET THE MOST FROM TODAY

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│    🎯 ENGAGE    │  │   💬 ASK       │  │   🔬 EXPERIMENT │
│                 │  │                 │  │                 │
│  Type along     │  │  Questions are  │  │  Try different  │
│  Don't just     │  │  welcome!       │  │  prompts        │
│  watch          │  │  Stop me        │  │                 │
│                 │  │  anytime        │  │  There's no     │
│  Muscle memory  │  │                 │  │  "wrong" way    │
│  matters        │  │  We're all      │  │  to experiment  │
│                 │  │  learning       │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘

🏆 Complete all exercises = Power User Certification
```

### Speaker Notes
> "Three rules for today: One - type along, don't just watch. Two - ask questions anytime. Three - experiment. Try your own prompts. Make mistakes. That's how you learn. Complete all the exercises and you'll earn your certification."

---

# 📍 SESSION 1: SECURITY & SUPERPOWERS (Slides 6-25)

---

## SLIDE 6: Session 1 Title

### Visual
- **Background:** Shield icon with electric glow
- **Color theme:** Blue and electric cyan
- **Animation suggestion:** Shield "powering up"

### Text on Slide
```
SESSION 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛡️ SECURITY & SUPERPOWERS ⚡

"Move fast, but move safely"

Duration: 30 minutes
```

### Speaker Notes
> "Session 1: Security and Superpowers. We're going to move fast today, but first we need to move safely. In 30 minutes, you'll set up your security foundation AND learn every AI mode available to you."

---

## SLIDE 7: Session 1 Objectives

### Visual
- **Layout:** Stacked objectives with icons
- **Progress indicators:** Empty circles (to be filled)

### Text on Slide
```
SESSION 1 OBJECTIVES

By the end of this session, you will:

○  Configure security-first environment
   (.copilotignore, terminal controls)

○  Master all 4 AI interaction modes
   (Ask, Edit, Agent, Plan)

○  Use all #mention types for context management
   (#file, #folder, #problems, #terminalSelection)

○  Understand Custom Instructions
   (.github/copilot-instructions.md)

○  Generate your first practice project
   with Agent Mode
```

### Speaker Notes
> "Five objectives. Security setup. All four AI modes. All the mention types. Custom instructions. And you'll generate an entire practice project. Let's go."

---

## SLIDE 8: Security First - Why It Matters

### Visual
- **Left side:** Warning icon (red)
- **Right side:** Shield icon (green)
- **Center:** Comparison arrows

### Text on Slide
```
🛡️ SECURITY FIRST - THE FOUNDATION

Before we move fast, we move safely.

┌─────────────────────────────────────────────────────────┐
│                    THE RISK                              │
│                                                         │
│  AI reads your files to help you.                       │
│  If it reads your .env file...                          │
│  Those secrets could leak.                              │
│                                                         │
│  ❌ API keys in prompts = compromised                   │
│  ❌ Database credentials exposed                        │
│  ❌ Authentication tokens visible                       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                   THE SOLUTION                           │
│                                                         │
│  ✅ .copilotignore - Files AI never sees                │
│  ✅ Command approval - You control terminal access      │
│  ✅ Review before accept - You're the gatekeeper        │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Here's why security matters: AI reads your files to help you. That's its power. But if it reads your .env file with your API keys, those secrets could leak into logs, suggestions, or cloud services. We prevent that with .copilotignore."

---

## SLIDE 9: .copilotignore Configuration

### Visual
- **Layout:** Code block with syntax highlighting
- **Icon:** Lock/shield beside filename
- **Style:** Terminal-like background

### Text on Slide
```
.COPILOTIGNORE - YOUR SECRET KEEPER

Create this file in your project root:

┌─────────────────────────────────────────────────────────┐
│ .copilotignore                                          │
├─────────────────────────────────────────────────────────┤
│ # Security - NEVER let AI see these                     │
│ .env                                                    │
│ .env.*                                                  │
│ *.key                                                   │
│ *.pem                                                   │
│ secrets/                                                │
│ credentials.json                                        │
│                                                         │
│ # API Keys and Tokens                                   │
│ *_TOKEN                                                 │
│ *_SECRET                                                │
│ *_API_KEY                                               │
│                                                         │
│ # Performance (large files)                             │
│ node_modules/                                           │
│ __pycache__/                                            │
│ *.log                                                   │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Create .copilotignore in your project root. These patterns tell Copilot: never read these files. Your secrets stay secret. Notice we also exclude large folders like node_modules for performance."

---

## SLIDE 10: Verify Your Protection

### Visual
- **Layout:** Step-by-step with screenshots
- **Green checkmark:** Success state
- **Style:** Tutorial format

### Text on Slide
```
✅ VERIFY YOUR PROTECTION

Test that .copilotignore is working:

Step 1: Create a test secret file
        echo "test-secret-key" > .env

Step 2: Open Copilot Chat
        Cmd+Shift+I (Mac) or Ctrl+Shift+I (Windows)

Step 3: Try to reference it
        Type: #file:.env

Step 4: Check the result
        ✅ "File is ignored" = Protected!
        ❌ Shows content = Not protected, check file

🛡️ Your secrets are now safe from AI access
```

### Speaker Notes
> "Let's verify it works. Create a test .env file. Open Copilot Chat. Try to reference it with #file .env. If you see 'file is ignored' or it can't find the file - you're protected. Your secrets are safe."

---

## SLIDE 10A: Controlling Copilot's Capabilities

### Visual
- **Layout:** Two-panel split screen
- **Left panel:** .copilotignore icon (eye with slash - "What it SEES")
- **Right panel:** VS Code settings gear (wrench - "What it CAN DO")
- **Center:** Shield with toggles showing control layers

### Text on Slide
```
🔧 CONTROLLING COPILOT'S POWERS

Two Layers of Control:

🔍 What Copilot SEES              ⚙️ What Copilot CAN DO
├─ .copilotignore                 ├─ VS Code Settings
├─ .github/copilot-instructions   │   chat.tools.autoApprove
                                   │   chat.tools.terminal.autoApprove
                                   └─ Configure Tools (Agent Mode)

KEY SETTINGS:
  chat.tools.autoApprove: false           ← Ask before any action
  chat.tools.terminal.autoApprove: false  ← Confirm terminal commands

AGENT MODE "CONFIGURE TOOLS":
  ✅ File editing
  ✅ Terminal commands
  ✅ Running tests
  ✅ MCP servers

💡 Pro Tip: Start restrictive (autoApprove: false), relax as you gain confidence!
```

### Speaker Notes
> "Beyond controlling what Copilot sees with .copilotignore, you control what it CAN DO through VS Code settings. The chat.tools.autoApprove settings determine whether Copilot asks permission before taking actions. In Agent Mode, the Configure Tools button shows which capabilities are enabled - file editing, terminal commands, running tests, etc. Start with autoApprove set to false for safety, then adjust based on your comfort level. Think of it as training wheels - you can remove them when you're ready!"

---

## SLIDE 11: Terminal Command Controls

### Visual
- **Layout:** Workflow diagram showing approval flow
- **Icons:** Terminal, checkmark, X for approve/reject
- **Animation suggestion:** Command appears, approval prompt shows

### Text on Slide
```
⚠️ TERMINAL COMMAND CONTROLS

Agent Mode can run terminal commands.
That's powerful... and requires YOUR approval.

┌─────────────────────────────────────────────────────────┐
│                   APPROVAL FLOW                          │
│                                                         │
│   Agent suggests:  pip install fastapi uvicorn          │
│                           ↓                              │
│              ┌─────────────────────────┐                │
│              │  [Continue]   [Cancel]  │                │
│              └─────────────────────────┘                │
│                      ↓              ↓                    │
│              Command runs     Agent tries               │
│                               different approach         │
└─────────────────────────────────────────────────────────┘

🔒 RULE: Never approve commands you don't understand
```

### Speaker Notes
> "Agent Mode can run terminal commands. Every time, you'll see exactly what it wants to run and a Continue/Cancel choice. Never approve commands you don't understand. You see 'rm -rf /' you hit Cancel. You see 'pytest' you hit Continue. You're always in control."

---

## SLIDE 12: The 4 AI Modes - Overview

### Visual
- **Layout:** 4 quadrant grid, each with icon and color
- **Colors:** Blue (Ask), Orange (Edit), Green (Agent), Purple (Plan)
- **Style:** Mode cards with clear visual distinction

### Text on Slide
```
🎮 THE 4 AI MODES

┌───────────────────────────┬───────────────────────────┐
│      ❓ ASK MODE          │      ✏️ EDIT MODE         │
│     "The Advisor"         │    "The Precise Editor"   │
│                           │                           │
│   • Thinks WITH you       │   • Controlled edits      │
│   • Explores options      │   • You choose files      │
│   • Answers questions     │   • Review before apply   │
│   • NO code changes       │   • Cmd+I inline          │
├───────────────────────────┼───────────────────────────┤
│      🤖 AGENT MODE        │      📋 PLAN MODE         │
│     "The Builder"         │     "The Architect"       │
│                           │                           │
│   • Implements FOR you    │   • Creates detailed plan │
│   • Creates files         │   • Research first        │
│   • Runs commands         │   • Shows before doing    │
│   • Autonomous work       │   • Hand off to Agent     │
└───────────────────────────┴───────────────────────────┘
```

### Speaker Notes
> "Four modes, four purposes. Ask Mode thinks with you - no changes made. Edit Mode for precise, controlled edits. Agent Mode builds autonomously - creates files, runs commands. Plan Mode shows you the full plan before execution. Let's experience the most powerful one first."

---

## SLIDE 13: Agent Mode - The Builder

### Visual
- **Layout:** Large robot icon with "building" animation effect
- **Sparkles/magic effect:** Around the icon
- **Code flying in:** Visual of files being created

### Text on Slide
```
🤖 AGENT MODE - THE BUILDER

The most powerful mode. Builds entire features autonomously.

WHAT IT DOES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Creates complete files
✓ Runs terminal commands
✓ Installs dependencies
✓ Iterates until task complete
✓ Multi-file operations

HOW TO ACCESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Copilot Chat (Cmd+Shift+I)
2. Select "Agent" from dropdown at bottom
3. Describe what you want built
4. Watch the magic happen ✨
```

### Speaker Notes
> "Agent Mode is your builder. Give it a task, it creates files, runs commands, iterates until done. Let me demonstrate by generating an entire practice project in 30 seconds."

---

## SLIDE 14: Agent Mode Demo - The Prompt

### Visual
- **Layout:** Full code block with prompt text
- **Style:** Terminal/editor appearance
- **Highlight:** Key parts of the prompt

### Text on Slide
```
AGENT MODE DEMO - GENERATE A PROJECT

Copy this prompt into Agent Mode:

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Create a minimal FastAPI learning project:             │
│                                                         │
│  Structure (6 files total):                             │
│  ├── routes/        # 3 files                           │
│  │   ├── hello.py   (basic endpoint)                    │
│  │   ├── users.py   (user endpoints with auth)          │
│  │   └── items.py   (CRUD operations)                   │
│  ├── helpers/       # 2 files                           │
│  │   ├── auth.py    (simple authentication)             │
│  │   └── validate.py (input validation)                 │
│  └── main.py        # 1 file (app entry point)          │
│                                                         │
│  Make each file 20-40 lines with:                       │
│  - Clear docstrings                                     │
│  - Type hints                                           │
│  - Error handling examples                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Here's the prompt. I'm asking for 6 files, specific structure, specific patterns. Watch what happens when I press Enter..."

---

## SLIDE 15: Exercise - Generate Your Project

### Visual
- **Layout:** Exercise card with timer
- **Icon:** Keyboard/hands typing
- **Style:** Action-oriented, urgent

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 1                          
              Generate Your Practice Project               
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 3 minutes

STEPS:
1. Open Copilot Chat (Cmd+Shift+I)
2. Select "Agent" from dropdown
3. Copy the prompt from previous slide
4. Press Enter
5. Watch files generate ✨

SUCCESS CRITERIA:
☐ 6 files created
☐ routes/ folder with 3 files
☐ helpers/ folder with 2 files
☐ main.py in root

🏆 Achievement: "First Build"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Your turn! Copy that prompt, paste into Agent Mode, press Enter. You should see 6 files appear. This is your first Agent Mode experience. Go!"

**[EXERCISE PLACEHOLDER: 3 minutes - Students generate practice project]**

---

## SLIDE 16: Safety Features - Your Safety Net

### Visual
- **Layout:** 3 column safety options
- **Icons:** Undo arrow, Git branch, Diff view
- **Colors:** Reassuring greens and blues

### Text on Slide
```
🛡️ SAFETY FEATURES - YOUR SAFETY NET

AI made a mess? You're covered.

┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   ⮌ UNDO        │  │   🔀 GIT        │  │   👁️ REVIEW     │
│                 │  │                 │  │                 │
│  Cmd+Z / Ctrl+Z │  │  Stage good     │  │  Edit Mode:     │
│                 │  │  changes        │  │  Shows diff     │
│  Works for      │  │                 │  │  before apply   │
│  individual     │  │  Discard bad    │  │                 │
│  file changes   │  │  changes        │  │  Agent Mode:    │
│                 │  │                 │  │  Review files   │
│                 │  │  Commit at      │  │  before finish  │
│                 │  │  checkpoints    │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘

💡 Golden Rule: Review before you accept
```

### Speaker Notes
> "What if AI makes changes you don't want? Standard undo works. Git integration - stage what you like, discard what you don't. And both Edit Mode and Agent Mode show you changes before they're final. You're always the quality gate."

---

## SLIDE 17: Inline Chat - Quick Edits

### Visual
- **Layout:** Before/after code comparison
- **Keyboard shortcut:** Large, prominent Cmd+I
- **Animation suggestion:** Selection → popup → transformation

### Text on Slide
```
⚡ INLINE CHAT - QUICK EDITS

Cmd+I (Mac) / Ctrl+I (Windows)

Edit code inline without opening chat panel.

WORKFLOW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Select code
2. Press Cmd+I
3. Type instruction
4. See diff preview
5. Accept or reject

BEFORE:                        AFTER:
┌─────────────────────┐       ┌─────────────────────┐
│ def greet(name):    │  ──▶  │ def greet(name: str)│
│     return "Hello"  │       │     -> str:         │
│                     │       │     """Return       │
│                     │       │     greeting."""    │
│                     │       │     return "Hello"  │
└─────────────────────┘       └─────────────────────┘

Perfect for: Refactoring, docstrings, type hints
```

### Speaker Notes
> "Superpower shortcut: Cmd+I. Select code, press Cmd+I, type what you want, see the diff, accept or reject. Lightning fast for quick refactoring."

---

## SLIDE 18: Ghost Text Completions

### Visual
- **Layout:** Code editor screenshot showing gray ghost text
- **Animation suggestion:** Text appearing as cursor moves
- **Tab key:** Highlighted

### Text on Slide
```
👻 GHOST TEXT - AUTOCOMPLETE ON STEROIDS

As you type, Copilot suggests completions in gray text.
Press Tab to accept.

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  def calculate_tax(income):                             │
│      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       │
│      rate = 0.25 if income > 50000 else 0.15           │
│      return income * rate                               │
│                                                         │
│  ░░░ = Ghost text suggestion (press Tab to accept)      │
│                                                         │
└─────────────────────────────────────────────────────────┘

Tab = Accept suggestion
Esc = Dismiss suggestion
Keep typing = See new suggestion
```

### Speaker Notes
> "The original Copilot magic. As you type, gray ghost text appears with suggestions. Press Tab to accept, Escape to dismiss, or just keep typing and it'll update. It's always there, always helping."

---

## SLIDE 19: Ask Mode & Plan Mode

### Visual
- **Layout:** Side-by-side comparison
- **Icons:** Question mark, Blueprint
- **Style:** Comparison card format

### Text on Slide
```
❓ ASK MODE                     📋 PLAN MODE

"Think with me"                 "Show me the plan"

• Select from agents dropdown   • Select from agents dropdown
• Questions and exploration     • Creates implementation plan
• No code changes               • Shows steps before executing
• Best for:                     • Best for:
  - Architecture decisions        - Complex features
  - Understanding options         - Multi-step tasks
  - Learning concepts             - Before major builds

EXAMPLE:                        EXAMPLE:
"What's the best way to        "Plan adding user auth
add rate limiting?"            with JWT tokens"

Result: Analysis and options   Result: Step-by-step plan
                              Then: "Start Implementation"
```

### Speaker Notes
> "Ask Mode for questions - it thinks with you, no changes. Plan Mode for complex tasks - it shows you the full plan, you review, then click 'Start Implementation' to hand off to Agent Mode."

---

## SLIDE 20: #mentions - Context Superpowers

### Visual
- **Layout:** Bingo card style grid
- **Icons:** Different icons for each mention type
- **Colors:** Each mention type has distinct color

### Text on Slide
```
🎯 #MENTIONS - GIVE AI X-RAY VISION

AI is only as good as the context you give it.

┌─────────────────────────────────────────────────────────┐
│                   MENTION BINGO                          │
├──────────────────┬──────────────────┬───────────────────┤
│   #file:         │   #folder:       │   #codebase       │
│   Specific file  │   Entire folder  │   Full workspace  │
│                  │                  │                   │
│   "Look at this  │   "Analyze all   │   "Search         │
│   file"          │   files here"    │   everything"     │
├──────────────────┼──────────────────┼───────────────────┤
│   #problems      │   #terminal      │   #fetch          │
│   Current errors │   Selected       │   Web content     │
│                  │   terminal       │                   │
│   "Fix these     │   "Debug this    │   "Use this       │
│   issues"        │   error"         │   documentation"  │
└──────────────────┴──────────────────┴───────────────────┘
```

### Speaker Notes
> "#mentions tell AI what to look at. #file for one file. #folder for a directory. #codebase for everything. #problems for current errors. #terminalSelection for command output. Let's practice each one."

---

## SLIDE 21: #file and #folder Demo

### Visual
- **Layout:** Code examples with results
- **Split screen:** Prompt on left, result on right

### Text on Slide
```
#FILE AND #FOLDER IN ACTION

#file - Look at ONE specific file:
┌─────────────────────────────────────────────────────────┐
│ "Looking at #file:routes/hello.py, add logging to      │
│  track each greeting request"                          │
└─────────────────────────────────────────────────────────┘
→ AI reads that exact file, adds logging statements

#folder - Look at ALL files in directory:
┌─────────────────────────────────────────────────────────┐
│ "What patterns do you see in #folder:routes ?"         │
└─────────────────────────────────────────────────────────┘
→ AI analyzes hello.py, users.py, items.py together
→ Returns: patterns, similarities, recommendations
```

### Speaker Notes
> "#file tells AI to look at one specific file. #folder gives AI the whole directory. Watch - when I use #folder:routes, AI analyzes all three route files and tells me the patterns it sees."

---

## SLIDE 22: #problems and #terminalSelection

### Visual
- **Layout:** Two-panel demonstration
- **Red highlighting:** Error messages
- **Green:** Resolution

### Text on Slide
```
#PROBLEMS AND #TERMINALSELECTION

#problems - Current errors in your code:
┌─────────────────────────────────────────────────────────┐
│ "Fix #problems in my code"                             │
└─────────────────────────────────────────────────────────┘
→ AI sees all red squiggles from Problems panel
→ Fixes syntax errors, type issues, imports

#terminalSelection - Debug with terminal output:
┌─────────────────────────────────────────────────────────┐
│ 1. Run code that errors: python test.py                 │
│ 2. Select the error in terminal                        │
│ 3. Ask: "Why is this error? #terminalSelection"        │
└─────────────────────────────────────────────────────────┘
→ AI sees exactly what crashed and why
→ Provides targeted fix
```

### Speaker Notes
> "#problems includes all the red squiggles from your Problems panel - instant fix for syntax and type errors. #terminalSelection - select error output in your terminal, AI sees exactly what crashed."

---

## SLIDE 23: Exercise - Mention Bingo

### Visual
- **Layout:** Exercise card with checklist
- **Bingo card:** To check off
- **Timer:** Prominent

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 2                          
                   Mention Bingo                           
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 3 minutes

Try each mention type. Check them off!

☐ #file:main.py - Ask about the file structure
☐ #folder:routes - "What patterns in these files?"
☐ #folder:helpers - "Analyze these utilities"
☐ #problems - If you have any errors, ask to fix

BONUS:
☐ Create an error on purpose
☐ Run in terminal
☐ Select error output
☐ Use #terminalSelection to debug

🏆 Achievement: "Context Master"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Mention Bingo time! Try each mention type and check them off. Use #file on main.py, #folder on routes and helpers. If you have errors, use #problems. Bonus points for creating an error and using #terminalSelection to debug it. Go!"

**[EXERCISE PLACEHOLDER: 3 minutes - Students practice #mentions]**

---

## SLIDE 24: Custom Instructions

### Visual
- **Layout:** File path + content preview
- **Icon:** Settings/configuration gear
- **Style:** Code file appearance

### Text on Slide
```
⚙️ CUSTOM INSTRUCTIONS

Teach AI YOUR project's patterns once.
Every conversation uses them automatically.

FILE: .github/copilot-instructions.md
┌─────────────────────────────────────────────────────────┐
│ # Project Custom Instructions                           │
│                                                         │
│ ## Architecture                                         │
│ - Use FastAPI with async/await                          │
│ - 3-tier: API → Services → Models                       │
│ - SQLAlchemy for database operations                    │
│                                                         │
│ ## Coding Standards                                     │
│ - All functions need type hints                         │
│ - Include docstrings for public methods                 │
│ - Use Pydantic for validation                           │
│                                                         │
│ ## Testing                                              │
│ - pytest with async support                             │
│ - Test files in tests/ mirror src/ structure            │
└─────────────────────────────────────────────────────────┘

✨ AI now follows YOUR rules by default
```

### Speaker Notes
> "Custom instructions are project-wide rules. Create .github/copilot-instructions.md and every Copilot conversation automatically follows these patterns. Write your architecture patterns, coding standards, testing requirements - AI remembers."

---

## SLIDE 25: Session 1 Complete!

### Visual
- **Layout:** Achievement card with checkmarks
- **Confetti/celebration effect:** Optional animation
- **Trophy icon:** Session 1 badge

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           🏆 SESSION 1 COMPLETE! 🏆                       
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've mastered:

✅ Security Configuration
   .copilotignore protecting your secrets

✅ All 4 AI Modes
   Ask, Edit, Agent, Plan

✅ #mention Types
   #file, #folder, #problems, #terminalSelection

✅ Custom Instructions
   .github/copilot-instructions.md

✅ First Project Generated
   6 files from one prompt!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Up Next: SESSION 2 - Context Mastery & Professional Prompting 🧠

[ 3 minute break ]
```

### Speaker Notes
> "Session 1 complete! You've got security configured, you know all four modes, you can use every mention type, and you've generated your first project. Take a 3-minute break, then we'll learn to think like professionals."

---
