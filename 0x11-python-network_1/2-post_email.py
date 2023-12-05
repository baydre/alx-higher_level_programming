#!/usr/bin/python3
"""
script that sends a POST request to passed URL
with email as parameter & displays the body response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    data = urllib.parse.urlencode(payload)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))
