import pytest
from test_api_mem.endpoints.authorize import Authorize


def test_get_token(base_url):
    auth = Authorize(base_url)
    token = auth.get_token("test_user")
    assert token is not None
    print("Token:", token)


def test_check_token(base_url, auth_token):
    auth = Authorize(base_url)
    response = auth.check_token(auth_token)
    assert response["status"] == "alive"
    print("Check token response:", response)
