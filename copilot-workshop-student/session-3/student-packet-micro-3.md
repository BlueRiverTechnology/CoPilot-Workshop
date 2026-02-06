# Student Packet: Micro Session 3
## Build Sprint - Context Edition 🚀⚡

**Name:** _________________________  
**Date:** _________________________  
**Achievement Goal:** 🏆 "Build Master"

---

## Learning Objectives

- [ ] Build features using Test-Driven Development
- [ ] Experience how context quality affects speed
- [ ] Apply Context+Task+Constraints+Format formula
- [ ] Use Subagents for parallel work
- [ ] Use Plan Mode for complex features
- [ ] Track and analyze your results

---

## The Build Challenge

**The Experiment:**
Next 30 minutes, build 3 complete CRUD features.

**Compare approaches:**
- Feature 1: TDD (tests first)
- Feature 2: Full context formula
- Feature 3: Speed challenge (3 min!)

**YOU track everything. YOU decide what works!**

**Let's PROVE context mastery works! 🚀**

---

## 🚀 Setup Before Starting

**1. Install dependencies (if not already done):**
```bash
pip install -r requirements.txt
```

**2. Start your development server:**
```bash
# In a separate terminal window
uvicorn src.main:app --reload
```

Server should be running at: **http://localhost:8000**

✅ Dependencies installed!  
✅ Server is running and ready!

---

## 📊 MY CONTEXT EXPERIMENT

### Feature 1: POST /todos (TDD Approach)

**Phase 1: Write Tests First**

My prompt for test creation:
```
[Context]


[Task]


[Constraints]


[Format]

```

- Time: _____ minutes
- Tests created: [ ] Success [ ] Auth failure [ ] Validation errors

**Phase 2: Implement to Pass Tests**

My implementation prompt:
```
[Context] #file:tests/api/test_todos.py #file:src/models/todo.py


[Task]


[Constraints]


[Format]

```

- Time: _____ minutes
- Iterations needed: _____
- Tests passing: [ ] All [ ] Some [ ] None

**Feature 1 Total:**
- Time: _____ minutes
- First-attempt success: [ ] Yes [ ] No
- Approach: TDD (tests first, then implement)

**What I learned:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "TDD Practitioner"

---

### Feature 2: GET /todos (Full Context Formula)

**My comprehensive prompt:**
```
[Context]
#folder:src/api/ #file:src/services/todo_service.py #file:src/schemas/todo.py






[Task]



[Constraints]






[Format]




```

**Results:**
- Time: _____ minutes
- Iterations needed: _____
- First-attempt success: [ ] Yes [ ] No

**Compared to Feature 1:**
```
Feature 1 (TDD):         _____ min, _____ iterations
Feature 2 (Full Context): _____ min, _____ iterations

What was different? _____
```

**Start Server (if not running):**
```bash
uvicorn src.main:app --reload
```
Server should be running at: http://localhost:8000

**Testing:**
- [ ] GET /api/v1/todos
- [ ] GET /api/v1/todos?completed=false
- [ ] GET /api/v1/todos?skip=0&limit=10

🏆 **Achievement:** [ ] "Context Master"

---

### Feature 3: PUT /todos/{id} (SPEED CHALLENGE! 🎯)

**Goal:** Complete in 3 minutes!

**Timer:** Start: ___:___ End: ___:___

**My approach:**
- [ ] TDD (tests first)
- [ ] Full context prompt
- [ ] Hybrid approach

**My optimized prompt:**
```






```

**Pair partner:** _________________________

**Results:**
- Time: _____ minutes
- Made 3-minute goal: [ ] Yes [ ] No
- Iterations needed: _____

**My performance pattern:**
```
Feature 1: _____ min
Feature 2: _____ min  
Feature 3: _____ min

Pattern I notice: _____
```

