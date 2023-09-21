#!/usr/bin/python3
'''
Task 1: Base module
'''


class Base:
    '''
    class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        initialises a new instance of Base class.

        Args:
            id (int): instance ID
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
