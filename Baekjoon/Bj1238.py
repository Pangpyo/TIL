# 1238 파티 G3

import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))

D = [100 * m + 1] * (n + 1)

D[x] = 0

H = []
heapq.heappush(H, (0, x))


while H:
    d, v = heapq.heappop(H)
    for nv, nd in graph[v]:
        ndd = nd + d
        if ndd < D[nv]:
            D[nv] = ndd
            heapq.heappush(H, (ndd, nv))
DD = [100 * m + 1] * (n + 1)
for i in range(1, n + 1):
    if i == x:
        continue
    H = []
    heapq.heappush(H, (0, i))
    nD = [100 * m + 1] * (n + 1)
    nD[i] = 0
    while H:
        d, v = heapq.heappop(H)
        for nv, nd in graph[v]:
            ndd = nd + d
            if ndd < nD[nv]:
                nD[nv] = ndd
                heapq.heappush(H, (ndd, nv))
    DD[i] = nD[x]

ans = 0
for i in range(1, n + 1):
    if i == x:
        continue
    ans = max(D[i] + DD[i], ans)

print(ans)
