from .base_endpoint import BaseEndpoint


class PostObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def post_object(self, data):
        return self.post("objects", data)
