from typing import Optional

from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.entities.teacher import Teacher
from src.features.admin.services.TeacherServiceContract import TeacherServiceContract
from src.models.teacher import TeacherOut, TeacherIn


class TeacherService(TeacherServiceContract):
    def __init__(
            self,
            teachers_repository: TeachersRepositoryContract,
    ):
        self.teachers_repository = teachers_repository

    async def create_teacher(self, teacher: TeacherIn) -> Optional[TeacherOut]:
        new_teacher = await self.teachers_repository.create(
            Teacher(

            )
        )
        pass

    async def get_teachers(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.teachers_repository.get_all()

    async def update_teacher(self, id: int, teacher: TeacherIn) -> Optional[TeacherOut]:
        pass

    async def delete_teacher(self, id: int) -> bool:
        return await self.teachers_repository.delete(id)

    async def get_teacher_by_id(self, id: int) -> Optional[TeacherOut]:
        return await self.teachers_repository.get_by_id(id)
