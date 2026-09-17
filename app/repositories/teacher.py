
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.teacher import Teacher
from app.repositories.base import BaseRepository


class TeacherRepository(BaseRepository[Teacher]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, entity_id: int) -> Teacher | None:
        return await self.session.get(Teacher, entity_id)

    async def get_by_email(self, email: str) -> Teacher | None:
        result = await self.session.execute(
            select(Teacher).where(Teacher.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, teacher: Teacher) -> Teacher:
        self.session.add(teacher)
        await self.session.flush()
        await self.session.refresh(teacher)
        return teacher