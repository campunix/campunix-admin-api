import xml.etree.ElementTree as ET
from typing import Dict, Any, List

from src.models.syllabus.syllabus_models import SyllabusParsed, Semester, Course, CourseDescription, Book


def parse_syllabus(root: ET.Element) -> SyllabusParsed:
    syllabus = SyllabusParsed(
        department_code=root.findtext("DepartmentCode"),
        department_name=root.findtext("DepartmentName"),
        semesters=[
            Semester(
                year=semester.get("year"),
                number = semester.get("number"),
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
                                Module=desc.findtext("Module"),
                                Content=desc.findtext("Content")
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


def create_template(department_id: int, semesters: List[Any], courses: List[Any],
                    filename="syllabus_template.xml") -> str:
    # Create the root element
    syllabus = ET.Element("Syllabus")

    # Department information
    department_id = ET.SubElement(syllabus, "DepartmentID")
    department_id.text = "1"  # Placeholder for Department ID

    department_code = ET.SubElement(syllabus, "DepartmentCode")
    department_code.text = "CSE"  # Placeholder for Department Code

    department_name = ET.SubElement(syllabus, "DepartmentName")
    department_name.text = "Computer Science and Engineering"
    semester = ET.SubElement(syllabus, "Semester")
    semester.text = "1"
    courses = ET.SubElement(syllabus, "Courses")

    add_course(
        courses,
        course_code=" ",
        title=" ",
        credit=" ",
        prerequisite=" ",
        course_type=" ",
        contact_hours=" ",
        rationale=" ",
        objectives=[
            # "Understand basic software design principles"
        ],
        outcomes=[
            # "Familiarize with algorithms and programming structure"
        ],
        modules={
            # "Structured Programming Language fundamentals": "C, Keywords, History and Features, Basic Structure",
        },
        books=[
            # {"title": "Teach Yourself C", "author": "Herbert Schildt", "publisher": "McGraw-Hill", "year": "1997"}
        ]
    )

    # Generate the XML tree and save to file
    # tree = ET.ElementTree(syllabus)
    # with open(filename, "wb") as file:
    # tree.write(file, encoding="utf-8", xml_declaration=True)

    # Generate the XML tree and return as string
    xml_string = ET.tostring(syllabus, encoding="utf-8", xml_declaration=True).decode("utf-8")
    return xml_string  # Return the XML string


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
