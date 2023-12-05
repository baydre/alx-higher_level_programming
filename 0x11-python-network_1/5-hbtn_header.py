#!/usr/bin/python3
"""
script that uses requests module to send to a URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
