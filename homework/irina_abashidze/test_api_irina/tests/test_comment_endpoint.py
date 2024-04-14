import pytest
from endpoints.comment_endpoint import CommentEndpoint
from utils.api_client import send_request


class TestCommentEndpoint:
    base_url = "https://api.restful-api.dev/objects"
    comment_endpoint = CommentEndpoint(base_url)

    @pytest.mark.parametrize("comment_id", [1, 2, 3])
    def test_get_comment(self, comment_id):
        comment = self.comment_endpoint.get_comment(comment_id)
        assert comment["id"] == comment_id

    def test_create_comment(self):
        comment_data = {"post_id": 1, "name": "New Comment", "body": "This is a new comment"}
        new_comment = self.comment_endpoint.create_comment(comment_data)
        assert new_comment["name"] == "New Comment"

    def test_delete_comment(self):
        # Создаем временный комментарий для последующего удаления
        comment_data = {"post_id": 1, "name": "Temporary Comment", "body": "This is a temporary comment"}
        response = send_request("POST", f"{self.base_url}/comments", json=comment_data)
        assert response.status_code == 201
        comment_id = response.json()["id"]

        # Удаляем созданный комментарий
        delete_response = self.comment_endpoint.delete_comment(comment_id)
        assert delete_response.status_code == 200
