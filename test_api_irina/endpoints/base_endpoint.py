import requests


class BaseEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path, data):
        url = f"{self.base_url}/{path}"
        response = requests.post(url, json=data)
        assert response.status_code == 200, f"Failed to post data. Status code: {response.status_code}"
        return response.json()

    def put(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.put(url, json=data)
        assert response.status_code == 200, f"Failed to put data. Status code: {response.status_code}"
        return response.json()

    def patch(self, path, object_id, data):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.patch(url, json=data)
        assert response.status_code == 200, f"Failed to patch data. Status code: {response.status_code}"
        return response.json()

    def delete(self, path, object_id):
        url = f"{self.base_url}/{path}/{object_id}"
        response = requests.delete(url)
        assert response.status_code == 200, f"Failed to delete data. Status code: {response.status_code}"
        return response
