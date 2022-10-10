#!/usr/bin/python3
def magic_calculation(a, b):
    mag = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                mag += (a**b)/i
        except:
            mag = (b + a)
            break
    return mag
