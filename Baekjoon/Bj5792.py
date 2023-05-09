# 5972 택배배송 G5

import sys
from heapq import heappop, heappush


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))

    heap = [(0, 1)]
    inf = sys.maxsize
    D = [inf] * (N + 1)
    D[1] = 0
    while heap:
        d, n = heappop(heap)
        if d > D[n]:
            continue
        for nn, nd in graph[n]:
            ndd = nd + d
            if ndd < D[nn]:
                D[nn] = ndd
                heappush(heap, (ndd, nn))
    return D[N]


if __name__ == "__main__":
    print(solution())
