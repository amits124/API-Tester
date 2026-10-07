import pytest
from api import main

# PATCH /posts/{post_id}
@pytest.fixture
def patch_post_response():
    return main.patch_post(1, "title")

def test_patch_post_response_status_code(patch_post_response):
    assert patch_post_response.status_code == 200

def test_patch_post_response_has_content(patch_post_response):
    assert patch_post_response.json()

def test_patch_post_response_type(patch_post_response):
    assert isinstance(patch_post_response.json(), dict)

def test_patch_post_response_content_has_keys(patch_post_response):
    assert "userId" in patch_post_response.json()
    assert "id" in patch_post_response.json()
    assert "title" in patch_post_response.json()
    assert "body" in patch_post_response.json()

def test_patch_post_content_match_request():
    original_post = main.get_post(1).json()
    response = main.patch_post(1, "title")
    updated_post = response.json()

    assert response.status_code == 200
    assert updated_post["id"] == original_post["id"]
    assert updated_post["userId"] == original_post["userId"]
    assert updated_post["title"] == "title"
    assert updated_post["body"] == original_post["body"]

def test_patch_post_body():
    original_post = main.get_post(1).json()
    response = main.patch_post(1, body="new body")
    updated_post = response.json()

    assert response.status_code == 200
    assert updated_post["title"] == original_post["title"]
    assert updated_post["body"] == "new body"
    assert updated_post["userId"] == original_post["userId"]