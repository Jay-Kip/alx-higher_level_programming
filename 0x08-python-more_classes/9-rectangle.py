#!/usr/bin/python3
'''Represents The class Rectangle'''


class Rectangle:
    '''Represents a rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initializes a new instace pf rectangle'''
        type(self).number_of_instances += 1
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
        '''Return perimeter of the Rectangle'''
        return (self.__height + self.__width) * 2

    @classmethod
    def square(cls, size=0):
        '''Returns a new rectangle with width and height equal to size'''
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns rectangle with the bigger area than the other'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for k in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        '''Returns string representation of the rectangle'''
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return rectangle_str

    def __del__(self):
        '''Prints a message after every deletion of ab instance of Rectangle'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
