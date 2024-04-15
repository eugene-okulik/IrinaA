import requests


class CommentEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_comment(self, comment_id):
        url = f"{self.base_url}/comments/{comment_id}"
        response = requests.get(url)
        comment = response.json()
        assert comment["id"] == comment_id  # Проверка корректности полученного комментария
        return comment

    def create_comment(self, comment_data):
        # Реализация метода создания комментария
        pass

    def update_comment(self, comment_id, updated_data):
        # Реализация метода обновления комментария
        pass

    def delete_comment(self, comment_id):
        # Реализация метода удаления комментария
        pass
