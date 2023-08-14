#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    muls = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            muls.append(True)
        else:
            muls.append(False)
    return (muls)
