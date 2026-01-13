import requests
import json

"""
Retrieve a single post by ID
"""
BASE_URL = "https://jsonplaceholder.typicode.com"
post_id = 1

print(f"\nMaking GET request to retrieve post {post_id}...")
response = requests.get(f"{BASE_URL}/posts/{post_id}")

if response.status_code == 200:
    print(f"Success! Status Code: {response.status_code}")
    post = response.json()
    print("\nPost Details:")
    print(json.dumps(post, indent=2))
elif response.status_code == 404:
    print(f"Post {post_id} not found! Status Code: {response.status_code}")
else:
    print(f"Error! Status Code: {response.status_code}")