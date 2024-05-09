from .base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def patch_object(self, object_id, data):
        response = self.patch("objects", object_id, data)
        assert response.status_code == 200, f"Failed to patch data. Status code: {response.status_code}"
        return response.json()
