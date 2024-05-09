import pytest
from test_api_irina.endpoints.post_object import PostObject
from test_api_irina.endpoints.put_object import PutObject
from test_api_irina.endpoints.patch_object import PatchObject
from test_api_irina.endpoints.delete_object import DeleteObject


class TestObjectsAPI:
    @pytest.fixture(scope="session")
    def base_url(self):
        return "https://api.restful-api.dev"

    def test_create_object(self, base_url):
        post_object = PostObject(base_url)
        response = post_object.post_object(
            {
                "name": "New Object",
                "data": {
                    "attribute1": "value1",
                    "attribute2": "value2"
                }
            }
        )
        assert response.status_code == 200
        post_object.check_id_in_response()

    def test_update_object_put(self, base_url, created_object_id):
        put_object = PutObject(base_url)
        response = put_object.put_object(created_object_id,
                                         {"name": "Updated Object", "data":
                                             {"attribute1": "updated_value1", "attribute2": "updated_value2"}})
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Object"
        assert response.json()["data"]["attribute1"] == "updated_value1"
        assert response.json()["data"]["attribute2"] == "updated_value2"

    def test_update_object_patch(self, base_url, created_object_id):
        patch_object = PatchObject(base_url)
        response = patch_object.patch_object(created_object_id, {"data": {"attribute2": "patched_value2"}})
        assert response.status_code == 200
        assert response.json()["data"]["attribute2"] == "patched_value2"

    def test_delete_object(self, base_url, created_object_id):
        delete_object = DeleteObject(base_url)
        delete_object_response = delete_object.delete_object(created_object_id)
        assert delete_object_response.status_code == 200
