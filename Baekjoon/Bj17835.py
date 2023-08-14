# 17835 면접보는 승범이네 G2

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M) :
        u, v, d = map(int, input().split())
        graph[v].append((u, d))
    inf = sys.maxsize
    D = [inf]*(N+2)
    heap = []
    for k in list(map(int, input().split())) :
        heappush(heap, (0, k))
        D[k] = 0
    while heap :
        d, n = heappop(heap)
        if D[n] < d :
            continue
        for nn, nd in graph[n] :
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    idx, d = 0, 0
    for i in range(1, N+1) :
        if D[i] > d :
            idx = i 
            d = D[i]
    return idx, d

if __name__ == "__main__" :
    print(*solution(), sep="\n")