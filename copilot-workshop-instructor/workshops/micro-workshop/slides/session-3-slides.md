# 📍 SESSION 3: BUILD SPRINT (Slides 41-56)

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

🚀 BUILD SPRINT - PROFESSIONAL WORKFLOWS

"Build on proven foundations, like the pros"

Duration: 30 minutes
```

### Speaker Notes
> "Session 3: Build Sprint! You learned the tools, you learned the thinking. Now you build like professionals - starting with working code, adding features incrementally, keeping the system working. This is real-world development with AI."

---

## SLIDE 42: The Professional Approach

### Visual
- **Layout:** Comparison diagram (Amateur vs Professional)
- **Icons:** Warning vs Checkmark
- **Emphasis:** "Start with working code"

### Text on Slide
```
THE PROFESSIONAL APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ AMATEUR APPROACH:
   Build everything from scratch
   Hope it all works together
   Fix when it breaks

✅ PROFESSIONAL APPROACH:
   Start with proven, working code
   Add features incrementally
   Test each change
   Keep the system working at all times

Today: You start with a FULLY WORKING Todo API!
```

### Speaker Notes
> "Here's what's different today. You're NOT starting from scratch. Professionals don't rebuild infrastructure every time. They start with proven, working code, add features incrementally, test each change, and keep the system working. That's what you're about to experience!"

---

## SLIDE 43: Checkpoint Verification

### Visual
- **Layout:** Terminal output preview
- **Checkmarks:** Green success indicators
- **Step-by-step:** Numbered verification steps

### Text on Slide
```
CHECKPOINT VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

First: Verify you have the working API

Run these commands:
┌─────────────────────────────────────────────────────────┐
│ # Switch to session-3-start checkpoint                  │
│ git checkout session-3-start                            │
│                                                         │
│ # Create database                                       │
│ python create_db.py                                     │
│                                                         │
│ # Run tests                                             │
│ pytest tests/api/test_todos.py -v                       │
└─────────────────────────────────────────────────────────┘

Expected: 8 PASSED tests ✅

This is your safety net - working code you can always
return to with git reset!
```

### Speaker Notes
> "First, everyone verify you have the working API. Run these three commands: switch to the checkpoint branch, create the database, run tests. You should see 8 green passing tests. This is your safety net. If anything breaks today, you can always git reset back to this working state."

---

## SLIDE 44: What's Already Built

### Visual
- **Layout:** File tree with checkmarks
- **Icons:** Folder and file icons
- **Color coding:** Green for complete

### Text on Slide
```
WHAT'S ALREADY BUILT FOR YOU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

src/
├── database.py              ✅ Async DB setup
├── schemas/
│   └── todo.py             ✅ TodoCreate, TodoUpdate, TodoResponse
├── services/
│   └── todo_service.py     ✅ Business logic (create, get_all, update)
├── api/v1/
│   └── todos.py            ✅ 3 endpoints (POST, GET, PUT)
└── main.py                 ✅ Router registration

tests/
├── conftest.py             ✅ Test fixtures
└── api/
    └── test_todos.py       ✅ 8 passing tests

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3-tier architecture in action:
  API layer → Service layer → Model layer

You're about to see how pros ADD to this foundation!
```

### Speaker Notes
> "Quick tour of what exists. Complete 3-tier architecture: API routes, service layer with business logic, model layer for database. You have POST to create todos, GET to list them, PUT to update. All tested, all working. You're about to see how professionals add to this foundation!"

---

## SLIDE 45: TDD with AI - The Concept

### Visual
- **Layout:** Circular workflow diagram
- **Icons:** Test tube, code, checkmark, repeat
- **Color flow:** Red → Green → Refactor cycle

### Text on Slide
```
🧪 TEST-DRIVEN DEVELOPMENT (TDD) WITH AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The workflow:

     ┌──────────────────────────────────┐
     │                                  │
     │   1. WRITE TESTS (they fail) 🔴  │
     │          ↓                       │
     │   2. IMPLEMENT CODE (pass) 🟢    │
     │          ↓                       │
     │   3. REFACTOR (improve) ♻️       │
     │          ↓                       │
     │   4. REPEAT                      │
     │                                  │
     └──────────────────────────────────┘

WHY TDD + AI WORKS:
• Tests give AI clear success criteria
• Less ambiguity = better code
• Automatic verification
• Regression protection
• Built-in documentation
```

### Speaker Notes
> "TDD with AI is powerful. Write tests first - they define what success looks like. AI implements code to make tests pass. You verify with tests. This works because tests give AI crystal-clear success criteria. No ambiguity about what 'done' means."

---

## SLIDE 46: Demo Feature - DELETE Endpoint

### Visual
- **Layout:** Feature card with requirements
- **Icon:** Demo/presentation icon
- **Emphasis:** "Watch and learn"

### Text on Slide
```
DEMO: DELETE ENDPOINT USING TDD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU'RE WATCHING (not coding yet!)

