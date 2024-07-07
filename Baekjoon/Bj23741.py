# 23741 야바위 게임 G4

import sys


def solution():
    input = sys.stdin.readline
    N, M, X, Y = map(int, input().split())
    graph = [set() for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    visit = [[0]*(Y+1) for _ in range(N+1)]
    answer = set()
    def dfs(x, cnt):
        visit[x][cnt] = 1
        if cnt == Y:
            answer.add(x)
            return
        for nx in graph[x]:
            if visit[nx][cnt+1]:
                continue
            dfs(nx, cnt+1)
    dfs(X, 0)
    if len(answer) > 1:
        answer = sorted(list(answer))
        return answer
    else:
        return [-1]

if __name__ == "__main__":
    print(*solution())