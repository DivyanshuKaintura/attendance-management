from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

app = FastAPI(
    title="Attendance Management System",
    description="A simple attendance management system",
    version="1.0.0"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Attendance Management System!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/health/db")
async def database_health_check(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(text("SELECT 1"))
    value = result.scalar_one()

    return {
        "database": "connected",
        "result": value,
    }