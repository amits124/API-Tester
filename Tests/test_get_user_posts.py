import pytest
from api import main

# GET /users/{user_id}/posts
@pytest.fixture
def user_posts_response():
    return main.get_user_posts(1)

def test_get_user_posts_response_status_code(user_posts_response):
    assert user_posts_response.status_code == 200

def test_get_user_posts_response_has_content(user_posts_response):
    assert user_posts_response.json()

def test_get_user_posts_response_type(user_posts_response):
    assert isinstance(user_posts_response.json(), list)

def test_get_user_posts_response_content_has_keys(user_posts_response):
    for post in user_posts_response.json():
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post

def test_get_user_posts_user_id(user_posts_response):
    for post in user_posts_response.json():
        assert post["userId"] == 1

def test_get_2nd_user_posts():
    response = main.get_user_posts(2)
    assert response.status_code == 200
    for post in response.json():
        assert post["userId"] == 2

def test_get_user_posts_with_zero_id():
    response = main.get_user_posts(0)
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_posts_with_negative_id():
    response = main.get_user_posts(-1)
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_posts_with_non_integer_id():
    response = main.get_user_posts("a")
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_posts_field_types(user_posts_response):
    for post in user_posts_response.json():
        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)

def test_get_non_existent_user_posts():
    response = main.get_user_posts(999)
    assert response.status_code == 200
    assert response.json() == []

def test_get_user_posts_response_content_type(user_posts_response):
    assert "application/json" in user_posts_response.headers["Content-Type"]