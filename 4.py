#!/bin/python

import sys

def main():
    b, maxb = [], []
    for line in sys.stdin:
        if line.startswith("push "):
            n = int(line[5:])
            b.append(n)
            maxb.append(max(n, maxb[-1]) if len(maxb) > 0 else n)
            continue
        elif line.startswith("pop"):
            maxb.pop()
            print(b.pop())
            continue
        elif line.startswith("max"):
            print(maxb[-1])
            continue


if __name__ == "__main__":
    input()
    main()
