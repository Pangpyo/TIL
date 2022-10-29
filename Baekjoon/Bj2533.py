# 2533 사회망 서비스(SNS) G3

import sys


sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())

nodes = [[] for _ in range(N + 1)]

for i in range(N - 1):
    p, s = map(int, input().split())
    nodes[p].append(s)
    nodes[s].append(p)
D = [[0, 0] for _ in range(N + 1)]
visit = [0] * (N + 1)


def dfs(n):
    D[n][0] = 1
    visit[n] = 1
    for nn in nodes[n]:
        if not visit[nn]:
            dfs(nn)
            D[n][0] += min(D[nn])
            D[n][1] += D[nn][0]


dfs(1)
print(D)
print(min(D[1]))
