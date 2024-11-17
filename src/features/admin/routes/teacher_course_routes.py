from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.models.response import APIResponse
from src.models.teacher_course import TeacherCourseIn

teacher_course_router = APIRouter(prefix="/teacherCourse")


@teacher_course_router.post("")
@inject
async def create_teacher_course(
        teacher_course_in: TeacherCourseIn,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    teacher = await teacher_course_service.create_teacher_course(teacher_course_in)
    return APIResponse(code=HTTP_201_CREATED, message="Created successfully", data=teacher)


@teacher_course_router.get("")
@inject
async def get_all_course_teacher(
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    course_teachers = await teacher_course_service.get_teacher_courses()
    return APIResponse(data=course_teachers)


@teacher_course_router.get("/{id}")
@inject
async def get_teacher_course(
        id: int,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    teacher_courses = await teacher_course_service.get_teacher_course_by_id(id)
    return APIResponse(data=teacher_courses)


@teacher_course_router.put("/{id}")
@inject
async def update_teacher_course(
        id: int,
        teacher_course_in: TeacherCourseIn,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    teacher = await teacher_course_service.update_teacher_course(id, teacher_course_in)
    return APIResponse(message="Updated successfully", data=teacher)


@teacher_course_router.delete("/{id}")
@inject
async def delete_teacher_course(
        id: int,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    res = await teacher_course_service.delete_teacher_course(id)
    return APIResponse(status=res, message="Deleted successfully")
