# 1240 노드사이의 거리 G5

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))


def dfs(x, v, d, pre):
    global ans
    for nx, l in graph[x]:
        if nx == pre:
            continue
        if nx == v:
            ans = d + l
            return
        dfs(nx, v, d + l, x)


for i in range(M):
    u, v = map(int, input().split())
    ans = 0
    dfs(u, v, 0, 0)
    print(ans)
