from typing import Optional

from src.core.contracts.preferences_repository_contract import PreferencesRepositoryContract
from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.converters import entity_to_model
from src.core.entities.enums.day import Day
from src.core.entities.preference import Preference
from src.core.exceptions.duplicate_exception import DuplicateException
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.PreferenceServiceContract import PreferenceServiceContract
from src.models.preference import PreferenceIn, PreferenceOut
from src.models.teacher import TeacherOut


class PreferenceService(PreferenceServiceContract):
    def __init__(
            self,
            preferences_repository: PreferencesRepositoryContract,
            teachers_repository: TeachersRepositoryContract
    ):
        self.preferences_repository = preferences_repository
        self.teachers_repository = teachers_repository

    async def create_preference(self, preference: PreferenceIn) -> Optional[TeacherOut]:
        teacher = await self.teachers_repository.get_by_id(id=preference.teacher_id)

        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        preference = await self.preferences_repository.create(
            Preference(
                teacher_id=teacher.id,
                day=Day.to_str(preference.day),
                slot_no=preference.slot_no
            )
        )

        if not preference:
            raise DuplicateException(detail="Preference already exist")

        preference_out = PreferenceOut(
            teacher_id=preference.teacher_id,
            day=preference.day.value,
            slot_no=preference.slot_no
        )

        return entity_to_model(entity=preference_out, model=PreferenceOut)

    async def get_preferences(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.preferences_repository.get_all()

    async def update_preference(self, id: int, preference: PreferenceIn) -> Optional[PreferenceOut]:
        teacher = await self.preferences_repository.get_by_id(id=id)

        if not teacher:
            raise NotFoundException(detail='Teacher not found')

        new_preference = await self.preferences_repository.update(
            id,
            Preference(
                teacher_id=preference.teacher_id,
                day=Day.to_str(preference.day),
                slot_no=preference.slot_no
            )
        )

        if not new_preference:
            raise NotFoundException(detail='Preference not found')

        return PreferenceOut(
            teacher_id=new_preference.teacher_id,
            day=Day.from_str(new_preference.day),
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

        return PreferenceOut(
            teacher_id=preference.teacher_id,
            day=preference.day.value,
            slot_no=preference.slot_no
        )
