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
│   ⚡ Built in 2.5 hours with AI assistance               │
└──────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "We'll build a professional-grade Todo API. This isn't a toy - it's production patterns you'll use in real work. The difference? We'll build it in 2.5 hours instead of 2.5 days."

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

# 📍 SESSION 2: CONTEXT MASTERY (Slides 26-43)

---

## SLIDE 26: Session 2 Title

### Visual
- **Background:** Brain with neural network glow
- **Color theme:** Purple and magenta
- **Icon:** Brain + lightbulb combination

### Text on Slide
```
SESSION 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 CONTEXT MASTERY & PROFESSIONAL PROMPTING

"Think like a professional, prompt like a pro"

Duration: 30 minutes
```

### Speaker Notes
> "Session 2: Context Mastery. You learned the tools. Now you'll learn to use them like a professional. This session transforms how you communicate with AI."

---

## SLIDE 27: Session 2 Objectives

### Visual
- **Layout:** Learning objectives with brain icons
- **Progress path:** Connected nodes

### Text on Slide
```
SESSION 2 OBJECTIVES

By the end of this session, you will:

○  Use Thinking Modes for extended reasoning
   (think, think hard, ultrathink)

○  Master the Explore → Plan → Code workflow
   The professional's approach

○  Create and reference PRDs
   Product Requirements Documents

○  Apply the 6-Element Framework
   The professional prompting toolbox

○  Combine #mentions with structured prompts
   Context + Structure = Perfect results
```

### Speaker Notes
> "Five new superpowers. Thinking modes for complex decisions. Professional workflow. PRDs for documentation. The 6-element framework for perfect prompts. And combining everything together."

---

## SLIDE 28: Thinking Modes - Extended Reasoning

### Visual
- **Layout:** Spectrum from quick to deep thinking
- **Icons:** Stopwatch showing longer times
- **Colors:** Gradient from light to deep purple

### Text on Slide
```
🧠 THINKING MODES - EXTENDED REASONING

Tell AI to take MORE TIME before responding.

┌─────────────────────────────────────────────────────────┐
│  KEYWORD        │  THINKING TIME  │  USE FOR            │
├─────────────────┼─────────────────┼─────────────────────┤
│  "think"        │  ~5-10 sec      │  Basic analysis     │
│  "think hard"   │  ~10-20 sec     │  Thorough review    │
│  "think harder" │  ~20-30 sec     │  Deep evaluation    │
│  "ultrathink"   │  ~30+ sec       │  Maximum analysis   │
└─────────────────────────────────────────────────────────┘

💡 Same credits, more compute time
💡 These are MODEL features, not Copilot features
💡 Worth it for: Architecture, complex planning, trade-offs

⚠️ Skip for: Simple tasks, file creation, basic edits
```

### Speaker Notes
> "Thinking modes. Add 'think hard' to your prompt and AI takes 15-20 seconds to really analyze before responding. Same cost, more thinking time, better decisions. Use for architecture and complex planning. Skip for simple tasks."

---

## SLIDE 29: Thinking Modes Demo

### Visual
- **Layout:** Side-by-side comparison
- **Before/After:** Quick vs deep response
- **Highlighting:** Quality difference

### Text on Slide
```
THINKING MODES - THE DIFFERENCE

WITHOUT thinking mode:
┌─────────────────────────────────────────────────────────┐
│ "What database for a todo app?"                         │
│                                                         │
│ → Quick response: "PostgreSQL is a good choice."        │
│   (Instant, surface-level)                              │
└─────────────────────────────────────────────────────────┘

WITH thinking mode:
┌─────────────────────────────────────────────────────────┐
│ "think hard about the best database for a todo app.     │
│  Consider: scale, complexity, team skills, hosting."    │
│                                                         │
│ → [Takes 15 seconds]                                    │
│ → Detailed comparison of SQLite vs PostgreSQL vs MongoDB│
│ → Trade-off analysis for each scenario                  │
│ → Clear recommendation with reasoning                   │
│ → Considerations for future scaling                     │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Watch the difference. Without thinking mode: quick, surface-level. With 'think hard': 15 seconds of processing, then a detailed comparison, trade-offs, clear reasoning. Same cost. Much better answer."

---

## SLIDE 30: Professional Workflow

### Visual
- **Layout:** 3-phase flow diagram
- **Icons:** Magnifying glass → Blueprint → Code
- **Arrows:** Connecting the phases

### Text on Slide
```
🔄 THE PROFESSIONAL WORKFLOW

Most developers:  IDEA → CODE → PROBLEMS → FIX → MORE PROBLEMS

Professionals:    EXPLORE → PLAN → CODE

┌─────────────────────────────────────────────────────────┐
│                                                         │
│   🔍 EXPLORE          📋 PLAN           💻 CODE         │
│   (Ask Mode)         (Document)        (Agent Mode)    │
│                                                         │
│   Think WITH AI      Create PRD         Reference PRD   │
│   before coding      Document scope     Build features  │
│   Identify issues    Define criteria    Full context    │
│   early              Capture decisions                  │
│                                                         │
│   "Help me think     "Create PRD        "#file:PRD.md   │
│   through this..."   for this..."       Build this..."  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Most developers jump straight to code, then fix problems. Professionals explore first, plan second, then code. Today you learn phases 1 and 2. Sessions 3-4 are phase 3 - building from your plan."

---

## SLIDE 31: Phase 1 - EXPLORE Demo

### Visual
- **Layout:** Full-width prompt example
- **Highlighting:** Key exploration elements
- **Icon:** Magnifying glass with brain

### Text on Slide
```
🔍 PHASE 1: EXPLORE

Don't ask for code. Ask for THINKING.

┌─────────────────────────────────────────────────────────┐
│ In ASK MODE:                                            │
│                                                         │
│ "I want to add a tagging feature to our todo API -      │
│  allowing many-to-many relationships.                   │
│                                                         │
│  Before we write any code, help me think through:       │
│  1. Essential features vs nice-to-have?                 │
│  2. Technical decisions needed upfront?                 │
│  3. Potential challenges to consider?                   │
│  4. Simplest viable implementation?                     │
│                                                         │
│  Don't write code yet - just help me explore.           │
│                                                         │
│  think about this carefully"                            │
└─────────────────────────────────────────────────────────┘

Result: Insights that save HOURS of rework
```

### Speaker Notes
> "Phase 1: EXPLORE. Use Ask Mode. Don't ask for code - ask for thinking. 'Help me think through this.' 'What should I consider?' This 2-minute conversation saves hours of rework because you find problems BEFORE coding."

