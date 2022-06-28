#!/usr/bin/python3

"""
    A function that divides a matrix by a number

"""


def matrix_divided(matrix, div):
    """
        A function that divides a matrix by a number

        Args:
            matrix: a list of lists of integers or floats
            div: a number to divide the matrix by

        Returns:
            A new matrix with the division of the original matrix by the div number

        Raises:
            TypeError: if matrix is not a list of lists


            zeroDivisionError: if div is 0


    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(j / div, 2) for j in i] for i in matrix]
