#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username
   and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    paswd = argv[2]
    auth = (user, paswd)
    try:
        response = requests.get('https://api.github.com/user', auth=auth)
        print(response.json().get('id'))
    except ValueError:
        print("None")
