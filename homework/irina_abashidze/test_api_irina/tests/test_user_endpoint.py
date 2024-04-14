import pytest
from endpoints.user_endpoint import UserEndpoint
from utils.api_client import send_request


class TestUserEndpoint:
    base_url = "https://api.restful-api.dev/objects"
    user_endpoint = UserEndpoint(base_url)

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_user(self, user_id):
        user = self.user_endpoint.get_user(user_id)
        assert user["id"] == user_id

    def test_create_user(self):
        user_data = {"name": "John Doe", "email": "john@example.com"}
        new_user = self.user_endpoint.create_user(user_data)
        assert new_user["name"] == "John Doe"

    def test_delete_user(self):
        # Создаем временного пользователя для последующего удаления
        user_data = {"name": "Temporary User", "email": "temporary@example.com"}
        response = send_request("POST", f"{self.base_url}/users", json=user_data)
        assert response.status_code == 201
        user_id = response.json()["id"]

        # Удаляем созданного пользователя
        delete_response = self.user_endpoint.delete_user(user_id)
        assert delete_response.status_code == 200
