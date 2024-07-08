import json
from locust import HttpUser, TaskSet, task, between


class ApiTasks(TaskSet):
    post_id = None  # Задаем начальное значение для post_id

    @task(1)
    def create_post(self):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = self.client.post("/posts", json=payload)
        print(f"Create Post Response: {response.status_code}, {response.text}")
        assert response.status_code == 201, (f"Failed to create post. "
                                             f"Status code: {response.status_code}")
        self.post_id = response.json()["id"]
        print(f"Created post with ID: {self.post_id}")

    @task(2)
    def update_post_put(self):
        if self.post_id is None:
            return
        payload = {
            "id": self.post_id,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        response = self.client.put(f"/posts/{self.post_id}", json=payload)
        print(f"Update Post PUT Response: {response.status_code}, {response.text}")
        assert response.status_code == 200, (f"Failed to update post with PUT. "
                                             f"Status code: {response.status_code}")
        assert response.json()["title"] == "updated title"
        assert response.json()["body"] == "updated body"

    @task(3)
    def update_post_patch(self):
        if self.post_id is None:
            return
        payload = {
            "title": "patched title"
        }
        response = self.client.patch(f"/posts/{self.post_id}", json=payload)
        print(f"Update Post PATCH Response: {response.status_code}, {response.text}")
        assert response.status_code == 200, f"Failed to update post with PATCH. Status code: {response.status_code}"
        assert response.json()["title"] == "patched title"

    @task(4)
    def delete_post(self):
        if self.post_id is None:
            return
        response = self.client.delete(f"/posts/{self.post_id}")
        print(f"Delete Post Response: {response.status_code}, {response.text}")
        assert response.status_code == 200, f"Failed to delete post. Status code: {response.status_code}"


class ApiUser(HttpUser):
    tasks = [ApiTasks]
    wait_time = between(1, 5)
    host = "https://jsonplaceholder.typicode.com"
