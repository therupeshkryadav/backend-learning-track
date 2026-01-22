# FastAPI Student Management System

A simple FastAPI application for learning purposes.

## Getting Started

### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn

### Installation
```bash
pip install fastapi uvicorn
```

### Running the Application
```bash
uvicorn myapi:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Response**: `{"message": "Hello, World!"}`

### 2. Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**: `{"status": "healthy"}`