#!/usr/bin/python3
"""
script that use requests module to send a POST to the
passed URL with the email as parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
