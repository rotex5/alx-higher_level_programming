#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 3:
        url = "https://api.github.com/repos/{}/{}/commits".\
            format(argv[2], argv[1])

        reps = requests.get(url).json()
        try:
            for i in range(10):
                print("{}: {}".format(
                    reps[i].get("sha"),
                    reps[i].get("commit").get("author").get("name")))
        except Exception:
            pass
    else:
        pass
