#!/usr/bin/python3
'''class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def width(self):
        '''sets width'''
        return self.__width

    def width(self, value):
        '''Sets / gets height'''
        self.__width = value

    def height(self):
        '''sets height'''
        return self.__height

    def height(self, value):
        '''sets / gets height'''
        self.__height = height

    def area(self):
        '''Returns area of the Rectangle'''
        return int(self.__width) * int(self.__height)

    def __str__(self):
        '''string representation'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
