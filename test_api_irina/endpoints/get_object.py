from .base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_object(self, object_id):
        return self.get("objects", object_id)
