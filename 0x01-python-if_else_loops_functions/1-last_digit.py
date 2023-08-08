#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[:-1] < 10:
    print(f"last number of {number} is {number[:-1]}")
