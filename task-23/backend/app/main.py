from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Student
from app.schemas import StudentCreate, StudentUpdate, StudentResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if db.query(Student).filter(Student.email == student.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(Student).filter(Student.enrollment_number == student.enrollment_number).first():
        raise HTTPException(status_code=400, detail="Enrollment number exists")
    
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students", response_model=List[StudentResponse])
def get_students(
    search: Optional[str] = Query(None, description="Search by name or enrollment number"),
    db: Session = Depends(get_db)
):
    query = db.query(Student)
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (Student.full_name.ilike(search_filter)) | 
            (Student.enrollment_number.ilike(search_filter))
        )
    return query.all()

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updates: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check email uniqueness if email updated
    if updates.email and updates.email != student.email:
        if db.query(Student).filter(Student.email == updates.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")
            
    # Check enrollment uniqueness if enrollment updated
    if updates.enrollment_number and updates.enrollment_number != student.enrollment_number:
        if db.query(Student).filter(Student.enrollment_number == updates.enrollment_number).first():
            raise HTTPException(status_code=400, detail="Enrollment number exists")

    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(student, key, value)
        
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return None
