# 16562 친구비 G4

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


N, M, k = map(int, input().split())
cost = []
for i, v in enumerate(list(map(int, input().split()))):
    cost.append((i + 1, v))
cost.sort(key=lambda x: x[1])


graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visit = [0] * (N + 1)
visit[0] = 1


cnt = 0


def dfs(n):
    global cnt
    visit[n] = 1
    cnt += 1
    for nn in graph[n]:
        if not visit[nn]:
            dfs(nn)


def answer():
    mincosts = 0
    for i, v in cost:
        if not visit[i]:
            mincosts += v
            if mincosts > k:
                return "Oh no"
            dfs(i)
        if cnt == N:
            return mincosts


print(answer())
