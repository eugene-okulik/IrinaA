import requests


class BaseEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url
        self.response = None

    def post(self, path, data):
        url = f"{self.base_url}/{path}"
        self.response = requests.post(url, json=data)
        self.check_status_is_200()
        return self.response

    def put(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        self.response = requests.put(url, json=data)
        self.check_status_is_200()
        return self.response

    def patch(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        self.response = requests.patch(url, json=data)
        self.check_status_is_200()
        return self.response

    def delete(self, path, object_id):
        url = f"{self.base_url}/{path}/{object_id}"
        self.response = requests.delete(url)
        self.check_status_is_200()
        return self.response

    def get(self, path, object_id):
        url = f"{self.base_url}/{path}/{object_id}"
        self.response = requests.get(url)
        self.check_status_is_200()
        return self.response

    def check_status_is_200(self):
        assert self.response.status_code == 200, f"Failed request. Status code: {self.response.status_code}"
