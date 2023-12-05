#!/usr/bin/python3
"""
script that sends a request to the URL
and displays the body response
"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
