#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(0, 2):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                res += a ** b / i
        except Exception as e:
            result = b + a
            break
    return (result)
