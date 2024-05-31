from .base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    def delete_object(self, object_id):
        self.response = self.delete("objects", object_id)
