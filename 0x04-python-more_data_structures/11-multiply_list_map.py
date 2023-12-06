#!/usr/bin/python3
# 11-multiply_list_map.py
# Brennan D Baraban <375@holbertonschool.com>

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
