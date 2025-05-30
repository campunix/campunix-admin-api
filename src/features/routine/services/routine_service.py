import json
from typing import Optional, Dict, Any

from sqlalchemy import or_

from src.core.contracts.routines_repository_contract import RoutinesRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.routine import Routine
from src.core.exceptions.db_exceptions import DatabaseError
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services import PreferenceServiceContract
from src.features.routine.models.gene import Gene
from src.features.routine.models.routine_course import RoutineCourse
from src.features.routine.models.routine_in import SavedRoutineIn
from src.features.routine.models.routine_out import RoutineOut, SavedRoutineOut
from src.features.routine.models.routine_semester import RoutineSemester
from src.features.routine.services.routine_generator_contract import RoutineGeneratorContract
from src.features.routine.services.routine_contract import RoutineServiceContract
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract


class RoutineService(RoutineServiceContract):
    def __init__(self,
                routine_generator: RoutineGeneratorContract, 
                routine_repository: RoutinesRepositoryContract,
                syllabus_service: SyllabusServiceContract,
                preference_service: PreferenceServiceContract):
        self.routine_generator = routine_generator
        self.routine_repository = routine_repository
        self.syllabus_service = syllabus_service
        self.preference_service = preference_service

    async def generate_routine_async(self, syllabus_id: int, total_slots: int):
        syllabus_courses = await self.syllabus_service.get_syllabus_course_list(syllabus_id)
        preferences = await self.preference_service.get_preferences()

        course_dict = self.get_courses_from_syllabus(syllabus_courses, preferences=preferences["items"])
        semester_dict = self.get_semesters_from_syllabus(syllabus_courses)
        available_genes = self.get_genes_from_syllabus(syllabus_courses, course_dict, semester_dict)

        chromosome = await self.routine_generator.generate_async(
            total_slots=total_slots,
            total_semesters=len(semester_dict),
            available_genes=available_genes)

        return RoutineOut(
            courses=list(course_dict.values()),
            semesters=list(semester_dict.values()),
            routine=chromosome
        )

    def get_genes_from_syllabus(self, syllabus_courses, course_dict, semester_dict):

        available_genes = []
        for x in syllabus_courses:
            course = course_dict[x["course"].code]
            semester = semester_dict[x["semester"].id]

            available_genes.append(Gene(
                semester = semester,
                course = course))

        return available_genes

    def get_courses_from_syllabus(self, syllabus_courses, preferences=None):
        course_dict: dict[str, RoutineCourse] = dict()

        for x in syllabus_courses:
            if x["course"].code not in course_dict:
                course_dict[x["course"].code] = RoutineCourse(
                    id = x["course"].id,
                    code = x["course"].code,
                    title = x["course"].title,
                    course_type = x["course"].course_type,
                    teachers = x["course"].course_teachers,
                    preferences = preferences or []
                )

        return course_dict

    def get_semesters_from_syllabus(self, syllabus_courses):
        semester_dict: dict[int, RoutineSemester] = dict()

        for x in syllabus_courses:
            if x["semester"].id not in semester_dict:
                semester_dict[x["semester"].id] = RoutineSemester(
                    id=x["semester"].id,
                    year=x["semester"].year,
                    number=x["semester"].number
                )

        sorted_semesters = sorted(
            semester_dict.values(),
            key=lambda semester: semester.number) or []

        semester_code_dict = {x.id: idx + 1 for idx, x in enumerate(sorted_semesters)}
        for key, value in semester_dict.items():
            value.serial_number = semester_code_dict[value.id]

        return semester_dict

    async def save_routine(self, routine_save_in: SavedRoutineIn) -> Optional[SavedRoutineOut]:
        new_routine = await self.routine_repository.create(
            Routine(
                syllabus_id=routine_save_in.syllabus_id,
                title=routine_save_in.title,
                description=routine_save_in.description,
                calendar_year=routine_save_in.calendar_year,
                is_active=routine_save_in.is_active,
                routine=json.loads(routine_save_in.routine)
            )
        )

        if new_routine is None:
            raise DatabaseError()

        return entity_to_model(entity=new_routine, model=SavedRoutineOut)

    async def delete_routine(self, id: int) -> bool:
        result = await self.routine_repository.delete(id)

        if result is False:
            raise NotFoundException(detail="Deletion unsuccessful")

        return result

    async def get_routine_by_id(self, id: int) -> Optional[SavedRoutineOut]:
        routine_data = await self.routine_repository.get_by_id(id=id)

        if not routine_data:
            raise NotFoundException(detail="Routine doesn't exists!")

        return entity_to_model(entity=routine_data, model=SavedRoutineOut)

    async def get_saved_routines(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                                 search_query: Optional[str] = None) -> Dict[str, Any]:
        filters = []

        if search_query:
            filters.append(
                or_(
                    Routine.title.ilike(f"%{search_query}%"),
                    Routine.calendar_year.ilike(f"%{search_query}%")
                )
            )

        routine_dict = await self.routine_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters
        )

        return entity_to_model_list(entity_dict=routine_dict, model=SavedRoutineOut, paginate=paginate)

    async def update_saved_routine(self, id: int, routine_save_in: SavedRoutineIn) -> Optional[SavedRoutineOut]:
        routine = await self.routine_repository.update(
            id=id,
            obj_data=Routine(
                syllabus_id=routine_save_in.syllabus_id,
                title=routine_save_in.title,
                description=routine_save_in.description,
                calendar_year=routine_save_in.calendar_year,
                is_active=routine_save_in.is_active,
                routine=json.loads(routine_save_in.routine)
            )
        )

        if routine is None:
            raise NotFoundException(detail="Routine doesn't found")

        return entity_to_model(entity=routine, model=SavedRoutineOut)
