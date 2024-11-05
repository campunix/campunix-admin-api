from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.teacher_course_service_contract import TeacherCourseServiceContract
from src.models.teacher_course import TeacherCourseIn

teacher_course_router = APIRouter(prefix="/teacherCourse")


@teacher_course_router.post("")
@inject
async def create_teacher_course(
        teacher_course_in: TeacherCourseIn,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    teacher = await teacher_course_service.create_teacher_course(teacher_course_in)
    return teacher


@teacher_course_router.get("")
@inject
async def get_all_course_teacher(
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    return await teacher_course_service.get_teacher_courses()


@teacher_course_router.get("/{id}")
@inject
async def get_teacher_course(
        id: int,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    return await teacher_course_service.get_teacher_course_by_id(id)


@teacher_course_router.put("/{id}")
@inject
async def update_teacher_course(
        id: int,
        teacher_course_in: TeacherCourseIn,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    teacher = await teacher_course_service.update_teacher_course(id, teacher_course_in)
    return teacher


@teacher_course_router.delete("/{id}")
@inject
async def delete_teacher_course(
        id: int,
        teacher_course_service: TeacherCourseServiceContract = Depends(Provide[AdminContainer.teacher_course_service]),
):
    status = await teacher_course_service.delete_teacher_course(id)
    return status
