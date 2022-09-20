#!/usr/bin/python3

"""Task 5 - A program that prints numbers from 0 to 99."""

for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
