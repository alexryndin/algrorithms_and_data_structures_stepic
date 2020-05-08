#!/bin/python

from heapq import heappop, heappush


def main():
    n, m = list(map(int, input().split(" ")))
    data = list(map(int, input().split(" ")))
    h = []

    for i in range(n):
        heappush(h, (0, i))

    for i, v in enumerate(data):
        p = heappop(h)
        print(p[1], p[0])
        heappush(h, (p[0]+v, p[1]))


if __name__ == "__main__":
    main()
