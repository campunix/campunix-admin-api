from http.client import HTTPException

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status, File, UploadFile

from src.features.auth.utils.oauth2_utils import oauth2_scheme
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_container import SyllabusContainer

router = APIRouter(prefix="/syllabus")


@router.post("", status_code=status.HTTP_201_CREATED, summary="Save Syllabus")
@inject
async def save(
        token: str = Depends(oauth2_scheme),
        file: UploadFile = File(...),
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    # Check if the uploaded file is an XML file
    if not file.filename.endswith(".xml"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only XML files are allowed.")

    syllabus = await syllabus_service.save(file)
    return syllabus


@router.get("/getByDeptID", summary="Get department wise syllabus")
@inject
async def getByDepartmentID(
        token: str = Depends(oauth2_scheme),
        department_id: int = None,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    course = await syllabus_service.getByDepartmentID(department_id)
    return course


@router.get("/getByCourseCode", summary="Get course wise syllabus")
@inject
async def getByDeptIDAndCourseCode(
        token: str = Depends(oauth2_scheme),
        department_id: int = None,
        course_code: str = None,
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    course = await syllabus_service.getByDeptIDAndCourseCode(department_id, course_code)
    return course

@router.get("/getSyllabus", summary="Get syllabus")
@inject
async def getSyllabus(
        syllabus_service: SyllabusServiceContract = Depends(Provide[SyllabusContainer.syllabus_service])
):
    print("start")
    await syllabus_service.getSyllabus()
    return 'hello'

