import requests


class PutObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def put_object(self, object_id, data):
        url = f"{self.base_url}/objects/{object_id}"
        response = requests.put(url, json=data)
        assert response.status_code == 200, f"Failed to update object. Status code: {response.status_code}"
        return response.json()
