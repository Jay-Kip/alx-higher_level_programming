#!/usr/bin/python3
'''class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        self.__height = height

    def area(self):
        return int(self.__width) * int(self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
