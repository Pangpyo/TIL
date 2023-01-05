# 1916 최소비용 구하기 G5

import sys

import heapq

input = sys.stdin.readline

N = int(input())

M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M) :
    u, v, d = map(int, input().split())
    graph[u].append((d, v))
start, end = map(int, input().split())

D = [10**8]*(N+1)
D[start] = 0
heap = []


heapq.heappush(heap, (0, start))
def answer() : 
    while 1 :
        d, v = heapq.heappop(heap)
        if v == end :
            return d
        for nd, nv in graph[v] :
            if nd + d < D[nv] :
                D[nv] = nd + d
                heapq.heappush(heap, (d+nd, nv))
    return D[end]
print(answer())