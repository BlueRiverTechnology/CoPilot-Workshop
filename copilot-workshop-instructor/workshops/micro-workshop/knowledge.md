# GitHub Copilot Knowledge Base
## Comprehensive Reference for Micro-Workshop

**Version:** 1.0  
**Last Updated:** Workshop Materials

---

## Table of Contents

1. [Copilot Overview](#copilot-overview)
2. [Copilot Modes](#copilot-modes)
3. [Context References (#mentions)](#context-references)
4. [Configuration Files](#configuration-files)
5. [Thinking Modes](#thinking-modes)
6. [Prompt Engineering](#prompt-engineering)
7. [Professional Workflows](#professional-workflows)
8. [Advanced Features](#advanced-features)
9. [Security Best Practices](#security-best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Copilot Overview

### What is GitHub Copilot?

GitHub Copilot is an AI-powered coding assistant that helps you write code faster and with less effort. It uses large language models to suggest code and entire functions based on:

- Your current code context
- File contents you reference
- Your natural language descriptions
- Project patterns and conventions

### Key Capabilities

| Capability | Description |
|------------|-------------|
| Code Completion | Real-time suggestions as you type |
| Copilot Chat | Conversational AI for questions and tasks |
| Code Generation | Create new code from descriptions |
| Code Explanation | Understand existing code |
| Code Review | Analyze and improve code quality |
| Bug Fixing | Identify and fix issues |
| Test Generation | Create tests for existing code |
| Documentation | Generate comments and docs |

### Copilot Products

- **Copilot Individual** - Personal subscription
- **Copilot Business** - Team features, management
- **Copilot Enterprise** - Full organization features, custom models

---

## Copilot Modes

### Ask Mode

**Purpose:** Questions, explanations, learning

**When to Use:**
- Understanding existing code
- Learning new concepts
- Asking about best practices
- Getting explanations

**Example:**
```
Explain how async/await works in Python.
What does this error message mean?
What's the best way to handle authentication in FastAPI?
```

### Edit Mode (Cmd/Ctrl+I)

**Purpose:** Inline code modifications

**When to Use:**
- Small, focused edits
- Refactoring specific sections
- Adding features to existing code
- Quick fixes

**How to Use:**
1. Select code (or place cursor)
2. Press Cmd+I (Mac) or Ctrl+I (Windows)
3. Describe the change
4. Accept or reject

**Example:**
```
Add error handling for database connection failures
Refactor to use list comprehension
Add type hints to all parameters
```

### Agent Mode

**Purpose:** Multi-file autonomous work

**When to Use:**
- Creating new features across files
- Complex refactoring
- Project-wide changes
- Multi-step implementations

**How to Use:**
1. Open Copilot Chat
2. Select Agent Mode (or let Copilot determine)
3. Describe your goal
4. Review and accept changes

**Example:**
```
Create a new User model with authentication endpoints,
service layer, and tests following the existing patterns
in this project.
```

### Plan Mode (/plan)

**Purpose:** Preview before execution

**When to Use:**
- Complex multi-file changes
- When you want visibility into AI's approach
- Before major implementations
- For teaching/learning

**How to Use:**
```
/plan Add a tagging feature to todos with:
- Tag model and association table
- CRUD endpoints
- Service layer methods
```

---

## Context References

### Available #mentions

| Mention | Description | Example |
|---------|-------------|---------|
| `#file:` | Reference specific file | `#file:src/main.py` |
| `#folder:` | Reference folder contents | `#folder:src/models/` |
| `#problems` | Current errors/warnings | `#problems` |
| `#terminalSelection` | Selected terminal output | `#terminalSelection` |
| `#terminalLastCommand` | Last command output | `#terminalLastCommand` |
| `#selection` | Currently selected code | `#selection` |

### Best Practices for Context

```
DO:
✅ Reference relevant files at start of prompt
✅ Include related files for patterns
✅ Use #folder: for broader context
✅ Include #problems when debugging

DON'T:
❌ Reference too many files (overwhelms context)
❌ Include irrelevant files
❌ Forget to include key dependencies
```

### Context Strategy by Task

| Task | Recommended Context |
|------|---------------------|
| New endpoint | `#file:existing-endpoint.py #file:models.py` |
| Bug fix | `#file:buggy-file.py #problems` |
| New model | `#folder:src/models/` |
| Refactoring | `#file:target.py #file:related-files.py` |
| Testing | `#file:source.py #folder:tests/` |

---

## Configuration Files

### .copilotignore

**Purpose:** Prevent files from being read by Copilot

**Location:** Repository root

**Format:** Same as .gitignore

```gitignore
# Environment and secrets
.env
.env.*
*.pem
**/secrets/

# Sensitive configuration
config/production.yaml
infrastructure/credentials/

# Large generated files
*.lock
node_modules/
dist/
build/

# Database files
*.db
*.sqlite
```

### .github/copilot-instructions.md

**Purpose:** Project-level instructions for Copilot

**Location:** `.github/copilot-instructions.md`

```markdown
# Copilot Instructions for [Project Name]

## Architecture
- FastAPI with async/await
- 3-tier architecture: API → Services → Models
- SQLAlchemy with async sessions

## Coding Standards
- Use type hints on all functions
- Write docstrings for public methods
- Follow PEP 8 style guide
- Use descriptive variable names

## Patterns
- All endpoints require authentication
- Service layer handles business logic
- Pydantic for request/response validation

## Testing
- Write pytest tests for all new code
- Use fixtures for database setup
- Mock external services

## Security
- Never hardcode secrets
- Always validate input
- Use parameterized queries
```

### Custom Agents (.agent.md)

**Purpose:** Specialized AI personas with pre-loaded context

**Location:** `.github/agents/*.agent.md`

```markdown
# .github/agents/api-expert.agent.md

# API Expert Agent

You are an expert in our API development. You know:

## Key Patterns
[List patterns here]

## Coding Standards
[List standards here]

## When implementing:
1. Follow existing patterns
2. Add comprehensive error handling
3. Write tests for new endpoints
```

---

## Thinking Modes

### Overview

Thinking modes increase the depth of reasoning before generating responses:

| Mode | Use Case | Token Cost |
|------|----------|------------|
| `think` | Basic analysis | Low |
| `think hard` | Complex problems | Medium |
| `think harder` | Very complex problems | High |
| `ultrathink` | Maximum reasoning | Very High |

### When to Use Each

```
THINK:
- Simple code generation
- Basic explanations
- Straightforward tasks

THINK HARD:
- Architecture decisions
- Complex debugging
- Multi-step planning
- Algorithm design

THINK HARDER:
- System design
- Security analysis
- Performance optimization
- Complex refactoring

ULTRATHINK:
- Critical decisions
- Novel problem solving
- Deep architecture work
- Difficult debugging
```

### Usage Patterns

```
# Basic
think about how to add pagination to this endpoint.

# Complex
think hard about the authentication flow for this API.
Consider security, user experience, and maintainability.

# Very Complex
think harder about redesigning this database schema
for better performance with these query patterns.

# Maximum
ultrathink about the best architecture for this
distributed system considering CAP theorem tradeoffs.
```

---

## Prompt Engineering

### The 6-Element Framework

```
1. CONTEXT
   Background information
   Current state
   Related files

2. TASK
   What needs to be done
   Clear objective

3. CONSTRAINTS
   Limitations
   Requirements
   Patterns to follow

4. FORMAT
   Expected output structure
   File locations
   Code style

5. TONE (optional)
   Explanatory vs. concise
   Teaching vs. production

6. EXAMPLES (optional)
   Sample inputs/outputs
   Pattern demonstrations
```

### Example Using All Elements

```
#file:src/api/v1/todos.py #file:src/models/todo.py

[Context]
I have a Todo API with CRUD operations. Users can create, 
read, update, and delete their own todos. Each todo has 
a title, description, completed status, and user_id.

[Task]
Add a "due_date" field to todos with:
- Optional due_date on creation
- Filter by due_date range
- Sort by due_date option

[Constraints]
- Must be backward compatible
- Use existing patterns in the codebase
- Include database migration
- Add validation (due_date must be in future)

[Format]
Provide:
1. Model updates
2. Schema updates
3. Migration file
4. API endpoint updates
5. Tests

[Tone]
Production-ready code with minimal comments.
```

### Prompt Templates

**Feature Addition:**
```
#file:[relevant file]

Add [feature] that:
- [Requirement 1]
- [Requirement 2]

Follow patterns in #folder:[pattern source]
```

**Bug Fix:**
```
#file:[buggy file] #problems

Error: [error message]
Expected: [expected behavior]
Actual: [actual behavior]

think hard about the root cause and fix.
```

**Code Review:**
```
Review #file:[file] for:
1. Security issues
2. Error handling
3. Performance
4. Best practices

List issues by severity with fixes.
```

**Refactoring:**
```
#file:[target file]

Refactor this code to:
- [Improvement 1]
- [Improvement 2]

Maintain existing functionality.
```

---

## Professional Workflows

### Explore → Plan → Code

**Phase 1: Explore**
```
What does #file:src/main.py do?
How does authentication work in this project?
Show me the database schema.
```

**Phase 2: Plan**
```
think hard about implementing [feature].

Consider:
- Database changes needed
- API design
- Service layer methods
- Error handling
- Testing approach

Give me an implementation plan.
```

**Phase 3: Code**
```
Based on the plan, implement [specific component].
#file:[relevant files]
Follow existing patterns.
```

### Test-Driven Development

**Step 1: Generate Test First**
```
#file:src/services/todo_service.py

Write a pytest test for a new method 
`mark_all_complete(user_id)` that marks all 
todos for a user as completed.

Include tests for:
- Normal case (multiple todos)
- Edge case (no todos)
- Authorization (only user's todos)
```

**Step 2: Implement to Pass**
```
#file:tests/test_todo_service.py

Now implement the mark_all_complete method to pass 
these tests. Follow existing patterns in the service.
```

**Step 3: Refactor**
```
Review and refactor the implementation for:
- Code clarity
- Error handling
- Performance
```

### Subagents for Parallel Work

Use multiple chat sessions for independent tasks:

**Main Chat:** Core implementation
**Subagent 1:** Tests
**Subagent 2:** Documentation
**Subagent 3:** Migration scripts

Each subagent has isolated context for focused work.

---

## Advanced Features

### Code Review on GitHub

1. Create Pull Request
2. Add "Copilot" as reviewer
3. Receive inline comments and suggestions
4. Address feedback

### In-Editor Code Review

```
Review my changes in #file:src/api/v1/todos.py.

Check for:
1. Security issues
2. Error handling
3. Performance
4. Best practices

Be thorough and critical.
```

### Custom Agents

Create specialized agents:

```markdown
# .github/agents/security-reviewer.agent.md

# Security Review Agent

You are a security expert reviewing code for:

## Common Vulnerabilities
- SQL injection
- XSS
- CSRF
- Authentication bypasses
- Authorization failures
- Input validation

## Review Process
1. Identify all user inputs
2. Trace data flow
3. Check validation at each step
4. Verify authentication/authorization
5. Check for sensitive data exposure

When reviewing, be thorough and paranoid.
List all potential issues with severity ratings.
```

---

## Security Best Practices

### The Golden Rules

1. **Never expose secrets** - Use .copilotignore
2. **Don't trust AI output blindly** - Review everything
3. **Verify security-critical code** - Auth, validation, data handling
4. **Keep .env out of context** - Never reference secret files

### .copilotignore Essential Patterns

```gitignore
# Secrets
.env
.env.*
*.pem
*.key
**/secrets/
**/credentials/

# Configuration with secrets
config/production.*
infrastructure/secrets/

# Sensitive data
**/customer_data/
**/pii/
```

### Security Review Checklist

```
[ ] Authentication required on protected endpoints?
[ ] Authorization checks (ownership, roles)?
[ ] Input validation complete?
[ ] SQL injection protected (parameterized queries)?
[ ] XSS prevention (output encoding)?
[ ] Secrets properly externalized?
[ ] Error messages don't leak info?
[ ] Logging doesn't include secrets?
```

---

## Troubleshooting

### Common Issues

**Issue:** Copilot doesn't understand my codebase
**Solution:** Add more context with #file: and #folder:

**Issue:** Generated code doesn't follow our patterns
**Solution:** Create .github/copilot-instructions.md

**Issue:** Copilot suggests outdated patterns
**Solution:** Provide examples of current patterns in prompts

**Issue:** Too much output / overwhelming responses
**Solution:** Be more specific in prompts, use constraints

**Issue:** Copilot ignores my instructions
**Solution:** Put critical instructions at the end of prompts

### Performance Tips

1. **Start specific** - Narrow scope = better results
2. **Build incrementally** - Small steps > big leaps
3. **Provide examples** - Show, don't just tell
4. **Use Plan Mode** - Visibility before execution
5. **Review early** - Catch issues before they compound

### Getting Better Results

```
INSTEAD OF:
"Make this better"

TRY:
"Refactor this function to:
- Use early returns
- Add type hints
- Handle the edge case where input is empty
- Follow our naming convention (snake_case)"
```

---

## Quick Reference Card

```
MODES:
Ask    - Questions, explanations
Edit   - Cmd/Ctrl+I inline
Agent  - Multi-file work
Plan   - /plan for visibility

CONTEXT:
#file:path    - Specific file
#folder:path  - Folder contents
#problems     - Current errors

THINKING:
think         - Basic analysis
think hard    - Complex problems
think harder  - Very complex
ultrathink    - Maximum reasoning

WORKFLOW:
Explore → Plan → Code → Review → Ship

CONFIG FILES:
.copilotignore              - Exclude from AI
.github/copilot-instructions.md - Project rules
.github/agents/*.agent.md   - Custom agents

THE 70/30 RULE:
AI delivers 70% fast. YOU add the critical 30%.
```

---

**End of Knowledge Base** 🎓
