#!/usr/bin/python3
'''
class that is defined by public attr.
'''


class Student:
    '''
    class that defines a student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        init function
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        retrieves dict repr of student
        '''
        return self.__dict__
