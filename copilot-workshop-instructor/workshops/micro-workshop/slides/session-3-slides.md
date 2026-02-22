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

