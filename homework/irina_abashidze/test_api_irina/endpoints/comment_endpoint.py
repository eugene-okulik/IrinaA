import requests


class CommentEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_comment(self, comment_id):
        url = f"{self.base_url}/comments/{comment_id}"
        response = requests.get(url)
        return response.json()

    def create_comment(self, comment_data):
        url = f"{self.base_url}/comments"
        response = requests.post(url, json=comment_data)
        return response.json()

    def update_comment(self, comment_id, updated_data):
        url = f"{self.base_url}/comments/{comment_id}"
        response = requests.put(url, json=updated_data)
        return response.json()

    def delete_comment(self, comment_id):
        url = f"{self.base_url}/comments/{comment_id}"
        response = requests.delete(url)
        return response.status_code