---

## SLIDE 32: Phase 2 - PLAN with PRD

### Visual
- **Layout:** PRD document preview
- **Icon:** Clipboard/document
- **Highlighting:** Key sections

### Text on Slide
```
📋 PHASE 2: PLAN - CREATE A PRD

Capture your exploration in a reference document.

┌─────────────────────────────────────────────────────────┐
│ In AGENT MODE:                                          │
│                                                         │
│ "Based on our planning discussion, create a PRD         │
│  (Product Requirements Document) for adding Tags.       │
│                                                         │
│  Include:                                               │
│  1. Feature Overview                                    │
│  2. Core Features (MVP only)                            │
│  3. User Stories                                        │
│  4. Technical Requirements                              │
│  5. Success Criteria                                    │
│  6. Out of Scope                                        │
│                                                         │
│  Save as PRD-Tags.md"                                   │
└─────────────────────────────────────────────────────────┘

✨ Now you have a REFERENCE for all future prompts
```

### Speaker Notes
> "Phase 2: PLAN. Turn your exploration into a PRD - a Product Requirements Document. This captures scope, requirements, and decisions. Most importantly: you can REFERENCE this document in every future prompt with #file:PRD.md."

---

## SLIDE 33: Using Your PRD

### Visual
- **Layout:** Prompt with #file reference highlighted
- **Connection line:** From PRD to prompt
- **Benefit callouts:** Around the edges

### Text on Slide
```
🔗 USING YOUR PRD IN DEVELOPMENT

Reference your PRD when building features:

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  #file:PRD-Tags.md                                      │
│                                                         │
│  Implement POST /api/v1/todos/{id}/tags endpoint        │
│  following PRD requirements.                            │
│                                                         │
│  Include:                                               │
│  - Tag schema per PRD specs                             │
│  - Many-to-many relationship per technical requirements │
│  - Error handling per success criteria                  │
│                                                         │
└─────────────────────────────────────────────────────────┘

AI now has FULL CONTEXT:
  ✓ Feature scope
  ✓ Technical decisions
  ✓ Success criteria
  ✓ What's out of scope
```

### Speaker Notes
> "Power move: reference your PRD with #file when building. AI now has your complete feature context. It knows the scope, technical decisions, success criteria, and what NOT to build. This is how professionals stay aligned."

---

## SLIDE 34: The 6-Element Framework

### Visual
- **Layout:** 6 boxes in 2 rows
- **Icons:** Distinct icon for each element
- **Colors:** Gradient or distinct colors per element

### Text on Slide
```
🎯 THE 6-ELEMENT FRAMEWORK

Your professional prompting toolbox:

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  [PERSONA]   │  │  [CONTEXT]   │  │   [TASK]     │
│              │  │              │  │              │
│  Who should  │  │  What's the  │  │  What needs  │
│  AI be?      │  │  situation?  │  │  to be done? │
│              │  │              │  │              │
│  Optional    │  │  🔴 REQUIRED │  │  🔴 REQUIRED │
└──────────────┘  └──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ [CONSTRAINTS]│  │  [FORMAT]    │  │  [EXAMPLES]  │
│              │  │              │  │              │
│  What are    │  │  Expected    │  │  Show        │
│  the rules?  │  │  output?     │  │  patterns    │
│              │  │              │  │              │
│  Recommended │  │  Recommended │  │  Optional    │
└──────────────┘  └──────────────┘  └──────────────┘

⚠️ It's a TOOLBOX, not a checklist. Use what you need!
```

### Speaker Notes
> "The 6-element framework. Not a checklist - a toolbox. Use what you need. Context and Task are always required. The rest depends on complexity. Simple task? Skip most. Complex task? Use all six."

---

## SLIDE 35: Framework Scaling

### Visual
- **Layout:** 3 complexity levels with element counts
- **Visual:** Stacking blocks showing elements used
- **Colors:** Green (simple), Yellow (medium), Red (complex)

### Text on Slide
```
📊 SCALE THE FRAMEWORK BY COMPLEXITY

SIMPLE TASK (config, basic file):
┌─────────────────────────────────────────────────────────┐
│  [CONTEXT] Python FastAPI project                       │
│  [TASK] Create .gitignore for venv/, .env               │
│                                                         │
│  ✅ 2 elements. Done!                                   │
└─────────────────────────────────────────────────────────┘

MEDIUM TASK (single feature):
┌─────────────────────────────────────────────────────────┐
│  [CONTEXT] #file:todos.py has POST endpoint             │
│  [TASK] Add validation for title length                 │
│  [CONSTRAINTS] Return 400, don't break tests            │
│  [FORMAT] Update endpoint function only                 │
│                                                         │
│  ✅ 4 elements. Right amount!                           │
└─────────────────────────────────────────────────────────┘

COMPLEX TASK (multi-part feature):
┌─────────────────────────────────────────────────────────┐
│  [PERSONA] + [CONTEXT] + [TASK] + [CONSTRAINTS]         │
│  + [FORMAT] + [EXAMPLES]                                │
│                                                         │
│  ✅ ALL 6 elements for complex work                     │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Scaling in action. Simple task - 2 elements, done. Medium task - 4 elements, add constraints and format. Complex task - all 6. Don't over-engineer simple prompts. Don't under-specify complex ones."

---

## SLIDE 36: Complete Complex Example

### Visual
- **Layout:** Full prompt with all 6 elements labeled
- **Highlighting:** Each element in different color
- **Callouts:** Pointing to key parts

### Text on Slide
```
COMPLEX PROMPT - ALL 6 ELEMENTS

[PERSONA] You're a senior SQLAlchemy developer
specializing in complex relationships.

[CONTEXT] #folder:src/models/ has User and Todo.
#file:src/services/todo_service.py shows service patterns.

[TASK] Add Tag model with many-to-many relationship to Todo,
plus endpoints to add/remove tags.

[CONSTRAINTS]
- Tag names unique, case-insensitive
- Users only tag their own todos
- POST and DELETE endpoints
- Follow 3-tier architecture

[FORMAT]
1. src/models/tag.py
2. src/services/tag_service.py
3. src/api/v1/tags.py
4. tests/api/test_tags.py

