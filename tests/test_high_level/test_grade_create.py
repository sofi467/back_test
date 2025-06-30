from faker import Faker
import random

from services.university.models.student.base_student import DegreeEnumStudent
from services.university.models.teacher.base_teacher import DegreeEnum
from services.university.university_service import UniversityService
from services.university.models.group.group_request import GroupRequest
from services.university.models.student.student_reguest import StudentRequest
from services.university.models.teacher.teacher_request import TeacherRequest
from services.university.models.grade.grade_request import GradeRequest
from services.constans import GRADE_MAX, GRADE_MIN

faker = Faker()


class TestGradeCreate:
    def test_create_grade(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        student = StudentRequest(first_name=faker.name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in DegreeEnumStudent]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)

        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([sub for sub in DegreeEnum]))
        teacher_response = university_service.create_teacher(teacher_request=teacher)

        grade_request = GradeRequest(teacher_id=teacher_response.id,
                                     student_id=student_response.id,
                                     grade = random.randint(GRADE_MIN, GRADE_MAX))
        grade_response = university_service.create_grade(grade_request)

        assert student_response.id == grade_response.student_id, \
            f"Wrong status code. Actual: {student_response.id}," \
            f" but expected: {grade_response.student_id}"
