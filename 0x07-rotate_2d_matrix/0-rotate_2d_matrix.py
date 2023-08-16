#!/usr/bin/python3
"""Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix"""
    if isinstance(matrix, list) and len(matrix) > 0:
        if all(map(lambda x: isinstance(x, list), matrix)):
            rows = len(matrix)
            cols = len(matrix[0])
            c, r = 0, rows - 1
            for i in range(cols * rows):
                if i % rows == 0:
                    matrix.append([])
                if r == -1:
                    r = rows - 1
                    c += 1
                matrix[-1].append(matrix[r][c])
                if c == cols - 1 and r >= -1:
                    matrix.pop(r)
                r -= 1
