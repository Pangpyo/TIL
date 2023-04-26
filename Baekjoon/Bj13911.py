# 13911 집 구하기 G2

import sys
from heapq import heappop, heappush


def solution():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 3)]
    for i in range(E):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    mm, mx = map(int, input().split())
    M = set(map(int, input().split()))
    sm, sx = map(int, input().split())
    S = set(map(int, input().split()))
    H = set(range(1, V + 1)) - M - S

    for m in M:
        graph[V + 1].append((m, 0))
    for s in S:
        graph[V + 2].append((s, 0))
    inf = sys.maxsize

    def dijkstra(n, x):
        D = [inf] * (V + 1) + [0, 0]
        heap = []
        heappush(heap, (0, n))
        while heap:
            d, n = heappop(heap)
            for nn, nd in graph[n]:
                ndd = nd + d
                if ndd < D[nn] and ndd <= x:
                    D[nn] = ndd
                    heappush(heap, (ndd, nn))
        return D

    mD = dijkstra(V + 1, mx)
    sD = dijkstra(V + 2, sx)
    ans = inf
    for h in H:
        if mD[h] == inf or sD[h] == inf:
            continue
        ans = min(ans, mD[h] + sD[h])
    return ans if ans != inf else -1


if __name__ == "__main__":
    print(solution())
