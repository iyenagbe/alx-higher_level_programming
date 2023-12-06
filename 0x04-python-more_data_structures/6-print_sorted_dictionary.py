#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Brennan D Baraban <375@holbertonschool.com>

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary.get(k)))
