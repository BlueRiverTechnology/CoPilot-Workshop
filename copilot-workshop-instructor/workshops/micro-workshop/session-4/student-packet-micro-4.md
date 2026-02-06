# Student Packet: Micro Session 4
## Code Review, Custom Agents & Boss Fight 🎮🏆

**Duration:** 33 minutes  
**Achievement:** 🏆 "Copilot Champion"

---

## What You'll Master

| Technique | Why It Matters |
|-----------|----------------|
| Copilot Code Review | Catch issues before they ship |
| Custom Agents | Pre-loaded context for your project |
| The 70% Problem | Know where YOU add value |
| Boss Fight | Prove complete mastery |

---

## 🔍 Copilot Code Review

### On GitHub (Pull Requests)

```
HOW TO USE:
1. Create a Pull Request on GitHub
2. Request review from "Copilot" as a reviewer
3. Copilot analyzes your changes
4. Get inline comments and suggestions

WHAT IT CHECKS:
✅ Code quality and best practices
✅ Potential bugs and edge cases
✅ Security vulnerabilities
✅ Performance issues
✅ Consistency with codebase patterns
```

### In-Editor Review

Copy this prompt to review your own code:

```
Review my recent changes in #file:src/api/v1/todos.py.

Check for:
1. Security issues (auth, validation)
2. Error handling completeness
3. Performance concerns
4. Best practice violations

Be thorough and critical.
```

**Exercise:** Run a code review on any file you've created in this workshop.

