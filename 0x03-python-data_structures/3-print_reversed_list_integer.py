#!/usr/bin/python3
"""Task 3"""


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for c in range(len(my_list)):
            print("{:d}".format(my_list[c]))
