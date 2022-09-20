#!/usr/bin/python3

"""Task 7 - A function that checks for lowercase characters."""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True   
    else:
        return False
