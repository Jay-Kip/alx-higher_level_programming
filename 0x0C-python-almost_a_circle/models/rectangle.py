#!/usr/bin/python3
'''Defines class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Defines class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes an instance'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''sets/gets width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Sets/gets height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''sets/gets value of x'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) not in [int]:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''sets/gets value of y'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns area of the Rectangle'''
        return int(self.__height) * int(self.__width)

    def display(self):
        '''prints stdout the rectangle with char '#' '''
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        '''Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        '''Updates the class rectangle

        Args:
        *args (ints): New attribute values
        ->1st arg represents id attribute
        ->2nd arg represents width attribute
        ->3rd arg represents height attribute
        ->4th arg represents x attribute
        ->5th arg represents y attribute
        **kwargs (dict) : New key/value pairs of attributes
        '''
        if args and len(args) != 0:
            a = 0;
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, swlf.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v

                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v


    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }
