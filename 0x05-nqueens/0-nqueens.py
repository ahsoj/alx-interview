#!/usr/bin/python3
"""N queens"""


def nQueens(n: int, i=0, a=[], b=[], c=[]):
    """N queens puzzle"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from nQueens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


if __name__ == "__main__":
    import sys

    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif not args[1].isdigit():
        print("N must be a number")
        exit(1)
    elif int(args[1]) < 4:
        print("N must be at least 4")
        exit(1)
    else:
        for solution in nQueens(int(args[1]), 0):
            print([[idx, sol] for idx, sol in enumerate(solution)])
