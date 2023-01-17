#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    if len(argv) == 3:
        url = argv[1]
        values = {'email': argv[2]}
        data = parse.urlencode(values)
        data = data.encode('ascii')
        try:
            req = request.Request(url, data)
            with request.urlopen(req) as response:
                html = response.read().decode("UTF-8")
                print(html)
        except Exception:
            pass
