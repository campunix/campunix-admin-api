from abc import abstractmethod, ABC
from typing import Optional, List, Dict, Any

from src.models.course import CourseIn, CourseOut


class CourseServiceContract(ABC):
    @abstractmethod
    async def create_course(self, course: CourseIn) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def get_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                          search_query: Optional[str] = None, department_id: Optional[int] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_courses_by_teacher_id(self, teacher_id: int, page: int = 1, page_size: int = 10,
                                        paginate: bool = False,
                                        search_query: Optional[str] = None) -> Dict[str, Any]:
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

    @abstractmethod
    async def get_course_types(self) -> Optional[Dict[str, Any]]:
        pass
