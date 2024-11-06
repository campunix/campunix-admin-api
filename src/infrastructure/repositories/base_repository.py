from math import ceil
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from typing import Generic, Type, TypeVar, Optional, List, Dict, Any

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select, func

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.exceptions.db_exceptions import DatabaseIntegrityError, DatabaseError

# Define a type variable for generic use in BaseRepository
T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T], BaseRepositoryContract):
    def __init__(self, db_session: AsyncSession, model: Type[T]):
        self.db_session = db_session
        self.model = model

    async def get_by_id(
            self,
            id: int,
            joins: Optional[List[Any]] = None
    ) -> Optional[T]:
        statement = select(self.model).where(self.model.id == id)

        # Apply joins if provided
        if joins:
            for related_model, condition in joins:
                statement = statement.join(related_model, condition).add_columns(related_model)

        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_all(
            self,
            page: int = 1,
            page_size: int = 10,
            paginate: bool = False,
            filters: Optional[List[Any]] = None,
            joins: Optional[List[Any]] = None
    ) -> Dict[str, Any]:
        # Start with base query
        statement = select(self.model)

        # Apply joins if provided
        if joins:
            for related_model, condition in joins:
                # statement = statement.join(related_model, condition)
                statement = statement.join(related_model, condition).add_columns(related_model)

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

        # Apply joins to total_items_stmt for accurate counts in joined queries
        if joins:
            for related_model, condition in joins:
                total_items_stmt = total_items_stmt.join(related_model, condition)

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
        try:
            self.db_session.add(obj)
            await self.db_session.commit()
            await self.db_session.refresh(obj)
            return obj

        except IntegrityError:
            await self.db_session.rollback()
            raise DatabaseIntegrityError(detail=f"Integrity error: {obj} already exists.")
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise DatabaseError(detail=f"Database error: {e}")

    async def update(self, id: int, obj_data: T) -> Optional[T]:
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**obj_data.model_dump(exclude_unset=True))
            .execution_options(synchronize_session="fetch")
            .returning(self.model)
        )

        result = await self.db_session.execute(stmt)
        updated_record = result.scalar_one_or_none()
        await self.db_session.commit()

        return updated_record

    async def delete(self, id: int) -> bool:
        statement = select(self.model).where(self.model.id == id)
        result = await self.db_session.execute(statement)
        obj = result.scalars().one_or_none()

        if obj:
            await self.db_session.delete(obj)
            await self.db_session.commit()
            return True

        return False

    async def bulk_insert(self, obj_list: List[T]):
        self.db_session.add_all(obj_list)
        await self.db_session.commit()
        pass
