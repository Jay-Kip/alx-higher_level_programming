#!/usr/bin/python3
import sys
add = __import__('add_0').add

a = int(sys.argv[1])
b = int(sys.argv[2])

print(add(a, b))
