import pytest
from test_api_abashidze.endpoints.user_endpoint import UserEndpoint
from test_api_abashidze.tests.base_test import BaseTest


class TestUserEndpoint(BaseTest):
    @pytest.fixture(scope="session")
    def base_url(self):
        return "https://api.restful-api.dev"

    def test_get_user(self, base_url):
        user_endpoint = UserEndpoint(base_url)
        user = user_endpoint.get_user(1)
        assert user["id"] == 1

    def test_create_user(self, base_url):
        user_endpoint = UserEndpoint(base_url)
        new_user_data = {"name": "John Doe", "email": "john@example.com"}
        new_user = user_endpoint.create_user(new_user_data)
        assert "id" in new_user

    def test_update_user(self, base_url):
        user_endpoint = UserEndpoint(base_url)
        user_id = 1
        updated_data = {"name": "Updated Name", "email": "updated_email@example.com"}
        updated_user = user_endpoint.update_user(user_id, updated_data)
        assert updated_user["name"] == "Updated Name"
        assert updated_user["email"] == "updated_email@example.com"

    def test_delete_user(self, base_url):
        user_endpoint = UserEndpoint(base_url)
        user_id = 1
        response_status_code = user_endpoint.delete_user(user_id)
        assert response_status_code == 204
