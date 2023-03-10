# 2240 자두나무 G5

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

D = [[0] * (M + 2) for _ in range(N)]

for i in range(N):
    a = int(input()) - 1
    for j in range(1, M + 2):
        if j % 2 != a:
            temp = 1
        else:
            temp = 0
        D[i][j] = max(D[i - 1][j] + temp, D[i - 1][j - 1] + temp)

print(max(D[-1]))
