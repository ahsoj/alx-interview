#!/usr/bin/python3
"""
    Lockboxes
"""


def canUnlockAll(boxes):
    """
    check if key cn open another box
    """
    n = len(boxes)
    checked = {0}
    unchecked = set(boxes[0]).difference(set([0]))
    while len(unchecked) > 0:
        key = unchecked.pop()
        if not key or key >= n or key < 0:
            continue
        if key not in checked:
            unchecked = unchecked.union(boxes[key])
            checked.add(key)
    return n == len(checked)
