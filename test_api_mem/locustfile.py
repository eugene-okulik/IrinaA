from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):

    def on_start(self):
        response = self.client.post("/authorize", json={"name": "test_user"})
        self.token = response.json()["token"]
        self.client.headers.update({"Authorization": self.token})

    @task
    def get_all_memes(self):
        self.client.get("/meme")

    @task
    def create_meme(self):
        meme_data = {
            "text": "Performance meme",
            "url": "http://example.com/performance_meme.jpg",
            "tags": ["performance", "test"],
            "info": {"author": "perf_tester"}
        }
        self.client.post("/meme", json=meme_data)

    @task
    def update_meme(self):
        meme_data = {
            "text": "Performance meme",
            "url": "http://example.com/performance_meme.jpg",
            "tags": ["performance", "test"],
            "info": {"author": "perf_tester"}
        }
        create_response = self.client.post("/meme", json=meme_data)
        meme_id = create_response.json()["id"]
        updated_data = {
            "id": meme_id,
            "text": "Updated performance meme",
            "url": "http://example.com/updated_performance_meme.jpg",
            "tags": ["performance", "updated"],
            "info": {"author": "perf_tester_updated"}
        }
        self.client.put(f"/meme/{meme_id}", json=updated_data)
        self.client.delete(f"/meme/{meme_id}")

    @task
    def delete_meme(self):
        meme_data = {
            "text": "Performance meme",
            "url": "http://example.com/performance_meme.jpg",
            "tags": ["performance", "test"],
            "info": {"author": "perf_tester"}
        }
        create_response = self.client.post("/meme", json=meme_data)
        meme_id = create_response.json()["id"]
        self.client.delete(f"/meme/{meme_id}")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://167.172.172.115:52355"
