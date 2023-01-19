# 10282 해킹 G4

import sys
from heapq import *

input = sys.stdin.readline


for t in range(int(input())):
    N, D, C = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for i in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    heap = []
    heappush(heap, (0, C))
    D = [10**9] * (N + 1)
    D[C] = 0
    cnt = [C]
    while heap:
        s, n = heappop(heap)
        for nn, ns in graph[n]:
            nss = ns + s
            if nss < D[nn]:
                if D[nn] == 10**9:
                    cnt.append(nn)
                D[nn] = nss
                heappush(heap, (nss, nn))
    sec = 0
    for n in cnt:
        sec = max(sec, D[n])
    print(len(cnt), sec)
