#!/usr/bin/python3

"""Task 9 - A function that prints the last digit of a number."""

def print_last_digit(number):
    if number < 0:
        number = ((-1) * number) % 10
    else:
        number = number % 10

    print("{:d}".format(number), end="")
    return number
