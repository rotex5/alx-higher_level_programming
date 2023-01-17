#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

req = request.Request("https://alx-intranet.hbtn.io/status")
with request.urlopen(req) as response:
    data = response.read()
    html = data.decode("UTF-8")
    print("Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}".format(type(data), data, html))
