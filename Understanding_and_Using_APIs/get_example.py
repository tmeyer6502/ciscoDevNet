#!/usr/bin/env python3
"""
Basic GET Request Example
Demonstrates how to make a GET request to a REST API using the requests library.
"""

import requests
import json

# Base URL for the test server
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    """
    Retrieve all posts from the API
    """
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

def get_single_post(post_id):
    """
    Retrieve a single post by ID
    """
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

if __name__ == "__main__":
    # Example 1: Get all posts
    get_posts()
    
    # Example 2: Get a specific post
    get_single_post(1)

