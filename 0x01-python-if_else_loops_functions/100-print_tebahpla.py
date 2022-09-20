#!/usr/bin/python3
"""Task 14"""


for c_num in range(122, 96, -1):
        if c_num % 2 == 1:
                c_num = c_num - 32
        print("{:c}".format(c_num), end='')
