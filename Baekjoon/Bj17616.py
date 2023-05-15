# 17616 등수 찾기 G3

import sys


def solution():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    graph = [[[] for _ in range(N + 1)] for _ in range(2)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[0][u].append(v)
        graph[1][v].append(u)
    visit = [[0] * (N + 1) for _ in range(2)]

    def dfs(n, updown):
        visit[updown][n] = 1
        temp = 1
        for nn in graph[updown][n]:
            if not visit[updown][nn]:
                temp += dfs(nn, updown)
        return temp

    U, V = dfs(X, 1), N - (dfs(X, 0) - 1)

    return U, V


if __name__ == "__main__":
    print(*solution())
