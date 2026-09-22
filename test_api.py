import pytest
import main

def test_get_posts():
    response = main.get_posts()
    assert response.status_code == 200
