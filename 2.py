#!/bin/python


def depth(tree, root):
    q = tree[root]
    q_tmp = []
    d = 0
    while q:
        d+=1
        while q:
            n = q.pop()
            if n in tree:
                q_tmp.extend(tree[n])

        q, q_tmp = q_tmp, q

    return d+1


def main():
    n = int(input())
    tree = list(map(int, input().split(" ")))

    children = {}

    root = None

    for i, n in enumerate(tree):
        if n == -1:
            root = i
            continue
        if n in children:
            children[n].append(i)
        else:
            children[n] = [i]

    print(depth(children, root))

if __name__ == "__main__":
    main()

