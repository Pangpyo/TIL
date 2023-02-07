# 11780 플로이드2 G2

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

inf = sys.maxsize

graph = [[inf] * N for _ in range(N)]
path = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    u, v, d = map(int, input().split())
    graph[u - 1][v - 1] = min(graph[u - 1][v - 1], d)
    path[u - 1][v - 1] = [u - 1, v - 1]

for i in range(N):
    graph[i][i] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k][0:-1] + path[k][j]


for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            graph[i][j] = 0

for i in range(N):
    print(*graph[i])

for i in range(N):
    for j in range(N):
        l = len(path[i][j])
        print(l, *[path[i][j][k] + 1 for k in range(l)])
