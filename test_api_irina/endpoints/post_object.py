from .base_endpoint import BaseEndpoint


class PostObject(BaseEndpoint):
    def post_object(self, data):
        self.response = self.post("objects", data)
        self.check_id_in_response()

    def check_id_in_response(self):
        assert 'id' in self.response.json(), "ID not found in response"
