# 15971 두 로봇 G4

import sys
from heapq import *

input = sys.stdin.readline

N, A, B = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]

for i in range(N - 1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))
ans = 0
heap = []
heappush(heap, (A, 0))

D = [[10**8, 0] for _ in range(N + 1)]
D[A][0] = 0
while heap:
    u, d = heappop(heap)
    for nu, nd in graph[u]:
        ndd = nd + d
        if ndd < D[nu][0]:
            D[nu][0] = ndd
            D[nu][1] = max(D[nu][1], nd, D[u][1])
            heappush(heap, (nu, ndd))

print(D[B][0] - D[B][1])
