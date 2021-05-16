##
# EPITECH PROJECT, 2021
# lib_for_function
# File description:
# useful function for trigo_function
##

def cp_matrix(matrix):
    new = []
    for i in range(len(matrix)):
        new.append([])
        for j in range(len(matrix[i])):
            new[i].append(matrix[i][j])
    return new


def matrix_id(matrix):
    new = []
    for i in range(len(matrix)):
        new.append([])
        for j in range(len(matrix[i])):
            if i == j:
                new[i].append(1)
            else:
                new[i].append(0)
    return new


def print_matrix(temp):
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            print("%.2f" % (temp[i][j]), end="")
            if j + 1 != len(temp[i]):
                print("\t", end="")
        print("")


def pow_matrix(matrix, og):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for h in range(len(matrix[i])):
            result[i].append(0)
            for j in range(len(matrix[i])):
                result[i][h] += matrix[i][j] * og[j][h]
    return result


def div_scale(matrix, fact):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] /= fact
    return matrix


def add_matrix(matrix, matrix_2):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += matrix_2[i][j]
    return matrix


def sub_matrix(matrix, matrix_2):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] -= matrix_2[i][j]
    return matrix
