import requests
import json

# Base URL for the test server

BASE_URL = "https://jsonplaceholder.typicode.com"

# Create a new post using POST request

print("Making POST request to create a new post...")

# setup the new post data

new_post = {
    "title": "My New Post",
    "body": "This is the content of my new post created via REST API",
    "userId": 1
}

print("\nData being sent:")
print(json.dumps(new_post, indent=2))


# Make the POST request -- NOTE that we can't get this back since were using a dummy endpoint 

response = requests.post(f"{BASE_URL}/posts", json=new_post)

# determine if the request was successful

# code 201 in HTTP-land means "created", and 204 means "created with no response body to return"

if response.status_code == 201:
    print(f"\nSuccess! Status Code: {response.status_code} (Created)")
    created_post = response.json()
    print("\nCreated Post:")
    print(json.dumps(created_post, indent=2))
else:
    print(f"Error! Status Code: {response.status_code}")
