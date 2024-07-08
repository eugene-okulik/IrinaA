import pytest
import sys
import os

from endpoints.authorize import Authorize

# Добавляем путь к корню проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def base_url():
    return "http://167.172.172.115:52355"


@pytest.fixture(scope="session")
def auth_token(base_url):
    auth = Authorize(base_url)
    token = auth.get_token("test_user")
    return token


@pytest.fixture(scope="session")
def headers(auth_token):
    return {"Authorization": auth_token}
