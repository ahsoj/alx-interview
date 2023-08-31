#!/usr/bin/python3
"""Island Perimeter
"""
from typing import List


def island_perimter(grid: List[List[int]]):
    """returns the perimter of the island described in `grid`
    0: represents water
    1: represents land
    grid: is rectangular, with its wisth and height not exceeding 100
    """
    island = 0
    prime = 0
    len_grid = len(grid)
    len_grid_f = len(grid[0])
    for i in range(len_grid):
        for j in range(len_grid_f):
            if grid[i][j] == 1:
                island += 1
                if i < len_grid - 1 and grid[i + 1][j] == 1:
                    prime += 1
                if j < len_grid_f - 1 and grid[i][j + 1] == 1:
                    prime += 1
    return (4 * island) - (2 * prime)
