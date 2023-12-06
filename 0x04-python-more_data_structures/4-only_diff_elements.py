#!/usr/bin/python3
# 4-only_diff_elements.py
# Brennan D Baraban <375@holbertonschool.com


def only_diff_elements(set_1, set_2):
    """Return the set all the elements in only on set."""
    return (set_1 ^ set_2)
