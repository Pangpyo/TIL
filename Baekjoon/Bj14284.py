# 14284 간선 이어가기 2 G5

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    s, t = map(int, input().split())
    inf = sys.maxsize
    D = [inf]*(n+1)
    D[s] = 0
    heap = [(0, s)]
    while heap :
        d, n = heappop(heap)
        if d > D[n] :
            continue
        for nn, nd in graph[n] :
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    return D[t]

if __name__ == "__main__" :
    print(solution())