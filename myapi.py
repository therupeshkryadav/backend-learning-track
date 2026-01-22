# =====================================================
# FastAPI Application - Basic Setup
# =====================================================
"""
Simple FastAPI application for learning purposes.
"""

# Import necessary modules
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application instance
app = FastAPI()


# =====================================================
# API Endpoints
# =====================================================

# Root endpoint - Returns basic greeting and API info
@app.get("/", tags=["Root"])
def index():
    """
    Root endpoint that returns API information.
    
    Returns:
        dict: API name and status
    """
    return {"message": "Hello, World!"}

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        dict: Health status
    """
    return {"status": "healthy"}