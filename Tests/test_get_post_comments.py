import pytest
from api import main

# GET /posts/{post_id}/comments
@pytest.fixture
def post_comments_response():
    return main.get_post_comments(1)

def test_get_post_comments_response_status_code(post_comments_response):
    assert post_comments_response.status_code == 200

def test_get_post_comments_response_has_content(post_comments_response):
    assert post_comments_response.json()

def test_get_post_comments_response_type(post_comments_response):
    assert isinstance(post_comments_response.json(), list)

def test_get_post_comments_response_content_has_keys(post_comments_response):
    for comment in post_comments_response.json():
        assert "postId" in comment
        assert "id" in comment
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment

def test_get_post_comments_id(post_comments_response):
    for comment in post_comments_response.json():
        assert comment["postId"] == 1
    
def test_get_2nd_post_comments():
    response = main.get_post_comments(2)
    assert response.status_code == 200
    for comment in response.json():
        assert comment["postId"] == 2

def test_get_post_comments_with_zero_id():
    response = main.get_post_comments(0)
    assert response.status_code == 200
    assert response.json() == []

def test_get_post_comments_with_negative_id():
    response = main.get_post_comments(-1)
    assert response.status_code == 200
    assert response.json() == []

def test_get_post_comments_with_non_integer_id():
    response = main.get_post_comments("a")
    assert response.status_code == 200
    assert response.json() == []

def test_get_post_comments_field_types(post_comments_response):
    for comment in post_comments_response.json():
        assert isinstance(comment["postId"], int)
        assert isinstance(comment["id"], int)
        assert isinstance(comment["name"], str)
        assert isinstance(comment["email"], str)
        assert isinstance(comment["body"], str)

def test_get_non_existent_post_comments():
    response = main.get_post_comments(999)
    assert response.status_code == 200
    assert response.json() == []

def test_get_post_comments_response_content_type(post_comments_response):
    assert "application/json" in post_comments_response.headers["Content-Type"]