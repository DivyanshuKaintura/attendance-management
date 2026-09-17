
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(ABC, Generic[ModelType]):
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def get_by_id(self, entity_id: int) -> ModelType | None:
        """Fetch an entity by its primary key."""
        raise NotImplementedError