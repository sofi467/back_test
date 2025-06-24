import requests.status_codes

from services.university.helpers.group_helper import GroupHelper

from faker import Faker

faker = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(university_api_utils_anonym)
        group_response = group_helper.post_group(json={"name": faker.name()})

        assert group_response.status_code == \
               requests.status_codes.codes.unauthorized, \
            f"Wrong status code. Actual: {group_response.status_code}," \
            f" but expected: {requests.status_codes.codes.unauthorized}"
