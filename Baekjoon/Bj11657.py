# 11657 타임머신 G4

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    INF = sys.maxsize
    edges = tuple(tuple(map(int, input().split())) for _ in range(M))
    distance = [INF]*(N+1)
    distance[1] = 0
    for i in range(N):
        for u, v, d in edges:
            if distance[u] != INF and distance[v] > distance[u] + d:
                distance[v] = distance[u] + d
                if i == N - 1:
                    return (-1,)
    return [distance[i] if distance[i] != INF else -1 for i in range(2, N+1)]

if __name__ == "__main__":
    print(*solution(), sep='\n')