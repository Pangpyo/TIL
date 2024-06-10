# 23793 두 단계 최단 경로 1 G4

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
    INF = sys.maxsize
    def dijkstra(s, block):
        D = [INF]*(N+1)
        D[s] = 0
        heap = [(0, s)]
        while heap:
            d, n = heappop(heap)
            if D[n] < d:
                continue
            for nn, nd in graph[n]:
                if nn == block:
                    continue
                ndd = nd + d
                if ndd < D[nn]:
                    D[nn] = ndd
                    heappush(heap, (ndd, nn))
        return tuple(n if n != INF else -1 for n in D)
    x, y, z = map(int, input().split())
    X = dijkstra(x, y)
    XY = dijkstra(x, 0)
    Y = dijkstra(y, 0)
    answer = [((XY[y]+Y[z]) if (XY[y] > 0 and Y[z] > 0) else -1), X[z]]
    return answer

if __name__ == "__main__":
    print(*solution())