import pytest
import main

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

#GET /post/{id}
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

def test_get_post_field_types(post_response):
    assert isinstance(post_response.json()["userId"], int)
    assert isinstance(post_response.json()["id"], int)
    assert isinstance(post_response.json()["title"], str)
    assert isinstance(post_response.json()["body"], str)

#GET /post/comments/{post_id}
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

def test_get_post_comments_field_types(post_comments_response):
    for comment in post_comments_response.json():
        assert isinstance(comment["postId"], int)
        assert isinstance(comment["id"], int)
        assert isinstance(comment["name"], str)
        assert isinstance(comment["email"], str)
        assert isinstance(comment["body"], str)

# GET /{user_id}/posts
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

def test_get_user_posts_field_types(user_posts_response):
    for post in user_posts_response.json():
        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)

#POST /posts

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

#PUT /posts/{post_id}

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

#PATCH /posts/{post_id}

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

def test_patch_post_content_match_request(patch_post_response):
    original_post = main.get_post(1).json()

    assert patch_post_response.json()["id"] == original_post["id"]
    assert patch_post_response.json()["userId"] == original_post["userId"]
    assert patch_post_response.json()["title"] == "title"
    assert patch_post_response.json()["body"] == original_post["body"]

def test_patch_post_field_types(patch_post_response):
    assert isinstance(patch_post_response.json()["userId"], int)
    assert isinstance(patch_post_response.json()["id"], int)
    assert isinstance(patch_post_response.json()["title"], str)
    assert isinstance(patch_post_response.json()["body"], str)

#DELETE /posts/{post_id}

@pytest.fixture
def delete_post_response():
    return main.delete_post(1)

def test_delete_post_response_status_code(delete_post_response):
    assert delete_post_response.status_code == 200

def test_delete_post_response_has_content(delete_post_response):
    assert delete_post_response.json() == {}