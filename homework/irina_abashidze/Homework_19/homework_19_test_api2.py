import pytest
import requests
import json


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


# Тест на создание объекта с параметризацией для трех разных объектов
@pytest.mark.parametrize("name, attribute1, attribute2", [("Object1", "value1", "value2"),
                                                          ("Object2", "value3", "value4"),
                                                          ("Object3", "value5", "value6")])
@pytest.mark.critical  # Помечаем тест как "critical"
def test_create_object(name, attribute1, attribute2):
    print("before test")
    base_url = "https://api.restful-api.dev/objects"
    headers = {"content-type": "application/json"}

    # Создаем данные для нового объекта
    data = {
        "name": name,
        "data": {
            "attribute1": attribute1,
            "attribute2": attribute2
        }
    }

    # Отправляем POST запрос для создания объекта
    response = requests.post(base_url, json=data, headers=headers)
    json_data = response.json()

    print("after test")

    # Проверяем успешность создания объекта и соответствие его атрибутов ожидаемым значениям
    assert response.status_code == 200, (
        f"Ошибка при создании объекта. Непредвиденный код состояния: {response.status_code}"
    )
    assert 'id' in json_data, "Созданный объект не содержит ID"
    assert json_data['name'] == name, "Имя созданного объекта не совпадает"
    assert json_data['data']['attribute1'] == attribute1, "Атрибут attribute1 созданного объекта не совпадает"
    assert json_data['data']['attribute2'] == attribute2, "Атрибут attribute2 созданного объекта не совпадает"


# Тест на обновление объекта методом PUT
@pytest.mark.medium  # Помечаем тест как "medium"
def test_update_object_put(created_object_id):
    print("before test")
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"
    headers = {"content-type": "application/json"}

    # Создаем данные для обновления объекта
    data = {
        "name": "Updated Object",
        "data": {
            "attribute1": "updated_value1",
            "attribute2": "updated_value2"
        }
    }

    # Отправляем PUT запрос для обновления объекта
    response = requests.put(base_url, json=data, headers=headers)
    json_data = response.json()

    print("after test")

    # Проверяем успешность обновления объекта и соответствие его атрибутов ожидаемым значениям
    assert response.status_code == 200, (
        f"Ошибка при обновлении объекта (PUT). Непредвиденный код состояния: {response.status_code}"
    )
    assert json_data['name'] == "Updated Object", "Имя обновленного объекта не совпадает"
    assert json_data['data']['attribute1'] == "updated_value1", "Атрибут attribute1 обновленного объекта не совпадает"
    assert json_data['data']['attribute2'] == "updated_value2", "Атрибут attribute2 обновленного объекта не совпадает"


# Тест на обновление объекта методом PATCH
def test_update_object_patch(created_object_id):
    print("before test")
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"
    headers = {"content-type": "application/json"}

    # Создаем данные для частичного обновления объекта
    data = {
        "data": {
            "attribute2": "patched_value2"
        }
    }

    # Отправляем PATCH запрос для обновления объекта
    response = requests.patch(base_url, json=data, headers=headers)
    json_data = response.json()

    print("after test")

    # Проверяем успешность обновления объекта и соответствие его атрибутов ожидаемым значениям
    assert response.status_code == 200, (f"Ошибка при обновлении объекта (PATCH). "
                                         f"Непредвиденный код состояния: {response.status_code}")
    assert json_data['data']['attribute2'] == "patched_value2", \
        "Значение атрибута attribute2 после обновления не совпадает"


# Тест на удаление объекта
def test_delete_object(created_object_id):
    print("before test")
    base_url = f"https://api.restful-api.dev/objects/{created_object_id}"

    # Отправляем DELETE запрос для удаления объекта
    response = requests.delete(base_url)

    print("after test")

    # Проверяем успешность удаления объекта и пустой ли ответ при удалении
    assert response.status_code == 200, (
        f"Ошибка при удалении объекта. Непредвиденный код состояния: {response.status_code}"
    )
    assert response.json() == {'message': f'Object with id = {created_object_id} has been deleted.'}, \
        "Некорректный ответ на удаление объекта"
