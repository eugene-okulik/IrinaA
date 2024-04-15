import pytest
from test_api_abashidze.endpoints.post_endpoint import PostEndpoint
from test_api_abashidze.tests.base_test import BaseTest


class TestPostEndpoint(BaseTest):
    @pytest.fixture(scope="session")
    def base_url(self):
        return "https://api.restful-api.dev"

    def test_get_post(self, base_url):
        post_endpoint = PostEndpoint(base_url)
        post = post_endpoint.get_post(1)
        assert post["id"] == 1

    def test_create_post(self, base_url):
        post_endpoint = PostEndpoint(base_url)
        new_post_data = {"title": "New Post", "body": "This is a new post."}
        new_post = post_endpoint.create_post(new_post_data)
        assert new_post["title"] == "New Post"

    def test_update_post(self, base_url):
        post_endpoint = PostEndpoint(base_url)
        updated_post_data = {"title": "Updated Post", "body": "This post has been updated."}
        updated_post = post_endpoint.update_post(1, updated_post_data)
        assert updated_post["title"] == "Updated Post"

    def test_delete_post(self, base_url):
        post_endpoint = PostEndpoint(base_url)
        post_endpoint.delete_post(1)
        # Проверка удаления может быть реализована через проверку наличия поста с указанным ID
        with pytest.raises(AssertionError):
            post_endpoint.get_post(1)
