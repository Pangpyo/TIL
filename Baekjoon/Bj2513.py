# 2513 통학버스 G3

import sys

input = sys.stdin.readline

N, K, S = map(int, input().split())

plus = []
minus = []

for i in range(N):
    d, n = map(int, input().split())
    if d > S:
        plus.append([d - S, n])
    elif d < S:
        minus.append([S - d, n])

plus.sort()
minus.sort()


def bus(L: list):
    a = 0
    while L:
        a += L[-1][0]
        k = K
        while k and L:
            if L[-1][1] > k:
                L[-1][1] -= k
                k = 0
            else:
                k -= L[-1][1]
                L.pop()

    return a * 2


print(bus(plus) + bus(minus))
