# =====================================================
# Configuration Management
# =====================================================
"""
Configuration module for FastAPI application.
Manages environment variables and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    # Application Info
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Student Management System")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    
    # Server Configuration
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    RELOAD: bool = os.getenv("RELOAD", "True").lower() == "true"

# Create global settings instance
settings = Settings()
