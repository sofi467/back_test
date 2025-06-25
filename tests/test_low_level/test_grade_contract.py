import random
import requests.status_codes
from faker import Faker

from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.teacher.base_teacher import DegreeEnum
from services.university.models.student.base_student import DegreeEnumStudent
from services.university.models.student.student_reguest import StudentRequest
from services.university.models.teacher.teacher_request import TeacherRequest
from services.university.models.group.group_request import GroupRequest

faker = Faker()


class TestGradeContract:
    def test_get_grade_with_stats(self, university_api_utils_admin):
        group_data = GroupRequest(name=faker.name())
        group = GroupHelper(university_api_utils_admin)
        group_response = group.post_group(json=group_data.model_dump())

        student_data = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice(list(DegreeEnumStudent)),
            phone=faker.numerify("+7##########"),
            group_id=group_response.json()["id"])
        student = StudentHelper(university_api_utils_admin)
        student_response = student.post_student(json=student_data.model_dump())

        teacher_data = TeacherRequest(first_name=faker.first_name(),
                                      last_name=faker.last_name(),
                                      subject=random.choice([sub for sub in DegreeEnum]))
        teacher = TeacherHelper(university_api_utils_admin)
        teacher_response = teacher.post_teacher(json=teacher_data.model_dump())

        grade = GradeHelper(university_api_utils_admin)
        grade_response = grade.get_grade_stats(params={"student_id": student_response.json()["id"],
                                                       "teacher_id": teacher_response.json()["id"],
                                                       "group_id": group_response.json()["id"],
                                                       })

        assert grade_response.status_code == \
               requests.status_codes.codes.ok, \
            f"Wrong status code. Actual: {grade_response.status_code}," \
            f" but expected: {requests.status_codes.codes.ok}"