[EXAMPLES]
Follow pattern in #file:src/models/user.py lines 15-30
```

### Speaker Notes
> "Here's a complex prompt with all six elements. Persona tells AI to be an expert. Context gives the files. Task is clear. Constraints list all rules. Format specifies outputs. Examples show patterns. For complex work, use all six."

---

## SLIDE 37: Exercise - PRD Creation

### Visual
- **Layout:** Exercise card with PRD outline
- **Timer:** Prominent
- **Checklist:** Sections to include

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 3                          
                 Create Your PRD                           
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 5 minutes

CREATE: PRD for a "Priority" feature for todos

STEPS:
1. EXPLORE first (Ask Mode):
   "Help me think through adding priority to todos"

2. PLAN (Agent Mode):
   "Create PRD-Priority.md with:
   - Feature Overview
   - Core Features
   - Technical Requirements
   - Success Criteria
   - Out of Scope"

SUCCESS CRITERIA:
☐ Explored before planning
☐ PRD-Priority.md created
☐ All sections populated

🏆 Achievement: "Strategic Planner"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Exercise time! Create a PRD for adding priority to todos. First, EXPLORE in Ask Mode - think through the feature. Then PLAN in Agent Mode - create the PRD document. You have 5 minutes. This is the professional workflow in action."

**[EXERCISE PLACEHOLDER: 5 minutes - Students create PRD for priority feature]**

---

## SLIDE 38: Advanced #mention Patterns

### Visual
- **Layout:** Pattern examples with descriptions
- **Code blocks:** Showing combination patterns
- **Icons:** Showing what each pattern accesses

### Text on Slide
```
⚡ ADVANCED #MENTION PATTERNS

Combine mentions for powerful context:

ARCHITECTURE UNDERSTANDING:
┌─────────────────────────────────────────────────────────┐
│ "Analyze #folder:src/models/ and #folder:src/api/       │
│  How do models relate to API endpoints?"                │
└─────────────────────────────────────────────────────────┘

PRD + EXISTING CODE:
┌─────────────────────────────────────────────────────────┐
│ "#file:PRD.md #folder:src/services/                     │
│  Implement feature following PRD specs and existing     │
│  service patterns"                                      │
└─────────────────────────────────────────────────────────┘

DEBUGGING CONTEXT:
┌─────────────────────────────────────────────────────────┐
│ "#file:broken.py #problems #terminalSelection           │
│  Fix this - here's the file, errors, and terminal"      │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Advanced patterns: combine mentions for rich context. Architecture questions - give both models and API folders. Implementation - give PRD plus existing code patterns. Debugging - give the file, errors, and terminal output all at once."

---

## SLIDE 39: The Complete Mental Model

### Visual
- **Layout:** Workflow diagram showing all pieces connected
- **Flow:** Explore → Plan → Prompt → Build
- **Integration:** All concepts connected

### Text on Slide
```
🧠 THE COMPLETE MENTAL MODEL

Putting it all together:

┌─────────────────────────────────────────────────────────┐
│                                                         │
│   1. EXPLORE (Ask Mode + think keywords)                │
│      ↓                                                  │
│   2. PLAN (PRD document)                                │
│      ↓                                                  │
│   3. PROMPT (6-element framework + #mentions)           │
│      ↓                                                  │
│   4. BUILD (Agent Mode)                                 │
│      ↓                                                  │
│   5. VERIFY (Review + iterate)                          │
│                                                         │
└─────────────────────────────────────────────────────────┘

Simple task? Skip to step 3-4.
Complex task? Do all 5 steps.
Critical decision? Add "think hard" to step 1.
```

### Speaker Notes
> "The complete mental model. Explore, Plan, Prompt, Build, Verify. Simple tasks skip to prompt and build. Complex tasks do all five. Critical decisions add thinking modes to explore. You now have the full professional toolkit."

---

## SLIDE 40: Session 2 Complete!

### Visual
- **Layout:** Achievement summary with badges
- **Celebration effect:** Confetti/stars
- **Progress indicator:** 2 of 4 sessions done

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           🏆 SESSION 2 COMPLETE! 🏆                       
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've mastered:

✅ Thinking Modes
   Extended reasoning for complex decisions

✅ Professional Workflow
   Explore → Plan → Code

✅ PRD Creation
   Document your plans, reference in prompts

✅ 6-Element Framework
   Scale prompts by complexity

✅ Advanced #mentions
   Rich context combinations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Up Next: SESSION 3 - Build Sprint! Time to CODE! 🚀

[ 3 minute break ]
```

### Speaker Notes
> "Session 2 complete! You think like a professional now. You have thinking modes, the workflow, PRDs, the framework, and advanced mentions. Break time, then Session 3 - we put it all into practice and BUILD."

---

# 📍 SESSION 3: BUILD SPRINT (Slides 41-58)

---

## SLIDE 41: Session 3 Title

### Visual
- **Background:** Rocket launch with code trails
- **Color theme:** Green and electric cyan
- **Energy:** High, dynamic

### Text on Slide
```
SESSION 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 BUILD SPRINT - CONTEXT EDITION

"Prove that context quality matters"

Duration: 30 minutes
```

### Speaker Notes
> "Session 3: Build Sprint! You learned the tools. You learned the thinking. Now you PROVE it works by building 3 complete CRUD features. This is where context mastery becomes real productivity."

---

## SLIDE 42: The Build Challenge

### Visual
- **Layout:** Challenge card with scoring
- **Timer graphic:** Showing urgency
- **Trophy icons:** For achievement levels

### Text on Slide
```
🎮 THE BUILD CHALLENGE

Next 30 minutes: Build 3 complete CRUD features

┌─────────────────────────────────────────────────────────┐
│  FEATURE 1: Create Todo (TDD Approach)                  │
│             Tests first, then implementation            │
│             ~10 minutes                                 │
├─────────────────────────────────────────────────────────┤
│  FEATURE 2: List Todos (Full Context Power)             │
│             One prompt, full implementation             │
│             ~7 minutes                                  │
├─────────────────────────────────────────────────────────┤
│  FEATURE 3: Update Todo (Speed Challenge)               │
│             Can you do it in 3 minutes? ⚡              │
│             ~3 minutes                                  │
└─────────────────────────────────────────────────────────┘

📊 Track: Time, iterations, success rate
🏆 Achievement: "Build Master"
```

### Speaker Notes
> "Three features, three approaches. Feature 1: TDD - tests first, methodical. Feature 2: Full context power - one prompt does everything. Feature 3: Speed challenge - can you build in 3 minutes? We're proving context quality matters."

---

## SLIDE 43: TDD with AI

### Visual
- **Layout:** TDD cycle diagram (Red → Green → Refactor)
- **AI integration:** Showing AI at each step
- **Icons:** Test tube, code, check mark

### Text on Slide
```
🧪 TDD WITH AI

