import pytest
import requests
import json


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def created_object_id():
    base_url = "https://api.restful-api.dev/objects"
    headers = {"content-type": "application/json"}

    # Создаем новый объект
    data = {
        "name": "New Object",
        "data": {
            "attribute1": "value1",
            "attribute2": "value2"
        }
    }

    response = requests.post(base_url, json=data, headers=headers)
    json_data = response.json()
    object_id = json_data['id']

    yield object_id

    # Удаляем созданный объект после использования
    delete_url = f"https://api.restful-api.dev/objects/{object_id}"
    requests.delete(delete_url)


def test_create_object(name="New Object", attribute1="value1", attribute2="value2"):
    base_url = "https://api.restful-api.dev/objects"
    headers = {"content-type": "application/json"}

    data = {
        "name": name,
        "data": {
            "attribute1": attribute1,
            "attribute2": attribute2
        }
    }

    response = requests.post(base_url, json=data, headers=headers)
    json_data = response.json()

    assert response.status_code == 200, f"Failed to create object. Unexpected status code: {response.status_code}"
    assert 'id' in json_data, "Created object has no ID"
    assert json_data['name'] == name, "Created object name does not match"
    assert json_data['data']['attribute1'] == attribute1, "Created object attribute1 does not match"
    assert json_data['data']['attribute2'] == attribute2, "Created object attribute2 does not match"


def test_update_object_put(created_object_id):
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"
    headers = {"content-type": "application/json"}

    data = {
        "name": "Updated Object",
        "data": {
            "attribute1": "updated_value1",
            "attribute2": "updated_value2"
        }
    }

    response = requests.put(base_url, json=data, headers=headers)
    json_data = response.json()

    assert response.status_code == 200, f"Failed to update object (PUT). Unexpected status code: {response.status_code}"
    assert json_data['name'] == "Updated Object", "Updated object name does not match"
    assert json_data['data']['attribute1'] == "updated_value1", "Updated object attribute1 does not match"
    assert json_data['data']['attribute2'] == "updated_value2", "Updated object attribute2 does not match"


def test_update_object_patch(created_object_id):
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"
    headers = {"content-type": "application/json"}

    data = {
        "data": {
            "attribute2": "patched_value2"
        }
    }

    response = requests.patch(base_url, json=data, headers=headers)
    json_data = response.json()

    assert response.status_code == 200, (f"Failed to update object (PATCH). "
                                         f"Unexpected status code: {response.status_code}")
    assert json_data['data']['attribute2'] == "patched_value2", "Patched attribute2 value does not match"


def test_delete_object(created_object_id):
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"

    response = requests.delete(base_url)

    assert response.status_code == 200, f"Failed to delete object. Unexpected status code: {response.status_code}"
    assert response.json() == {}, "Delete response data is not empty"
