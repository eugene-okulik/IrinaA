import pytest
from test_api_irina.endpoints.post_object import PostObject
from test_api_irina.endpoints.delete_object import DeleteObject


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

    # Создаем новый объект
    data = {
        "name": "New Object",
        "data": {
            "attribute1": "value1",
            "attribute2": "value2"
        }
    }

    # Отправляем POST запрос для создания объекта
    new_object_endpoint = PostObject(base_url)
    response = new_object_endpoint.post_object(data)
    object_id = response['id']

    yield object_id  # Передаем ID созданного объекта для использования в тесте

    # Удаляем созданный объект после использования
    delete_object_endpoint = DeleteObject(base_url)
    delete_object_endpoint.delete_object(object_id)
