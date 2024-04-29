# 14217 그래프 탐색 G5

from heapq import heappop, heappush
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    INF = sys.maxsize
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    q = int(input())
    def dijkstra():
        D = [INF]*(N+1)
        D[1] = 0
        heap = [(0, 1)]
        while heap:
            d, n = heappop(heap)
            if d > D[n]:
                continue
            for nn, nd in enumerate(graph[n]):
                if not nd:
                    continue
                ndd = d+1
                if ndd < D[nn]:
                    D[nn] = ndd
                    heappush(heap, (ndd, nn))        
        return D
    def to_str(n):
        if n == INF:
            n = -1
        return str(n)
    answer = []
    for _ in range(q):
        a, u, v = map(int, input().split())
        if a == 1:
            graph[u][v] = 1
            graph[v][u] = 1 
        else:
            graph[u][v] = 0
            graph[v][u] = 0
        dp = dijkstra()
        answer.append(' '.join(map(to_str, dp[1::])))    
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')