from typing import Optional

from src.core.contracts.semesters_repository_contract import SemestersRepositoryContract
from src.core.entities.semester import Semester
from src.features.admin.services.semester_service_contract import SemesterServiceContract
from src.models.semester import SemesterOut, SemesterIn


class SemesterService(SemesterServiceContract):
    def __init__(
            self,
            semester_repository: SemestersRepositoryContract,
    ):
        self.semester_repository = semester_repository

    async def create_semester(self, semester: SemesterIn) -> Optional[SemesterOut]:
        new_semester = await self.semester_repository.create(
            Semester(
                year=semester.year,
                number=semester.number,
                department_id=semester.department_id
            )
        )
        return SemesterOut(id=new_semester.id, year=new_semester.year, number=new_semester.number)

    async def get_semesters(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.semester_repository.get_all()

    async def update_semester(self, id: int, semester: SemesterIn) -> Optional[SemesterOut]:
        new_semester = await self.semester_repository.update(
            id,
            Semester(
                year=semester.year,
                number=semester.number,
                department_id=semester.department_id
            )
        )
        return SemesterOut(id=new_semester.id, year=new_semester.year, number=new_semester.number)

    async def delete_semester(self, id: int) -> bool:
        return await self.semester_repository.delete(id)

    async def get_semester_by_id(self, id: int) -> Optional[SemesterOut]:
        return await self.semester_repository.get_by_id(id)
