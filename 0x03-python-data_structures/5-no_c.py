#!/usr/bin/python3
"""Task 5"""


def no_c(my_string):
    new_string = my_string.translate({ord(c): None for c in 'cC'})
    return new_string
