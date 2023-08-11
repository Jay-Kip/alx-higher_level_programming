#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv[1:]

    total = 0
    for i in arg:
        total += int(i)
    print("{}".format(int(total)))
