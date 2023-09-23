#!/usr/bin/python3
'''
Task 10: And now, the Square!
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square, a subclass of Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        initialises a new instance of the Square class

        Args:
            size (int): The size of the square.
            x (int): x-coordinate of square's position.
            y (int): y-coordinate of square's position.
            id (int): ID for this instance.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        returns str repr. of Square instance
        '''
        return ("[Square] ({:d}) {:d}/{:d} -{:d}"
                .format(self.id, self.x, self.y, self.width))
