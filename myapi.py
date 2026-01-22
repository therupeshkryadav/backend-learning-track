# =====================================================
# FastAPI Student Management System
# =====================================================
# This module implements a RESTful API for managing
# student data with multiple query methods

# Import necessary modules from FastAPI
from fastapi import FastAPI, Path  # FastAPI framework and Path validator
from typing import Optional  # For optional type hints

# =====================================================
# Application Setup
# =====================================================
# Create a FastAPI application instance
# This will automatically generate OpenAPI documentation
app = FastAPI()

# =====================================================
# Data Models
# =====================================================
# Sample student data dictionary with student ID as key
# Each student record contains: name, age, and year information
students = {
    1: {
        "name": "John Doe",
        "age": 21,
        "year": "Year 12"  
    },
    2: {
        "name": "Jane Smith",
        "age": 22,
        "year": "Year 13"  
    }
}

# =====================================================
# API Endpoints
# =====================================================

# Root endpoint - Returns basic greeting message
# Route: GET /
@app.get("/")
def index():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        dict: A greeting message
    """
    return {"name": "First Data"}

# Get student by ID with validation
# Route: GET /get-student/{student_id}
# Validation: student_id must be between 1 and 2 (gt=0, lt=3)
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to get", gt=0, lt=3)):
    """
    Retrieve a specific student by their ID.
    
    Args:
        student_id (int): The student's ID (must be 1 or 2)
    
    Returns:
        dict: Student object containing name, age, and year
    
    Raises:
        KeyError: If student_id doesn't exist
    """
    return students[student_id]

# Get student by name using query parameter
# Route: GET /get-by-name?name=<student_name>
# This allows flexible searching by student name
@app.get("/get-by-name")
def get_student_by_name(name: Optional[str] = None):
    """
    Retrieve a student by their name using query parameter.
    
    Args:
        name (Optional[str]): The student's name to search for
    
    Returns:
        dict: Student object if found, otherwise "Not Found" message
    """
    # Iterate through all students to find matching name
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    # Return not found message if no student matches the name
    return {"Data": "Not Found"}