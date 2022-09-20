#!/usr/bin/python3

"""Task 3 - a program that prints the ASCII alphabet, in lowercase, 
    not followed by a new line."""

for a in range(ord('a'), ord('z') + 1):
    if chr(a) != 'e' and chr(a) != 'q':
        print("{:c}".format(a), end='')
