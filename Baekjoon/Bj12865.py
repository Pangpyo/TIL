# 12865 평볌한 배낭 G5


import sys


sys.stdin = open("input.txt")

N, K = map(int, input().split())
items = []
for i in range(N):
    items.append(tuple(map(int, input().split())))

D = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        W, V = items[i - 1]
        if j < W:
            D[i][j] = D[i - 1][j]
        else:
            D[i][j] = max(D[i - 1][j - W] + V, D[i - 1][j])

print(D[-1][-1])
