from typing import Optional

from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.entities.enums.teacher_designation import TeacherDesignation
from src.core.entities.enums.teacher_status import TeacherStatus
from src.core.entities.teacher import Teacher
from src.core.exceptions.duplicate_exception import DuplicateException
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.TeacherServiceContract import TeacherServiceContract
from src.models.teacher import TeacherOut, TeacherIn


class TeacherService(TeacherServiceContract):
    def __init__(
            self,
            teachers_repository: TeachersRepositoryContract,
            users_repository: UsersRepositoryContract,
    ):
        self.teachers_repository = teachers_repository
        self.users_repository = users_repository

    async def create_teacher(self, teacher: TeacherIn) -> Optional[TeacherOut]:
        user = await self.users_repository.get_user_by_id(user_id=teacher.user_id)

        if not user:
            raise NotFoundException(detail="User not found")

        new_teacher = await self.teachers_repository.create(
            Teacher(
                user_id=teacher.user_id,
                department_id=teacher.department_id,
                designation=TeacherDesignation.from_str(teacher.designation),
                status=TeacherStatus.from_str(teacher.status)
            )
        )

        if not new_teacher:
            raise DuplicateException(detail="Teacher already exist")

        return TeacherOut(
            id=new_teacher.id,
            name=user.full_name,
            email=user.email,
            designation=new_teacher.designation,
            status=new_teacher.status
        )

    async def get_teachers(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.teachers_repository.get_all()

    async def update_teacher(self, id: int, teacher: TeacherIn) -> Optional[TeacherOut]:
        user = await self.users_repository.get_user_by_id(user_id=teacher.user_id)

        if not user:
            raise NotFoundException

        new_teacher = await self.teachers_repository.update(
            id,
            Teacher(
                user_id=teacher.user_id,
                department_id=teacher.department_id,
                designation=TeacherDesignation.from_str(teacher.designation),
                status=TeacherStatus.from_str(teacher.status)
            )
        )

        if not new_teacher:
            raise NotFoundException

        return TeacherOut(
            id=new_teacher.id,
            name=user.full_name,
            email=user.email,
            designation=new_teacher.designation,
            status=new_teacher.status
        )

    async def delete_teacher(self, id: int) -> bool:
        return await self.teachers_repository.delete(id)

    async def get_teacher_by_id(self, id: int) -> Optional[TeacherOut]:
        teacher = await self.teachers_repository.get_by_id(id)
        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        user = await self.users_repository.get_user_by_id(user_id=teacher.user_id)
        if not user:
            raise NotFoundException(detail="User not found")

        return TeacherOut(
            id=teacher.id,
            name=user.full_name,
            email=user.email,
            designation=teacher.designation,
            status=teacher.status
        )
