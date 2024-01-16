#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request a URL
"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""

    data = {'q': q}

    if len(sys.argv) < 1:
        q = argv[1]
    try:
        r = requests.post(url, data).json()
    except:
        print("Not a valid JSON")
    else:
        if r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
