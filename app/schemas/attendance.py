from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import date
from app.models import AttendanceStatus

class AttendanceCreate(BaseModel):
    student_id: int
    teacher_id: int
    date: date 
    status: AttendanceStatus 

class AttendanceResponse(BaseModel):
    id: int
    student_id: int
    teacher_id: int
    date: str
    status: AttendanceStatus

    model_config = ConfigDict(from_attributes=True)