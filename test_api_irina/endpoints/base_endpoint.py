import requests


class BaseEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, object_id):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.get(url)
        return response.json()

    def post(self, path, data):
        url = f"{self.base_url}/{path}"
        response = requests.post(url, json=data)
        return response.json()

    def put(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.put(url, json=data)
        return response.json()

    def patch(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.patch(url, json=data)
        return response.json()

    def delete(self, path, object_id):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.delete(url)
        return response
