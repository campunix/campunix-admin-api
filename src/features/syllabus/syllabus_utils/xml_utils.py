import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict, Any, List

from src.models.syllabus.syllabus_models import SyllabusParsed, Semester, Course, CourseDescription, Book


def parse_syllabus(root: ET.Element) -> SyllabusParsed:
    syllabus = SyllabusParsed(
        department_code=root.findtext("DepartmentCode"),
        department_name=root.findtext("DepartmentName"),
        semesters=[
            Semester(
                year=semester.get("year"),
                number=semester.get("number"),
                courses=[
                    Course(
                        course_code=course.findtext("CourseCode"),
                        title=course.findtext("Title"),
                        credit=course.findtext("Credit"),
                        prerequisite=course.findtext("Prerequisite"),
                        type=course.findtext("Type"),
                        contact_hours=course.findtext("ContactHours"),
                        rationale=course.findtext("Rationale"),
                        course_objectives=[
                            obj.text for obj in course.findall("CourseObjectives/Objective")
                        ],
                        outcomes=[
                            outcome.text for outcome in course.findall("StudentLearningOutcomes/Outcome")
                        ],
                        course_description=[
                            CourseDescription(
                                module=desc.findtext("Module"),
                                content=desc.findtext("Content")
                            ) for desc in course.findall("CourseDescription")
                        ],
                        recommended_books=[
                            Book(
                                title=book.findtext("Title"),
                                author=book.findtext("Author"),
                                publisher=book.findtext("Publisher"),
                                year=book.findtext("Year")
                            ) for book in course.findall("RecommendedBooks/Book")
                        ],
                        hardware_software_requirements={
                            "HW": course.findtext("HardwareSoftwareRequirements/HW"),
                            "SW": course.findtext("HardwareSoftwareRequirements/SW")
                        }

                    ) for course in semester.findall("Courses/Course")
                ]
            ) for semester in root.findall("Semesters/Semester")
        ]
    )

    return syllabus


def create_template(
        department_code: str,
        department_name: str,
        semesters_list: List[Any],
) -> Any:
    version = datetime.now().strftime("%d/%m/%Y")

    syllabus = ET.Element("Syllabus", version=version)

    department_code_element = ET.SubElement(syllabus, "DepartmentCode")
    department_code_element.text = department_code

    department_name_element = ET.SubElement(syllabus, "DepartmentName")
    department_name_element.text = department_name
    semesters_element = ET.SubElement(syllabus, "Semesters")

    for semester in semesters_list:
        if not semester.disabled:
            semester_element = ET.SubElement(
                semesters_element,
                "Semester",
                year=str(semester.year),
                number=str(semester.number),
            )

            courses_element = ET.SubElement(semester_element, "Courses")

            add_course(
                courses_element,
                course_code="Add Course Code",
                title="Add Course title here",
                credit="Add total credits here",
                prerequisite="Add prerequisite here",
                course_type="THEORY/LAB/VIVA (👈 Add one of these)",
                contact_hours="Add contact hours here",
                rationale="Add rationales here",
                objectives=["Example objective 1", "Example objective 2"],
                outcomes=["Add outcome here"],
                modules={
                    "Example module title": "Example module details",
                },
                books=[
                    {
                        "title": "Example title",
                        "author": "Example Author",
                        "publisher": "Example Publisher",
                        "year": "DD/MM/YYYY (👈 Use this date format)"
                    },
                ]
            )

    return ET.tostring(syllabus, encoding="utf-8", xml_declaration=True).decode("utf-8")


# Helper function to add a course
def add_course(courses, course_code, title, credit, prerequisite, course_type, contact_hours, rationale, objectives,
               outcomes,
               modules, books):
    course = ET.SubElement(courses, "Course")

    ET.SubElement(course, "CourseCode").text = course_code
    ET.SubElement(course, "Title").text = title
    ET.SubElement(course, "Credit").text = credit
    ET.SubElement(course, "Prerequisite").text = prerequisite
    ET.SubElement(course, "Type").text = course_type
    ET.SubElement(course, "ContactHours").text = contact_hours

    # Rationale
    rationale_elem = ET.SubElement(course, "Rationale")
    rationale_elem.text = rationale

    # Course Objectives
    course_objectives = ET.SubElement(course, "CourseObjectives")
    for obj in objectives:
        objective = ET.SubElement(course_objectives, "Objective")
        objective.text = obj

    # Student Learning Outcomes
    slo = ET.SubElement(course, "StudentLearningOutcomes")
    for outcome in outcomes:
        outcome_elem = ET.SubElement(slo, "Outcome")
        outcome_elem.text = outcome

    # Course Description with Modules and Content
    description = ET.SubElement(course, "CourseDescription")
    for module, content in modules.items():
        module_elem = ET.SubElement(description, "Module")
        module_elem.text = module
        content_elem = ET.SubElement(description, "Content")
        content_elem.text = content

    # Recommended Books
    recommended_books = ET.SubElement(course, "RecommendedBooks")
    for book in books:
        book_elem = ET.SubElement(recommended_books, "Book")
        ET.SubElement(book_elem, "Title").text = book["title"]
        ET.SubElement(book_elem, "Author").text = book["author"]
        ET.SubElement(book_elem, "Publisher").text = book["publisher"]
        ET.SubElement(book_elem, "Year").text = book["year"]
