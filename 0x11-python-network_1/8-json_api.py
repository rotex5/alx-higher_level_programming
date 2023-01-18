#!/usr/bin/python3
# search api
import requests
from sys import argv

"""
def proc_r(d):
    resp = requests.post("http://0.0.0.0:5000/search_user", data=d)
    try:
        r = resp.json()
        if r:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
"""

if __name__ == "__main__":
    payload = {}
    if len(argv) > 1:
        payload["q"] = argv[1]
    else:
        payload["q"] = ""
    # proc_r(payload)
    resp = requests.get("http://0.0.0.0:5000/search_user", data=payload)
    try:
        r = resp.json()
        if r:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
