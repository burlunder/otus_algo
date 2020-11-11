#!/usr/bin/env python3
"""
http://ega-math.narod.ru/Quant/Tickets.htm
https://habr.com/ru/post/274689/
"""
import os
import sys

if len(sys.argv) != 2:
    print("Error with input")
    sys.exit()

indata = sys.argv.pop()

if os.path.isfile(indata):
    with open(indata, 'r') as f:
        n = int(f.readline())
        f.close()
else:
    n = int(indata)


bcs = [] # cache for Binc func

def Binc(n, k, bcs=bcs):
    """ Calculates binomial coefficients
    (using cache to store precalculated values)"""
    if (k > n):
        return 0
    if k > n // 2:
        k = n - k # symmetric
    if k == 0:
        return 1
    if k == 1:
        return n
    while len(bcs) < n - 3:
        for i in range(len(bcs), n - 3):
            r=[]
            for j in range(2, i // 2 + 3):
                r.append(Binc(i+3, j-1, bcs)
                        + Binc(i+3, j, bcs))
            bcs.append(r)

    r = bcs[n - 4]
    if len(r) < k - 1:
        for i in range(len(r), k - 1):
            r.append(Binc(n - 1, k - 1, bcs)
                    + Binc(n - 1, k, bcs))

    return bcs[n - 4][k - 2]


def recfunc(m, n, N, kmin):
    """ general formula """
    C = 0
    for k in range(0, kmin + 1):
        c = ((-1) ** k) * Binc(n, k) * Binc(n + N - k * m - 1, n - 1)
        C = C + c
        # print("k={}, c={}, C={}".format(k, c, C))
    return C


def CountLucky(x):
    """ formula adapter for problem"""
    m = 10 # ten digits from 0 to 9
    n = x * 2
    N = 9 * x
    kmin = min(n, N // m)
    # print("n={}, m={}, N={}, kmin={}".format(n, m, N, kmin))

    return recfunc(m, n, N, kmin)


print(CountLucky(n))
