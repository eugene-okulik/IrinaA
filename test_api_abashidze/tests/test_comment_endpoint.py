import pytest
from test_api_abashidze.endpoints.comment_endpoint import CommentEndpoint


class TestCommentEndpoint:
    @pytest.fixture(scope="session")
    def base_url(self):
        return "https://api.restful-api.dev"

    def test_get_comment(self, base_url):
        comment_endpoint = CommentEndpoint(base_url)
        comment = comment_endpoint.get_comment(1)
