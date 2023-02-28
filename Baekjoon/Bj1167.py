# 1167 트리의 지름 G2

import sys

input = sys.stdin.readline

V = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(V):
    a = list(map(int, input().split()))
    u = a[0]
    for i in range(1, len(a) - 1, 2):
        v = a[i]
        d = a[i + 1]
        graph[u].append((v, d))

visit = [0] * (V + 1)

md = 0
mv = 0


def dfs(n, d):
    global md, mv
    if md < d:
        mv = n
        md = d
    visit[n] = 1
    for nn, nd in graph[n]:
        if visit[nn]:
            continue
        dfs(nn, d + nd)


dfs(1, 0)

ev = mv

md = 0
mv = 0
visit = [0] * (V + 1)

dfs(ev, 0)

print(md)
