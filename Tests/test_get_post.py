import pytest
from api import main

# GET /posts/{id}
@pytest.fixture
def post_response():
    return main.get_post(1)

def test_get_post_response_status_code(post_response):
    assert post_response.status_code == 200

def test_get_post_response_has_content(post_response):
    assert post_response.json()

def test_get_post_response_type(post_response):
    assert isinstance(post_response.json(), dict)

def test_get_post_response_content_has_keys(post_response):
    assert "userId" in post_response.json()
    assert "id" in post_response.json()
    assert "title" in post_response.json()
    assert "body" in post_response.json()

def test_get_post_id(post_response):
    assert post_response.json()["id"] == 1

def test_get_2nd_post_id():
    response = main.get_post(2)
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert isinstance(response.json(), dict)

def test_get_post_with_zero_id():
    response = main.get_post(0)
    assert response.status_code == 404

def test_get_post_with_negative_id():
    response = main.get_post(-1)
    assert response.status_code == 404

def test_get_post_with_non_integer_id():
    response = main.get_post("a")
    assert response.status_code == 404

def test_get_post_field_types(post_response):
    assert isinstance(post_response.json()["userId"], int)
    assert isinstance(post_response.json()["id"], int)
    assert isinstance(post_response.json()["title"], str)
    assert isinstance(post_response.json()["body"], str)

def test_get_non_existent_post():
    assert main.get_post(999).status_code == 404

def test_get_post_response_content_type(post_response):
    assert "application/json" in post_response.headers["Content-Type"]