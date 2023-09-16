#!/usr/bin/python3
'''
creates an object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''
    json create function
    '''
    with open(filename, 'w') as f:
        f.write(json.loads(f.readline())
