#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inf  = 0
    for i in sys.argv[1:]:
        inf += int(i)
        print("{:d}".format(inf))
        
