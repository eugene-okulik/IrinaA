import requests


class GetObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_object(self, object_id):
        url = f"{self.base_url}/objects/{object_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Failed to get object. Status code: {response.status_code}"
        return response.json()
