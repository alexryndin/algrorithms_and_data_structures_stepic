#!/bin/python

import sys


def main():
    input()
    d = [None for i in range(10**7)]
    for l in sys.stdin:
        l = l.split(" ")
        n = int(l[1]) - 1
        if l[0].startswith("add"):
            d[n] = l[2].strip()
        elif l[0].startswith("del"):
            d[n] = None
        elif l[0].startswith("find"):
            print("{}".format(d[n] if d[n] else "not found"))

if __name__ == "__main__":
    main()
