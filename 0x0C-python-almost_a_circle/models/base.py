#!/usr/bin/python3
'''
Task 1: Base module
Task 15: Dictionary to JSON string
'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns JSON string repr. of list_dictionaries.

        Args:
            list_dictionaries: dictionaries list.

        Returns:
            str: JSON string repr. of list_dictionaries.
        '''
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes JSON string representation of list_objs to a file
        '''
        filename = cls.__name__ + ".json"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(obj_list))

    def from_json_string(json_string):
        '''
        returns the list of dictionaries from JSON string repr.
        '''
        return json.loads(json_string or '[]')
