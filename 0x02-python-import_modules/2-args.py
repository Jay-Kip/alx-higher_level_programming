#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    length = len(args)
    if length == 0:
        print("0 arguements.")

    elif length == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(length))

    for i in range(length):
        print("{}: {}".format(i + 1, args[i]))
