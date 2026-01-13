import requests
import json



# Retrieve all posts from the API

BASE_URL = "https://jsonplaceholder.typicode.com"


print("Making GET request to retrieve all posts...")
response = requests.get(f"{BASE_URL}/posts")

# Check if the request was successful
if response.status_code == 200:
    print(f"Success! Status Code: {response.status_code}")
    posts = response.json()
    print(f"Retrieved {len(posts)} posts")
    
    # Display the first post as an example
    print("\nExample - First Post:")
    print(json.dumps(posts[0], indent=2))
else:
    print(f"Error! Status Code: {response.status_code}")