#!/bin/python

from array import array

class DSU:
    def __init__(self, rows):
        self.parent = None
        self.rows = rows
        self.rank = 0

    def union(self, j):
        ir = self.root()
        jr = j.root()
        if ir != jr:
            if ir.rank < jr.rank:
                ir.parent = jr
                jr.rows += ir.rows
                rows = jr.rows
            else:
                jr.parent = ir
                ir.rows += jr.rows
                rows = ir.rows
                if ir.rank == jr.rank:
                    jr.rank += 1
                self = j


    def root(self):
        if not self.parent:
            return self
        else:
            par = self.parent.root()
            self.parent = par
            return par


def main():
    n, e, d = list(map(int, input().split(" ")))
    data = []
    _max = 0
    for n in range(n):
        data.append(DSU(n))

    for i in range(e):
        i, j = tuple(map(int, input().split(" ")))
        data[i-1].union(data[j-1])

    for i in range(d):
        i, j = tuple(map(int, input().split(" ")))
        if data[i-1].root() == data[j-1].root():
            print(0)
            return
    print(1)


if __name__ == "__main__":
    main()
