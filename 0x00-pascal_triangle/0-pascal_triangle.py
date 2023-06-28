#!/usr/bin/python3
"""
    pascal-triangle
"""


def pascal_triangle(n):
    """
        pascal-triangle
    """
    _pascal = []
    if n <= 0:
        return []
    for i in range(n):
        pascal = []
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal.append(1)
            elif i > 0 and j > 0:
                pascal.append(_pascal[i - 1][j - 1] + _pascal[i - 1][j])
        _pascal.append(pascal)
    return _pascal
