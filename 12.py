#!/bin/python


P = 1_000_000_007
X = 263

def h(s):
    SS = ord(s[0])
    x = X
    if len(s)>1:
        S = (ord(s[1]) * x) % P
        SS = (SS + S) % P

    if len(s)>2:
        print(s[2:])
        for i, c in enumerate(s[2:]):
            x = (x*X)%P
            S = ord(c)
            S = (S * x) % P
            SS = (SS + S) % P

    return SS


def hashes(s, ws):
    slen = len(s)
    ret = [None for i in range(slen-ws+1)]
    ret[-1] = h(s[slen-ws:slen])
    Xpowp_1 = 1
    for i in range(ws-1):
        Xpowp_1 = (Xpowp_1 * X) % P


    for i in range(slen-ws):
        _i = slen-ws-i-1
        ret[_i] = ((((ret[_i+1] - (ord(s[_i+ws]) * Xpowp_1)%P))%P * X)%P + ord(s[_i]))%P


    return ret


def main():
    p = input()
    t = input()
    hs = hashes(t, len(p))
    p_hash = h(p)
    print(hs)
    print(p_hash)
    for i, v in enumerate(hs):
        if p_hash == v:
            if p == t[i:i+len(p)]:
                print(i)

if __name__ == "__main__":
    main()

