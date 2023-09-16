#!/usr/bin/python3
'''
function that writes object to text file in JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    json write function
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