Test-Driven Development workflow:

        ┌──────────────────────────────────────────┐
        │                                          │
        │   1. WRITE TESTS (they fail) 🔴          │
        │          ↓                               │
        │   2. IMPLEMENT CODE (tests pass) 🟢      │
        │          ↓                               │
        │   3. REFACTOR (improve quality) ♻️       │
        │          ↓                               │
        │   4. REPEAT                              │
        │                                          │
        └──────────────────────────────────────────┘

WHY TDD + AI WORKS:
• Tests give AI clear success criteria
• Less ambiguity = better code
• Automatic verification
• Built-in documentation
```

### Speaker Notes
> "TDD with AI is powerful. Write tests first - they define what success looks like. AI implements to make tests pass. You run tests to verify. This works because tests give AI crystal-clear success criteria."

---

## SLIDE 44: Feature 1 - Write Tests First

### Visual
- **Layout:** Prompt in code block
- **Highlighting:** Key TDD elements
- **Step indicator:** Step 1 of 3

### Text on Slide
```
🧪 FEATURE 1: CREATE TODO - WRITE TESTS

STEP 1: Write tests FIRST (Agent Mode)

┌─────────────────────────────────────────────────────────┐
│ #file:PRD.md #folder:src/models/                        │
│                                                         │
│ [Context]                                               │
│ Working on todo API per PRD. Models in src/models/.     │
│                                                         │
│ [Task]                                                  │
│ Create tests/api/test_todos.py for POST /api/v1/todos   │
│                                                         │
│ [Constraints]                                           │
│ - Use pytest with async support                         │
│ - Test: successful creation, empty title, title too long│
│ - DON'T implement endpoint yet                          │
│ - Tests should FAIL initially (TDD)                     │
│                                                         │
│ [Format]                                                │
│ Create tests/api/test_todos.py                          │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Step 1: Write tests. Notice I explicitly say 'DON'T implement yet' and 'Tests should FAIL'. We're defining success criteria before writing any implementation code."

---

## SLIDE 45: Feature 1 - Verify Failure

### Visual
- **Layout:** Terminal output showing failed tests
- **Red highlighting:** Test failures
- **Checkmark:** This is expected!

### Text on Slide
```
🔴 STEP 2: RUN TESTS - VERIFY FAILURE

Run the tests (they should fail!):

┌─────────────────────────────────────────────────────────┐
│ $ pytest tests/api/test_todos.py -v                     │
│                                                         │
│ test_create_todo_success FAILED                         │
│ test_create_todo_empty_title FAILED                     │
│ test_create_todo_title_too_long FAILED                  │
│                                                         │
│ ========== 3 failed in 0.42s ==========                 │
└─────────────────────────────────────────────────────────┘

✅ PERFECT! This is exactly what we want.

The tests define WHAT we need.
Now we implement to make them pass.
```

### Speaker Notes
> "Run the tests. They fail. Perfect! That's TDD working correctly. The tests now define exactly what our implementation needs to do. No ambiguity."

---

## SLIDE 46: Feature 1 - Implement

### Visual
- **Layout:** Implementation prompt
- **Highlighting:** Test file referenced for context
- **Step indicator:** Step 3 of 3

### Text on Slide
```
🟢 STEP 3: IMPLEMENT TO PASS TESTS

Give AI the tests as context:

┌─────────────────────────────────────────────────────────┐
│ #file:PRD.md #file:tests/api/test_todos.py              │
│ #file:src/models/todo.py                                │
│                                                         │
│ [Context]                                               │
│ Tests in test_todos.py define success criteria.         │
│ Todo model exists. Following 3-tier architecture.       │
│                                                         │
│ [Task]                                                  │
│ Implement POST /api/v1/todos to make all tests pass     │
│                                                         │
│ [Constraints]                                           │
│ - Create: Pydantic schemas, Service layer, API route    │
│ - Handle all test cases                                 │
│ - Use async/await patterns                              │
│                                                         │
│ [Format]                                                │
│ Create all 3 files, register router in main.py          │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Step 3: Implement. Notice I give AI the TESTS as context. AI can see exactly what success looks like. The tests define the contract, AI writes the implementation."

---

## SLIDE 47: Feature 1 - Verify Success

### Visual
- **Layout:** Terminal output showing passing tests
- **Green highlighting:** All tests pass
- **Celebration icon:** Checkmark/trophy

### Text on Slide
```
✅ RUN TESTS - VERIFY SUCCESS

┌─────────────────────────────────────────────────────────┐
│ $ pytest tests/api/test_todos.py -v                     │
│                                                         │
│ test_create_todo_success PASSED                         │
│ test_create_todo_empty_title PASSED                     │
│ test_create_todo_title_too_long PASSED                  │
│                                                         │
│ ========== 3 passed in 0.58s ==========                 │
└─────────────────────────────────────────────────────────┘

🎉 ALL TESTS PASS!

That's TDD with AI:
  Write test → Watch fail → Implement → Watch pass

Time: ~10 minutes for complete CRUD feature
```

### Speaker Notes
> "Run tests again. All pass. That's TDD with AI. Write test, watch fail, implement, watch pass. You now have a tested, working feature with automatic verification."

---

## SLIDE 48: Exercise - TDD Feature 1

### Visual
- **Layout:** Exercise card with timer
- **Steps:** Clear numbered steps
- **Checkboxes:** For completion tracking

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 4                          
              Build Create Todo (TDD)                      
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 10 minutes

STEPS:
1. Write tests (prompt from slide 44)
2. Run tests - verify they FAIL
3. Implement (prompt from slide 46)
4. Run tests - verify they PASS
5. Start dev server: uvicorn src.main:app --reload

SUCCESS CRITERIA:
☐ Tests created in tests/api/
☐ All 3 test cases fail initially
☐ Implementation creates 3 layers
☐ All tests pass after implementation
☐ Server runs at localhost:8000

🏆 Achievement: "TDD Master"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Your turn! Build the Create Todo feature using TDD. Write tests first, verify they fail, implement, verify they pass. You have 10 minutes. This is real-world TDD with AI assistance."

**[EXERCISE PLACEHOLDER: 10 minutes - Students build Create Todo with TDD]**

---

## SLIDE 49: Feature 2 - Full Context Power

### Visual
- **Layout:** Single comprehensive prompt
- **Highlighting:** All context elements
- **Timer:** Showing speed

### Text on Slide
```
⚡ FEATURE 2: LIST TODOS - FULL CONTEXT POWER

One prompt. All layers. Watch this...

