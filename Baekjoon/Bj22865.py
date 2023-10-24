# 22865 가장 먼 곳 G4

import sys
from heapq import heappop, heappush

def solution() :
    input = sys.stdin.readline
    N = int(input())
    F = tuple(map(int, input().split()))
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    inf = sys.maxsize
    dist = [[inf]*3 for _ in range(N+1)]
    for i in range(3) :
        heap = []
        heappush(heap, (0, F[i]))
        dist[F[i]][i] = 0
        while heap :
            d, n = heappop(heap)
            if dist[n][i] > d :
                continue
            for nn, nd in graph[n] :
                ndd = nd + d
                if ndd < dist[nn][i] :
                    dist[nn][i] = ndd
                    heappush(heap, (ndd, nn))
    ans = 0
    d = 0
    for i in range(1, N+1) :
        temp = min(dist[i])
        if i in F :
            continue
        if temp > d :
            d = temp
            ans = i
    return ans

if __name__ == "__main__" :
    print(solution())