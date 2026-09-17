from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.student import StudentRepository
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student import (
    StudentAlreadyExistsError,
    StudentService,
)

router = APIRouter(prefix="/students", tags=["Students"])


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    data: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    repository = StudentRepository(db)
    service = StudentService(repository, db)

    try:
        student = await service.create_student(data)
        return student

    except StudentAlreadyExistsError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
        

@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    repository = StudentRepository(db)
    student = await repository.get_by_id(student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student