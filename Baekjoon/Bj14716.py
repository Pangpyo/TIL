# 14716 현수막 S1

import sys


sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

card = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

visit = [[0] * M for _ in range(N)]


def dfs(x, y):

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if not card[nx][ny]:
            continue
        if visit[nx][ny]:
            continue
        visit[nx][ny] = 1
        dfs(nx, ny)


cnt = 0
for i in range(N):
    for j in range(M):
        if card[i][j] and not visit[i][j]:
            visit[i][j] = 1
            dfs(i, j)
            cnt += 1

print(cnt)
