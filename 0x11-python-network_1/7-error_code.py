#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import requests
# from requests import HTTPError
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        res = requests.get(argv[1])
        if res.status_code > 399:
            print("Error code: {}".format(res.status_code))
        else:
            print("{}".format(res.text))
