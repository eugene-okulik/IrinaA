import requests


class PostEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)
        return response.json()

    def create_post(self, post_data):
        url = f"{self.base_url}/posts"
        response = requests.post(url, json=post_data)
        return response.json()

    def update_post(self, post_id, updated_data):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.put(url, json=updated_data)
        return response.json()

    def delete_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.delete(url)
        return response.status_code
