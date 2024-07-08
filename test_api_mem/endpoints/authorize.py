import requests


class Authorize:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_token(self, name):
        response = requests.post(f"{self.base_url}/authorize", json={"name": name})
        print(f"POST /authorize response: {response.json()}")
        response.raise_for_status()
        return response.json().get("token")

    def check_token(self, token):
        response = requests.get(f"{self.base_url}/authorize/{token}")
        print(f"GET /authorize/{token} response: {response.json()}")
        response.raise_for_status()
        return response.json()
