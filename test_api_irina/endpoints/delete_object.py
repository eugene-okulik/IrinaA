from .base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def delete_object(self, object_id):
        return self.delete("objects", object_id)
