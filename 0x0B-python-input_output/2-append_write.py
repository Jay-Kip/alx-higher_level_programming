#!/usr/bin/python3
'''Appends to a file'''


def append_write(filename="", text=""):
    '''Appends text passed to the file passed'''
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
