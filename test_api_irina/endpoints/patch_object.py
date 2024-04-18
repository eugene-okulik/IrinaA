import requests


class PatchObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def patch_object(self, object_id, data):
        url = f"{self.base_url}/objects/{object_id}"
        response = requests.patch(url, json=data)
        assert response.status_code == 200, f"Failed to patch object. Status code: {response.status_code}"
        return response.json()