What issues did Copilot find?
```
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Review Master"

---

## 🤖 Custom Agents

### What Are Custom Agents?

Custom Agents are pre-configured AI specialists for your project:

```
Location: .github/agents/*.agent.md

What they do:
- Define specialized AI personas
- Include project-specific knowledge
- Set constraints and patterns
- Reusable across conversations
```

### Create Your First Custom Agent

Create this file: `.github/agents/todo-api.agent.md`

```markdown
# Todo API Expert Agent

You are an expert in our Todo API codebase. You know:

## Architecture
- FastAPI with async/await
- 3-tier architecture: API → Services → Models
- SQLAlchemy with async sessions
- Pydantic for validation

## Key Patterns
- All endpoints require authentication (get_current_user)
- Service layer handles business logic
- Models use UUID primary keys
- Responses use Pydantic schemas

## File Structure
- src/api/v1/ - API endpoints
- src/services/ - Business logic
- src/models/ - SQLAlchemy models
- src/schemas/ - Pydantic schemas
- tests/api/ - API tests

## Coding Standards
- Use async/await for all database operations
- Return appropriate HTTP status codes
- Include comprehensive error handling
- Write tests for all new endpoints

When asked to implement features:
1. Follow existing patterns in the codebase
2. Create tests first (TDD approach)
3. Use the 3-tier architecture
4. Include proper validation and error handling
```

### Use Your Custom Agent

```
Using #file:.github/agents/todo-api.agent.md context:

Add a DELETE /api/v1/todos/{id} endpoint that:
- Requires authentication
- Checks ownership
- Returns 204 on success, 404/403 on errors
```

**Reflection:** How does including the agent context improve the output?
```
_______________________________________________
_______________________________________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Agent Creator"

---

## ⚠️ The 70% Problem - Critical Understanding

### The Reality Check

```
THE 70/30 SPLIT

AI Delivers Fast (70%):
┌────────────────────────────────────┐
│ ✅ Boilerplate code                │
│ ✅ Standard CRUD operations        │
│ ✅ Happy path implementation       │
│ ✅ Basic structure                 │
│ ✅ Common patterns                 │
└────────────────────────────────────┘

YOU Must Add (30%):
┌────────────────────────────────────┐
│ 🎯 Edge cases AI missed            │
│ 🎯 Ownership validation            │
│ 🎯 Security hardening              │
│ 🎯 Error message quality           │
│ 🎯 Production-ready error handling │
│ 🎯 Business logic nuances          │
└────────────────────────────────────┘
```

### Why This Matters

- Organizations that understand this: **26% productivity gains**
- Organizations that don't: **Accumulating technical debt**

**Your Professional Value:**
The 30% is why companies hire professionals. AI handles the routine. YOU handle the critical.

**Reflection:** Think of a time when "done" code wasn't production-ready:
```
What was missing? ____________________________
Who caught it? ______________________________
What could have gone wrong? __________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "70/30 Understander"

---

## 🎮 BOSS FIGHT - The Ultimate Challenge

### The Challenge

Build a **complete TODO TAGGING feature** with many-to-many relationships using ALL techniques from Sessions 1-3.

### Requirements

```
ENDPOINTS:
- POST /api/v1/todos/{id}/tags - Add tag to todo
- GET /api/v1/todos?tag=name - Filter todos by tag
- DELETE /api/v1/todos/{id}/tags/{tag_id} - Remove tag

DATABASE:
- Tag model: id, name, user_id, created_at
- todo_tags association table (many-to-many)

CONSTRAINTS:
- Ownership validation required
- Case-insensitive tags (store lowercase)
- Proper error handling (404, 403, 400)
- 3-tier architecture (models, services, API)
```

### Scoring

| Time | Level | Description |
|------|-------|-------------|
| ≤6 min | 🏆 PLATINUM | Top 1% - Elite |
| ≤8 min | 🥇 GOLD | Top 10% - Expert |
| ≤10 min | 🥈 SILVER | Top 25% - Skilled |
| Completed | ✅ CERTIFIED | Passed! |

**Bonus:** +1 level for each technique used:
- [ ] think hard for planning
- [ ] Plan Mode (/plan)
- [ ] TDD approach
- [ ] Custom Agent

---

### Your Boss Fight Tracker

**Start Time:** _____________

#### Phase 1: Planning (30 seconds)
```
I used: [ ] think hard  [ ] Plan Mode

My plan:
_______________________________________________
_______________________________________________
```

#### Phase 2: Implementation (3 minutes)
```
Files created/modified:
[ ] models/tag.py
[ ] schemas/tag.py
[ ] services/todo_service.py
[ ] api/v1/todos.py
```

#### Phase 3: The Critical 30% (1.5 minutes)
```
I verified:
[ ] Ownership validation works
[ ] Tags are case-insensitive
[ ] Error handling is complete
[ ] Edge cases covered
```

#### Phase 4: Testing (1 minute)
```
Tests I ran:
[ ] Create todo
[ ] Add tag to todo
[ ] Filter by tag
[ ] Remove tag
```

**End Time:** _____________

**Total Time:** _____________ minutes

---

### My Score

```
BASE LEVEL (by time):
[ ] ≤6 min = PLATINUM
[ ] ≤8 min = GOLD
[ ] ≤10 min = SILVER
[ ] Completed = CERTIFIED

BONUSES EARNED:
[ ] Used think hard (+1)
[ ] Used Plan Mode (+1)
[ ] Used TDD (+1)
[ ] Used Custom Agent (+1)

FINAL LEVEL: _________________
```

🏆 **ACHIEVEMENT UNLOCKED:** "Boss Fighter"

---

## 🏆 Power User Certification

Congratulations! You've completed the GitHub Copilot Power User Workshop!

### Skills Mastered

```
SESSION 1: FOUNDATION
✅ Security-first development
✅ Copilot modes (Ask, Edit, Agent, Plan)
✅ #file and #folder mentions
✅ .copilotignore configuration

SESSION 2: CONTEXT MASTERY
✅ Thinking modes (think hard)
✅ Explore → Plan → Code workflow
✅ 6-element framework
✅ PRD-driven development

SESSION 3: BUILD SPRINT
✅ Test-Driven Development
✅ Subagents for parallel work
✅ Plan Mode for visibility
✅ Three features in 30 minutes

SESSION 4: MASTERY
✅ Code Review
✅ Custom Agents
✅ The 70/30 Problem
✅ Boss Fight completion
```

### Your Certification

```
┌─────────────────────────────────────────────┐
│                                             │
│       GITHUB COPILOT POWER USER             │
│              CERTIFIED                      │
│                                             │
│   Successfully completed Power User         │
│   Workshop and demonstrated mastery of:     │
│                                             │
│   ✅ Security-first development             │
│   ✅ All Copilot modes                      │
│   ✅ Context mastery & prompting            │
│   ✅ Professional workflows                 │
│   ✅ Test-Driven Development                │
│   ✅ Subagents & Plan Mode                  │
│   ✅ Code Review & Custom Agents            │
│   ✅ Boss Fight completion                  │
│                                             │
│   Name: _____________________               │
│   Level: ____________________               │
│   Date: _____________________               │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Final Reflection

### What I Learned

**Most valuable technique:**
```
_______________________________________________
```

**Biggest mindset shift:**
```
_______________________________________________
```

**What I'll use Monday morning:**
```
_______________________________________________
```

### My Action Plan

**This week, I will:**
```
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
```

**In 30 days, I want to:**
```
_______________________________________________
_______________________________________________
```

---

## Key Takeaways

1. **Security First** - Never expose secrets to AI
2. **Context is King** - Better context = better results
3. **Plan Before Code** - Explore → Plan → Code
4. **Trust but Verify** - Review ALL AI output
5. **Know Your 30%** - YOU add the critical value

---

## Session 4 Achievement Summary

| Achievement | Earned |
|-------------|--------|
| 🔍 Review Master | [ ] |
| 🤖 Agent Creator | [ ] |
| ⚠️ 70/30 Understander | [ ] |
| 🎮 Boss Fighter | [ ] |
| 🏆 COPILOT CHAMPION | [ ] |

---

## Resources for Continued Learning

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot Chat Documentation](https://docs.github.com/en/copilot/github-copilot-chat)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

**End of Student Packet: Session 4** 🎓

**🎉 CONGRATULATIONS - You're a Copilot Power User! 🎉**
