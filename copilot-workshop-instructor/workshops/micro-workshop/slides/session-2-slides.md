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

