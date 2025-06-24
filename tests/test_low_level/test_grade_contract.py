import random
import requests.status_codes
from faker import Faker

from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.teacher.base_teacher import DegreeEnum
from services.university.models.student.base_student import DegreeEnumStudent

faker = Faker()


class TestGradeContract:
    def test_get_grade_with_stats(self, university_api_utils_admin):
        group = GroupHelper(university_api_utils_admin)
        group_response = group.post_group(json={"name": faker.name()})

        student = StudentHelper(university_api_utils_admin)
        student_response = student.post_student(json={"first_name": faker.name(),
                                                      "last_name": faker.last_name(),
                                                      "email": faker.email(),
                                                      "degree": random.choice([option for option in DegreeEnumStudent]),
                                                      "phone": faker.numerify("+7##########"),
                                                      "group_id": group_response.json()["id"]})

        teacher = TeacherHelper(university_api_utils_admin)
        teacher_response = teacher.post_teacher(json={"first_name": faker.first_name(),
                                                      "last_name": faker.last_name(),
                                                      "subject": random.choice([sub for sub in DegreeEnum])})

        grade = GradeHelper(university_api_utils_admin)
        params = {"student_id": student_response.json()["id"],
                  "teacher_id": teacher_response.json()["id"],
                  "group_id": group_response.json()["id"],
                  }
        grade_response = grade.get_grade_stats(params=params)
        print("Request URL:", grade.api_utils.url + grade.STATS_ENDPOINT)
        print("Query params:", params)
        print("Response status:", grade_response.status_code)
        print("Response body:", grade_response.json())

        assert grade_response.status_code == \
               requests.status_codes.codes.ok, \
            f"Wrong status code. Actual: {grade_response.status_code}," \
            f" but expected: {requests.status_codes.codes.ok}"
