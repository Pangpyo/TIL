# 12834 주간 미팅 G4

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, V, E = map(int, input().split())
    A, B = map(int, input().split())
    H = tuple(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    INF = sys.maxsize
    def dijkstra(n):
        heap = [(0, n)]
        D = [INF]*(V+1)
        D[n] = 0
        while heap:
            d, n = heappop(heap)
            if D[n] < d:
                continue
            for nn, nd in graph[n]:
                ndd = d + nd
                if ndd < D[nn]:
                    D[nn] = ndd
                    heappush(heap, (ndd, nn))
        for i in range(V+1):
            if D[i] == INF:
                D[i] = -1
        return D
    dest = (dijkstra(A), dijkstra(B))
    answer = 0
    for h in H:
        answer += dest[0][h]+dest[1][h]
    return answer

if __name__ == "__main__":
    print(solution())