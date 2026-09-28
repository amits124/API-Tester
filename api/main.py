import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    return response

def get_post_comments(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    response = requests.get(url)
    return response

def get_user_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/posts"
    response = requests.get(url)
    return response

def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(url, json=payload)
    return response

def update_post(post_id, title, body, user_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.put(url, json=payload)
    return response

def patch_post(post_id, title=None, body=None, user_id=None):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    payload = {}
    if title != None:
        payload["title"] = title
    if body != None:
        payload["body"] = body
    if user_id != None:
        payload["userId"] = user_id
    response = requests.patch(url, json=payload)
    return response

def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.delete(url)
    return response