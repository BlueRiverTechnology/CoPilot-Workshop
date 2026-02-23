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

Duration: 30 minutes
```

### Speaker Notes
> "The finale! Session 4 is where you prove mastery. Checkpoint verification, Code Review, Custom Agents, Memory Bank, the 70% Problem, and the Boss Fight. Complete the Boss Fight and you're a certified Copilot Power User!"

---

## SLIDE 58: Session 4 Objectives

### Visual
- **Layout:** Final objectives with trophy icons
- **Style:** Epic/climactic feeling

### Text on Slide
```
SESSION 4 OBJECTIVES - THE FINALE

By the end of this session, you will:

○  Verify session-4-start checkpoint
   Start with working API + Tags infrastructure

○  Use Copilot Code Review for PR feedback
   Automated quality checks

○  Create Custom Agents (.agent.md files)
   Specialized AI personas for your project

○  Build a Memory Bank
   Persistent project context across sessions

○  Understand the 70% Problem
   Where AI helps, where YOU add value

○  Complete the BOSS FIGHT
   Build tag endpoint using ALL techniques

○  EARN POWER USER CERTIFICATION 🏆
   Prove your mastery
```

### Speaker Notes
> "Seven objectives for the finale. Checkpoint verification, Code Review, Custom Agents, Memory Bank, the 70% Problem, Boss Fight, and certification. Complete the Boss Fight - you're certified. Let's go!"

---

## SLIDE 59: Checkpoint Verification - Session 4 Start

### Visual
- **Layout:** Terminal commands with expected output
- **Checkmarks:** Green verification indicators
- **Safety net:** Highlighted

### Text on Slide
```
CHECKPOINT VERIFICATION - SESSION 4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Verify you have the working API with Tags:

┌─────────────────────────────────────────────────────────┐
│ # Switch to session-4-start checkpoint                  │
│ git checkout session-4-start                            │
│                                                         │
│ # Create database                                       │
│ python create_db.py                                     │
│                                                         │
│ # Run tests (should have 10 passing)                    │
│ pytest tests/api/test_todos.py -v                       │
└─────────────────────────────────────────────────────────┘

EXPECTED: 10 tests PASSED ✅
(8 from Session 3 + 2 new DELETE tests)

WHAT'S NEW IN THIS CHECKPOINT:
✅ DELETE endpoint working
✅ Tag model created (id, name, created_at)
✅ todo_tags association table
✅ Many-to-many relationship ready

Your safety net for the Boss Fight!
```

### Speaker Notes
> "First: checkpoint verification. Everyone switch to session-4-start, create the database, run tests. You should see 10 tests pass. This checkpoint gives you everything from Session 3 PLUS the Tag infrastructure. Tag model exists, association table is ready, many-to-many relationship is defined. This is your safety net for the Boss Fight!"

---

## SLIDE 60: Copilot Code Review

### Visual
- **Layout:** GitHub PR interface mockup
- **Icons:** Review checkmark, comments
- **Two-panel:** GitHub + VS Code

### Text on Slide
```
🔍 COPILOT CODE REVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Automated code review on every Pull Request

TWO WAYS TO USE:

1️⃣ GITHUB PR REVIEW:
   • Create PR on GitHub
   • Request review from "copilot"
   • Get inline comments and suggestions

2️⃣ IN-EDITOR REVIEW:
   • No PR needed!
   • Use Copilot Chat directly
   • Instant feedback

WHAT IT CHECKS:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns

Like having a tireless reviewer on every PR!
```

### Speaker Notes
> "Copilot Code Review works two ways. On GitHub, request 'copilot' as a reviewer on any PR. It analyzes changes, leaves inline comments, finds bugs, security issues. Or use it in VS Code Chat for instant feedback without creating a PR. Either way, it's like having a tireless code reviewer!"

---

## SLIDE 61: In-Editor Code Review Demo

### Visual
- **Layout:** Chat panel with review prompt
- **Output:** Sample review comments
- **Highlighting:** Specific issues found

### Text on Slide
```
IN-EDITOR CODE REVIEW - INSTANT FEEDBACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Review code WITHOUT creating a PR:

┌─────────────────────────────────────────────────────────┐
│ Review my implementation in #file:src/api/v1/todos.py  │
│                                                         │
│ Check for:                                              │
│ 1. Security issues (auth, validation, ownership)        │
│ 2. Error handling completeness                          │
│ 3. Performance concerns (N+1 queries, missing indexes)  │
│ 4. Best practice violations                             │
│                                                         │
│ Be thorough and critical. Point out line numbers.       │
└─────────────────────────────────────────────────────────┘

