import pytest
from api import main

# DELETE /posts/{post_id}
@pytest.fixture
def delete_post_response():
    return main.delete_post(1)

def test_delete_post_response_status_code(delete_post_response):
    assert delete_post_response.status_code == 200

def test_delete_post_response_has_content(delete_post_response):
    assert delete_post_response.json() == {}

def test_delete_2nd_post():
    response = main.delete_post(2)
    assert response.status_code == 200
    assert response.json() == {}

def test_delete_non_existent_post():
    response = main.delete_post(999)
    assert response.status_code == 200
    assert response.json() == {}

def test_delete_post_response_content_type(delete_post_response):
    assert "application/json" in delete_post_response.headers["Content-Type"]