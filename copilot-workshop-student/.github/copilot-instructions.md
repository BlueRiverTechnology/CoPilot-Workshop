# Copilot Instructions for Todo API

## Workshop Simplifications

**IMPORTANT:** This is a workshop environment with simplified patterns:
- **Authentication:** For workshop purposes, use fixed `owner_id = "default-user"` instead of implementing full JWT authentication
- **Production Note:** In production, all endpoints would use `get_current_user` dependency
- Follow the specific session instructions which may override these patterns for learning purposes

---

## Architecture
- FastAPI with async/await
- 3-tier architecture: API → Services → Models
- SQLAlchemy with async sessions
- Pydantic for request/response validation

## Coding Standards
- Use type hints on all functions
- Write docstrings for public methods
- Follow PEP 8 style guide
- Use descriptive variable names
- Prefer async/await for I/O operations

## Key Patterns
- All endpoints require authentication (use get_current_user dependency)
- Service layer handles business logic
- Models use UUID primary keys (string format)
- Responses use Pydantic schemas
- Use HTTPException for errors with appropriate status codes

## File Structure
- src/api/v1/ - API endpoints (FastAPI routers)
- src/services/ - Business logic layer
- src/models/ - SQLAlchemy ORM models
- src/schemas/ - Pydantic request/response schemas
- tests/ - Pytest test files

## Testing
- Write pytest tests for all new code
- Use fixtures for database setup
- Mock external services
- Test both success and error paths

## Security
- Never hardcode secrets (use environment variables)
- Always validate user input
- Use parameterized queries (SQLAlchemy handles this)
- Check ownership before modifying resources
- Return 404 for not found, 403 for forbidden

## Error Handling
- Use specific HTTP status codes (400, 401, 403, 404, 500)
- Return helpful error messages
- Log errors for debugging
- Don't leak sensitive information in error responses
