#!/usr/bin/python3
# 102-complex_delete.py
# Brennan D Baraban <375@hplbertonschool.com>



def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
