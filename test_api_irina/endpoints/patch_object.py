from .base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def patch_object(self, object_id, data):
        return self.patch("objects", object_id, data)
