#!/usr/bin/python3
"""Task 4. Who are you?"""


if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{:s}".format(i))
