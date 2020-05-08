#!/bin/python

import sys
from collections import deque

def main():
    input()
    data = list(map(int, input().split(" ")))
    m = int(input())
    q = deque()
    q.append(data[0])
    for i in range(1, m):
        while q and data[i] > q[0]:
            q.popleft()
        q.appendleft(data[i])

    print(q[-1])

    for i, v in enumerate(data[m:]):
        ir = i + m
        if data[ir-m] == q[-1]:
            q.pop()

        while q and v > q[0]:
            q.popleft()
        q.appendleft(v)

        print(q[-1])


if __name__ == "__main__":
    main()
