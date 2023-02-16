# 4781 사탕가게 G4

import sys

input = sys.stdin.readline

while 1:
    n, m = input().split()
    n = int(n)
    m = int(float(m) * 100 + 0.5)
    candys = []
    if n == m == 0:
        break
    for i in range(n):
        c, p = input().split()
        candys.append((int(c), int(float(p) * 100 + 0.5)))
    candys.sort()
    D = [0] * (m + 1)

    for i in range(n):
        c, p = candys[i]
        for j in range(p, m + 1):
            D[j] = max(D[j], D[j - p] + c)
    print(D[-1])
