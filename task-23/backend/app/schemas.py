from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    full_name: str
    email: EmailStr
    course: str
    enrollment_number: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    course: str | None = None
    enrollment_number: str | None = None

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True
