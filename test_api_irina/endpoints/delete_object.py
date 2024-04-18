import requests


class DeleteObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def delete_object(self, object_id):
        url = f"{self.base_url}/objects/{object_id}"
        response = requests.delete(url)
        assert response.status_code == 200, f"Failed to delete object. Status code: {response.status_code}"
        return response
