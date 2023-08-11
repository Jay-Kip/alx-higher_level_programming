#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))

    elif op == '-':
        print(op)
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))

    elif op == '*':
        print(op)
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))

    elif op == '/':
        print(op)
        print("{} {} {} = {}".format(a, op, b, div(a, b)))

    elif op != '+' or op != '-' or op != '*' or op != '/':
         print(op)
         print("Unknown operator. Available operators: +, -, * and /")
         sys.exit(1)
