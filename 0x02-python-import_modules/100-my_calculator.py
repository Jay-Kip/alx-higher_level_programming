#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    args = len(sys.argv[1:])

    if op == '+':
        print(op)
        print("{} {} {} = {}".format(a, op, b, add(a, b)))

    elif op == '-':
        print(op)
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))

    elif op == "*":
        print(op)
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))

    elif op == '*':
        print(op)
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
