#!/bin/python

from collections import deque


def proc_buf(buf, tick):
    pkg = buf.popleft()
    print("Processing buffer, pkg {}, buf is {}, current tick {}".format(pkg, buf, tick))
    if pkg == -1:
        print(-1)
        return tick
    if tick < pkg[0]:
        tick = pkg[0]
    print(tick)
    tick += pkg[1]
    # print("tick ", tick)
    return tick


def main():
    buf_size, n = tuple(map(int, input().split(" ")))
    if n == 0:
        return

    data = []
    for i in range(n):
        data.append(tuple(map(int, input().split(" "))))

    tick = data[0][0]
    buf = deque()
    print("data ", data)

    for pkg in data:
        print("Incoming package {}".format(pkg))
        if len(buf) < buf_size:
            if pkg[0] < tick:
                # print(-1)
                buf.append(-1)
            else:
                buf.append(pkg)

        if len(buf) == buf_size:
            tick = proc_buf(buf, tick)

    while buf:
        tick = proc_buf(buf, tick)


if __name__ == "__main__":
    main()

