import json
from typing import Optional, Dict, Any

from sqlalchemy import or_

from src.core.contracts.exam_routines_repository_contract import ExamRoutinesRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.exam_routines import ExamRoutine
from src.core.exceptions.db_exceptions import DatabaseError
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.exam.services.exam_routine_service_contract import ExamRoutineServiceContract
from src.models.exam_routine import ExamRoutineOut, ExamRoutineIn


class ExamRoutineService(ExamRoutineServiceContract):
    def __init__(
            self,
            exam_routines_repository: ExamRoutinesRepositoryContract,
    ):
        self.exam_routines_repository = exam_routines_repository

    async def save_exam_routine(self, exam_routine_in: ExamRoutineIn) -> Optional[ExamRoutineOut]:
        new_routine = await self.exam_routines_repository.create(
            ExamRoutine(
                syllabus_id=exam_routine_in.syllabus_id,
                title=exam_routine_in.title,
                description=exam_routine_in.description,
                calendar_year=exam_routine_in.calendar_year,
                is_active=exam_routine_in.is_active,
                exam_routine=json.loads(exam_routine_in.exam_routine)
            )
        )

        if new_routine is None:
            raise DatabaseError()

        return entity_to_model(entity=new_routine, model=ExamRoutineOut)

    async def get_exam_routines(
            self,
            page: int = 1,
            page_size: int = 10,
            paginate: bool = False,
            search_query: Optional[str] = None
    ) -> Dict[str, Any]:

        filters = []

        if search_query:
            filters.append(
                or_(
                    ExamRoutine.title.ilike(f"%{search_query}%"),
                    ExamRoutine.calendar_year.ilike(f"%{search_query}%")
                )
            )

        routine_dict = await self.exam_routines_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters
        )

        return entity_to_model_list(entity_dict=routine_dict, model=ExamRoutineOut, paginate=paginate)

    async def get_exam_routine_by_id(self, id: int) -> Optional[ExamRoutineOut]:
        exam_routine = await self.exam_routines_repository.get_by_id(id=id)

        if not exam_routine:
            raise NotFoundException("Routine doesn't exist!")

        return entity_to_model(entity=exam_routine, model=ExamRoutineOut)

    async def update_exam_routine(self, id: int, exam_routine_in: ExamRoutineIn) -> Optional[ExamRoutineOut]:
        routine = await self.exam_routines_repository.update(
            id=id,
            obj_data=ExamRoutine(
                syllabus_id=exam_routine_in.syllabus_id,
                title=exam_routine_in.title,
                description=exam_routine_in.description,
                calendar_year=exam_routine_in.calendar_year,
                is_active=exam_routine_in.is_active,
                exam_routine=json.loads(exam_routine_in.exam_routine)
            )
        )

        if not routine:
            raise NotFoundException(detail="Routine doesn't exist")

        return entity_to_model(entity=routine, model=ExamRoutineOut)

    async def delete_exam_routine(self, id: int) -> bool:
        result = await self.exam_routines_repository.delete(id)

        if not result:
            raise NotFoundException(detail="Deletion unsuccessful")

        return result
