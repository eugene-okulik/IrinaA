from .base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):
    def put_object(self, object_id, data):
        self.response = self.put("objects", object_id, data)
        self.check_updated_data()

    def check_updated_data(self):
        response_json = self.response.json()
        assert response_json["name"] == "Updated Object", "Name was not updated"
        assert response_json["data"]["attribute1"] == "updated_value1", "attribute1 was not updated"
        assert response_json["data"]["attribute2"] == "updated_value2", "attribute2 was not updated"
