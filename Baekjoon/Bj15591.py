# 15591 MooTube (Silver) G5

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    INF = sys.maxsize
    def dijikstra(n):
        D = [INF]*(N+1)
        que = deque()
        que.append(n)
        while que:
            n = que.popleft()
            d = D[n]
            for nn, nd in graph[n]:
                ndd = min(nd, d)
                if D[nn] != INF:
                    continue
                if ndd < D[nn]:
                    D[nn] = ndd
                    que.append(nn)
        return D

    dist = tuple(dijikstra(i) for i in range(N+1))
    answer = [0]*Q
    for q in range(Q):
        k, v = map(int, input().split())
        cnt = 0
        for i in range(1, N+1):
            if v == i:
                continue
            elif dist[v][i] >= k:
                cnt += 1
        answer[q] = cnt
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')