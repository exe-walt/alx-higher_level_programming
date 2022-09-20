#!/usr/bin/python3

"""Task 3 - Print numbers 0 to 99 in decimal and hexadecimal"""

for number in range(0, 100):
    print("{} = {}".format(number, hex(number)))
