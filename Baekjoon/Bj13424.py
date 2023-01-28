# 13424 비밀 모임 G4


import sys

input = sys.stdin.readline
for _ in range(int(input())):

    N, M = map(int, input().split())

    inf = 10**8

    D = [[inf] * N for _ in range(N)]

    for i in range(N):
        D[i][i] = 0

    for m in range(M):
        u, v, d = map(int, input().split())
        D[u - 1][v - 1] = d
        D[v - 1][u - 1] = d

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[k][j] + D[i][k])

    ans = 0
    maxd = inf

    f = int(input())
    fs = list(map(int, input().split()))
    for i in range(N):
        sums = sum([D[i][j - 1] for j in fs])
        if sums < maxd:
            ans = i + 1
            maxd = sums
    print(ans)
