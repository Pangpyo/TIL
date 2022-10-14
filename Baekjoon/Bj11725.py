# 11725 트리의 부모찾기 S2

import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(n):
    for nn in graph[n]:
        if not parent[nn]:
            parent[nn] = n
            dfs(nn)


for i in range(1, N + 1):
    if not parent[i]:
        dfs(i)
print(*parent[2::], sep="\n")
