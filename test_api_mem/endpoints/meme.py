import requests


class Meme:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_all_memes(self):
        response = requests.get(f"{self.base_url}/meme", headers=self.headers)
        print(f"GET /meme response: {response.json()}")
        response.raise_for_status()
        return response.json()

    def get_meme(self, meme_id):
        response = requests.get(f"{self.base_url}/meme/{meme_id}",
                                headers=self.headers)
        print(f"GET /meme/{meme_id} response: {response.json()}")
        response.raise_for_status()
        return response.json()

    def create_meme(self, meme_data):
        response = requests.post(f"{self.base_url}/meme", json=meme_data,
                                 headers=self.headers)
        print(f"POST /meme response: {response.json()}")
        response.raise_for_status()
        return response.json()

    def update_meme(self, meme_id, meme_data):
        response = requests.put(f"{self.base_url}/meme/{meme_id}", json=meme_data,
                                headers=self.headers)
        print(f"PUT /meme/{meme_id} response: {response.json()}")
        response.raise_for_status()
        return response.json()

    def delete_meme(self, meme_id):
        response = requests.delete(f"{self.base_url}/meme/{meme_id}",
                                   headers=self.headers)
        print(f"DELETE /meme/{meme_id} response: {response.json()}")
        response.raise_for_status()
        return response.json()
