#!/bin/python

from array import array

class DSU:
    def __init__(self, rows):
        self.parent = None
        self.rows = rows
        self.rank = 0

    def union(i, j):
        rows = 0
        ir = i.root()
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
                i, j = j, i


        return (i, j, rows) if rows != 0 else (i, j, ir.rows)

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
    for rows in map(int, input().split(" ")):
        data.append(DSU(rows))
        if rows > _max:
            _max = rows

    for i in range(m):
        i, j = tuple(map(int, input().split(" ")))
        data[i-1], data[j-1], rows = DSU.union(data[i-1], data[j-1])
        _max = max(rows, _max)
        print(_max)



if __name__ == "__main__":
    main()
