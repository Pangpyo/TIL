# 23801 두 단계 최단 경로2 G3

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    INF = sys.maxsize
    def dijkstra(s):
        D = [INF]*(N+1)
        heap = [(0, s)]
        D[s] = 0
        while heap:
            d, n = heappop(heap)
            if D[n] < d:
                continue
            for nn, nd in graph[n]:
                ndd = nd + d
                if ndd < D[nn]:
                    D[nn] = ndd
                    heappush(heap, (ndd, nn))
        return D
    x, y = map(int, input().split())
    X = dijkstra(x)
    Y = dijkstra(y)
    P = int(input())
    answer = INF
    for n in map(int, input().split()):
        answer = min(answer, X[n]+Y[n])
    return answer if answer != INF else -1

if __name__ == "__main__":
    print(solution())