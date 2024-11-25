from abc import abstractmethod, ABC
from typing import Optional, List

from src.models.course import CourseIn, CourseOut


class CourseServiceContract(ABC):
    @abstractmethod
    async def create_course(self, course: CourseIn) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def get_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        pass

    @abstractmethod
    async def update_course(self, id: int, course: CourseIn) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def delete_course(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_course_by_id(self, id: int) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def get_course_by_course_code(self, department_id: int, course_code: str) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def bulk_insert_courses(self, courses_in: List[CourseIn]):
        pass
