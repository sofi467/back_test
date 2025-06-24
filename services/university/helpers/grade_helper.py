import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grade(self, param) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, param)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT + str(grade_id))
        return response

    def put_grade(self, grade_id: int, data: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT + str(grade_id), data=data)
        return response

    def get_grade_stats(self, params: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response
