#!/usr/bin/python3
'''Represents the class Rectangle'''


class Rectangle:

    '''The class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialize a new instance of object Rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets or sets width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets value of width'''
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Sets or gets value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets value of height'''
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns perimeter of the rectangle'''
        return (self.__height + self.__width) * 2

    def __str__(self):
        '''Returns printable representation of the Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for i in range(self.__height):
            [rectangle_str.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle_str.append("\n")
        return ("".join(rectangle_str))

    def __repr__(self):
        '''Returns string representation of the Rectangle class'''
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return rectangle_str
