# 11952 좀비 G2

import sys
from heapq import heappop, heappush

def solution() :
    input = sys.stdin.readline
    N, M, K, S = map(int, input().split())
    p, q = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    Z = [int(input()) for _ in range(K)]
    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    inf = sys.maxsize
    danger = [inf]*(N+1)
    heap = []
    for z in Z :
        heappush(heap, (0, z))
        danger[z] = 0
    while heap :
        d, n = heappop(heap)
        if d > danger[n] :
            continue
        for nn in graph[n] :
            ndd = d + 1
            if danger[nn] > ndd :
                danger[nn] = ndd
                heappush(heap, (ndd, nn))
    heap = [(0, 1)]
    D = [inf]*(N+1)
    D[1] = 0
    route = [0]*(N+1)
    while heap :
        d, n = heappop(heap)
        if d > D[n] :
            continue
        for nn in graph[n] :
            if danger[nn] == 0 :
                continue
            ndd = d + (p if danger[nn] > S else q)
            if D[nn] > ndd :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
                route[nn] = n
    return D[-1] - (p if danger[-1] > S else q)

if __name__ == "__main__" :
    print(solution())