#!/usr/bin/python3

from add_0 import add
from calculator_1 import sub, mul, div

if __name__ == '__main__':

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
