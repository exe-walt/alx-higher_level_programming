#!/usr/bin/python3
"""Creating a a Class Square based on previous task"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
