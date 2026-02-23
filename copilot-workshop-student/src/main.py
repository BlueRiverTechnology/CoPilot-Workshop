"""FastAPI Todo Application - Main Entry Point

Basic FastAPI app setup for Copilot Workshop.
Students will add API routes in Session 2-3.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import todos_router

# Initialize FastAPI app
app = FastAPI(
    title="Todo API",
    description="GitHub Copilot Workshop - Power User Training",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(todos_router, prefix="/api/v1", tags=["todos"])


@app.get("/")
async def root() -> dict:
    """
    Root endpoint - health check.
    
    :return: Welcome message
    """
    return {
        "message": "Welcome to Todo API",
        "workshop": "GitHub Copilot Power User Workshop",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check() -> dict:
    """
    Health check endpoint.
    
    :return: Service status
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
