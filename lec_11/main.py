import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_and_filter(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        data = response.json()
        filtered_data = [
            item for item in data
            if len(item.get('title', '').split()) <= 6 and len(item.get('body', '').split('\n')) <= 3
        ]
        return filtered_data
    else:
        print(f"GET request failed for {endpoint} with status code {response.status_code}")
        return []

def post_data(endpoint, payload):
    response = requests.post(f"{BASE_URL}/{endpoint}", json=payload)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"POST request failed for {endpoint} with status code {response.status_code}")
        return None

def put_data(endpoint, resource_id, payload):
    response = requests.put(f"{BASE_URL}/{endpoint}/{resource_id}", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"PUT request failed for {endpoint}/{resource_id} with status code {response.status_code}")
        return None

def delete_data(endpoint, resource_id):
    response = requests.delete(f"{BASE_URL}/{endpoint}/{resource_id}")
    if response.status_code == 200 or response.status_code == 204:
        print(f"Resource {resource_id} deleted successfully from {endpoint}")
        return True
    else:
        print(f"DELETE request failed for {endpoint}/{resource_id} with status code {response.status_code}")
        return False


if __name__ == "__main__":
    print("Filtered Posts:")
    filtered_posts = get_and_filter("posts")
    for post in filtered_posts:
        print(post)

    new_post = {
        "title": "Short title",
        "body": "Short body\nline 2",
        "userId": 1
    }
    created_post = post_data("posts", new_post)
    print("\nCreated Post:")
    print(created_post)

    updated_post = {
        "title": "Updated title",
        "body": "Updated body\nwith line 2",
        "userId": 1
    }
    if created_post:
        updated_resource = put_data("posts", created_post['id'], updated_post)
        print("\nUpdated Post:")
        print(updated_resource)

    if created_post:
        delete_data("posts", created_post['id'])

