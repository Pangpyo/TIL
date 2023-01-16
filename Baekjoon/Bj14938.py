# 14938 서강그라운드 G4

import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

items = list(map(int, input().split()))

graph = [[10**5] * (N) for _ in range(N)]

for i in range(R):
    u, v, d = map(int, input().split())
    graph[u - 1][v - 1] = d
    graph[v - 1][u - 1] = d

for i in range(N):
    graph[i][i] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ans = 0
for i in range(N):
    temp = 0
    for j in range(N):
        if graph[i][j] <= M:
            temp += items[j]
    ans = max(temp, ans)

print(ans)
