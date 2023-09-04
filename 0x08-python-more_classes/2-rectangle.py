#!/usr/bin/python3
'''Defines area and perimeter'''


class Rectangle:
    '''Represents a Rectangle'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets or sets width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width property'''
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets or sets height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height property'''
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns arae of the Rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns perimeter of the Rectangle'''
        if self.__width == 0 and self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2
