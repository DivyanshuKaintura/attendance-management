from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_student_service
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student import (
    StudentAlreadyExistsError,
    StudentNotFoundError,
    StudentService,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    data: StudentCreate,
    service: StudentService = Depends(get_student_service),
):
    try:
        return await service.create_student(data)

    except StudentAlreadyExistsError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
async def get_student(
    student_id: int,
    service: StudentService = Depends(get_student_service),
):
    try:
        return await service.get_student(student_id)

    except StudentNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error