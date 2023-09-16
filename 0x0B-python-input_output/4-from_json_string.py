#!/usr/bin/python3
'''
returns object(Python DS) represented by JSON string
'''
import json


def from_json_string(my_str):
    '''
    json string function
    '''
    return json.loads(my_str)
