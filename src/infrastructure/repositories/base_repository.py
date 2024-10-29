from typing import Generic, Type, TypeVar, Optional, List, Dict, Any
from sqlmodel import SQLModel, select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, or_
from math import ceil

# Define a type variable for generic use in BaseRepository
T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, db_session: AsyncSession, model: Type[T]):
        self.db_session = db_session
        self.model = model

    async def get_by_id(self, id: int) -> Optional[T]:
        statement = select(self.model).where(self.model.id == id)
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_all(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None,  # Adjusted type to Any
    ) -> Dict[str, Any]:
        # Start with base query
        statement = select(self.model)

        # Apply filters if provided
        if filters:
            for condition in filters:
                statement = statement.where(condition)

        # Calculate total items based on the filtered query
        total_items_stmt = (
            select(func.count()).select_from(self.model).where(*filters)
            if filters
            else select(func.count()).select_from(self.model)
        )
        total_items_result = await self.db_session.execute(total_items_stmt)
        total_items = total_items_result.scalar_one()

        # Calculate total pages based on total items and page size
        total_pages = ceil(total_items / page_size)

        # Apply pagination if enabled
        if paginate:
            statement = statement.offset((page - 1) * page_size).limit(page_size)

        result = await self.db_session.execute(statement)
        items = result.scalars().all()

        if paginate:
            return {
                "items": items,
                "current_page": page,
                "total_pages": total_pages,
                "page_size": page_size,
                "total_items": total_items,
            }

        return {
            "items": items,
        }

    async def create(self, obj: T) -> T:
        self.db_session.add(obj)
        await self.db_session.commit()
        await self.db_session.refresh(obj)
        return obj

    async def update(self, id: int, obj_data: dict) -> Optional[T]:
        statement = select(self.model).where(self.model.id == id)
        result = await self.db_session.execute(statement)
        obj = result.scalars().one_or_none()

        if obj:
            for key, value in obj_data.items():
                setattr(obj, key, value)
            await self.db_session.commit()
            await self.db_session.refresh(obj)

        return obj

    async def delete(self, id: int) -> None:
        statement = select(self.model).where(self.model.id == id)
        result = await self.db_session.execute(statement)
        obj = result.scalars().one_or_none()

        if obj:
            await self.db_session.delete(obj)
            await self.db_session.commit()
