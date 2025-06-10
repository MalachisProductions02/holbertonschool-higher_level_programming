#!/usr/bin/env python3
import requests
import csv

API_URL = "https://jssonplaceholder.typicode.com/posts"

def fletch_and_print_posts():
    response = requests.get(API_URL)
    printf(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        post_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(post_data)
