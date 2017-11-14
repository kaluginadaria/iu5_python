import baseclass
import requests


class GetId(baseclass.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = "users.get"

    def _get_data(self, name):
        response = requests.get(GetId.BASE_URL + GetId.method + '?user_ids=' + name).json()

        if 'error' in response:
            print('error in user id or smth else, try again')
            raise SystemExit

        return response

    def response_handler(self, response):
        id = response["response"][0]["uid"]
        return id

    def execute(self, name):
        response = self._get_data(
            name,

        )
        return self.response_handler(
            response,

        )
