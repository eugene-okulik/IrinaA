from .base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)

    def delete_object(self, object_id):
        response = self.delete("objects", object_id)
        assert response.status_code == 200, f"Failed to delete data. Status code: {response.status_code}"
        return response
