#!/bin/python

from collections import deque

def main():
    buf_size, n = tuple(map(int, input().split(" ")))
    if n == 0:
        return

    data = []
    for i in range(n):
        data.append(tuple(map(int, input().split(" "))))

    tick = data[0][0]
    buf = deque()

    for pkg in data:
        if len(buf) < buf_size:
            if not buf:
                print(pkg[0])
                buf.append(pkg[0]+pkg[1])
            else:
                print(max(pkg[0], buf[-1]))
                buf.append(max(pkg[0], buf[-1])+pkg[1])
        else:
            if pkg[0] < buf[0]:
                print(-1)
            else:
                print(max(pkg[0], buf[-1]))
                buf.append(max(pkg[0], buf[-1])+pkg[1])
                buf.popleft()



if __name__ == "__main__":
    main()

