from .base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):
    def patch_object(self, object_id, data):
        self.response = self.patch("objects", object_id, data)
        self.check_patched_data()

    def check_patched_data(self):
        response_json = self.response.json()
        assert response_json["data"]["attribute2"] == "patched_value2", "attribute2 was not patched"
