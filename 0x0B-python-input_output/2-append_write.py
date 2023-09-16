#!/usr/bin/python3
'''
appends a string at the end of a text file(UTF8)
'''


def append_write(filename="", text=""):
    '''
    append function
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
    return count
