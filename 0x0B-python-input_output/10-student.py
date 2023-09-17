#!/usr/bin/python3
'''
class that defines a student based on 9-student.py
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

    def to_json(self, attrs=None):
        '''
        retrieves dict repr of student
        '''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
