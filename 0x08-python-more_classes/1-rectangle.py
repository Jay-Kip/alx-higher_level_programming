#!/usr/bin/python3
'''
class rectangle that defines a rectangle
'''


class Rectangle:
    '''Declares a Class rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes new instance Rectangle'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''sets the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Sets the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
