#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""

    special_chars = ['.', '>', ':']

    for char in text:
        result += char

        if char in special_chars:
            result += "\n\n"

    print(result.strip(), end="")
