#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        value = {'email': argv[2]}
        try:
            response = requests.post(url, data=value)
            print("{}".format(response.text))
        except Exception:
            pass