┌─────────────────────────────────────────────────────────┐
│ #file:PRD.md #folder:src/api/ #folder:src/services/     │
│                                                         │
│ [Context]                                               │
│ Working on todo API per PRD. Existing patterns in       │
│ src/api/ and src/services/ from Feature 1.              │
│                                                         │
│ [Task]                                                  │
│ Add GET /api/v1/todos endpoint to list all todos        │
│                                                         │
│ [Constraints]                                           │
│ - Pagination: skip and limit query params               │
│ - Filtering: completed (optional) query param           │
│ - Only return user's todos                              │
│ - Return List[TodoResponse]                             │
│ - Add get_all() to TodoService                          │
│                                                         │
│ [Format]                                                │
│ Update todo_service.py and todos.py                     │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Feature 2: Full context power. One prompt, everything specified. Notice the context - PRD for requirements, existing folders for patterns. Constraints are crystal clear. One prompt, complete feature."

---

## SLIDE 50: Feature 2 - Verify

### Visual
- **Layout:** curl commands and responses
- **Terminal style:** Command outputs
- **Green checkmarks:** Working endpoints

### Text on Slide
```
✅ VERIFY FEATURE 2

Test your endpoints:

┌─────────────────────────────────────────────────────────┐
│ # List all todos                                        │
│ $ curl http://localhost:8000/api/v1/todos               │
│ → [{"id": "...", "title": "...", "completed": false}]   │
│                                                         │
│ # With pagination                                       │
│ $ curl "http://localhost:8000/api/v1/todos?limit=10"    │
│ → First 10 todos                                        │
│                                                         │
│ # Filter by completed                                   │
│ $ curl "http://localhost:8000/api/v1/todos?completed=true"
│ → Only completed todos                                  │
└─────────────────────────────────────────────────────────┘

⏱️ Time: ~3-5 minutes (vs 10+ without good context)
```

### Speaker Notes
> "Test it. All endpoints working. Pagination works. Filtering works. That was 3-5 minutes for a complete feature because we gave AI perfect context upfront."

---

## SLIDE 51: Feature 3 - Speed Challenge

### Visual
- **Layout:** Challenge card with timer
- **Racing theme:** Speed lines, stopwatch
- **Competitive element:** Can you beat 3 minutes?

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                🏎️ SPEED CHALLENGE 🏎️                      
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ CAN YOU BUILD IN 3 MINUTES?

Feature: PUT /api/v1/todos/{id}

Requirements:
• Update title, description, completed
• Only if user owns the todo
• Return 404 if not found, 403 if not owner
• Return updated TodoResponse

YOUR APPROACH:
• TDD? Full context? Both?
• Use what you learned!
• Pair up, help each other!

🏆 Fastest completion wins!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Speed challenge! Build PUT endpoint in 3 minutes. You decide the approach - TDD, full context, or both. Use everything you've learned. Pair up if you want. Fastest completion wins. Timer starts NOW!"

**[EXERCISE PLACEHOLDER: 3 minutes - Students build Update Todo speed challenge]**

---

## SLIDE 52: Subagents - Parallel Work

### Visual
- **Layout:** Diagram showing main agent + parallel subagents
- **Arrows:** Showing parallel execution
- **Icons:** Multiple robot icons working simultaneously

### Text on Slide
```
🤖 SUBAGENTS - PARALLEL VERIFICATION

Copilot can spawn parallel agents for complex tasks:

┌─────────────────────────────────────────────────────────┐
│                                                         │
│        MAIN AGENT (you're working with)                 │
│                    │                                    │
│           ┌───────┴───────┐                            │
│           ↓               ↓                            │
│    ┌──────────────┐ ┌──────────────┐                   │
│    │  SUBAGENT 1  │ │  SUBAGENT 2  │                   │
│    │              │ │              │                   │
│    │  Code Review │ │  Run Tests   │                   │
│    │  (parallel)  │ │  (parallel)  │                   │
│    └──────────────┘ └──────────────┘                   │
│           ↓               ↓                            │
│           └───────┬───────┘                            │
│                   ↓                                    │
│         Results merged back                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Subagents are parallel workers. Copilot can spawn them automatically for complex tasks, or you can request them. One agent reviews code while another runs tests. Parallel AI work!"

---

## SLIDE 53: Using Subagents

### Visual
- **Layout:** Prompt example for spawning subagent
- **Highlight:** Explicit request for parallel work

### Text on Slide
```
⚡ SPAWNING SUBAGENTS

Request parallel work explicitly:

┌─────────────────────────────────────────────────────────┐
│ "Launch a subagent to review all the code we created    │
│  in src/api/v1/todos.py and src/services/ for:          │
│                                                         │
│  - Error handling completeness                          │
│  - Async/await correctness                              │
│  - Security issues                                      │
│                                                         │
│  While that runs, I'll continue with the next task."    │
└─────────────────────────────────────────────────────────┘

PERFECT FOR:
• Code review while building
• Running tests in parallel
• Documentation generation
• Multiple independent tasks
```

### Speaker Notes
> "Request subagents explicitly. 'Launch a subagent to review this while I continue.' The subagent works in parallel and reports back when done. Perfect for code review while you keep building."

---

## SLIDE 54: Plan Mode

### Visual
- **Layout:** Plan Mode output example
- **Step-by-step:** Showing plan before execution
- **Button:** "Start Implementation"

### Text on Slide
```
📋 PLAN MODE - SEE BEFORE YOU BUILD

Use /plan for complex implementations:

┌─────────────────────────────────────────────────────────┐
│ /plan Implement tagging feature for todos:              │
│                                                         │
│ 1. Create Tag model with association table              │
│ 2. Create TagCreate and TagResponse schemas             │
│ 3. Add service methods for add/remove tags              │
│ 4. Add API endpoints                                    │
│ 5. Include tests                                        │
└─────────────────────────────────────────────────────────┘

RESULT:
┌─────────────────────────────────────────────────────────┐
│ 📋 IMPLEMENTATION PLAN                                  │
│                                                         │
│ Step 1: Create src/models/tag.py with...                │
│ Step 2: Update src/schemas/...                          │
│ Step 3: Add methods to...                               │
│ ...                                                     │
│                                                         │
│         [Start Implementation]                          │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Plan Mode shows you the full implementation plan before any code is written. Review the plan, adjust if needed, then click 'Start Implementation' to hand off to Agent Mode. Full visibility before execution."

---

## SLIDE 55: Session 3 Results

### Visual
- **Layout:** Results tracking card
- **Metrics:** Time, iterations, success rate
- **Comparison:** Showing improvement

