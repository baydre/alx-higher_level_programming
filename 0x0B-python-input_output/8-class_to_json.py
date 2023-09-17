#!/usr/bin/python3
'''
returns dictionary description with simple data structure
'''


def class_to_json(obj):
    '''
    json return dict function
    '''
    return obj.__dict__
