# 2307 도로검문 G1

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

inf = sys.maxsize

heap = [(1, 0)]
D = [inf] * (N + 1)
D[1] = 0
route = [0] * (N + 1)
while heap:
    n, d = heappop(heap)
    for nn, nd in graph[n]:
        nnd = nd + d
        if D[nn] > nnd:
            heappush(heap, (nn, nnd))
            D[nn] = nnd
            route[nn] = n
idx = N
mroute = []
while 1:
    idx = route[idx]
    if idx == 1:
        break
    mroute.append(idx)

mind = D[-1]


def dijkstra(b):
    heap = [(0, 1)]
    D = [inf] * (N + 1)
    D[1] = 0
    while heap:
        d, n = heappop(heap)
        for nn, nd in graph[n]:
            if nn == b:
                continue
            nnd = nd + d
            if D[nn] > nnd:
                heappush(heap, (nnd, nn))
                D[nn] = nnd
    return D[-1]


def answer():
    ans = 0
    for b in mroute:
        maxd = dijkstra(b)
        if maxd == inf:
            return -1
        else:
            ans = max(ans, maxd - mind)
    return ans


print(answer())
