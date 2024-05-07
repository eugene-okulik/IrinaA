from .base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def put_object(self, object_id, data):
        return self.put("objects", object_id, data)
