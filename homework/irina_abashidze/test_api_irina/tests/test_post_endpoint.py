import pytest
from endpoints.post_endpoint import PostEndpoint
from utils.api_client import send_request


class TestPostEndpoint:
    base_url = "https://api.restful-api.dev/objects"
    post_endpoint = PostEndpoint(base_url)

    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post(self, post_id):
        post = self.post_endpoint.get_post(post_id)
        assert post["id"] == post_id

    def test_create_post(self):
        post_data = {"title": "New Post", "body": "This is a new post"}
        new_post = self.post_endpoint.create_post(post_data)
        assert new_post["title"] == "New Post"

    def test_delete_post(self):
        # Создаем временный пост для последующего удаления
        post_data = {"title": "Temporary Post", "body": "This is a temporary post"}
        response = send_request("POST", f"{self.base_url}/posts", json=post_data)
        assert response.status_code == 201
        post_id = response.json()["id"]

        # Удаляем созданный пост
        delete_response = self.post_endpoint.delete_post(post_id)
        assert delete_response.status_code == 200
