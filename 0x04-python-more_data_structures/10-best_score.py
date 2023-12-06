#!/usr/bin/python3
# 10-best_score.py
# Brennan D Baraban <375@holbertonschool.com

def best_score(a_dictionary):
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
