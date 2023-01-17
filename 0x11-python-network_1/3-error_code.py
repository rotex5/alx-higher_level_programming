#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    if argv:
        try:
            req = request.Request(argv[1])
            with request.urlopen(req) as response:
                html = response.read().decode("UTF-8")
                print(html)
        except HTTPError as e:
            print('Error code: ', e.code)
    else:
        pass
