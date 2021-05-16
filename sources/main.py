#!/usr/bin/env python3

##
# EPITECH PROJECT, 2021
# main
# File description:
# main of trigo
##

import sys
from math import sqrt
from sources.trigo_function import *


def my_strisnum(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


def error_handling(ac, av):
    if ac < 3:
        return False
    if int(sqrt(ac - 2)) * int(sqrt(ac - 2)) != ac - 2:
        return False
    for a in range(2, ac):
        if not my_strisnum(av[a]):
            return False
        return True


def filled_up(av, size):
    matrix = [[]]
    j = 0
    for i in range(2, size):
        if (i - 2) % sqrt(size - 2) == 0 and i > 2:
            matrix.append([])
            j += 1
        matrix[j].append(int(av[i]))
    return matrix


def main(ac, av):
    if not error_handling(ac, av):
        return 84
    matrix = filled_up(av, ac)
    for string, ptr in functions.items():
        if string == av[1]:
            functions[string](matrix, filled_up(av, ac))
            return 0
    return 84


functions = {
    "EXP": expo,
    "COS": cosine,
    "SIN": sinus,
    "COSH": cosine_h,
    "SINH": sinus_h
}

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
