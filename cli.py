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
            if response.status_code == 200:
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
                print(f"ID: {post['id']}")
                print(f"User ID: {post['userId']}")
                print(f"Title: {post['title']}")
                print(f"Body:\n{post['body']}")
                print("====================")
            elif response.status_code == 404:
                print(f"Post with ID {post_id} was not found.")
            else:
                print("Failed to retrieve post.")

        #option 3: get post comments
        elif choice == "3":
            post_id = input("Enter post ID: ")
            post_response = api.get_post(post_id)

            if post_response.status_code == 404:
                print(f"\nPost with ID {post_id} was not found.")
            elif post_response.status_code != 200:
                print(f"\nFailed to verify post. Status code: {post_response.status_code}")
            else:
                response = api.get_post_comments(post_id)
                print(f"\nStatus code: {response.status_code}")

                if response.status_code != 200:
                    print("Failed to retrieve comments.")
                else:
                    comments = response.json()
                    print(f"\n=== Comments for Post {post_id} ===") 

                    for comment in comments:
                        print(f"Comment ID: {comment['id']}")
                        print(f"Name: {comment['name']}")
                        print(f"Email: {comment['email']}")
                        print(f"Comment:\n{comment['body']}")
                        print("-" * 40)
                    print(f"Total comments: {len(comments)}")


        #option 4: get posts by user ID
        elif choice == "4":
            user_id = input("Enter user ID: ")
            response = api.get_user_posts(user_id)
            print(f"\nStatus code: {response.status_code}")

            if response.status_code != 200:
                print("Failed to retrieve user posts.")
            else:
                posts = response.json()

                if not posts:
                    print(f"No posts found for user {user_id}.")
                else:
                    print(f"\n=== Posts by User {user_id} ===")

                    for post in posts:
                        print(f"Post ID: {post['id']}")
                        print(f"Title: {post['title']}")
                        print(f"Body:\n{post['body']}")
                        print("-" * 40)

                    print(f"Total posts: {len(posts)}")

        
        # Option 5: Create a post
        elif choice == "5":
            title = input("Enter title: ")
            body = input("Enter body: ")
            user_id = input("Enter user ID: ")

            response = api.create_post(title, body, user_id)
            print(f"\nStatus code: {response.status_code}")

            if response.status_code == 201:
                post = response.json()

                print("\n=== Post Created Successfully ===")
                print(f"ID:      {post['id']}")
                print(f"User ID: {post['userId']}")
                print(f"Title:   {post['title']}")
                print(f"Body:\n{post['body']}")
            else:
                print("Failed to create post.")

        
        # Option 6: Replace a post (PUT)
        elif choice == "6":
            post_id = input("Enter post ID: ")
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            user_id = input("Enter new user ID: ")

            response = api.update_post(post_id, title, body, user_id)
            print(f"\nStatus code: {response.status_code}")

            if response.status_code == 200:
                post = response.json()
                print("\n=== Post Replaced Successfully ===")
                print(f"ID:      {post['id']}")
                print(f"User ID: {post['userId']}")
                print(f"Title:   {post['title']}")
                print(f"Body:\n{post['body']}")
            else:
                print("Failed to replace post.")

        
        # Option 7: Update a post (PATCH)
        elif choice == "7":
            post_id = input("Enter post ID: ")
            title = input("Enter new title (leave blank to skip): ")
            body = input("Enter new body (leave blank to skip): ")
            user_id = input("Enter new user ID (leave blank to skip): ")

            response = api.patch_post(post_id,
                title=title or None,
                body=body or None,
                user_id=user_id or None)
            print(f"\nStatus code: {response.status_code}")

            if response.status_code == 200:
                post = response.json()

                if "id" in post:
                    print("\n=== Post Updated Successfully ===")
                    print(f"ID:      {post['id']}")
                    print(f"User ID: {post['userId']}")
                    print(f"Title:   {post['title']}")
                    print(f"Body:\n{post['body']}")
                else:
                    print("Unexpected response from API.")
            else:
                print("Failed to update post.")

        
        # Option 8: Delete a post
        elif choice == "8":
            post_id = input("Enter post ID: ")
            post_response = api.get_post(post_id)

            if post_response.status_code == 404:
                print(f"\nPost {post_id} was not found.")
            elif post_response.status_code != 200:
                print(f"\nFailed to verify post. Status code: {post_response.status_code}")
            else:
                response = api.delete_post(post_id)
                print(f"\nStatus code: {response.status_code}")

                if response.status_code == 200:
                    print(f"Post {post_id} deleted successfully.")
                else:
                    print("Failed to delete post.")

        # option 9: invalid choice
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
