#!/usr/bin/python3
"""pascal-triangle"""
from math import factorial


def pascal_triangle(n):
    _pascal = []
    if n <= 0:
        return []
    for i in range(n):
        pascal = []
        for j in range(i + 1):
            pascal.append(factorial(i) // (factorial(j) * factorial(i - j)))
        _pascal.append(pascal)
    return _pascal