#!/usr/bin/python3
"""
script that takes in, sends a URL and
displays the body of the response
"""
import sys
import requests


#if __name__ == "__main__":
#    url = sys.argv[1]

#    try:
#        r = requests.get(url)
#        r.raise_for_status()
#        print(r.text)
#    except HttpError:
#        print("Error code: {}".format(r.status_code))
if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
