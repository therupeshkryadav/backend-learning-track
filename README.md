# FastAPI Student Management System

A modern, production-ready FastAPI application demonstrating RESTful API design patterns with complete CRUD operations for student management.

## 🎯 Features

- ✅ **Full CRUD Operations** - Create, Read, Update, Delete students
- ✅ **Path Parameter Validation** - Secure endpoint parameters with validation
- ✅ **Query Parameters** - Flexible search by student name
- ✅ **Error Handling** - Comprehensive HTTP exception handling
- ✅ **Type Safety** - Pydantic models for request/response validation
- ✅ **Auto Documentation** - Interactive Swagger UI and ReDoc
- ✅ **Environment Configuration** - Configurable settings via .env
- ✅ **Well Commented** - Detailed code comments and docstrings
- ✅ **Modular Architecture** - Separated concerns (app, models, database, config)

## 📁 Project Structure

```
fastapi-job-switch-2026/
├── myapi.py              # Main application with all endpoints
├── config.py             # Configuration management
├── models.py             # Pydantic data models
├── database.py           # In-memory database operations
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
cd fastapi-job-switch-2026
```

2. **Create a virtual environment** (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env if needed (optional)
```

### Running the Application

```bash
uvicorn myapi:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger UI** (Interactive docs): http://localhost:8000/docs
- **ReDoc** (Alternative docs): http://localhost:8000/redoc

## 📚 API Endpoints

### Health Check
```
GET /health
```
Check if the API is running.

### Student Management

#### Get All Students
```
GET /students
```
Returns a list of all students.

#### Get Student by ID
```
GET /students/{student_id}
```
**Parameters:**
- `student_id` (path): Student ID (must be > 0)

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 21,
  "year": "Year 12"
}
```

#### Search Student by Name
```
GET /students-by-name/search?name=John Doe
```
**Parameters:**
- `name` (query): Student name to search for

#### Create New Student
```
POST /students
```
**Request Body:**
```json
{
  "name": "Alice Johnson",
  "age": 20,
  "year": "Year 11"
}
```

**Response:** (HTTP 201 Created)
```json
{
  "id": 3,
  "name": "Alice Johnson",
  "age": 20,
  "year": "Year 11"
}
```

#### Update Student
```
PUT /students/{student_id}
```
**Request Body:** (All fields optional)
```json
{
  "name": "John Updated",
  "age": 22,
  "year": "Year 13"
}
```

#### Delete Student
```
DELETE /students/{student_id}
```
**Response:** (HTTP 204 No Content)

## 📊 Sample Data

The application comes pre-loaded with 2 students:

1. **John Doe**
   - ID: 1
   - Age: 21
   - Year: Year 12

2. **Jane Smith**
   - ID: 2
   - Age: 22
   - Year: Year 13

## 🔧 Configuration

Environment variables can be set in `.env`:

```env
APP_NAME=FastAPI Student Management System
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0
PORT=8000
RELOAD=True
```

## 📝 Code Organization

- **myapi.py** - Main application with all endpoint definitions
- **config.py** - Application configuration and environment management
- **models.py** - Pydantic models for data validation and documentation
- **database.py** - Database operations and in-memory storage

## 🧪 Testing Endpoints

### Using curl

```bash
# Get all students
curl http://localhost:8000/students

# Get student by ID
curl http://localhost:8000/students/1

# Search by name
curl "http://localhost:8000/students-by-name/search?name=John%20Doe"

# Create new student
curl -X POST http://localhost:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Bob","age":23,"year":"Year 12"}'

# Update student
curl -X PUT http://localhost:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"age":22}'

# Delete student
curl -X DELETE http://localhost:8000/students/3
```

### Using Swagger UI

Visit http://localhost:8000/docs to test all endpoints interactively with the built-in Swagger UI.

## 📈 Progress Checklist

- [x] Created FastAPI application
- [x] Implemented GET endpoints (all students, by ID, by name)
- [x] Implemented POST endpoint (create student)
- [x] Implemented PUT endpoint (update student)
- [x] Implemented DELETE endpoint (delete student)
- [x] Added error handling with HTTP exceptions
- [x] Created Pydantic data models
- [x] Separated concerns (config, models, database)
- [x] Added environment configuration
- [x] Created requirements.txt
- [x] Added comprehensive documentation
- [x] Added detailed code comments
- [x] Committed to GitHub

## 🎨 Code Quality

- ✅ Type hints for all functions
- ✅ Comprehensive docstrings
- ✅ Organized with section headers
- ✅ Error handling with descriptive messages
- ✅ RESTful API design patterns
- ✅ PEP 8 compliant code style

## 🤝 Future Enhancements

- Add database integration (PostgreSQL/MongoDB)
- Add authentication and authorization
- Add input validation rules
- Add API rate limiting
- Add logging system
- Add unit tests
- Add API versioning
- Add pagination for large datasets

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as part of FastAPI learning journey - 2026