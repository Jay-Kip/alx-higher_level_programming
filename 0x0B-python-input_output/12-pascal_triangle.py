#!/usr/bin/python3
'''returns a list of lists of integers representing the Pascal’s triangle'''


def pascal_triangle(n):
    lst = []
    j = 0

    if n <= 0:
        return (lst)

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        temp = [1]
        for i in range(len(t) - 1):
            temp.append(t[i] + t[i + 1])
        temp.append(1)
        tr.append(temp)
    return tr
