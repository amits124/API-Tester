import requests

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    return response

post_id = int(input("Enter the desired post ID: "))
response = get_post(post_id)

if response.status_code == 200:
    print("Request succeded")
    data = response.json()

    if "title" in data:
        print("Title field was found")
    else:
        print("Title field is missing")

    if "id" in data:
        if data["id"] == post_id:
            print("ID Test Passed")
        else:
            print("ID Test Failed")
            print("Expected: ", post_id)
            print("Actual: ", data["id"])
    else:
        print("ID Test Failed")
        print("id field is missing from response")
else:
    if response.status_code == 404:
        print(f"Post with ID {post_id} was not found")
    else:
        print("Request failed")
        print("Status Code:", response.status_code)