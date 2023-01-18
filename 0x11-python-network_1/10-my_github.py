#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    resp = requests.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
