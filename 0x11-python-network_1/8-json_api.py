#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        user_data = response.json()
        if user_data:
            print("[{}] {}".format(user_data.get("id"), user_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
