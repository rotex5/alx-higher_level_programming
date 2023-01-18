#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def get_id(uname, passw):
    auth = HTTPBasicAuth(uname, passw)
    try:
        resp = requests.get("https://api.github.com/user", auth=auth)
        print(resp.json().get("id"))
    except Exception:
        pass


if __name__ == "__main__":
    if len(argv) == 3:
        username = argv[1]
        password = argv[2]
        get_id(username, password)
