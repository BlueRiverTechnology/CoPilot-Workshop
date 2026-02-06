# GitHub Copilot Model Guide

**Quick Reference:** Understanding Copilot's AI capabilities

---

## How Copilot Works

GitHub Copilot uses advanced language models (including GPT-4 and Claude) optimized for code generation. Unlike tools with model selection, Copilot automatically uses the best model for each task.

---

## Copilot Modes

Instead of choosing models, you choose **modes** in Copilot:

### Ask Mode
**Purpose:** Questions, explanations, learning

| Best For | Examples |
|----------|----------|
| Understanding code | "What does this function do?" |
| Learning concepts | "Explain async/await in Python" |
| Getting advice | "What's the best way to handle auth?" |

### Edit Mode (Cmd/Ctrl+I)
**Purpose:** Inline code modifications

| Best For | Examples |
|----------|----------|
| Small refactors | "Add type hints" |
| Quick fixes | "Handle the null case" |
| Code improvements | "Make this more readable" |

### Agent Mode
**Purpose:** Multi-file autonomous work

| Best For | Examples |
|----------|----------|
| New features | "Add user authentication" |
| Complex refactoring | "Convert to async" |
| Project-wide changes | "Update all error handling" |

### Plan Mode (/plan)
**Purpose:** Preview before execution

| Best For | Examples |
|----------|----------|
| Complex implementations | "/plan add tagging system" |
| Learning | See AI's approach before running |
| Review | Approve steps before changes |

---

## Thinking Modes

Increase reasoning depth with these keywords:

| Mode | Use Case | When to Use |
|------|----------|-------------|
| `think` | Basic analysis | Simple tasks |
| `think hard` | Complex problems | Architecture, debugging |
| `think harder` | Very complex | System design, security |
| `ultrathink` | Maximum reasoning | Critical decisions |

### Example Usage

```
think hard about implementing a many-to-many 
relationship between todos and tags.

Consider:
- Database schema
- API design  
- Edge cases
```

---

## Context Optimization

Better context = better results. Use #mentions:

| Mention | Purpose | Example |
|---------|---------|---------|
| `#file:` | Specific file | `#file:src/models/todo.py` |
| `#folder:` | Entire folder | `#folder:src/models/` |
| `#problems` | Current errors | Debug with error context |

### Context Strategy

| Task | Recommended Context |
|------|---------------------|
| New endpoint | `#file:existing-endpoint.py #file:models.py` |
| Bug fix | `#file:buggy-file.py #problems` |
| New feature | `#folder:src/ #file:PRD.md` |

---

## Task Recommendations

### Simple Code Generation
- **Use:** Ask Mode or Edit Mode
- **Context:** 1-2 relevant files
- **Thinking:** None needed

### Complex Feature
- **Use:** Agent Mode or Plan Mode
- **Context:** `#folder:` for patterns
- **Thinking:** `think hard`

### Debugging
- **Use:** Ask Mode with `#problems`
- **Context:** Error file + related files
- **Thinking:** `think hard` for complex bugs

### Architecture Planning
- **Use:** Ask Mode
- **Context:** PRD + existing structure
- **Thinking:** `think harder` or `ultrathink`

### Code Review
- **Use:** Ask Mode
- **Context:** File to review
- **Thinking:** `think hard`

---

## Best Practices

### 1. Start Specific
```
# Good
"Add pagination to GET /todos endpoint with 
skip and limit parameters"

# Less Good  
"Make the API better"
```

### 2. Provide Context
```
# Good
#file:src/api/v1/todos.py #file:src/models/todo.py

Add a completed_at timestamp...

# Less Good
Add a completed_at timestamp...
```

### 3. Use Thinking Modes for Complex Tasks
```
# For architecture decisions
think hard about the best way to implement 
real-time notifications for todo updates.

# For simple tasks - no thinking mode needed
Add a docstring to this function.
```

### 4. Iterate
- Start with a basic prompt
- Refine based on results
- Add constraints if output is too broad
- Add examples if output misses the pattern

---

## Comparison with Other Tools

| Feature | Copilot | Other AI Tools |
|---------|---------|----------------|
| Model Selection | Automatic | Manual choice |
| Code Context | #mentions | Varies |
| Modes | Ask/Edit/Agent/Plan | Varies |
| Integration | VS Code native | Extensions |

---

## Quick Reference Card

```
MODES:
Ask      → Questions, learning
Edit     → Cmd/Ctrl+I, inline changes
Agent    → Multi-file, autonomous
Plan     → /plan, preview before execute

CONTEXT:
#file:path    → Include specific file
#folder:path  → Include folder
#problems     → Include current errors

THINKING:
think         → Basic (simple tasks)
think hard    → Complex (architecture)
think harder  → Very complex (security)
ultrathink    → Maximum (critical)

FORMULA:
Good Context + Right Mode + Appropriate Thinking = Great Results
```

---

**End of Model Guide** 🎓
