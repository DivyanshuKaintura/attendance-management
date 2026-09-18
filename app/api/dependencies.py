from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.student import StudentRepository
from app.services.student import StudentService


def get_student_repository(
    db: AsyncSession = Depends(get_db),
) -> StudentRepository:
    return StudentRepository(db)


def get_student_service(
    repository: StudentRepository = Depends(get_student_repository),
    db: AsyncSession = Depends(get_db),
) -> StudentService:
    return StudentService(repository, db)