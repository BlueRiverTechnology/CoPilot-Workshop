# Prompt: Restructure My GitHub Copilot Workshop

## Who You Are Helping

I'm an instructor who runs this GitHub Copilot Power User Workshop. I need your help restructuring and improving it based on a detailed review of the current materials and feedback from a previous delivery.

---
Process: 1) Read existing files, 2) Identify what needs to change per your restructuring plan, 3) Update each file with only the necessary changes."

---

## Workshop Format

- **3 one-hour segments** covering **4 sessions** (Session 1 gets a full hour; Sessions 2, 3, and 4 share the remaining two hours)
- In-person or virtual, instructor-led
- Class size: 10-30 developers
- Students use VS Code with GitHub Copilot installed

---

## What Currently Exists

I have a complete workshop with:

### Instructor Materials (per session)
- Instructor guides with minute-by-minute scripts, energy cues, exact wording
- Prompt sheets with copy-paste prompts for demos
- PowerPoint slides (described in markdown slide deck guides with verbatim text, visual descriptions, and speaker notes per slide)

### Student Materials (per session)
- Student packets (workbooks with exercises, tracking sheets, reflection prompts)
- Student reference guides (deep-dive technical references)
- Prompt sheets (copy-paste prompts for hands-on exercises)

### Student Repo (`copilot-workshop-student`)
A partially scaffolded FastAPI Todo API with:
- `src/main.py` — basic FastAPI app with health check
- `src/models/` — complete User and Todo SQLAlchemy models (UUID PKs, relationships)
- `src/schemas/` — empty (students fill in)
- `src/services/` — empty (students fill in)
- `src/api/v1/` — empty (students fill in)
- `tests/` — empty
- `PRD.md` — Product Requirements Document for the Todo API
- `.github/copilot-instructions.md` — coding standards, architecture patterns, simplified auth (fixed "default-user" instead of JWT)
- `.copilotignore-example`
- `requirements.txt` with FastAPI, SQLAlchemy, aiosqlite, pytest, httpx, etc.
- `model-selection-guide.md`
- Session folders with student packets, references, and prompt sheets

### Existing Slide Deck
There is already a comprehensive slide deck guide (72 slides across 4 sessions) written in markdown. Each slide entry includes:
- Verbatim text content (in code blocks)
- Visual/layout descriptions
- Speaker notes (in blockquotes)
- Exercise placeholders with durations

The slides follow this structure:
- Pre-Session: Title & Intro (Slides 1-5)
- Session 1: Security & Superpowers (Slides 6-25)
- Session 2: Context Mastery (Slides 26-40)
- Session 3: Build Sprint (Slides 41-56)
- Session 4: Mastery & Boss Fight (Slides 57-72)

