#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Usamos comprensión de listas para crear una nueva matriz con los valores al cuadrado
    return [[x ** 2 for x in row] for row in matrix]
