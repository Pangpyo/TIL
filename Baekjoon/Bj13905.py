# 13905 세부 G4

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    s, e = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    INF = sys.maxsize
    D = [0]*(N+1)
    D[s] = INF
    heap = [(-INF, s)]
    while heap:
        d, n = heappop(heap)
        d = -d
        if d < D[n]:
            continue
        for nn, nd in graph[n]:
            ndd = min(nd, d)
            if ndd > D[nn]:
                D[nn] = ndd
                heappush(heap, (-ndd, nn))
    return D[e]

if __name__ == "__main__":
    print(solution())