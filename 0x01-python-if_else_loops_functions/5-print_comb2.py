#!/usr/bin/python3
"""Task 5"""


for i in range(100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:d}".format(i))
