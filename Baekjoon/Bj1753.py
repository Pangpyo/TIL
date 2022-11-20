# 1753 최단경로 G4


import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

hque = []

heapq.heappush(hque, (0, K))

nodes = [10 * E + 1] * (V + 1)

nodes[0] = 0
nodes[K] = 0

while hque:
    w, v = heapq.heappop(hque)
    if nodes[v] < w:
        continue
    for nw, nv in graph[v]:
        cost = nw + nodes[v]
        if cost < nodes[nv]:
            heapq.heappush(hque, (cost, nv))
            nodes[nv] = cost
    print(hque)
for i in range(1, V + 1):
    if nodes[i] <= 10 * E:
        print(nodes[i])
    else:
        print("INF")
