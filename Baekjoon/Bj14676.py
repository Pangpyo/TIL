# 14676 영우는 사기꾼? G3

import sys


def solution():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    lines = [0]*(N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        lines[v] += 1
    buildings = [0]*(N+1)
    LIE = "Lier!"
    for i in range(K):
        a, n = map(int, input().split())
        if a == 1:
            if lines[n]:
                return LIE
            if buildings[n] == 0:
                for nn in graph[n]:
                    lines[nn] -= 1
            buildings[n] += 1
        else:
            if buildings[n] == 0:
                return LIE
            buildings[n] -= 1
            if buildings[n] == 0:
                for nn in graph[n]:
                    lines[nn] += 1
    return "King-God-Emperor"

if __name__ == "__main__":
    print(solution())