# 17404 RGB거리 2 G4

import sys


input = sys.stdin.readline

N = int(input())

color = [tuple(map(int, input().split())) for _ in range(N)]

ans = 1e9

for i in range(3):
    D = [[1e9] * 3 for _ in range(N)]
    D[0][i] = color[0][i]
    for j in range(1, N):
        D[j][0] = color[j][0] + min(D[j - 1][1], D[j - 1][2])
        D[j][1] = color[j][1] + min(D[j - 1][0], D[j - 1][2])
        D[j][2] = color[j][2] + min(D[j - 1][0], D[j - 1][1])
    for k in range(3):
        if i != k:
            ans = min(ans, D[-1][k])

print(ans)
