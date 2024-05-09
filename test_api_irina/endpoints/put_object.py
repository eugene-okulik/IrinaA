from .base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):

    def __init__(self, base_url):
        super().__init__(base_url)

    def put_object(self, object_id, data):
        response = self.put("objects", object_id, data)
        assert response.status_code == 200, f"Failed to put data. Status code: {response.status_code}"
        return response.json()
