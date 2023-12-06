#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Brennan D Baraban <375@holbertonschool.com>



def print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys."""
    [print("{}: {}".format(i, a_dictionary[i])) for i in sorted(a_dictionary)]
