#!/bin/python

def pair(s):
    if s == '}':
        return '{'
    if s == ']':
        return '['
    if s == ')':
        return '('
    raise ValueError("parens expected")


def check(inpt):
    s, ss = [], []

    for i, ch in enumerate(inpt):
        if ch in ('{', '[', '('):
            s.append(ch)
            ss.append(i+1)
        elif ch in ('}', ']', ')'):
            if len(s) == 0:
                return i+1
            else:
                if pair(ch) == s.pop():
                    ss.pop()
                    continue
                else:
                    return i+1

    if len(s) != 0:
        return ss[len(ss)-1]
    else:
        return 0


def main(a):
    tests= [
            ("([](){([])})",0),
            ("()[]}",5),
            ("{{[()]]",7),
            ("{{{[][][]",3),
            ("()(",3),
            ("{*{{}",3),
            ("[[*",2),
            ("{*}",0),
            ("{{",2),
            ("{}",0),
            ("",0),
            ("}",1),
            ("*{}",0),
            ("{{{**[][][]",3),
            ]
    if a:
        for t in tests:
            if check(t[0]) != t[1]:
                print("{} failed, expected {}, got {}".format(t[0], t[1], check(t[0])))
    else:
        rt = check(input())
        if rt != 0:
            print(rt)
        else:
            print("Success")

if __name__ == "__main__":
    main(False)
