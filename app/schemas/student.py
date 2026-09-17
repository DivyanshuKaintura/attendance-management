from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    enrollment_number: str = Field(
        min_length=5, max_length=20
    )
    
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    enrollment_number: str
    
    model_config = ConfigDict(from_attributes=True)