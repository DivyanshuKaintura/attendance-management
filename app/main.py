from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.router import api_router
from app.db.session import get_db

app = FastAPI(
    title="Attendance Management System",
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Attendance Management API is running"}


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