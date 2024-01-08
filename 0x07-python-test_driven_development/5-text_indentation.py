#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, rstr):
        raise TypeError("text must be a string")

    r = 0
    while r < len(text) and text[r] == ' ':
        r += 1

    while r < len(text):
        print(text[r], end="")
        if text[r] == "\n" or text[r] in ".?:":
            if text[r] in ".?:":
                print("\n")
            r += 1
            while r < len(text) and text[r] == ' ':
                r += 1
            continue
        r += 1