### Text on Slide
```
📊 SESSION 3 RESULTS

What you built in 30 minutes:

┌─────────────────────────────────────────────────────────┐
│  FEATURE           │  TIME    │  APPROACH              │
├────────────────────┼──────────┼────────────────────────┤
│  Create Todo       │  ~10 min │  TDD (tests first)     │
│  List Todos        │  ~5 min  │  Full context          │
│  Update Todo       │  ~3 min  │  Speed challenge       │
└────────────────────┴──────────┴────────────────────────┘

TOTAL: 3 complete CRUD operations in ~18 minutes

KEY INSIGHT:
• TDD: More setup, but automatic verification
• Full Context: Fastest for clear requirements
• Both work - choose based on situation
```

### Speaker Notes
> "Look at what you built. Three CRUD operations in under 20 minutes. TDD gives you verification. Full context gives you speed. Both work - you choose based on the situation."

---

## SLIDE 56: Session 3 Complete!

### Visual
- **Layout:** Achievement summary
- **Trophy:** Build Master badge
- **Progress:** 3 of 4 sessions done

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           🏆 SESSION 3 COMPLETE! 🏆                       
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've mastered:

✅ TDD with AI
   Tests first, implementation to pass

✅ Full Context Implementation
   One prompt, complete features

✅ Speed Building
   3 CRUD operations in 20 minutes

✅ Subagents
   Parallel verification and tasks

✅ Plan Mode
   See the plan before building

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Up Next: SESSION 4 - BOSS FIGHT! Prove everything! 🎮

[ 3 minute break ]
```

### Speaker Notes
> "Session 3 complete! You can now build features fast with TDD, full context, subagents, and plan mode. One more session - the Boss Fight where you prove everything you've learned. Break time!"

---

# 📍 SESSION 4: MASTERY & BOSS FIGHT (Slides 57-72)

---

## SLIDE 57: Session 4 Title

### Visual
- **Background:** Gaming/boss fight theme
- **Color theme:** Gold and purple
- **Icons:** Trophy, crown, controller

### Text on Slide
```
SESSION 4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎮 MASTERY & BOSS FIGHT 🏆

"Prove everything you've learned"

Duration: 33 minutes
```

### Speaker Notes
> "The finale! Session 4 is where you prove mastery. Code Review, Custom Agents, the 70% Problem, and the Boss Fight. Complete the Boss Fight and you're a certified Copilot Power User."

---

## SLIDE 58: Session 4 Objectives

### Visual
- **Layout:** Final objectives with trophy icons
- **Style:** Epic/climactic feeling

### Text on Slide
```
SESSION 4 OBJECTIVES - THE FINALE

By the end of this session, you will:

○  Use Copilot Code Review for PR feedback
   Automated quality checks on every PR

○  Create Custom Agents (.agent.md files)
   Specialized AI personas for your project

○  Understand the 70% Problem
   Where AI helps, where YOU add value

○  Complete the BOSS FIGHT
   Build complex feature using ALL techniques

○  EARN POWER USER CERTIFICATION 🏆
   Prove your mastery
```

### Speaker Notes
> "Four final skills, then the ultimate test. Code Review, Custom Agents, the 70% Problem, and Boss Fight. Complete the Boss Fight - you're certified."

---

## SLIDE 59: Copilot Code Review

### Visual
- **Layout:** GitHub PR interface mockup
- **Copilot reviewer:** Shown in reviewer section
- **Inline comments:** Example feedback

### Text on Slide
```
🔍 COPILOT CODE REVIEW

Automated code review on every Pull Request

HOW IT WORKS:
┌─────────────────────────────────────────────────────────┐
│  1. Create Pull Request on GitHub                       │
│  2. Request review from "copilot" as reviewer           │
│  3. Copilot analyzes your changes                       │
│  4. Get inline comments and suggestions                 │
└─────────────────────────────────────────────────────────┘

WHAT IT CHECKS:
  ✅ Code quality and best practices
  ✅ Potential bugs and edge cases
  ✅ Security vulnerabilities
  ✅ Performance issues
  ✅ Consistency with codebase patterns

Like having a tireless reviewer on every PR!
```

### Speaker Notes
> "Copilot Code Review. On GitHub, request 'copilot' as a reviewer on any PR. It analyzes your changes, leaves inline comments, finds bugs, security issues, performance problems. Tireless code reviewer on every PR."

---

## SLIDE 60: In-Editor Code Review

### Visual
- **Layout:** VS Code chat panel with review prompt
- **Output:** Review comments example

### Text on Slide
```
🔍 IN-EDITOR CODE REVIEW

Review without creating a PR:

┌─────────────────────────────────────────────────────────┐
│ "Review my recent changes in #file:src/api/v1/todos.py │
│                                                         │
│  Check for:                                             │
│  1. Security issues (auth, validation)                  │
│  2. Error handling completeness                         │
│  3. Performance concerns                                │
│  4. Best practice violations                            │
│                                                         │
│  Be thorough and critical."                             │
└─────────────────────────────────────────────────────────┘

USE FOR:
• Self-review before committing
• Quick sanity check on changes
• Learning from AI feedback
```

### Speaker Notes
> "You can also review in the editor. Ask Copilot to review a file, be thorough and critical. Great for self-review before committing or quick sanity checks."

---

## SLIDE 61: Custom Agents

### Visual
- **Layout:** Agent file structure
- **Icons:** Different specialized robot icons
- **File path:** .github/agents/*.agent.md

### Text on Slide
```
🤖 CUSTOM AGENTS (.agent.md)

Create specialized AI personas for your project:

