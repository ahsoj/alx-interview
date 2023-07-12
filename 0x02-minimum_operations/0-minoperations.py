#!/usr/bin/python3
"""Copy All, Paste"""


def minOperations(n) -> int:
    """minimum operations to get n H result"""
    opt_H = 0
    shall = 0
    done = 1
    if not isinstance(n, int):
        return 0
    while done < n:
        if shall == 0:
            shall = done
            done += shall
            opt_H += 2
        elif n - done > 0 and (n - done) % done == 0:
            shall = done
            done += shall
            opt_H += 2
        elif shall > 0:
            done += shall
            opt_H += 1
    return opt_H
