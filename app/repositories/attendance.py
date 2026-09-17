
from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.attendance import Attendance
from app.repositories.base import BaseRepository


class AttendanceRepository(BaseRepository[Attendance]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(
        self,
        entity_id: int,
    ) -> Attendance | None:
        return await self.session.get(Attendance, entity_id)

    async def get_by_student_teacher_date(
        self,
        student_id: int,
        teacher_id: int,
        attendance_date: date,
    ) -> Attendance | None:
        result = await self.session.execute(
            select(Attendance).where(
                Attendance.student_id == student_id,
                Attendance.teacher_id == teacher_id,
                Attendance.date == attendance_date,
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        attendance: Attendance,
    ) -> Attendance:
        self.session.add(attendance)
        await self.session.flush()
        await self.session.refresh(attendance)
        return attendance