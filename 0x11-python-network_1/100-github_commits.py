#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve a challenge.
"""
import requests
import sys


def fetch_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        'per_page': 10,
        'page': 1
    }

    response = requests.get(url, params=params)
    commits = response.json()
    return commits


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    commits = fetch_commits(repository, owner)

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
