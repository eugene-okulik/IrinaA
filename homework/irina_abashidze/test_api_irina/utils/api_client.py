import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()

    def post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        return response.json()

    def put_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        return response.json()

    def delete_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response.status_code
