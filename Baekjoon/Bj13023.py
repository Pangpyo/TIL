# 13023 ABCDE G5

import sys


def solution():
    def dfs(n, cnt):
        nonlocal ans, visit
        if cnt == 5:
            ans = 1
            return
        for nn in graph[n]:
            if not visit[nn]:
                visit[nn] = 1
                dfs(nn, cnt + 1)
                visit[nn] = 0

    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N)]

    input = sys.stdin.readline
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    ans = 0
    visit = [0] * N
    for i in range(N):
        visit[i] = 1
        dfs(i, 1)
        if ans == 1:
            break
        visit[i] = 0
    return ans


if __name__ == "__main__":
    print(solution())
