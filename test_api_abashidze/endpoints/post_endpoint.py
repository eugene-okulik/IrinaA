import requests


class PostEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)
        post = response.json()
        assert response.status_code == 200, f"Failed to get post with ID {post_id}: {response.text}"
        return post

    def create_post(self, post_data):
        url = f"{self.base_url}/posts"
        response = requests.post(url, json=post_data)
        new_post = response.json()
        assert response.status_code == 201, f"Failed to create post: {response.text}"
        return new_post

    def update_post(self, post_id, updated_data):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.put(url, json=updated_data)
        updated_post = response.json()
        assert response.status_code == 200, f"Failed to update post with ID {post_id}: {response.text}"
        return updated_post

    def delete_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.delete(url)
        assert response.status_code == 204, f"Failed to delete post with ID {post_id}: {response.text}"
        