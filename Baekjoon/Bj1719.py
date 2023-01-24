# 1719 택배 G3

from heapq import heappop, heappush
from pprint import pprint


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))


def dijkstra(n):
    D = [[1000 * N + 1, 0] for _ in range(N + 1)]
    D[n][0] = 0
    heap = []
    heappush(heap, (0, n))
    while heap:
        d, n = heappop(heap)
        for nn, nd in graph[n]:
            ndd = nd + d
            if ndd < D[nn][0]:
                D[nn][0] = ndd
                D[nn][1] = n
                heappush(heap, (ndd, nn))
    return D


ans = [["-"] * N for _ in range(N)]

for i in range(N):
    temp = dijkstra(i + 1)
    for j in range(N):
        if i == j:
            continue
        ans[j][i] = temp[j + 1][1]

for a in ans:
    print(*a)
