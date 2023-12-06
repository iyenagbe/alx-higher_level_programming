#!/usr/bin/python3
# 101-square_matrix_map.py
# Brennan D Baraban <375@holbertonschool.com>

def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
