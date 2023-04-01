# 15486 퇴사2 G5

import sys


input = sys.stdin.readline

N = int(input())

heap = []
ans = 0
D = [0] * (N + 1)
for i in range(N):
    nt, np = map(int, input().split())
    D[i] = max(D[i - 1], D[i])
    if nt + i <= N:
        D[nt + i] = max(D[i] + np, D[nt + i])

print(max(D))
