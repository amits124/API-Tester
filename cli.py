from api import main as api
def display_menu():
    print("\n=== API Tester ===")
    print("1. Get all posts")
    print("2. Get a post by ID")
    print("3. Get post comments")
    print("4. Get posts by user ID")
    print("5. Create a post")
    print("6. Replace a post (PUT)")
    print("7. Update a post (PATCH)")
    print("8. Delete a post")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an operation: ")

        #option 0: exit
        if choice == "0":
            print("Exiting API Tester.")
            break

        #option 1: get all posts
        elif choice == "1":
            response = api.get_posts()
            print(f"\nStatus code: {response.status_code}")
            if response.ok:
                posts = response.json()
                print(f"Successfully retrieved {len(posts)} posts.")
            else:
                print("Failed to retrieve posts.")

        #option 2: get a post by ID
        elif choice == "2":
            post_id = input("Enter post ID: ")
            response = api.get_post(post_id)
            print(f"\nStatus code: {response.status_code}")
            if response.status_code == 200:
                post = response.json()
                print("\n=== Post Details ===")
                print(f"ID:      {post['id']}")
                print(f"User ID: {post['userId']}")
                print(f"Title:   {post['title']}")
                print(f"Body:\n{post['body']}")
                print("====================")
            elif response.status_code == 404:
                print(f"Post with ID {post_id} was not found.")
            else:
                print("Failed to retrieve post.")

        #option 3: get post comments
        elif choice == "3":
            post_id = input("Enter post ID: ")
            response = api.get_post_comments(post_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        elif choice == "4":
            user_id = input("Enter user ID: ")
            response = api.get_user_posts(user_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        elif choice == "5":
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")
            response = api.create_post(title, body, user_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        elif choice == "6":
            post_id = input("Enter post ID: ")
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")
            response = api.update_post(post_id, title, body, user_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        elif choice == "7":
            post_id = input("Enter post ID: ")
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")
            response = api.patch_post(post_id, title, body, user_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        elif choice == "8":
            post_id = input("Enter post ID: ")
            response = api.delete_post(post_id)
            print(f"\nStatus code: {response.status_code}")
            print(response.json())
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
