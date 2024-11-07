from http.client import HTTPException

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status, File, UploadFile

from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_container import SyllabusContainer

router = APIRouter(prefix="/syllabus")


@router.post("/save", status_code=status.HTTP_201_CREATED, summary="Save Syllabus")
@inject
async def save(
        file: UploadFile = File(...),
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    if not file.filename.endswith(".xml"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only XML files are allowed.")

    syllabus_parsed = await syllabus_service.save(file)
    return syllabus_parsed


@router.get("/getByDeptID", summary="Get department wise syllabus")
@inject
async def getByDepartmentID(
        department_id: int = None,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    course = await syllabus_service.getByDepartmentID(department_id)
    return course


@router.get("/getBySemesterCode", summary="Get semester wise syllabus")
@inject
async def getByDeptIDAndSemesterCode(
        department_id: int = None,
        semester_code: int = None,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    syllabus = await syllabus_service.getByDeptIDAndSemesterCode(department_id, semester_code)
    return syllabus


@router.put("/updateSyllabus", summary="Update syllabus details")
@inject
async def updateSyllabus(
        department_id: int,
        semester_code: int,
        course_code: str,
        course_type: str,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    updated_syllabus = await syllabus_service.updateSyllabus(
        department_id=department_id,
        semester_code=semester_code,
        course_code=course_code,
        course_type=course_type
    )

    if not updated_syllabus:
        raise HTTPException(status_code=404, detail="Syllabus not found")

    return updated_syllabus


@router.get("/template", summary="Get syllabus template xml file")
@inject
async def template(
        department_id: int = None,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    syllabus_template = await syllabus_service.template(department_id)
    return syllabus_template
