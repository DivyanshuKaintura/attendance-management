from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.student import Student
from app.repositories.base import BaseRepository

class StudentRepository(BaseRepository[Student]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        
    async def get_by_id(self, entity_id: int) -> Student | None:
        return await self.session.get(Student, entity_id)
    
    async def create(self, student: Student) -> Student:
        self.session.add(student)
        await self.session.flush()
        await self.session.refresh(student)
        return student
    
    async def get_by_email(self, email: str) -> Student | None:
        result = await self.session.execute(
            select(Student).where(Student.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_by_enrollment_number(self, enrollment_number: str) -> Student | None:
        result = await self.session.execute(
            select(Student).where(Student.enrollment_number == enrollment_number)
        )
        return result.scalar_one_or_none()
    
    
    
    