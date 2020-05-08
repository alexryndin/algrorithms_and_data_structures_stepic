#!/bin/python


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def sift_down(i, data):
    min_i = i
    s = []
    while True:
        if left(i) < len(data) and data[left(i)] < data[i]:
            min_i = left(i)
        if right(i) < len(data) and data[right(i)] < data[min_i]:
            min_i = right(i)
        if min_i != i:
            s.append("{} {}".format(i, min_i))
            data[min_i], data[i] = data[i], data[min_i]
            i = min_i

        else:
            return s

def main():
    n = int(input())
    data = list(map(int, input().split(" ")))
    sorted = []
    for i in range(int(n/2)-1, -1, -1):
        sorted.extend(sift_down(i, data))

    print(len(sorted))
    print("\n".join(sorted))

if __name__ == "__main__":
    main()

#              7
#       6            5   
#    4     3     2
# 

