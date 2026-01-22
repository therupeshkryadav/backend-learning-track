# =====================================================
# FastAPI Student Management System
# =====================================================
"""
Main application module implementing a RESTful API for 
managing student data with multiple query methods.
Includes CRUD operations and comprehensive error handling.
"""

# Import necessary modules from FastAPI
from fastapi import FastAPI, Path, HTTPException, status  # FastAPI framework components
from typing import List, Optional  # Type hints
from config import settings  # Configuration management
from models import Student, StudentCreate, StudentUpdate, StudentResponse  # Pydantic models
from database import StudentDatabase  # Database operations

# =====================================================
# Application Setup
# =====================================================
# Create a FastAPI application instance with metadata
# This automatically generates OpenAPI documentation
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A REST API for managing student records with full CRUD operations"
)

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
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        dict: Health status
    """
    return {"status": "healthy", "service": settings.APP_NAME}

# =====================================================
# Student Endpoints - GET Operations
# =====================================================

# Get all students
@app.get("/students", response_model=List[Student], tags=["Students"])
def get_all_students():
    """
    Retrieve all students from the database.
    
    Returns:
        List[Student]: List of all student objects
    """
    return StudentDatabase.get_all()

# Get student by ID with validation
@app.get("/students/{student_id}", response_model=Student, tags=["Students"])
def get_student(student_id: int = Path(..., gt=0, description="The ID of the student to retrieve")):
    """
    Retrieve a specific student by their ID.
    
    Args:
        student_id (int): The student's ID (must be greater than 0)
    
    Returns:
        Student: Student object containing name, age, and year
    
    Raises:
        HTTPException: If student_id doesn't exist (404)
    """
    student = StudentDatabase.get_by_id(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    return student

# Get student by name using query parameter
@app.get("/students-by-name/search", response_model=Student, tags=["Students"])
def get_student_by_name(name: str):
    """
    Retrieve a student by their name using query parameter.
    
    Args:
        name (str): The student's name to search for
    
    Returns:
        Student: Student object if found
    
    Raises:
        HTTPException: If student not found (404)
    """
    student = StudentDatabase.get_by_name(name)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with name '{name}' not found"
        )
    return student

# =====================================================
# Student Endpoints - POST Operations (Create)
# =====================================================

# Create a new student
@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED, tags=["Students"])
def create_student(student: StudentCreate):
    """
    Create a new student record.
    
    Args:
        student (StudentCreate): Student data to create
    
    Returns:
        Student: The created student object with assigned ID
    """
    return StudentDatabase.create(student)

# =====================================================
# Student Endpoints - PUT Operations (Update)
# =====================================================

# Update an existing student
@app.put("/students/{student_id}", response_model=Student, tags=["Students"])
def update_student(
    student_id: int = Path(..., gt=0, description="The ID of the student to update"),
    student_update: StudentUpdate = None
):
    """
    Update an existing student's information.
    
    Args:
        student_id (int): The student's ID to update
        student_update (StudentUpdate): Fields to update
    
    Returns:
        Student: The updated student object
    
    Raises:
        HTTPException: If student not found (404)
    """
    if not StudentDatabase.exists(student_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    updated_student = StudentDatabase.update(student_id, student_update)
    return updated_student

# =====================================================
# Student Endpoints - DELETE Operations
# =====================================================

# Delete a student
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Students"])
def delete_student(student_id: int = Path(..., gt=0, description="The ID of the student to delete")):
    """
    Delete a student record from the database.
    
    Args:
        student_id (int): The student's ID to delete
    
    Raises:
        HTTPException: If student not found (404)
    """
    if not StudentDatabase.delete(student_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    return None