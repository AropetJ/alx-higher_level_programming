#!/usr/bin/python3
# Python script that takes in a URL, sends a request
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    content = response.text

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(content)
