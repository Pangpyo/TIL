# 11085 군사 이동 G3

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    s, e = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))

    inf = sys.maxsize
    heap = [(-inf, s)]
    D = [0]*N
    
    while heap :
        d, n = heappop(heap)
        for nn, nd in graph[n] :
            ndd = min(nd, -d)
            if ndd > D[nn] :
                D[nn] = ndd
                heappush(heap, (-ndd, nn))

    return D[e]

if __name__ == "__main__" :
    print(solution())