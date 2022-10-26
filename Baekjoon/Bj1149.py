# 1149 RGB거리 S1

import sys


input = sys.stdin.readline

N = int(input())

D = [[0] * 3 for _ in range(N)]

D[0] = list(map(int, input().split()))

for i in range(1, N):
    color = tuple(map(int, input().split()))
    for j in range(3):
        minD = max(D[i - 1])
        for k in range(3):
            if k == j:
                continue
            minD = D[i - 1][k] if D[i - 1][k] < minD else minD
        D[i][j] = minD + color[j]
print(min(D[N - 1]))
