#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        data = response.read()
        html = data.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(html))
