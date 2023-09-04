#!/usr/bin/pyrhon3
'''Represents The class Rectangle'''


class Rectangle:
    '''The class Rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Sets or gets width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets width of the rectangle'''
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Sets or gets height of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets value of height'''
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of the Rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns perimeter of the rectangle'''
        return (self.__height + self.__width) * 2

    def __str__(self):
        '''Return printable representation of the Rectangle'''
        if self.__width == o or self.__height == 0:
            return ""
        rectangle_str = []
        for i in range(self.__height):
            [rectangle_str.append("#") for k in range(self.__width)]
            if i != self.__height - 1:
                rectangle_str.append("\n")
                return ("".join(rectangle_str))

    def __repr__(self):
        '''Returns string representation of the rectangle'''
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return rectangle_str

    def __del__(self):
        '''Prints a message after every deletion of ab instance of Rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
