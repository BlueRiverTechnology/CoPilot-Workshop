# Todo API - Product Requirements

## Overview
Simple personal todo list API for single users

## Core Features (MVP)
1. **Create Todo**
   - Title (required, max 200 chars)
   - Description (optional, max 1000 chars)
   - Starts as not completed

2. **List Todos**
   - Show all user's todos
   - Filter by completed status
   - Pagination (skip, limit)

3. **Update Todo**
   - Change title, description
   - Mark as completed/not completed

4. **Delete Todo**
   - Remove todo permanently

5. **User Authentication** (pre-built)
   - JWT-based auth
   - Each user sees only their todos

## Non-Goals (Not Building)
- Sharing todos between users
- Due dates
- Categories/tags
- Reminders
