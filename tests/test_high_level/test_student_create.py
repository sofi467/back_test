import random

from faker import Faker

from services.university.models.group.group_request import GroupRequest
from services.university.models.student.student_reguest import StudentRequest
from services.university.university_service import UniversityService
from services.university.models.student.base_student import DegreeEnumStudent

faker = Faker()


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
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

        assert student_response.group_id == group_response.id, \
            (f"Wrong group id. Actual: '{student_response.group_id}', "
             f"but excepted: '{group_response.id}'")
