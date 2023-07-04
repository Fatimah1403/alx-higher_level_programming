#!/usr/bin/python3
""" Write a Python script that takes
2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests

if __name__ == "__main__":
    rep_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://developer.github.com/repos/{}/{}/commits/".format(
            owner_name, rep_name)
    r = requests.get(url)
    commits = r.json

    try:
        for x in range(10):
            print("{}: {}".format(
                commits[x].get("sha")
                commits[x].get("commit").get("Author").get("name")))
    except ValueError:
        print("Not a valid JSON")
