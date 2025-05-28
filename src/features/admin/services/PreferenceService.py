from typing import Optional, Dict, Any

from sqlmodel import or_

from src.core.contracts.preferences_repository_contract import PreferencesRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.enums.day import Day
from src.core.entities.preference import Preference
from src.core.entities.teacher import Teacher
from src.core.entities.user import User
from src.core.exceptions.duplicate_exception import DuplicateException
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.PreferenceServiceContract import PreferenceServiceContract
from src.features.admin.services.teacher_service_contract import TeacherServiceContract
from src.models.preference import PreferenceIn, PreferenceOut
from src.models.teacher import TeacherOut


class PreferenceService(PreferenceServiceContract):
    def __init__(
            self,
            preferences_repository: PreferencesRepositoryContract,
            teacher_service: TeacherServiceContract
    ):
        self.preferences_repository = preferences_repository
        self.teacher_service = teacher_service

    async def create_preference(self, preference: PreferenceIn) -> Optional[TeacherOut]:
        teacher = await self.teacher_service.get_teacher_by_id(preference.teacher_id)

        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        # Check if both day and slot_no are None
        if preference.day is None and preference.slot_no is None:
            raise ValueError("At least one of 'day' or 'slot_no' must be provided.")

        new_preference = await self.preferences_repository.create(
            Preference(
                teacher_id=preference.teacher_id,
                day=preference.day,
                slot_no=preference.slot_no
            )
        )

        if not preference:
            raise DuplicateException(detail="Preference already exist")

        preference_out = PreferenceOut(
            id=new_preference.id,
            teacher_id=teacher.id,
            teacher_name=teacher.full_name,
            day=preference.day,
            slot_no=preference.slot_no
        )

        return entity_to_model(entity=preference_out, model=PreferenceOut)

    async def get_preferences(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                              search_query: Optional[str] = None, ):

        filters = []

        if search_query:
            filters.append(
                or_(
                    User.full_name.ilike(f"%{search_query}%")
                )
            )

        columns = [
            Preference.id,
            Teacher.id.label("teacher_id"),
            User.full_name.label("teacher_name"),
            Preference.day,
            Preference.slot_no
        ]

        preferences_dict = await self.preferences_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters,
            joins=[
                (Teacher, Preference.teacher_id == Teacher.id),
                (User, Teacher.user_id == User.id)
            ],
            columns=columns
        )

        if "items" in preferences_dict and isinstance(preferences_dict["items"], list):
            preferences_dict["items"] = [
                {**dict(item), "day": item["day"].name if isinstance(item["day"], Day) else item["day"]}
                for item in preferences_dict["items"]
            ]

        return entity_to_model_list(entity_dict=preferences_dict, model=PreferenceOut, paginate=paginate)

    async def get_preferences_by_teacher_id(self, teacher_id: int, page: int = 1, page_size: int = 10,
                                            paginate: bool = False,
                                            search_query: Optional[str] = None, ):

        filters = []

        if teacher_id:
            filters.append(Teacher.id == teacher_id)

        if search_query:
            filters.append(
                or_(
                    User.full_name.ilike(f"%{search_query}%")
                )
            )

        columns = [
            Preference.id,
            Teacher.id.label("teacher_id"),
            User.full_name.label("teacher_name"),
            Preference.day,
            Preference.slot_no
        ]

        preferences_dict = await self.preferences_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters,
            joins=[
                (Teacher, Preference.teacher_id == Teacher.id),
                (User, Teacher.user_id == User.id)
            ],
            columns=columns
        )

        if "items" in preferences_dict and isinstance(preferences_dict["items"], list):
            preferences_dict["items"] = [
                {**dict(item), "day": item["day"].name if isinstance(item["day"], Day) else item["day"]}
                for item in preferences_dict["items"]
            ]

        return entity_to_model_list(entity_dict=preferences_dict, model=PreferenceOut, paginate=paginate)

    async def update_preference(self, id: int, preference: PreferenceIn) -> Optional[PreferenceOut]:
        teacher = await self.teacher_service.get_teacher_by_id(preference.teacher_id)

        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        new_preference = await self.preferences_repository.update(
            id,
            Preference(
                teacher_id=preference.teacher_id,
                day=preference.day,
                slot_no=preference.slot_no
            )
        )

        if not new_preference:
            raise NotFoundException(detail='Preference not found')

        return PreferenceOut(
            id=new_preference.id,
            teacher_id=teacher.id,
            teacher_name=teacher.full_name,
            day=new_preference.day,
            slot_no=new_preference.slot_no
        )

    async def delete_preference(self, id: int) -> bool:
        res = await self.preferences_repository.delete(id)

        if res is False:
            raise NotFoundException(detail="Deletion unsuccessful")

        return res

    async def get_preference_by_id(self, id: int) -> Optional[PreferenceOut]:
        preference = await self.preferences_repository.get_by_id(id=id)

        if not preference:
            raise NotFoundException(detail="Preference not found")

        teacher = await self.teacher_service.get_teacher_by_id(preference.teacher_id)

        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        return PreferenceOut(
            id=preference.id,
            teacher_id=teacher.id,
            teacher_name=teacher.full_name,
            department_id=teacher.department.id,
            day=preference.day.name if preference.day is not None else None,
            slot_no=preference.slot_no if preference.slot_no is not None else None
        )

    async def get_days(self) -> Dict[str, Any]:
        course_types = await self.preferences_repository.get_days()

        if not course_types:
            raise NotFoundException()

        return course_types
