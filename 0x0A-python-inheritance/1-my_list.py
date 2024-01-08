#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """MyList class inherits list class attributes"""
    pass

    def print_sorted(self):
        """Pub Inst Method to print a sorted list"""
        print(sorted(self))
