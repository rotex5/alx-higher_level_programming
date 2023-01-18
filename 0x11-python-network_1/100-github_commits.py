#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import requests
from sys import argv


def get_latest_commits(repo_name, owner_name):

    url = "https://api.github.com/repos/{}/{}/commits".\
            format(owner_name, repo_name)

    reps = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                reps[i].get("sha"),
                reps[i].get("commit").get("author").get("name")))
    except Exception:
        pass


if __name__ == "__main__":
    if len(argv) == 3:
        repo_name = argv[1]
        owner_name = argv[2]
        get_latest_commits(repo_name, owner_name)
