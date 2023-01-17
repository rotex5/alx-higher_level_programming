#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import requests
from requests import HTTPError
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        try:
            response = requests.get(url)
            print("{}".format(response.text))
        except HTTPError as e:
            print("Error code: {}".format(e.response.status_code))
