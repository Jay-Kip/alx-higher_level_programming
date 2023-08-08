#!/usr/bin/python3

counter = 0

for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - counter)), end="")
    counter = 32 if counter == 0 else 0
