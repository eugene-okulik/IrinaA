import requests
import json


def create_object():
    base_url = "https://api.restful-api.dev/objects"
    headers = {"content-type": "application/json"}

    # Данные для создания объекта
    data = {
        "name": "New Object",
        "data": {
            "attribute1": "value1",
            "attribute2": "value2"
        }
    }

    # Отправка запроса на создание объекта
    response = requests.post(base_url, json=data, headers=headers)

    try:
        # Попытка декодировать ответ в JSON
        json_data = response.json()
        assert response.status_code == 200, (f"Failed to create object. "
                                             f"Unexpected status code: {response.status_code}")
        print("Create Object:", response.status_code, json_data)
    except json.decoder.JSONDecodeError:
        # Если возникла ошибка декодирования JSON, вывести текст ответа
        print("Create Object:", response.status_code, response.text)


def update_object_put(object_id):
    base_url = f"https://api.restful-api.dev/objects/{object_id}"
    headers = {"content-type": "application/json"}

    # Данные для обновления объекта
    data = {
        "name": "Updated Object",
        "data": {
            "attribute1": "updated_value1",
            "attribute2": "updated_value2"
        }
    }

    # Отправка запроса на обновление объекта методом PUT
    response = requests.put(base_url, json=data, headers=headers)

    try:
        # Попытка декодировать ответ в JSON
        json_data = response.json()
        assert response.status_code == 200, (f"Failed to update object (PUT). "
                                             f"Unexpected status code: {response.status_code}")
        print("Update Object (PUT):", response.status_code, json_data)
    except json.decoder.JSONDecodeError:
        # Если возникла ошибка декодирования JSON, вывести текст ответа
        print("Update Object (PUT):", response.status_code, response.text)


def update_object_patch(object_id):
    base_url = f"https://api.restful-api.dev/objects/{object_id}"
    headers = {"content-type": "application/json"}

    # Данные для частичного обновления объекта
    data = {
        "data": {
            "attribute2": "patched_value2"
        }
    }

    # Отправка запроса на обновление объекта методом PATCH
    response = requests.patch(base_url, json=data, headers=headers)

    try:
        # Попытка декодировать ответ в JSON
        json_data = response.json()
        assert response.status_code == 200, (f"Failed to update object (PATCH). "
                                             f"Unexpected status code: {response.status_code}")
        print("Update Object (PATCH):", response.status_code, json_data)
    except json.decoder.JSONDecodeError:
        # Если возникла ошибка декодирования JSON, вывести текст ответа
        print("Update Object (PATCH):", response.status_code, response.text)


def delete_object(object_id):
    base_url = f"https://api.restful-api.dev/objects/{object_id}"

    # Отправка запроса на удаление объекта
    response = requests.delete(base_url)

    try:
        # Попытка декодировать ответ в JSON
        json_data = response.json()
        assert response.status_code == 200, (f"Failed to delete object. "
                                             f"Unexpected status code: {response.status_code}")
        print("Delete Object:", response.status_code, json_data)
    except json.decoder.JSONDecodeError:
        # Если возникла ошибка декодирования JSON, вывести текст ответа
        print("Delete Object:", response.status_code, response.text)


# Пример использования
if __name__ == "__main__":
    # Создание объекта
    create_object()

    # Получение ID созданного объекта
    object_id = input("Введите ID созданного объекта: ")

    # Изменение объекта с помощью метода PUT
    update_object_put(object_id)

    # Изменение объекта с помощью метода PATCH
    update_object_patch(object_id)

    # Удаление объекта
    delete_object(object_id)