LOCATION: .github/agents/*.agent.md

┌─────────────────────────────────────────────────────────┐
│  .github/                                               │
│  └── agents/                                            │
│      ├── fastapi-expert.agent.md                        │
│      ├── testing-specialist.agent.md                    │
│      └── security-reviewer.agent.md                     │
└─────────────────────────────────────────────────────────┘

WHAT THEY DO:
• Define specialized AI personas
• Include project-specific knowledge
• Set constraints and patterns
• Reusable across conversations

Pre-configured experts for YOUR codebase!
```

### Speaker Notes
> "Custom Agents are specialized AI personas. Create .agent.md files in .github/agents/. Each agent knows your specific patterns, architecture, coding standards. Pre-configured experts for your project."

---

## SLIDE 62: Creating a Custom Agent

### Visual
- **Layout:** Full agent file example
- **Syntax highlighting:** Markdown content
- **Sections:** Clearly labeled

### Text on Slide
```
CREATING A CUSTOM AGENT

# .github/agents/todo-api.agent.md

┌─────────────────────────────────────────────────────────┐
│ # Todo API Expert Agent                                 │
│                                                         │
│ You are an expert in our Todo API codebase.             │
│                                                         │
│ ## Architecture                                         │
│ - FastAPI with async/await                              │
│ - 3-tier: API → Services → Models                       │
│ - SQLAlchemy with async sessions                        │
│                                                         │
│ ## Key Patterns                                         │
│ - All endpoints require authentication                  │
│ - Service layer handles business logic                  │
│ - Models use UUID primary keys                          │
│                                                         │
│ ## When implementing:                                   │
│ 1. Follow existing patterns                             │
│ 2. Create tests first (TDD)                             │
│ 3. Use 3-tier architecture                              │
│ 4. Include proper error handling                        │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Here's a custom agent. It knows your architecture, patterns, file structure, coding standards. Reference it with #file and AI automatically follows all these rules. Less explaining, better results."

---

## SLIDE 63: The 70% Problem

### Visual
- **Layout:** Split graphic - 70% / 30%
- **Icons:** Robot for 70%, Human for 30%
- **Color coding:** Blue for AI, Gold for Human

### Text on Slide
```
⚠️ THE 70% PROBLEM - CRITICAL UNDERSTANDING

AI delivers rapid initial progress.
But the final 30%? That's where YOU add value.

┌─────────────────────────┬───────────────────────────────┐
│   AI DELIVERS (70%)     │    YOU MUST ADD (30%)         │
├─────────────────────────┼───────────────────────────────┤
│ ✅ Boilerplate code      │ 🎯 Edge cases AI missed       │
│ ✅ Standard patterns     │ 🎯 Performance optimization   │
│ ✅ Happy path impl       │ 🎯 Security hardening         │
│ ✅ Basic structure       │ 🎯 Production-readiness       │
│                         │ 🎯 Business logic nuances     │
│                         │ 🎯 Real-world error handling  │
└─────────────────────────┴───────────────────────────────┘

Organizations that understand this: 26% productivity gains
Those that don't: Accumulating technical debt
```

### Speaker Notes
> "Critical understanding: AI gets you 70% there fast. But the final 30% - edge cases, performance, security, production-readiness - that's where YOU add value. In the Boss Fight, AI will get you 70% quickly. YOUR job is to finish the 30%."

---

## SLIDE 64: Boss Fight Introduction

### Visual
- **Layout:** Epic challenge announcement
- **Gaming theme:** Boss health bar, challenge card
- **Timer:** Prominent countdown graphic

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              🎮 BOSS FIGHT 🎮                              
          THE ULTIMATE CHALLENGE                           
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHALLENGE: Build complete TODO TAGGING feature
           Many-to-many relationships

TIME LIMIT: 10 minutes

REQUIREMENTS:
• POST /api/v1/todos/{id}/tags - Add tag
• GET /api/v1/todos?tag=name - Filter by tag
• DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag
• Full 3-tier architecture
• Ownership validation (THE 30%!)
• Error handling (404, 403, 400)

USE ALL TECHNIQUES FROM SESSIONS 1-3! 🔥
```

### Speaker Notes
> "This is it. The Boss Fight. Build a complete tagging feature with many-to-many relationships. 10 minutes. Use EVERYTHING you've learned. AI gets you 70% - you add the 30%. Ownership validation, proper error handling. That's YOUR value."

---

## SLIDE 65: Boss Fight Techniques

### Visual
- **Layout:** Technique checklist
- **Icons:** Each technique from previous sessions
- **Scoring bonus:** Points for each technique used

### Text on Slide
```
🛠️ TECHNIQUES TO USE

From Session 1:
☐ Agent Mode for building
☐ #mentions for context

From Session 2:
☐ "think hard" for planning
☐ 6-element framework prompts
☐ PRD reference

From Session 3:
☐ TDD approach
☐ Subagents for parallel work
☐ Plan Mode for visibility

From Session 4:
☐ Custom Agent (bonus!)

SCORING:
• Complete in 6 min: 🏆 PLATINUM
• Complete in 8 min: 🥇 GOLD
• Complete in 10 min: 🥈 SILVER
• Complete at all: ✅ CERTIFIED
```

### Speaker Notes
> "Use everything. Agent Mode, mentions, thinking modes, 6-element framework, TDD, subagents, Plan Mode. Each technique used is bonus points. Platinum if you finish in 6 minutes, certified if you finish at all. Let's go!"

---

## SLIDE 66: Boss Fight Strategy - Planning

### Visual
- **Layout:** Initial planning prompt
- **Highlighting:** think hard keyword
- **Step indicator:** Step 1

### Text on Slide
```
🎮 BOSS FIGHT STRATEGY - STEP 1: PLAN

Start with "think hard":

┌─────────────────────────────────────────────────────────┐
│ #file:PRD-Tags.md #file:src/models/todo.py              │
│                                                         │
│ think hard about implementing many-to-many tagging      │
│ for todos.                                              │
│                                                         │
│ Requirements:                                           │
│ - POST /api/v1/todos/{id}/tags                          │
│ - GET /api/v1/todos?tag=name                            │
│ - DELETE /api/v1/todos/{id}/tags/{tag_id}               │
│ - 3-tier architecture                                   │
│ - Ownership validation                                  │
│                                                         │
│ Consider: Schema, case sensitivity, API design          │
│                                                         │
│ Give me the complete implementation plan.               │
└─────────────────────────────────────────────────────────┘

⏱️ ~30 seconds for planning
```

### Speaker Notes
> "Step 1: Plan with think hard. Get a complete implementation plan before writing any code. 30 seconds of planning saves minutes of iteration."

---

## SLIDE 67: Boss Fight Strategy - Implementation

### Visual
- **Layout:** Plan Mode or sequential approach
- **Options:** Two paths shown
- **Step indicator:** Step 2

### Text on Slide
```
🎮 BOSS FIGHT STRATEGY - STEP 2: IMPLEMENT

OPTION A: Plan Mode (recommended)
┌─────────────────────────────────────────────────────────┐
│ /plan Implement tagging feature:                        │
│ 1. Create Tag model and association table               │
│ 2. Create schemas                                       │
│ 3. Add service methods                                  │
│ 4. Add API endpoints                                    │
│ 5. Include ownership validation                         │
│                                                         │
│ Follow patterns in #folder:src/                         │
└─────────────────────────────────────────────────────────┘

OPTION B: Sequential (TDD style)
• Step 1: Database models
• Step 2: Schemas
• Step 3: Service layer
• Step 4: API endpoints
• Step 5: Add the 30% (validation, errors)
```

### Speaker Notes
> "Step 2: Implement. Use Plan Mode to see everything before it runs, or go sequential with TDD. Either works - choose what fits your style."

---

## SLIDE 68: Boss Fight - Your Turn!

### Visual
- **Layout:** Large timer graphic
- **Action button:** START
- **Countdown style:** Digital clock

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 5                          
                    BOSS FIGHT                             
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 10 minutes

Build the tagging feature!

SUCCESS CRITERIA:
☐ Tag model with many-to-many relationship
☐ POST endpoint to add tag
☐ GET endpoint with tag filter
☐ DELETE endpoint to remove tag
☐ Ownership validation (THE 30%!)
☐ Proper error codes (404, 403, 400)

REMEMBER: AI gives you 70%. YOU add the final 30%!

                    ⏱️ 10:00
                    
            BOSS FIGHT STARTS NOW!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "This is it! 10 minutes. Build the tagging feature. Use everything you learned. AI gets you 70%, you add the 30%. Timer starts NOW!"

**[EXERCISE PLACEHOLDER: 10 minutes - Students complete Boss Fight]**

---

## SLIDE 69: Boss Fight Complete!

### Visual
- **Layout:** Victory screen
- **Confetti/celebration:** Animation
- **Scoring results:** Space for results

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              🎉 BOSS FIGHT COMPLETE! 🎉                    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Results:

🏆 PLATINUM (<6 min):  ___ participants
🥇 GOLD (<8 min):      ___ participants
🥈 SILVER (<10 min):   ___ participants
✅ CERTIFIED:          Everyone who completed!

Techniques used:
□ think hard    □ 6-element framework
□ TDD           □ Subagents
□ Plan Mode     □ #mentions
□ Custom Agent

YOU DID IT! 🏆
```

### Speaker Notes
> "Time! Who finished? Let's see the results. Platinum if under 6 minutes... Gold under 8... Silver under 10... Everyone who completed is CERTIFIED. You just built a complex many-to-many feature using AI assistance!"

---

## SLIDE 70: What You Mastered

### Visual
- **Layout:** Complete skill tree, all unlocked
- **Icons:** All badges earned
- **Visual:** Full journey map

### Text on Slide
```
🏆 WHAT YOU MASTERED TODAY

SESSION 1: Security & Superpowers
  ✅ .copilotignore for secrets
  ✅ All 4 AI modes (Ask, Edit, Agent, Plan)
  ✅ All #mention types
  ✅ Custom Instructions

SESSION 2: Context Mastery
  ✅ Thinking modes
  ✅ Explore → Plan → Code workflow
  ✅ PRDs for documentation
  ✅ 6-element framework

SESSION 3: Build Sprint
  ✅ TDD with AI
  ✅ Full context implementation
  ✅ Subagents
  ✅ Plan Mode

SESSION 4: Mastery
  ✅ Code Review
  ✅ Custom Agents
  ✅ The 70% Problem
  ✅ BOSS FIGHT COMPLETE!
```

### Speaker Notes
> "Look at what you mastered. Security. All the modes. Context strategies. Professional workflow. Building at speed. Code review. Custom agents. And you proved it all in the Boss Fight. You're a Copilot Power User."

---

## SLIDE 71: Power User Certification

### Visual
- **Layout:** Certificate design
- **Gold/prestigious:** Official looking
- **Space for name:** Personalization

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              🏆 POWER USER CERTIFIED 🏆                    

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                  This certifies that

                 ___________________

              has completed the GitHub Copilot
             Power User Workshop and demonstrated
                 mastery of AI-assisted coding

                      Skills Proven:
           ✅ Security-first development
           ✅ Professional prompting techniques
           ✅ Context mastery
           ✅ Test-driven development with AI
           ✅ Complex feature implementation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "You earned this. Power User Certified. You have security skills, professional prompting, context mastery, TDD with AI, and you proved it by building complex features. Congratulations!"

---

## SLIDE 72: Thank You & Next Steps

### Visual
- **Layout:** Closing slide with resources
- **QR codes:** For resource links
- **Contact info:** How to reach out

### Text on Slide
```
🙏 THANK YOU!

WHAT'S NEXT:

📚 Resources
   • Student reference guides (all sessions)
   • Prompt sheets for quick reference
   • knowledge.md - complete Copilot reference

💪 Practice
   • Build features in your own projects
   • Try new techniques daily
   • Experiment with Custom Agents

🤝 Community
   • Share what you build
   • Help others learn
   • Keep experimenting!

Questions? [Your contact info]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         From First Prompt to Power User 🚀               
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Thank you for joining today! You have all the resources - reference guides, prompt sheets, the knowledge base. Practice in your own projects, experiment with custom agents, share what you build. You went from first prompt to power user. Now go change how you code. Questions?"

---

# 📋 QUICK REFERENCE: Exercise Placeholders Summary

| Slide | Exercise | Duration | Description |
|-------|----------|----------|-------------|
| 15 | Exercise 1 | 3 min | Generate practice project with Agent Mode |
| 23 | Exercise 2 | 3 min | Mention Bingo - try all #mention types |
| 37 | Exercise 3 | 5 min | Create PRD for priority feature |
| 48 | Exercise 4 | 10 min | Build Create Todo with TDD |
| 51 | Speed Challenge | 3 min | Build Update Todo in 3 minutes |
| 68 | Exercise 5 (Boss Fight) | 10 min | Complete tagging feature |

**Total Exercise Time:** ~34 minutes of hands-on practice

---

# 🎨 VISUAL DESIGN NOTES

## Color Palette
- **Primary Blue:** #0066FF (Copilot brand)
- **Secondary Purple:** #8B5CF6 (Session 2)
- **Success Green:** #10B981 (Session 3)
- **Gold/Achievement:** #F59E0B (Session 4)
- **Background Dark:** #0D1117 (GitHub dark)
- **Text Light:** #E6EDF3

## Icon Suggestions
- Use consistent icon set (Lucide, Heroicons, or Font Awesome)
- Shield for security
- Brain for thinking/planning
- Rocket for building
- Trophy for achievements
- Robot for AI/agents

## Typography
- **Headings:** Bold, clean sans-serif
- **Body:** Regular weight, good line height
- **Code:** Monospace font (JetBrains Mono, Fira Code)

## Animation Suggestions (if using presentation software)
- Slide transitions: Simple fade or slide
- Element reveals: Fade in for bullet points
- Highlights: Subtle pulse for emphasis
- Timer animations: For exercises

---

*End of Slide Deck Guide*
