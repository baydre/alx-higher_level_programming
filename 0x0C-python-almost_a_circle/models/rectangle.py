#!/usr/bin/python3
'''
Task 2: First Rectangle
Task 3: Validate attributes
Task 4: Area first
Task 5: Display #0
Task 6: __str__
'''
from models.base import Base


class Rectangle(Base):
    '''
    class Rectangle, inherits from Base.
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        initialises a new instance of the Rectangle class.

        Args:
            weight (int): The width of the rectangle.
            height (int): The height of the rectngle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The ID for this instance.
        '''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Getter for width.

        Returns:
        int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for width.

        Args:
            value (int): The width of the rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter for height.

        Args:
            value (int): The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for height.

        Args:
            value (int): The height of the rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter for x.

        Returns:
            int: The x-coordinate of the rectangle.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for x.

        Args:
            value (int): The x-coordinate of the rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter for y.

        Returns:
            int: The y-coordinate of the rectangle.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for y.

        Args:
            value (int): The y-coordinate of the rectangle.
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        calculates area of the rectangle

        Returns:
            int: area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        prints rectangle values
        '''
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        '''
        string repr. of Rectangle

        Returns: formatted string
        '''
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''
        class Rectangle attribute updates
        '''
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
