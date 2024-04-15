import pytest
from test_api_abashidze.endpoints.user_endpoint import UserEndpoint
from test_api_abashidze.endpoints.post_endpoint import PostEndpoint
from test_api_abashidze.endpoints.comment_endpoint import CommentEndpoint


@pytest.fixture(scope="session")
def base_url():
    return "https://api.restful-api.dev"


@pytest.fixture(scope="session")
def user_endpoint(base_url):
    return UserEndpoint(base_url)


@pytest.fixture(scope="session")
def post_endpoint(base_url):
    return PostEndpoint(base_url)


@pytest.fixture(scope="session")
def comment_endpoint(base_url):
    return CommentEndpoint(base_url)
