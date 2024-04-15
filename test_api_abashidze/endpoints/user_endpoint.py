import requests


class UserEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        """
        Получить информацию о пользователе по его ID.
        """
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        user = response.json()

        assert response.status_code == 200, f"Failed to get user. Status code: {response.status_code}"
        assert user.get("id") == user_id, f"User ID does not match. Expected: {user_id}, Actual: {user.get('id')}"

        return user

    def create_user(self, user_data):
        """
        Создать нового пользователя.
        """
        url = f"{self.base_url}/users"
        response = requests.post(url, json=user_data)
        new_user = response.json()

        assert response.status_code == 201, f"Failed to create user. Status code: {response.status_code}"

        return new_user

    def update_user(self, user_id, updated_data):
        """
        Обновить информацию о пользователе.
        """
        url = f"{self.base_url}/users/{user_id}"
        response = requests.put(url, json=updated_data)
        updated_user = response.json()

        assert response.status_code == 200, f"Failed to update user. Status code: {response.status_code}"
        assert updated_user.get("id") == user_id, (f"User ID does not match. Expected: "
                                                   f"{user_id}, Actual: {updated_user.get('id')}")

        return updated_user

    def delete_user(self, user_id):
        """
        Удалить пользователя по его ID.
        """
        url = f"{self.base_url}/users/{user_id}"
        response = requests.delete(url)

        assert response.status_code == 204, f"Failed to delete user. Status code: {response.status_code}"

        return response.status_code
