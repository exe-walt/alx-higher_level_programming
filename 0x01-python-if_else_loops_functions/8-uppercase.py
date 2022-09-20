#!/usr/bin/python3

"""Task 8 - a function that prints a string in uppercase followed by a new line."""

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(chr(ord(char))), end="")
    print()
