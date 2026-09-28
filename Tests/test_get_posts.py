import pytest
from api import main 

# GET /posts
@pytest.fixture
def posts_response():
    return main.get_posts()

def test_get_posts_response_status_code(posts_response):
    assert posts_response.status_code == 200

def test_get_posts_response_has_content(posts_response):
    assert posts_response.json()

def test_get_posts_response_type(posts_response):
    assert isinstance(posts_response.json(), list)

def test_get_posts_response_content_has_keys(posts_response):
    for post in posts_response.json():
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post   
    
def test_get_posts_response_content_type():
    response = main.get_posts()
    assert "application/json" in response.headers["Content-Type"]