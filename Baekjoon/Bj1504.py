# 1504 특정한 최단 경로 G4

import sys

input = sys.stdin.readline
import heapq

N, e = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(e):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

v1, v2 = map(int, input().split())


load = [1, 1]


def dijkstra(start, end, c):
    heap = []
    heapq.heappush(heap, (0, start))
    D = [1001 * (N + 1)] * (N + 1)
    while heap:
        d, n = heapq.heappop(heap)
        if n == end:
            return d
        for nn, nd in graph[n]:
            ndd = nd + d
            if ndd < D[nn]:
                D[nn] = ndd
                heapq.heappush(heap, (ndd, nn))
    load[c] = False
    return D[end]


def answer():
    a = 1001 * (N + 1) * 3
    b = 1001 * (N + 1) * 3
    if load[0]:
        a = dijkstra(1, v1, 0) + dijkstra(v1, v2, 0) + dijkstra(v2, N, 0)
    if load[1]:
        b = dijkstra(1, v2, 1) + dijkstra(v2, v1, 1) + dijkstra(v1, N, 1)
    if not load[0] and not load[1]:
        return -1
    else:
        return min(a, b)


print(answer())
