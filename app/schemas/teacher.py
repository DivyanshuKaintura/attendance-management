from pydantic import Field, BaseModel, ConfigDict, EmailStr

class TeacherCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr


class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)