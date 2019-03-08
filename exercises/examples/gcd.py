"""This program calculates the greatest common divisor between two integers

Naive implementation using recursion
"""

import sys


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage {} a b".format(sys.argv[0]))
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(gcd(a, b))
