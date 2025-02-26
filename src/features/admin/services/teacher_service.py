from typing import Optional, Dict, Any

from sqlalchemy import or_

from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.contracts.users_repository_contract import UsersRepositoryContract
from src.core.converters import entity_to_model, entity_to_model_list
from src.core.entities.enums.teacher_designation import TeacherDesignation
from src.core.entities.enums.teacher_status import TeacherStatus
from src.core.entities.teacher import Teacher
from src.core.entities.user import User
from src.core.exceptions.db_exceptions import DatabaseError
from src.core.exceptions.not_found_exception import NotFoundException
from src.core.exceptions.validation_exception import ValidationException
from src.features.admin.services.teacher_service_contract import TeacherServiceContract
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

        is_teacher = await self.teachers_repository.is_teacher(user_id=teacher.user_id)
        if is_teacher:
            raise ValidationException(detail="This user is already a teacher!")

        new_teacher = await self.teachers_repository.create(
            Teacher(
                user_id=teacher.user_id,
                department_id=teacher.department_id,
                designation=TeacherDesignation.from_str(teacher.designation),
                status=TeacherStatus.from_str(teacher.status)
            )
        )

        if not new_teacher:
            raise DatabaseError()

        teacher_out = TeacherOut(
            id=new_teacher.id,
            full_name=user.full_name,
            email=user.email,
            designation=new_teacher.designation,
            status=new_teacher.status
        )

        return entity_to_model(entity=teacher_out, model=TeacherOut)

    async def get_teachers(self, page: int = 1, page_size: int = 10, paginate: bool = False, search_query: Optional[str] = None):

        columns = [
            Teacher.id,
            User.full_name,
            User.email,
            Teacher.designation,
            Teacher.status
        ]

        filters = []

        if search_query:
            filters.append(
                or_(
                    User.full_name.ilike(f"%{search_query}%"),
                    User.email.ilike(f"%{search_query}%")
                )
            )

        teacher_dict = await self.teachers_repository.get_all(
            page=page,
            page_size=page_size,
            paginate=paginate,
            filters=filters,
            joins=[(User, Teacher.user_id == User.id)],
            columns=columns
        )
        return entity_to_model_list(entity_dict=teacher_dict, model=TeacherOut, paginate=paginate)

    async def update_teacher(self, id: int, teacher: TeacherIn) -> Optional[TeacherOut]:
        user = await self.users_repository.get_user_by_id(user_id=teacher.user_id)

        if not user:
            raise NotFoundException(detail='User not found')

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
            raise NotFoundException(detail='Teacher not found')

        return TeacherOut(
            id=new_teacher.id,
            full_name=user.full_name,
            email=user.email,
            designation=new_teacher.designation,
            status=new_teacher.status
        )

    async def delete_teacher(self, id: int) -> bool:
        res = await self.teachers_repository.delete(id)

        if res is False:
            raise NotFoundException(detail="Deletion unsuccessful")

        return res

    async def get_teacher_by_id(self, id: int) -> Optional[TeacherOut]:
        teacher = await self.teachers_repository.get_by_id(
            id,
            joins=[(User, Teacher.user_id == User.id)]
        )
        if not teacher:
            raise NotFoundException(detail="Teacher not found")

        user = await self.users_repository.get_user_by_id(user_id=teacher.user_id)
        if not user:
            raise NotFoundException(detail="User not found")

        return TeacherOut(
            id=teacher.id,
            full_name=user.full_name,
            email=user.email,
            designation=teacher.designation,
            status=teacher.status
        )

    async def get_teacher_designation(self) -> Dict[str, Any]:
        teacher_designations = await self.teachers_repository.get_teacher_designation()

        if not teacher_designations:
            raise NotFoundException()

        return teacher_designations

    async def get_teacher_status(self) -> Dict[str, Any]:
        teacher_designations = await self.teachers_repository.get_teacher_status()

        if not teacher_designations:
            raise NotFoundException()

        return teacher_designations
