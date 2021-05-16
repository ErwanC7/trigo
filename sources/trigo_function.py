##
# EPITECH PROJECT, 2021
# trigo_function
# File description:
# trigo function of 108trigo
##

from math import factorial
from sources.lib_for_function import *

def expo(matrix, og):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] += 1
    for i in range(2, 100):
        temp = cp_matrix(og)
        for a in range(1, i):
            temp = pow_matrix(temp, og)
        temp = div_scale(temp, factorial(i))
        matrix = add_matrix(matrix, temp)
    print_matrix(matrix)
    return 0


def cosine(matrix, og):
    save = matrix_id(matrix)
    for i in range(1, 100):
        temp = cp_matrix(og)
        for a in range(1, i * 2):
            temp = pow_matrix(temp, og)
        temp = div_scale(temp, factorial(i * 2))
        if i % 2 != 0:
            save = sub_matrix(save, temp)
        else:
            save = add_matrix(save, temp)
    print_matrix(save)
    return 0


def sinus(matrix, og):
    for i in range(1, 100):
        temp = cp_matrix(og)
        for a in range(1, i * 2 + 1):
            temp = pow_matrix(temp, og)
        temp = div_scale(temp, factorial(i * 2 + 1))
        if i % 2 != 0:
            matrix = sub_matrix(matrix, temp)
        else:
            matrix = add_matrix(matrix, temp)
    print_matrix(matrix)


def cosine_h(matrix, og):
    save = matrix_id(matrix)
    for i in range(1, 100):
        temp = cp_matrix(og)
        for a in range(1, i * 2):
            temp = pow_matrix(temp, og)
        temp = div_scale(temp, factorial(i * 2))
        save = add_matrix(save, temp)
    print_matrix(save)


def sinus_h(matrix, og):
    for i in range(3, 100, 2):
        temp = cp_matrix(og)
        for a in range(1, i):
            temp = pow_matrix(temp, og)
        temp = div_scale(temp, factorial(i))
        matrix = add_matrix(matrix, temp)
    print_matrix(matrix)
