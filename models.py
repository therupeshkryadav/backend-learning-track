# =====================================================
# Data Models using Pydantic
# =====================================================
"""
Pydantic models for request/response validation.
Provides type safety and automatic documentation.
"""

from pydantic import BaseModel
from typing import Optional


class StudentBase(BaseModel):
    """Base student model with common fields"""
    name: str
    age: int
    year: str


class StudentCreate(StudentBase):
    """Model for creating a new student"""
    pass


class StudentUpdate(BaseModel):
    """Model for updating student information"""
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


class Student(StudentBase):
    """Student model with ID"""
    id: int
    
    class Config:
        """Pydantic config"""
        from_attributes = True


class StudentResponse(BaseModel):
    """Standard API response wrapper"""
    success: bool
    data: Optional[Student] = None
    message: str = ""
