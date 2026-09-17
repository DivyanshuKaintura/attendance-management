from sqlalchemy.ext.asyncio import AsyncSession

from app.models.student import Student
from app.repositories.student import StudentRepository
from app.schemas.student import StudentCreate


class StudentAlreadyExistsError(Exception):
    pass


class StudentService:
    def __init__(
        self,
        repository: StudentRepository,
        session: AsyncSession,
    ):
        self.repository = repository
        self.session = session

    async def create_student(self, data: StudentCreate) -> Student:
        # 1. Check whether the email is already registered
        email = str(data.email)

        existing_email = await self.repository.get_by_email(email)

        if existing_email:
            raise StudentAlreadyExistsError(
                "Email is already registered"
            )

        # 2. Check whether the enrollment number is already registered
        existing_enrollment = (
            await self.repository.get_by_enrollment_number(
                data.enrollment_number
            )
        )

        if existing_enrollment:
            raise StudentAlreadyExistsError(
                "Enrollment number is already registered"
            )

        # 3. Convert the validated schema into a database model
        student = Student(
            name=data.name,
            email=str(data.email),
            enrollment_number=data.enrollment_number,
        )

        # 4. Ask the repository to persist the model
        student = await self.repository.create(student)

        # 5. Commit the transaction
        await self.session.commit()

        return student