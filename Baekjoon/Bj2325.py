# 2325 개코전쟁 P5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for e in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d, e))
    graph[v].append((u, d, e))


inf = sys.maxsize


def dijkstra(b):
    heap = [(0, 1)]
    D = [inf] * (N + 1)
    D[1] = 0
    while heap:
        d, n = heappop(heap)
        for nn, nd, e in graph[n]:
            if e == b:
                continue
            nnd = nd + d
            if D[nn] > nnd:
                heappush(heap, (nnd, nn))
                D[nn] = nnd
    return D[-1]


def answer():
    heap = [(0, 1)]
    D = [inf] * (N + 1)
    D[1] = 0
    route = [[0, 0]] * (N + 1)

    while heap:
        d, n = heappop(heap)
        for nn, nd, e in graph[n]:
            nnd = nd + d
            if D[nn] > nnd:
                heappush(heap, (nnd, nn))
                D[nn] = nnd
                route[nn] = [n, e]
    idx = route[N]
    mroute = []
    while 1:
        mroute.append(idx)
        if idx[0] == 1:
            break
        idx = route[idx[0]]
    d = 0
    for v, ne in mroute:
        maxd = dijkstra(ne)
        d = max(d, maxd)
    return d


print(answer())
