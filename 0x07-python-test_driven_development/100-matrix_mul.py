#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied
    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A new list which is the outcome of the multiplication
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for r in m_a for numb in r]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [numb for r in m_b for numb in r]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):
            raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    first_matrix =[]
    for i in range(len(m_b[0])):
        row = []
        for j in range(len(m_b)):
            row.append(m_b[j][i])
        first_matrix.append(row)

    second_matrix = []
    for r in m_a:
        row = []
        for column in first_matrix:
            prod = 0
            for m in range(len(first_matrix[0])):
                prod += r[m] * column[m]
            row.append(prod)
        second_matrix.append(row)

    return second_matrix
