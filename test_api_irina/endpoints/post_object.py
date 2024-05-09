from .base_endpoint import BaseEndpoint


class PostObject(BaseEndpoint):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.response = None

    def post_object(self, data):
        self.response = self.post("objects", data)
        return self.response

    def check_status_is_200(self):
        assert self.response.status_code == 200, f"Failed to post data. Status code: {self.response.status_code}"

    def check_id_in_response(self):
        assert 'id' in self.response.json(), "ID not found in response"
