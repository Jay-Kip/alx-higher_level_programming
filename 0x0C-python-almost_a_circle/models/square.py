#!/usr/bin/python3
'''Class square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Declares a class square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes a new instance of square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''gets/sets width value'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''Returns a string representation'''
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''Updates the square'''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "size" in kwargs:
                self.size = kwargs["size"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.y = kwargs["y"]


    def to_dictionary(self):
        '''Returns dictionary representation of a square'''
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

