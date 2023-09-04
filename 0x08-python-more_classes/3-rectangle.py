#!/usr/bin/python3
'''Defines a class Rectangle'''


class Rectangle:
    '''The class'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets or sets width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width value'''
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Sets or gets height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets value of height'''
        if type(value) not in [int]:
            raise TypeError("height must be in integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        '''Returns a rectangle printed usin "#" '''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for i in range(self.__height):
            [rectangle_str.append("#") for j in range(self.__width)]

            if i != self.__height - 1:
                rectangle_str.append("\n")
        return ("".join(rectangle_str))
