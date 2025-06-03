#!/usr/bin/python3
"""Defines a function that returns Pascal's triangle of n."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            prev = triangle[i - 1]
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