Feature: DELETE /api/v1/todos/{id}

Requirements:
• Delete a specific todo by ID
• Return 204 No Content on success
• Return 404 if todo doesn't exist
• Verify todo is actually removed

Watch the 4-step TDD workflow:
  1. Write tests (Ask Mode for planning)
  2. Run tests - watch them FAIL
  3. Implement code (Agent Mode)
  4. Run tests - watch them PASS

Take notes on the workflow!
```

### Speaker Notes
> "Watch me build a DELETE endpoint using TDD. You're watching, not coding yet. Take notes on the workflow. I'll show you all four steps: write tests, watch them fail, implement, watch them pass. This is professional TDD with AI!"

---

## SLIDE 47: Step 1 - Write Tests First

### Visual
- **Layout:** Prompt example with highlighting
- **Mode indicator:** Ask Mode selected
- **Emphasis:** "Tests BEFORE code"

### Text on Slide
```
STEP 1: WRITE TESTS FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Using Ask Mode (not Agent!) to review first:

┌─────────────────────────────────────────────────────────┐
│ I need to write tests for DELETE /api/v1/todos/{id}    │
│                                                         │
│ The test should:                                        │
│ 1. Create a todo first                                  │
│ 2. Delete it via DELETE /api/v1/todos/{id}              │
│ 3. Verify 204 No Content response                       │
│ 4. Verify todo is gone (GET returns empty)              │
│                                                         │
│ Also test:                                              │
│ - Deleting non-existent todo returns 404                │
│                                                         │
│ Add tests to tests/api/test_todos.py following         │
│ existing patterns.                                      │
└─────────────────────────────────────────────────────────┘

WHY ASK MODE?
Review test code before creating files
Professional judgment: when to review vs auto-execute
```

### Speaker Notes
> "Step 1: Write tests. Notice I'm using Ask Mode, not Agent Mode. Why? Because I want to review the test code before creating files. Agent Mode would auto-create. Ask Mode shows me first. This is professional judgment - knowing when to review versus when to auto-execute."

---

## SLIDE 48: Step 2 - Verify Tests Fail

### Visual
- **Layout:** Terminal output showing failures
- **Color:** Red highlighting on FAILED
- **Checkmark:** "This is good!"

### Text on Slide
```
STEP 2: RUN TESTS - VERIFY FAILURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run the tests (they should fail!):

