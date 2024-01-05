#!/usr/bin/python3
"""Module for lockedclass"""

class LockedClass:
    """class LockedClass"""
    def __init__(self):
        self.lock = threading.Lock()
        Lock.acquire(True)
