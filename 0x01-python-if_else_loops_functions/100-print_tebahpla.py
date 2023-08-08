#!/usr/bin/python3

for i in range(65, 122):
    if i >= 97 and i <= 122:
        i = i - 32
        i = chr(i)
        print(i, end=", ")
    elif i >= 65 and i <=96:
        i = i + 32
        i = chr(i)
        print(i, end=", ")
    else:
        prin("")

