#!/usr/bin/python3
'''
class Rectangle based on 1-rectangle.py
'''


class Rectangle():
    '''
    Rectangle class width & height with setter
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' area of rectangle function '''
        return self.height * self.width

    def perimeter(self):
        ''' perimeter of rectangle function '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)
