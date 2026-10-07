import pytest
from api import main

# PUT /posts/{post_id}
@pytest.fixture
def update_post_response():
    return main.update_post(1, "title", "body", 1)

def test_update_post_response_status_code(update_post_response):
    assert update_post_response.status_code == 200

def test_update_post_response_has_content(update_post_response):
    assert update_post_response.json()

def test_update_post_response_type(update_post_response):
    assert isinstance(update_post_response.json(), dict)

def test_update_post_response_content_has_keys(update_post_response):
    assert "userId" in update_post_response.json()
    assert "id" in update_post_response.json()
    assert "title" in update_post_response.json()
    assert "body" in update_post_response.json()

def test_update_post_content_match_request(update_post_response):
    assert update_post_response.json()["userId"] == 1
    assert update_post_response.json()["id"] == 1
    assert update_post_response.json()["title"] == "title"
    assert update_post_response.json()["body"] == "body"

def test_update_post_field_types(update_post_response):
    assert isinstance(update_post_response.json()["userId"], int)
    assert isinstance(update_post_response.json()["id"], int)
    assert isinstance(update_post_response.json()["title"], str)
    assert isinstance(update_post_response.json()["body"], str)

def test_update_non_existent_post():
    response = main.update_post(999, "title", "body", 1)
    assert response.status_code == 500

def test_update_2nd_post():
    response = main.update_post(2, "title", "body", 1)
    assert response.status_code == 200
    assert response.json()["id"] == 2

def test_update_post_empty_title():
    response = main.update_post(1, "", "body", 1)
    assert response.status_code == 200
    assert response.json()["title"] == ""

def test_update_post_empty_body():
    response = main.update_post(1, "title", "", 1)
    assert response.status_code == 200
    assert response.json()["body"] == ""

def test_update_post_response_content_type(update_post_response):
    assert "application/json" in update_post_response.headers["Content-Type"]