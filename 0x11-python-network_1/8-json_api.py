#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request a URL
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload).json()
        if r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except as Error:
        print("Not a valid JSON")
