#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = ord(char) - 32
            char = chr(char)
        print("{}".format(char), end="")
    print("")
