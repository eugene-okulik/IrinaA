import pytest
from test_api_mem.endpoints.meme import Meme


@pytest.fixture
def meme_instance(base_url, headers):
    return Meme(base_url, headers)


def test_get_all_memes(meme_instance):
    memes = meme_instance.get_all_memes()
    assert isinstance(memes, list)
    print("All memes:", memes)


def test_create_meme(meme_instance):
    new_meme = {
        "text": "Funny meme",
        "url": "http://example.com/meme.jpg",
        "tags": ["funny", "lol"],
        "info": {"author": "user"}
    }
    response = meme_instance.create_meme(new_meme)
    assert response["text"] == new_meme["text"]
    meme_instance.delete_meme(response["id"])
    print("Create meme response:", response)


def test_get_meme(meme_instance):
    new_meme = {
        "text": "Funny meme",
        "url": "http://example.com/meme.jpg",
        "tags": ["funny", "lol"],
        "info": {"author": "user"}
    }
    created_meme = meme_instance.create_meme(new_meme)
    meme_id = created_meme["id"]
    meme = meme_instance.get_meme(meme_id)
    assert meme["text"] == new_meme["text"]
    meme_instance.delete_meme(meme_id)
    print("Get meme response:", meme)


def test_update_meme(meme_instance):
    new_meme = {
        "text": "Funny meme",
        "url": "http://example.com/meme.jpg",
        "tags": ["funny", "lol"],
        "info": {"author": "user"}
    }
    created_meme = meme_instance.create_meme(new_meme)
    meme_id = created_meme["id"]
    updated_meme = {
        "id": meme_id,
        "text": "Updated meme",
        "url": "http://example.com/updated_meme.jpg",
        "tags": ["updated", "meme"],
        "info": {"author": "updated_user"}
    }
    response = meme_instance.update_meme(meme_id, updated_meme)
    assert response["text"] == "Updated meme"
    meme_instance.delete_meme(meme_id)
    print("Update meme response:", response)


def test_delete_meme(meme_instance):
    new_meme = {
        "text": "Funny meme",
        "url": "http://example.com/meme.jpg",
        "tags": ["funny", "lol"],
        "info": {"author": "user"}
    }
    created_meme = meme_instance.create_meme(new_meme)
    meme_id = created_meme["id"]
    response = meme_instance.delete_meme(meme_id)
    assert response["status"] == "deleted"
    print("Delete meme response:", response)
