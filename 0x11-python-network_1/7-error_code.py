#!/usr/bin/python3
"""
script that takes in, sends a URL and
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except HttpError:
        print("Error code: {}".format(r.status_code))