RESULT:
Copilot provides detailed feedback with line numbers,
specific issues, and suggestions for fixes

USE FOR:
• Self-review before committing
• Quick sanity check on changes
• Learning from AI feedback
• Finding edge cases you missed
```

### Speaker Notes
> "In-editor review is powerful. Ask Copilot to review a file, be thorough and critical. It provides detailed feedback with line numbers, specific issues, suggestions. Use this for self-review before committing, quick sanity checks, learning from AI, finding edge cases. This is YOUR 30% work - ensuring quality!"

---

## SLIDE 62: Custom Agents Overview

### Visual
- **Layout:** Agent file structure diagram
- **Icons:** Different specialized robot icons
- **Hierarchy:** Showing relationship to instructions

### Text on Slide
```
🤖 CUSTOM AGENTS (.agent.md)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create specialized AI personas for your project

LOCATION: .github/agents/*.agent.md

FILE STRUCTURE:
┌─────────────────────────────────────────────────────────┐
│ .github/                                                │
│ └── agents/                                             │
│     ├── todo-api-expert.agent.md                        │
│     ├── testing-specialist.agent.md                     │
│     └── security-reviewer.agent.md                      │
└─────────────────────────────────────────────────────────┘

WHAT THEY DO:
• Define specialized AI personas
• Include project-specific knowledge
• Set constraints and patterns
• Reusable across conversations

THE HIERARCHY:
.github/copilot-instructions.md → Repo-wide, always active
.github/instructions/*.md → Path-specific rules
.github/agents/*.agent.md → Custom personas

Pre-configured experts for YOUR codebase!
```

### Speaker Notes
> "Custom Agents are specialized AI personas. Create .agent.md files in .github/agents/. Each agent knows your specific patterns, architecture, coding standards. They sit in the hierarchy: repo-wide instructions are always active, path-specific scope to files, and agents are specialized personas you invoke. Pre-configured experts for your codebase!"

---

## SLIDE 63: Creating a Custom Agent

### Visual
- **Layout:** Full agent file example
- **Syntax highlighting:** Markdown content
- **Sections:** Clearly labeled

### Text on Slide
```
CREATING A CUSTOM AGENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

.github/agents/todo-api-expert.agent.md

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
│ - Fixed owner_id = "default-user" (no JWT auth)         │
│ - Service layer handles business logic                  │
│ - Models use UUID string primary keys                   │
│                                                         │
│ ## When Implementing                                    │
│ 1. Follow existing patterns                             │
│ 2. Use 3-tier architecture                              │
│ 3. Include proper error handling                        │
│ 4. Return appropriate HTTP status codes                 │
└─────────────────────────────────────────────────────────┘

Reference with #file:.github/agents/todo-api-expert.agent.md
AI automatically follows all these rules!
```

### Speaker Notes
> "Here's a custom agent for our Todo API. It knows the architecture, patterns, file structure, coding standards. Reference it with #file in your prompt and AI automatically follows all these rules. Less explaining in each prompt, better results, consistent code. This is persistent expertise you invoke on demand!"

---

## SLIDE 64: The Memory Problem

### Visual
- **Layout:** Split screen - repeated messages vs frustration
- **Animation:** Messages stacking up
- **Emphasis:** "Every session starts from zero"

### Text on Slide
```
🧠 THE PROBLEM: COPILOT FORGETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every new chat session starts from zero

Monday:    "We use FastAPI with async..."
Tuesday:   "Remember, we use FastAPI..."
Wednesday: "I ALREADY TOLD YOU..."
Thursday:  😤

Your context. Your decisions. Your progress.
Gone. Every. Single. Time.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Custom Agents define HOW you work
But they don't remember WHERE you are

What if Copilot could REMEMBER?
```

### Speaker Notes
> "Custom Agents are great for defining how you work - your patterns and rules. But here's the problem: Copilot forgets between sessions. Every new chat starts from zero. You end up repeating your project setup, your decisions, your progress. Monday you explain, Tuesday you repeat, Wednesday you're frustrated. The Memory Bank solves this."

---

## SLIDE 65: Memory Bank Structure

### Visual
- **Layout:** Folder tree with descriptions
- **Color coding:** Each file different color
- **Highlight:** activeContext.md glows

### Text on Slide
```
🧠 THE MEMORY BANK - 6 FILES FOR PERSISTENT CONTEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

memory-bank/
├── projectbrief.md      → What is this project?
├── productContext.md    → Why does it exist?
├── techContext.md       → What tech do we use?
├── systemPatterns.md    → How do we build things?
├── activeContext.md  ⚡ → What's happening NOW?
└── progress.md          → Where do we stand?

+ Update .github/copilot-instructions.md
  Tell Copilot: "Read memory-bank/ first"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Copilot reads these EVERY session
✨ Say "update memory bank" to save state
✨ Zero context lost between sessions

activeContext.md changes most - current focus, recent
changes, next steps. Others are more stable.
```

### Speaker Notes
> "The Memory Bank is six markdown files, each answering a question Copilot needs. Project brief is the foundation. Tech context is your stack. System patterns is your architecture. Active context is what changes most - your current focus, recent changes, next steps. Progress is where you stand. Update copilot-instructions to tell Copilot to read these files first. Then say 'update memory bank' at end of session to save state!"

---

## SLIDE 66: Memory Bank Daily Workflow

### Visual
- **Layout:** Circular flow diagram
- **Steps:** Morning → Code → End of Day → Loop
- **Key insight:** Custom Agents vs Memory Bank

### Text on Slide
```
🧠 THE DAILY WORKFLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────┐
  │   MORNING   │ Copilot reads memory-bank/
  │  Context restored automatically
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │   CODING    │ Better suggestions
  │  No repeating yourself
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │ END OF DAY  │ "update memory bank"
  │  State saved to markdown
  └──────┬──────┘
         │
         └──────→ Next day: zero context lost

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHT:
Custom Agents → HOW you work (patterns, rules)
Memory Bank   → WHERE you are (current state)

Together: Copilot becomes a true project partner!
```

### Speaker Notes
> "This is the workflow. Morning: context automatically restored. Coding: better results, no repeating. End of day: update the bank. Next morning: pick up where you left off. Think of it this way - Custom Agents tell Copilot HOW you work. Memory Bank tells Copilot WHERE you are. Together, Copilot becomes a true project partner with persistent knowledge!"

---

## SLIDE 67: The 70% Problem

### Visual
- **Layout:** Split graphic - 70% / 30%
- **Icons:** Robot for 70%, Human for 30%
- **Color coding:** Blue for AI, Gold for Human

### Text on Slide
```
⚠️ THE 70% PROBLEM - CRITICAL UNDERSTANDING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI delivers rapid initial progress
But the final 30%? That's where YOU add value

┌─────────────────────────┬───────────────────────────┐
│   AI DELIVERS (70%)     │   YOU MUST ADD (30%)      │
├─────────────────────────┼───────────────────────────┤
│ ✅ Boilerplate code      │ 🎯 Edge cases AI missed   │
│ ✅ Standard patterns     │ 🎯 Ownership validation   │
│ ✅ Happy path impl       │ 🎯 Performance optimization│
│ ✅ Basic structure       │ 🎯 Security hardening     │
│                         │ 🎯 Production-readiness   │
│                         │ 🎯 Business logic nuances │
│                         │ 🎯 Real-world errors      │
└─────────────────────────┴───────────────────────────┘

Organizations that understand this: 26% productivity gains
Those that don't: Accumulating technical debt

In Boss Fight: AI gets 70% fast. YOU finish the 30%!
```

### Speaker Notes
> "Critical understanding: AI gets you 70% there fast. Boilerplate, standard patterns, basic structure. But the final 30% - edge cases, ownership validation, performance, security, production-readiness - that's where YOU add value. Organizations that understand this see 26% productivity gains. Those that don't accumulate technical debt. In the Boss Fight, AI will get you 70% quickly. Your job is to finish the critical 30%!"

---

## SLIDE 68: Boss Fight Introduction

### Visual
- **Layout:** Epic challenge announcement
- **Gaming theme:** Boss health bar, challenge card
- **Timer:** Prominent 5-minute countdown

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              🎮 BOSS FIGHT 🎮
          THE ULTIMATE CHALLENGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHALLENGE: Build POST /api/v1/todos/{todo_id}/tags

TIME LIMIT: 5 minutes ⏱️

WHAT'S ALREADY BUILT (session-4-start):
✅ Tag model (id, name, created_at)
✅ todo_tags association table
✅ Todo.tags relationship defined

WHAT YOU BUILD:
• POST /api/v1/todos/{todo_id}/tags
• Request body: { "name": "urgent" }
• Creates tag if doesn't exist (case-insensitive)
• Associates tag with todo
• Returns updated TodoResponse with tags
• THE 30%: Ownership validation (404/403 errors)
• THE 30%: Proper error handling and messages

USE ALL TECHNIQUES FROM SESSIONS 1-3! 🔥
```

### Speaker Notes
> "This is it. The Boss Fight. Build a POST endpoint to add tags to todos. 5 minutes. Infrastructure is already built - Tag model exists, association table is ready. You build ONE endpoint with proper ownership validation and error handling. That's YOUR 30%. Use EVERYTHING you've learned!"

---

## SLIDE 69: Boss Fight Techniques Checklist

### Visual
- **Layout:** Technique checklist with bonuses
- **Icons:** Each technique from previous sessions
- **Scoring:** Points for each technique

### Text on Slide
```
🛠️ BOSS FIGHT TECHNIQUES CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

USE THESE TECHNIQUES:

FROM SESSION 1:
☐ Agent Mode for building
☐ #mentions for context (#file, #folder)
☐ Custom instructions reference

FROM SESSION 2:
☐ "think hard" for planning
☐ Context+Task+Constraints+Format framework
☐ PRD reference

FROM SESSION 3:
☐ Start from checkpoint (session-4-start)
☐ Verify with tests

FROM SESSION 4:
☐ Custom Agent reference (bonus!)
☐ Code Review when done

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCORING:
• Complete in 3 min: 🏆 PLATINUM
• Complete in 4 min: 🥇 GOLD
• Complete in 5 min: 🥈 SILVER
• Complete at all: ✅ CERTIFIED

+1 level for each technique used!
```

### Speaker Notes
> "Use everything. Agent Mode, mentions, think hard, the framework, checkpoint start, custom agents, code review. Each technique used is bonus points. Platinum if under 3 minutes, certified if you finish at all. Let's go!"

---

## SLIDE 70: Boss Fight - Winning Strategy

### Visual
- **Layout:** Step-by-step strategy guide
- **Highlighting:** Key prompt elements
- **Timer:** Step durations

### Text on Slide
```
BOSS FIGHT WINNING STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: PLAN (30 seconds)
Use "think hard" to get implementation plan

STEP 2: IMPLEMENT (3-4 minutes)
One comprehensive prompt with:
  #file:.github/agents/todo-api-expert.agent.md
  #file:PRD.md
  #file:src/models/tag.py
  #folder:src/api/v1/

  [Context] - Tag infrastructure exists
  [Task] - POST /api/v1/todos/{todo_id}/tags
  [Constraints] - Layer by layer specs
    - TagCreate schema
    - Service method (get/create tag, add to todo)
    - API endpoint (ownership validation!)
  [Format] - Which files to create/update

STEP 3: THE 30% (30 seconds)
Verify ownership validation:
  "Can ANY user tag ANY todo? Or just their own?"
  Fix any issues!

STEP 4: QUICK TEST (30 seconds)
curl test or pytest
```

### Speaker Notes
> "Winning strategy: Plan with think hard for 30 seconds. Implement with one comprehensive prompt including custom agent, PRD, model files. Specify constraints layer by layer. Then verify the critical 30% - ownership validation. Finally, quick test. This strategy gets you there!"

---

## SLIDE 71: Exercise - Boss Fight!

### Visual
- **Layout:** Large timer graphic
- **Action button:** START
- **Countdown:** Digital clock style

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 5
                    BOSS FIGHT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 5 minutes

Build POST /api/v1/todos/{todo_id}/tags endpoint!

SUCCESS CRITERIA:
☐ TagCreate and TagResponse schemas created
☐ Service method add_tag_to_todo() implemented
☐ POST endpoint in src/api/v1/todos.py
☐ TodoResponse includes tags: List[TagResponse]
☐ Ownership validation (404 if not found, 403 if not owned)
☐ Case-insensitive tag creation
☐ Proper error codes and messages

REMEMBER:
AI gives you 70%. YOU add the final 30%!
(Ownership checks, error handling, edge cases)

                    ⏱️ 5:00

            BOSS FIGHT STARTS NOW!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "This is it! 5 minutes. Build the tag endpoint. Use everything you learned. AI gets you 70%, you add the 30%. Ownership validation, error handling, edge cases - that's YOUR value. Timer starts NOW!"

**[EXERCISE PLACEHOLDER: 5 minutes - Students complete Boss Fight]**

---

## SLIDE 72: Boss Fight Complete - Results

### Visual
- **Layout:** Victory screen with results
- **Confetti:** Celebration animation
- **Scoring:** Level breakdown

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              🎉 BOSS FIGHT COMPLETE! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESULTS:

🏆 PLATINUM (<3 min):  ___ participants
🥇 GOLD (<4 min):      ___ participants
🥈 SILVER (<5 min):    ___ participants
✅ CERTIFIED:          Everyone who completed!

TECHNIQUES USED:
□ think hard         □ Custom Agent
□ 6-element framework □ #mentions
□ TDD approach       □ Code Review
□ Ownership validation (THE 30%!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU DID IT! 🏆

You just built a many-to-many tag endpoint
using AI assistance + YOUR critical 30%!
```

### Speaker Notes
> "Time! Who finished? Let's see the results. Platinum under 3 minutes... Gold under 4... Silver under 5... Everyone who completed is CERTIFIED. You just built a many-to-many relationship endpoint with ownership validation using AI assistance. You proved your mastery!"

---

## SLIDE 73: What You Mastered Today

### Visual
- **Layout:** Complete skill tree, all unlocked
- **Icons:** All badges earned
- **Journey map:** Full workshop path

### Text on Slide
```
🏆 WHAT YOU MASTERED TODAY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SESSION 1: Security & Superpowers
  ✅ .copilotignore for secrets
  ✅ All 4 AI modes (Ask, Edit, Agent, Plan)
  ✅ All #mention types
  ✅ Writing Effective AI Rules (7 principles)
  ✅ Custom Instructions

SESSION 2: Context Mastery
  ✅ Thinking modes
  ✅ Explore → Plan → Code workflow
  ✅ PRDs for documentation
  ✅ 6-element framework

SESSION 3: Build Sprint
  ✅ Checkpoint-based development
  ✅ TDD with AI
  ✅ Full context implementation
  ✅ Professional workflows

SESSION 4: Mastery
  ✅ Code Review
  ✅ Custom Agents
  ✅ Memory Bank
  ✅ The 70% Problem
  ✅ BOSS FIGHT COMPLETE!
```

### Speaker Notes
> "Look at what you mastered in one day. Security-first development. All the AI modes. Writing effective rules. Context mastery. Professional prompting. Checkpoint-based workflows. TDD. Code Review. Custom Agents. Memory Bank. The 70/30 understanding. And you proved it all in the Boss Fight. You're a Copilot Power User!"

---

## SLIDE 74: Power User Certification

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
           ✅ All AI interaction modes
           ✅ Writing effective AI rules
           ✅ Professional prompting techniques
           ✅ Context mastery
           ✅ Checkpoint-based workflows
           ✅ Test-driven development with AI
           ✅ Custom Agents and Memory Bank
           ✅ Complex feature implementation

                  Level: _______________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "You earned this. Power User Certified. You have security skills, know all modes, can write effective rules, master context and prompting, use checkpoints, do TDD with AI, build Custom Agents and Memory Banks, and you proved it by building a complex feature. Congratulations!"

---

## SLIDE 75: Thank You & Next Steps

### Visual
- **Layout:** Closing slide with resources
- **QR codes:** For resource links
- **Contact info:** How to reach out

### Text on Slide
```
🙏 THANK YOU!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT'S NEXT:

📚 RESOURCES
   • Student reference guides (all sessions)
   • Prompt sheets for quick reference
   • knowledge.md - complete Copilot reference
   • 🌟 GitHub Awesome Copilot
     (github.com/github/awesome-copilot)
     → Advanced tips, best practices, community

💪 PRACTICE
   • Build features in your own projects
   • Try new techniques daily
   • Experiment with Custom Agents and Memory Bank
   • Share what you learn

🤝 COMMUNITY
   • Share what you build
   • Help others learn
   • Keep experimenting!
   • Join the AI-augmented developer movement

Questions? [Your contact info]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         From First Prompt to Power User 🚀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Thank you for joining today! You have all the resources - reference guides, prompt sheets, the knowledge base, GitHub Awesome Copilot for community resources. Practice in your own projects, experiment with custom agents and memory banks, share what you build. You went from first prompt to power user. Now go transform how you code. Questions?"

---

# 📋 QUICK REFERENCE: Exercise Placeholders Summary

| Slide | Exercise | Duration | Description |
|-------|----------|----------|-------------|
| 15 | Exercise 1 | 3 min | Generate practice project with Agent Mode |
| 23 | Exercise 2 | 3 min | Mention Bingo - try all #mention types |
| 34 | Exercise 3 | 2 min | Write your own AI rules |
| 51 | Exercise 4 | 12 min | Build priority feature with support |
| 71 | Exercise 5 (Boss Fight) | 5 min | Build tag endpoint (simplified) |

**Total Exercise Time:** ~25 minutes of hands-on practice

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

*End of Session 4 Slides*
