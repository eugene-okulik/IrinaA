import requests


class UserEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url)
        return response.json()

    def create_user(self, user_data):
        url = f"{self.base_url}/users"
        response = requests.post(url, json=user_data)
        return response.json()

    def update_user(self, user_id, updated_data):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.put(url, json=updated_data)
        return response.json()

    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.delete(url)
        return response.status_code
