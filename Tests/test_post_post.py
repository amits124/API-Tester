import pytest
from api import main

# POST /posts
@pytest.fixture
def create_post_response():
    return main.create_post("title", "body", 1)

def test_create_post_response_status_code(create_post_response):
    assert create_post_response.status_code == 201

def test_create_post_response_has_content(create_post_response):
    assert create_post_response.json()

def test_create_post_response_type(create_post_response):
    assert isinstance(create_post_response.json(), dict)

def test_create_post_response_content_has_keys(create_post_response):
    assert "userId" in create_post_response.json()
    assert "id" in create_post_response.json()
    assert "title" in create_post_response.json()
    assert "body" in create_post_response.json()

def test_create_post_content_match_request(create_post_response):
    assert create_post_response.json()["userId"] == 1
    assert create_post_response.json()["title"] == "title"
    assert create_post_response.json()["body"] == "body"

def test_create_post_field_types(create_post_response):
    assert isinstance(create_post_response.json()["userId"], int)
    assert isinstance(create_post_response.json()["id"], int)
    assert isinstance(create_post_response.json()["title"], str)
    assert isinstance(create_post_response.json()["body"], str)

def test_create_post_empty_title():
    response = main.create_post("", "body", 1)
    assert response.status_code == 201
    assert response.json()["title"] == ""

def test_create_post_empty_body():
    response = main.create_post("title", "", 1)
    assert response.status_code == 201
    assert response.json()["body"] == ""

def test_create_post_negative_user_id():
    response = main.create_post("title", "body", -1)
    assert response.status_code == 201
    assert response.json()["userId"] == -1

def test_create_post_zero_user_id():
    response = main.create_post("title", "body", 0)
    assert response.status_code == 201
    assert response.json()["userId"] == 0

def test_create_post_non_string_title():
    response = main.create_post(123, "body", 1)
    assert response.status_code == 201
    assert response.json()["title"] == 123

def test_create_post_non_string_body():
    response = main.create_post("title", 123, 1)
    assert response.status_code == 201
    assert response.json()["body"] == 123

def test_create_post_response_content_type(create_post_response):
    assert "application/json" in create_post_response.headers["Content-Type"]