import requests


class PostObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def post_object(self, data):
        url = f"{self.base_url}/objects"
        response = requests.post(url, json=data)
        assert response.status_code == 200, f"Failed to create object. Status code: {response.status_code}"
        return response.json()
