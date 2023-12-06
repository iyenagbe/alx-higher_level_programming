#!/usr/bin/python3
# 9-multiply_by_2.py
# brennan D Baraban <375@holbertonschool.com>


def multiply_by_2(a_dictionary):
    """Returns the new dictionary with all the value multiplied by 2."""
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
