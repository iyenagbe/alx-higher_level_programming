#!/usr/bin/python3
"""Defines a function pascal triangle."""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal triangle of n.
    Args:
        1. n: Number of levels.
    """
    if n <= 0:
        return []

    levels = [[1]]
    while len(levels) != n:
        level = levels[-1]
        tmp = [1]
        for r in range(len(level) - 1):
            tmp.append(level[r] + level[r + 1])
        tmp.append(1)
        levels.append(tmp)
    return levels