**Testing (server should be running at http://localhost:8000):**
- [ ] Can update title
- [ ] Can update description
- [ ] Can toggle completed status
- [ ] Returns 404 if not found
- [ ] Returns 403 if not owned by user

🏆 **Achievement:** [ ] "Speed Demon"

---

## 🤖 Subagents - Parallel Work

### What I Learned About Subagents

**Subagent concept:**
- Isolated agents that run in parallel
- Main agent continues working
- Subagent reports back when done

**Example subagent prompt I tried:**
```



```

**What it did:**
_____________________________________________________________________

**When I'd use subagents:**
- [ ] Code review while building
- [ ] Running tests in parallel
- [ ] Documentation generation
- [ ] Multiple independent tasks

🏆 **Achievement:** [ ] "Parallel Worker"

---

## 📋 Plan Mode

### Using /plan for Complex Features

**I used /plan for:**
```



```

**What the plan showed:**
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________

**Why Plan Mode is useful:**
_____________________________________________________________________

🏆 **Achievement:** [ ] "Strategic Planner"

---

## Results Analysis

### My Build Sprint Statistics

| Feature | Approach | Time | Iterations | Success? |
|---------|----------|------|------------|----------|
| Feature 1 | TDD | _____ | _____ | _____ |
| Feature 2 | Full Context | _____ | _____ | _____ |
| Feature 3 | Speed Challenge | _____ | _____ | _____ |
| **TOTAL** | | _____ | | |

### What Made the Biggest Difference?

**Rank these (1 = most impact, 5 = least):**
- _____ Better #mentions
- _____ Clear constraints in prompts
- _____ More context upfront
- _____ Structured requests (Context+Task+Constraints+Format)
- _____ TDD approach
- _____ Subagents
- _____ Plan Mode

### My Pattern Discovery

**Best results with:**
- [ ] TDD (tests first gives clear target)
- [ ] Full context (one comprehensive prompt)
- [ ] Speed challenge (forcing optimization)

**Why it worked:**
_____________________________________________________________________

**What I'd improve next time:**
_____________________________________________________________________

---

## What I Built Today

### Features Completed:
- [ ] POST /api/v1/todos - Create todo
- [ ] GET /api/v1/todos - List with pagination & filtering
- [ ] PUT /api/v1/todos/{id} - Update todo
- [ ] Used Subagents for parallel verification
- [ ] Used Plan Mode for complex planning

**Total endpoints:** _____  
**Total files created/modified:** _____  
**Approaches tested:** 3 different strategies

---

## My Insights

**Context quality impact:**
```
Weak context → _____ iterations
Strong context → _____ iterations

Difference: _____
```

**TDD benefits I experienced:**
_____________________________________________________________________

**Full context formula benefits:**
_____________________________________________________________________

**Subagents benefits:**
_____________________________________________________________________

**Plan Mode benefits:**
_____________________________________________________________________

**Would I use these techniques on real projects?**
_____________________________________________________________________

**Which approach fits which situation:**
- TDD when: ___________________________________________________________
- Full context when: __________________________________________________
- Subagents when: _____________________________________________________
- Plan Mode when: _____________________________________________________

---

## Session 3 Achievement Summary

### Achievements Unlocked Today:

- [ ] 🧪 **TDD Practitioner** - Used Test-Driven Development
- [ ] 🎯 **Context Master** - Applied full context formula
- [ ] 🏃 **Speed Demon** - Completed 3-minute challenge
- [ ] 📊 **Results Tracker** - Tracked and analyzed performance
- [ ] 🤖 **Parallel Worker** - Used Subagents
- [ ] 📋 **Strategic Planner** - Used Plan Mode
- [ ] 🏆 **Build Master** - Complete session

**Total Achievements:** ______ / 7

---

## Self-Assessment

Rate your confidence (1-5):

| Skill | Before | After | Growth |
|-------|--------|-------|--------|
| Test-Driven Development with AI | ___ | ___ | ___ |
| Writing comprehensive prompts | ___ | ___ | ___ |
| Using Subagents | ___ | ___ | ___ |
| Using Plan Mode | ___ | ___ | ___ |
| Context optimization | ___ | ___ | ___ |

**Biggest win:**
_____________________________________________________________________

**Most surprising discovery:**
_____________________________________________________________________

**What I'll do differently from now on:**
_____________________________________________________________________

---

## Preview: Session 4

**Next up: Advanced Tools & Boss Fight! 🎮**

You'll learn:
- Advanced prompting (thinking modes, specificity)
- Code Review with Copilot
- Custom Agents (.agent.md files)
- Professional patterns from industry
- **BOSS FIGHT:** Complex feature using ALL techniques!

**The finale where you become a certified Power User! 🚀**

---

## Notes & Questions

_____________________________________________________________________

_____________________________________________________________________

_____________________________________________________________________

---

**End of Student Packet: Micro Session 3** 🎓
