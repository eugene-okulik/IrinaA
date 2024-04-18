import pytest
import requests


# fixture для настройки и завершения тестирования
@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("Start testing")
    yield
    print("Testing completed")


# fixture для создания объекта перед каждым тестом и его удаления после
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

    # Отправляем POST запрос для создания объекта
    response = requests.post(base_url, json=data, headers=headers)
    json_data = response.json()
    object_id = json_data['id']

    yield object_id  # Передаем ID созданного объекта для использования в тесте

    # Удаляем созданный объект после использования
    delete_url = f"https://api.restful-api.dev/objects/{object_id}"
    requests.delete(delete_url)