The slide deck also includes: color palette (#0066FF primary blue, #8B5CF6 purple, #10B981 green, #F59E0B gold, #0D1117 dark background), icon suggestions, typography guidance, and animation suggestions.

---

## Current Session Structure

### Session 1: Security & Superpowers (60 min)
- `.copilotignore` configuration
- Terminal command approval model
- VS Code Copilot capability settings (autoApprove, Configure Tools)
- All AI modes overview (Ask, Edit, Agent, Plan)
- Agent Mode demo — generate a throwaway practice project
- Safety features (undo, git integration, review before accepting)
- Inline AI tools (Inline Chat Cmd+I, Ghost Text/Tab completion)
- `@workspace` search
- Mode switching practice
- `#mentions` — #file, #folder, #terminalSelection, #problems, #codebase, #fetch
- Custom Instructions (`.github/copilot-instructions.md`) — currently a brief overview
- Path-specific instructions mention

### Session 2: Context Mastery & Project Planning (30 min)
- Transition to the real workshop project (copilot-workshop-student)
- Thinking modes (think, think hard, think harder, ultrathink)
- Professional workflow: Explore → Plan → Code
- Phase 1: EXPLORE demo (Ask Mode — think through tagging feature)
- Phase 2: PLAN demo (Agent Mode — generate PRD-Tags.md)
- Using PRDs as context during development
- 6-Element Prompt Framework (Persona, Context, Task, Constraints, Format, Examples) — scaled by complexity
- Advanced #mention patterns (glob/folder, combining mentions, #problems)
- Framework practice — transform weak prompts into strong ones
- Toolkit summary

### Session 3: Build Sprint (30 min)
- Feature 1: POST /todos using TDD (write tests → fail → implement → pass) — 10 min
- Feature 2: GET /todos using full context formula (one comprehensive prompt) — 7 min
- Feature 3: PUT /todos as a 3-minute speed challenge — 3 min
- Subagents concept and demo — 3 min
- Plan Mode demo — 3 min
- Victory lap and results analysis — 2 min

### Session 4: Code Review, Custom Agents & Boss Fight (33 min)
- Copilot Code Review (GitHub PR review + in-editor review) — 6 min
- Custom Agents (.agent.md files) — 6 min
- Memory Bank (persistent project context via markdown files) — 6 min
- The 70% Problem (AI gets you 70%, you add the critical 30%) — 4 min
- Boss Fight: Build complete many-to-many tagging feature (Tag model, association table, 3 endpoints) — 10 min
- Victory lap and certification — 5 min

---

## What Went Wrong / Current Problems

### Session 3 is the fragile core

1. **Zero time buffer.** 28 minutes of content in 30 minutes. When Copilot generates code that doesn't compile, database setup fails, imports are wrong, or tests fail for unexpected reasons — each issue eats 3-5 minutes per stuck student. There's no recovery time.

2. **Too many things need to work simultaneously.** The repo starts with empty services/schemas/api directories. Session 3 prompts assume conftest.py with an async test client, create_db.py, a get_db dependency, proper database URL configuration, etc. All of this generated glue code needs to be correct AND work together. With async SQLAlchemy + FastAPI + test fixtures, first-try success is uncommon.

3. **The TDD cycle is realistically 15-20 minutes**, not 10. Write tests → run them → see failure → implement → run again → debug failures. Each iteration with Copilot potentially generates slightly different code that needs debugging.

4. **Students who fall behind in Session 3 can't do Session 4.** The Boss Fight builds on top of the CRUD endpoints from Session 3. If someone's API isn't working, they can't add tagging.

### The Boss Fight compounds the risk

Many-to-many tagging (new model, association table, schemas, service methods, 3 endpoints, case-insensitive lookup) in 6-10 minutes is ambitious even for experienced developers with Copilot. If Session 3 didn't go smoothly, this falls apart.

### Missing: How to write good rules/instructions

The current workshop shows students WHAT a `.github/copilot-instructions.md` file looks like and gives them one to copy, but it doesn't show them HOW to write effective rules for their own projects. This is one of the most transferable skills — every project benefits from well-written Copilot instructions. Students should learn the principles of writing rules that actually shape AI behavior: what to include, what level of specificity works, how to structure them, common anti-patterns, and how to iterate on them.

### Previous delivery feedback

The API building portion was the shakiest part. Students struggled, it went too fast, and too many things could go wrong due to happenstance/circumstance.

---

## The Restructuring Plan

### Core approach: "Pre-built checkpoint" safety net + simplified hands-on + rules-writing depth

### Session 1: Security & Superpowers (60 min) — KEEP MOSTLY AS-IS, ADD RULES WRITING

This session works well. The throwaway practice project generation demo is a good Agent Mode showcase. Keep all existing content.

**NEW ADDITION: Expand the Custom Instructions section into a proper "Writing Effective Rules" segment.** Currently it's ~3 minutes of "here's a file, copy it." Expand to ~8-10 minutes covering:

1. **The rules ecosystem** — There are now multiple layers of instruction files, and students should understand the hierarchy:
   - `.github/copilot-instructions.md` — repository-wide, always active, applies to Chat, Agent Mode, and Code Review
   - `.github/instructions/*.instructions.md` — path-specific rules with `applyTo` glob frontmatter (e.g., `applyTo: "**/*.py"` or `applyTo: "**/tests/*.py"`)
   - `.github/agents/*.agent.md` — custom agent definitions (covered more in Session 4)
   - `AGENTS.md` — cross-tool instructions file (works with Copilot, Claude Code, Cursor, etc. — emerging open standard from Linux Foundation)
   - VS Code settings for code generation, test generation, review, and commit message instructions (each can point to different rule files)

2. **What makes rules effective — research-backed principles:**
   - **Short, imperative, self-contained statements** — GitHub's own docs say instructions should be "short, self-contained statements that add context." Not paragraphs. Not essays.
   - **Tell the AI what TO DO, not what to avoid** — LLMs are poor at negations. "Use NSubstitute for mocking" works. "Don't use fake repositories" doesn't work reliably. Positive directives > negative prohibitions.
   - **Be specific and actionable** — "Use camelCase for variables" beats "follow good naming conventions." Show the exact pattern you want.
   - **Use structured Markdown** — Distinct headings that separate topics, bullet points for scanning, imperative directives rather than narrative paragraphs. Copilot parses structured content better than prose.
   - **Include code examples where they clarify intent** — A before/after code snippet in your rules file removes ambiguity. Show the pattern, don't just describe it.
   - **Keep files under ~1,000 lines** — GitHub's docs explicitly warn that beyond this, quality deteriorates. Start minimal, add iteratively.
   - **Iterate based on what works** — Rules writing is empirical. Start with 5-10 rules, test them, see if Copilot follows them, refine. This is the most important principle.

3. **XML tags for structured rules (Anthropic best practice)** — When writing rules for Claude-based tools (Claude Code, Claude in IDE), Anthropic specifically recommends using XML tags to structure instructions. XML tags create clear boundaries that prevent the AI from mixing up context, instructions, and examples. This is a transferable skill that works across AI tools:
   ```
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
   Key principle: XML tags work because they give the AI unambiguous section boundaries. Whether you use XML tags or Markdown headings depends on the tool — Copilot prefers Markdown structure, Claude prefers XML — but the principle is the same: **create clear, labeled compartments for different types of information.**

5. **Live exercise: Write your own rules** — Students write 3-5 custom rules for the Todo API project (not just copy the pre-made file). They should write rules that answer: "What would a new developer on my team need to know to write code that fits this project?" Then they test one rule by giving Copilot a prompt and checking if the output follows their rule. Show them how to verify rules are being used by checking the References section in Copilot Chat responses.

6. **Path-specific instructions** — Brief demo of creating a `.github/instructions/testing.instructions.md` with frontmatter:
   ```yaml
   ---
   applyTo: "**/tests/**"
   ---
   ```
   This applies test-specific rules only when working on test files. Mention that path-specific instructions + repo-wide instructions stack together.

7. **How rules connect to everything else** — Rules + PRD + Memory Bank = Copilot that truly knows your project. Custom instructions are "always-on context" that saves you from repeating yourself. This sets up Sessions 2 and 4.

To make room: compress the mode switching practice slightly (it currently has 2 separate 1-minute timed exercises — combine into one). The Mention Bingo section can be slightly tightened too since students will use mentions heavily in later sessions.

### Session 2: Context Mastery & Project Planning (30 min) — KEEP MOSTLY AS-IS

Thinking modes, Explore → Plan → Code workflow, 6-element framework, PRD — all good. Keep all of it.

### Session 3: Build Sprint (30 min) — MAJOR RESTRUCTURE

**New approach:**

1. **Provide a "session-3-start" checkpoint** in the student repo — a branch or folder with a fully working API that has POST, GET, and PUT /todos already implemented with schemas, services, routes, database setup, conftest.py, and passing tests. Students can verify it works (`pytest -v` → all green) before they touch anything.

2. **Feature 1 (TDD): Instructor-led live coding demo** (~10 min). The instructor walks through adding DELETE /todos using TDD while students WATCH. This demonstrates the TDD workflow without 20 students simultaneously debugging different async SQLAlchemy issues. Students see: write test → fail → implement → pass.

3. **Feature 2: Students build ONE feature themselves** (~12 min). Using the full context formula from Session 2, students add a single feature to the already-working API. This could be something like adding a "priority" field to todos or a "mark as favorite" toggle — something simpler than the current 3-feature sprint. The working infrastructure is already proven from the checkpoint. If it breaks, they can reset.

4. **Reflection and comparison** (~5 min). Compare the instructor's TDD approach vs their own approach. What worked, what didn't. Brief Subagent and Plan Mode mention (conceptual, not hands-on).

5. **~3 min buffer** for things going wrong.

### Session 4: Advanced Tools & Boss Fight (30 min) — RESTRUCTURE

**New approach:**

1. **Code Review + Custom Agents + Memory Bank** (~10 min) — keep but tighten.
2. **70% Problem** (~3 min) — keep as-is.
3. **Boss Fight** (~12 min) — SIMPLIFY. Instead of full many-to-many tagging (3 endpoints), have students add just ONE tag-related endpoint (e.g., POST /todos/{id}/tags to add a tag). Provide the Tag model and association table as part of a "session-4-start" checkpoint so students aren't also debugging schema creation. The challenge is building the service + route + schema layer for one operation.
4. **Victory lap and certification** (~5 min).

### Critical safety net: Checkpoint branches

Create branches in the student repo:
- `main` — the starting scaffolding (current state)
- `session-3-start` — fully working API with POST, GET, PUT /todos, all infrastructure (database.py, conftest.py, get_db, etc.)
- `session-4-start` — everything from session-3-start PLUS DELETE /todos endpoint, plus the Tag model and association table already created

If a student falls behind, they run `git checkout session-3-start` or `git checkout session-4-start` and they're back on track. This is the single most important structural change.

---

## What I Need You To Produce

Please produce the following **complete, ready-to-use** files for the restructured workshop: Please only update the existing files and only create new files if necessary

### 1. Updated Instructor Guides (4 files)
- `instructor-guide-micro-1.md` — Session 1 (UPDATED: expanded rules-writing section)
- `instructor-guide-micro-2.md` — Session 2 (minor updates if needed)
- `instructor-guide-micro-3.md` — Session 3 (MAJOR REWRITE per the plan above)
- `instructor-guide-micro-4.md` — Session 4 (MAJOR REWRITE per the plan above)

Each instructor guide should include:
- Minute-by-minute timing with time stamps
- Exact wording for key teaching moments (SAY blocks)
- Demo instructions (DO blocks)
- Energy cues
- Checkpoints
- Common issues and solutions
- Time flexibility notes (what to cut if behind, what to add if ahead)
- Achievements/gamification elements

### 2. Updated Student Packets (4 files)
- `student-packet-micro-1.md` — UPDATED for rules-writing exercise
- `student-packet-micro-2.md`
- `student-packet-micro-3.md` — MAJOR REWRITE
- `student-packet-micro-4.md` — MAJOR REWRITE

Each student packet should include:
- Learning objectives with checkboxes
- Exercise instructions
- Blank spaces for student responses and tracking
- Prompt templates for copy-paste
- Achievement checklists
- Self-assessment sections
- Reflection questions

### 3. Updated Prompt Sheets (4 files)
- `PROMPT-SHEET-SESSION-1.md` — UPDATED for rules-writing exercise
- `PROMPT-SHEET-SESSION-2.md`
- `PROMPT-SHEET-SESSION-3.md` — MAJOR REWRITE
- `PROMPT-SHEET-SESSION-4.md` — MAJOR REWRITE

Copy-paste ready prompts for every exercise in the session.

### 4. Updated Student Reference Guides (4 files)
- `student-reference-micro-1.md` — UPDATED: add comprehensive "Writing Effective Copilot Rules" reference section
- `student-reference-micro-2.md`
- `student-reference-micro-3.md` — UPDATE
- `student-reference-micro-4.md` — UPDATE

Deep-dive technical references students can refer back to after the workshop.

### 5. Updated Slide Deck Guides (4 files)
- `session-1-slides.md` — UPDATED: add slides for expanded rules-writing section
- `session-2-slides.md` — minor updates if needed
- `session-3-slides.md` — MAJOR REWRITE to match new Session 3 flow
- `session-4-slides.md` — MAJOR REWRITE to match new Session 4 flow

Each slide entry should follow the existing format:
- Slide number and title
- **Visual** section describing layout, icons, colors, animation suggestions
- **Text on Slide** section with exact verbatim text in code blocks
- **Speaker Notes** section with exact wording in blockquotes
- **[EXERCISE PLACEHOLDER]** markers for hands-on segments with durations

Follow the existing color palette: Primary Blue #0066FF, Purple #8B5CF6, Green #10B981, Gold #F59E0B, Dark Background #0D1117, Light Text #E6EDF3.

Also include an updated `SLIDE-DECK-GUIDE.md` that combines all sessions with the complete slide index, exercise summary table, and visual design notes.

### 6. Pre-built Checkpoint Code

Provide the complete code files needed for the `session-3-start` and `session-4-start` checkpoints:

**session-3-start checkpoint should include:**
- `src/main.py` — updated with router registration
- `src/database.py` — async engine, session factory, get_db dependency
- `src/schemas/todo.py` — TodoCreate, TodoResponse, TodoUpdate schemas
- `src/services/todo_service.py` — TodoService with create, get_all, update methods
- `src/api/v1/todos.py` — POST, GET, PUT endpoints
- `create_db.py` — database creation script
- `tests/conftest.py` — async test client fixture
- `tests/api/test_todos.py` — passing tests for POST, GET, PUT
- Any other files needed for the API to work

**session-4-start checkpoint should include:**
- Everything from session-3-start PLUS:
- DELETE /todos/{id} endpoint with tests
- `src/models/tag.py` — Tag model and todo_tags association table
- Updated `src/models/todo.py` — with tags relationship added
- Updated `src/models/__init__.py` — registering Tag model

All code should:
- Use async SQLAlchemy with aiosqlite
- Use UUID string primary keys
- Use fixed `owner_id = "default-user"` (no JWT auth)
- Follow the 3-tier architecture (api → services → models)
- Have Pydantic v2 schemas
- Work with `pytest -v` out of the box
- Work with `uvicorn src.main:app --reload` out of the box

### 7. Updated Curriculum Summary
- `copilot-curriculum.md` — updated executive summary reflecting the restructured workshop

### 8. Updated README for Student Repo
- `README.md` — updated to reflect the new checkpoint branch structure and session flow

---

## Style and Tone Guidelines

- **Instructor guides:** High energy, scripted but natural. Include exact SAY blocks with quotes. Include DO blocks with specific steps. Include ENERGY cues. Gamification elements (achievements, challenges) throughout. Time stamps at every section.
- **Student packets:** Interactive workbook style. Checkboxes, fill-in-the-blank, tracking tables. Encouraging but not patronizing. Clear instructions that work even if the student falls behind.
- **Prompt sheets:** Pure copy-paste. Minimal explanation. Just the prompts, organized by exercise.
- **Reference guides:** Technical deep-dives. Comprehensive but scannable. Students refer to these after the workshop.
- **Slide deck guides:** Follow the exact format from the existing slides — Visual description, Text on Slide in code blocks, Speaker Notes in blockquotes. Include exercise placeholder markers. Be specific about layouts (grids, split screens, code blocks, etc.).
- **Code:** Clean, well-commented, production-quality patterns. Working out of the box. No placeholder or TODO comments in the checkpoint code.

---

## Important Context

- The workshop teaches **GitHub Copilot in VS Code**, not other IDEs
- Students range from junior to senior developers
- The core thesis is: **Context mastery is what separates AI amateurs from AI professionals**
- The key transferable framework is: **Context + Task + Constraints + Format** (scaled by complexity)
- The professional workflow is: **Explore → Plan → Code → Commit**
- Workshop uses Python/FastAPI but principles apply to any language
- Authentication is simplified to `owner_id = "default-user"` throughout — no JWT implementation
- The gamification (achievements, speed challenges, Boss Fight, certification levels) is important for engagement — keep it
- The **rules-writing** addition should feel like a first-class teaching moment, not a bolt-on. It connects directly to the thesis (context mastery) and pays off in every later session when students see how their rules shape Copilot's behavior. The teaching should be grounded in real best practices: GitHub's official docs recommend short imperative statements, structured Markdown, iterative refinement, and keeping files under ~1,000 lines. Anthropic recommends XML tags for structured prompts with Claude-based tools. The community consensus is: tell the AI what TO DO (positive directives), not what to avoid (negations). Include code examples in rules to remove ambiguity. Show the full hierarchy of instruction files (repo-wide → path-specific → agent-specific). The rules-writing exercise should have students write their OWN rules and verify Copilot follows them — not just copy a pre-made file.

---

## Please produce all files listed above. Start with the instructor guides and checkpoint code (the most critical pieces), then slide deck guides, then student packets, then prompt sheets, then reference guides, then curriculum summary and README.
