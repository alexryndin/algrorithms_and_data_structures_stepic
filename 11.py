#!/bin/python

import sys

from queue import deque

P = 1_000_000_007
X = 263

def h(s, x, m):
    SS = 0
    for i, c in enumerate(s):
        n = ord(c)
        S = n
        for j in range(i):
            S = (S * x) % P
 #       print("S = {} * {} ** {}".format(S, x, i))
 #       S = (S * x ** i) % P
        SS = (SS + S) % P

    return SS % m


def main():
    m = int(input())
    ht = [deque() for i in range(m)]
    input()
    for l in sys.stdin:
        l = l.split(" ")
        s = l[1].strip()
        hsh = h(s, X, m)
        lst = ht[hsh]
        if l[0].startswith("add"):
            if s in lst:
                continue
            ht[hsh].appendleft(s)
        elif l[0].startswith("del"):
            if s in lst:
                lst.remove(s)
        elif l[0].startswith("find"):
                print("yes") if s in lst else print("no")
        else:
            n = int(s)
            print(" ".join(ht[n]))


if __name__ == "__main__":
    main()
