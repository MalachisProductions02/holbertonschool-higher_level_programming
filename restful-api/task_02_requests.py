import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]

        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
