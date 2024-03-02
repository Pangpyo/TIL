# 11779 최소비용 구하기 2

from heapq import heappop, heappush
import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
    A, B = map(int, input().split())

    heap = [(0, A)]
    inf = sys.maxsize
    D = [inf]*(N+1)
    D[A] = 0
    pre = [0]*(N+1)
    while heap :
        d, n = heappop(heap)
        if d > D[n] :
            continue
        for nn, nd in graph[n] :
            ndd = nd + d
            if ndd < D[nn] :
                D[nn] = ndd
                heappush(heap, (ndd, nn))
                pre[nn] = n
    
    route = []
    n = B
    while n :
        route.append(n)
        n = pre[n]
    route.reverse()
    print(D[B])
    print(len(route))
    print(*route)


if __name__ == "__main__" :
    solution()