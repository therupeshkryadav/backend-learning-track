# =====================================================
# Database Module
# =====================================================
"""
In-memory database for student management.
Can be replaced with actual database (PostgreSQL, MongoDB, etc.)
"""

from typing import Dict, List, Optional
from models import Student, StudentCreate, StudentUpdate

# In-memory database
students_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "name": "John Doe",
        "age": 21,
        "year": "Year 12"
    },
    2: {
        "id": 2,
        "name": "Jane Smith",
        "age": 22,
        "year": "Year 13"
    }
}

# Counter for new student IDs
next_id: int = 3


class StudentDatabase:
    """In-memory student database operations"""
    
    @staticmethod
    def get_all() -> List[Student]:
        """Get all students"""
        return [Student(**student) for student in students_db.values()]
    
    @staticmethod
    def get_by_id(student_id: int) -> Optional[Student]:
        """Get student by ID"""
        if student_id in students_db:
            return Student(**students_db[student_id])
        return None
    
    @staticmethod
    def get_by_name(name: str) -> Optional[Student]:
        """Get student by name"""
        for student in students_db.values():
            if student["name"].lower() == name.lower():
                return Student(**student)
        return None
    
    @staticmethod
    def create(student: StudentCreate) -> Student:
        """Create a new student"""
        global next_id
        new_student = {
            "id": next_id,
            **student.dict()
        }
        students_db[next_id] = new_student
        next_id += 1
        return Student(**new_student)
    
    @staticmethod
    def update(student_id: int, student_update: StudentUpdate) -> Optional[Student]:
        """Update an existing student"""
        if student_id not in students_db:
            return None
        
        update_data = student_update.dict(exclude_unset=True)
        students_db[student_id].update(update_data)
        return Student(**students_db[student_id])
    
    @staticmethod
    def delete(student_id: int) -> bool:
        """Delete a student"""
        if student_id in students_db:
            del students_db[student_id]
            return True
        return False
    
    @staticmethod
    def exists(student_id: int) -> bool:
        """Check if student exists"""
        return student_id in students_db