┌─────────────────────────────────────────────────────────┐
│ $ pytest tests/api/test_todos.py::test_delete_todo -v  │
│                                                         │
│ test_delete_todo FAILED                                 │
│ test_delete_todo_not_found FAILED                       │
│                                                         │
│ 404: Not Found (endpoint doesn't exist yet)             │
│                                                         │
│ ========== 2 failed in 0.42s ==========                 │
└─────────────────────────────────────────────────────────┘

✅ PERFECT! This is exactly what we want!

The tests define WHAT we need.
Now we implement to make them pass.
```

### Speaker Notes
> "Step 2: Run the tests. They fail. Perfect! That's TDD working correctly. The endpoint doesn't exist yet, so we get 404 errors. The tests now define exactly what our implementation needs to do. This is test-first development!"

---

## SLIDE 49: Step 3 - Implement to Pass

### Visual
- **Layout:** Comprehensive prompt example
- **Highlighting:** Context, Task, Constraints sections
- **Mode:** Agent Mode indicator

### Text on Slide
```
STEP 3: IMPLEMENT TO MAKE TESTS PASS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Using Agent Mode with full context:

┌─────────────────────────────────────────────────────────┐
│ #file:tests/api/test_todos.py #file:src/services/     │
│ todo_service.py #file:src/api/v1/todos.py              │
│                                                         │
│ [Context]                                               │
│ Working on Todo API, 3-tier architecture.               │
│ Tests in test_todos.py define DELETE requirements.      │
│                                                         │
│ [Task]                                                  │
│ Implement DELETE /api/v1/todos/{id} to pass tests.      │
│                                                         │
│ [Constraints]                                           │
│ Two layers:                                             │
│ 1. Service: delete_todo(todo_id, owner_id, db)          │
│    - Return False if not found                          │
│    - Delete and commit, return True                     │
│ 2. API: DELETE "/{todo_id}" endpoint                    │
│    - 404 if False, 204 if True                          │
│                                                         │
│ [Format]                                                │
│ Update src/services/todo_service.py and                │
│ src/api/v1/todos.py                                     │
└─────────────────────────────────────────────────────────┘
```

### Speaker Notes
> "Step 3: Implement. See my prompt structure? #file mentions give AI the tests (success criteria) plus existing code patterns. Context explains what we're doing. Task is clear. Constraints specify exact implementation, layer by layer. This is the Session 2 framework in action. AI has everything it needs!"

---

## SLIDE 50: Step 4 - Verify Tests Pass

### Visual
- **Layout:** Terminal output showing success
- **Color:** Green highlighting on PASSED
- **Celebration:** Checkmark/trophy

### Text on Slide
```
STEP 4: RUN TESTS - VERIFY SUCCESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│ $ pytest tests/api/test_todos.py -v                     │
│                                                         │
│ test_create_todo PASSED                                 │
│ test_create_todo_minimal PASSED                         │
│ test_get_todos_empty PASSED                             │
│ test_get_todos PASSED                                   │
│ test_update_todo PASSED                                 │
│ test_update_todo_partial PASSED                         │
│ test_update_todo_not_found PASSED                       │
│ test_create_todo_validation PASSED                      │
│ test_delete_todo PASSED               ← NEW!            │
│ test_delete_todo_not_found PASSED     ← NEW!            │
│                                                         │
│ ========== 10 passed in 0.58s ==========                │
└─────────────────────────────────────────────────────────┘

🎉 ALL TESTS PASS! Including old ones (regression protection)

That's TDD: Write test → Fail → Implement → Pass
```

### Speaker Notes
> "Step 4: Run tests again. All green! 10 tests pass, including the 8 old ones. That's regression protection - we didn't break existing functionality. That's TDD with AI: Write test, watch fail, implement, watch pass. You now have a tested, working DELETE endpoint with automatic verification!"

---

## SLIDE 51: Your Turn - Build Priority Feature

### Visual
- **Layout:** Exercise card with full requirements
- **Timer:** Prominent 12-minute indicator
- **Support:** "You'll have help" callout

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🎮 EXERCISE 4
            Build the Priority Feature
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TIME: 12 minutes

FEATURE: Add priority field to todos

REQUIREMENTS:
• Priority is integer: 1 (low), 2 (medium), 3 (high)
• Default priority is 2 (medium)
• Can be set when creating a todo
• Can be updated
• Returned in responses

APPROACH: Use Session 2 full context formula
ONE comprehensive prompt with all context!

I'll help if you get stuck! You've got this! 💪

🏆 Achievement: "Feature Builder"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Speaker Notes
> "Your turn! Build a priority feature. You have 12 minutes and I'll help if you get stuck. Add a priority field to todos - integer 1-3 for low/medium/high. Use the Session 2 full context formula: one comprehensive prompt with Context, Task, Constraints, and Format. You've got this!"

**[EXERCISE PLACEHOLDER: 12 minutes - Students build priority feature with support]**

---

## SLIDE 52: Verification - Did It Work?

### Visual
- **Layout:** Verification checklist
- **Terminal examples:** Test commands
- **Success criteria:** Clear checkboxes

### Text on Slide
```
VERIFICATION - DID IT WORK?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How to verify your priority feature:

┌─────────────────────────────────────────────────────────┐
│ # Run the test suite                                    │
│ pytest tests/api/test_todos.py -v                       │
│                                                         │
│ # Start the dev server                                  │
│ uvicorn src.main:app --reload                           │
│                                                         │
│ # Test via curl                                         │
│ curl -X POST http://localhost:8000/api/v1/todos \      │
│   -H "Content-Type: application/json" \                │
│   -d '{"title": "High priority", "priority": 3}'        │
└─────────────────────────────────────────────────────────┘

SUCCESS CRITERIA:
☐ Database schema updated (priority column)
☐ TodoCreate accepts priority (default 2)
☐ TodoResponse includes priority
☐ Tests pass
☐ Manual testing works
```

### Speaker Notes
> "Time's up! Let's verify. Run your tests. Start the dev server. Test manually with curl. Did your priority field work? Can you create todos with priority? Is it in responses? Tests passing?"

---

## SLIDE 53: Reflection - TDD vs Full Context

### Visual
- **Layout:** Comparison table
- **Icons:** Test tube vs Lightning bolt
- **When to use:** Decision guide

### Text on Slide
```
REFLECTION: TDD VS FULL CONTEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've experienced both approaches. When to use each?

┌───────────────────────────┬───────────────────────────┐
│   🧪 TDD APPROACH         │   ⚡ FULL CONTEXT         │
├───────────────────────────┼───────────────────────────┤
│ WHEN TO USE:              │ WHEN TO USE:              │
│ • Complex business logic  │ • Clear requirements      │
│ • Critical functionality  │ • Standard patterns       │
│ • Need verification       │ • Speed is priority       │
│ • Learning codebase       │ • Low-risk changes        │
│                           │                           │
│ BENEFITS:                 │ BENEFITS:                 │
│ • Automatic verification  │ • Faster implementation   │
│ • Regression protection   │ • Less setup overhead     │
│ • Clear success criteria  │ • Good for simple features│
│                           │                           │
│ TIME: ~10 min for feature │ TIME: ~5-7 min for feature│
└───────────────────────────┴───────────────────────────┘

Both are valid! Choose based on situation.
```

### Speaker Notes
> "Reflection time. You've experienced both TDD and full-context approaches. When should you use each? TDD for complex logic, critical functionality, when you need verification. Full context for clear requirements, standard patterns, when speed matters. Both are valid professional approaches. Choose based on the situation!"

---

## SLIDE 54: Subagents - Parallel AI Work

### Visual
- **Layout:** Diagram showing main agent + parallel subagents
- **Arrows:** Parallel execution flow
- **Icons:** Multiple robot icons working

### Text on Slide
```
🤖 SUBAGENTS - PARALLEL VERIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Copilot can spawn parallel agents for complex tasks:

        MAIN AGENT (you're working with)
                    │
           ┌───────┴───────┐
           ↓               ↓
    ┌──────────────┐ ┌──────────────┐
    │  SUBAGENT 1  │ │  SUBAGENT 2  │
    │ Code Review  │ │  Run Tests   │
    │  (parallel)  │ │  (parallel)  │
    └──────────────┘ └──────────────┘
           ↓               ↓
           └───────┬───────┘
                   ↓
         Results merged back

Request explicitly:
"Launch a subagent to review src/api/ for security
issues while I continue with the next feature."

PERFECT FOR: Code review, tests, docs, independent tasks
```

### Speaker Notes
> "Advanced feature: Subagents. Copilot can spawn parallel agents for complex tasks. One agent reviews code while another runs tests. You can request them explicitly: 'Launch a subagent to review this while I continue.' Perfect for code review, running tests, generating docs - any independent work that can happen in parallel!"

---

## SLIDE 55: Session 3 Wins

### Visual
- **Layout:** Achievement summary
- **Metrics:** Time saved, features built
- **Comparison:** Before/after

### Text on Slide
```
📊 SESSION 3 WINS - WHAT YOU BUILT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

In 30 minutes, you:

✅ STARTED WITH WORKING CODE
   Checkpoint-based development (session-3-start)

✅ LEARNED TDD WITH AI
   Watched DELETE endpoint demo (4 steps)

✅ BUILT A COMPLETE FEATURE
   Priority field (12 minutes with support)

✅ EXPERIENCED PROFESSIONAL WORKFLOWS
   Incremental development, testing, safety nets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY INSIGHTS:
• Start with working code (checkpoints)
• TDD gives verification confidence
• Full context gives speed
• Choose approach based on situation
• Keep system working at all times

This is how professionals work with AI!
```

### Speaker Notes
> "Look at what you accomplished. You started with working code from a checkpoint. You learned TDD by watching the demo. You built a complete priority feature in 12 minutes. You experienced professional workflows: incremental development, testing, safety nets. This is how professionals work with AI!"

---

## SLIDE 56: Session 3 Complete!

### Visual
- **Layout:** Achievement card
- **Trophy:** Build Master badge
- **Progress:** 3 of 4 sessions done

### Text on Slide
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           🏆 SESSION 3 COMPLETE! 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You've mastered:

✅ Checkpoint-Based Development
   Start with working code, stay working

✅ TDD with AI
   Tests first, implementation to pass

✅ Full Context Implementation
   Comprehensive prompts for speed

✅ Professional Workflows
   Incremental, tested, safe

✅ Subagents
   Parallel AI work

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Up Next: SESSION 4 - BOSS FIGHT! 🎮
Code Review, Custom Agents, Memory Bank, and
the ultimate challenge to prove mastery!

[ 3 minute break ]
```

### Speaker Notes
> "Session 3 complete! You can now work from checkpoints, use TDD with AI, build features fast with full context, and leverage subagents for parallel work. One more session - the Boss Fight where you prove everything you've learned. Three-minute break!"

---
