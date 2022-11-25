# 2638 치즈 G3

import sys


sys.setrecursionlimit(10**5)
N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if space[x][y] == 0:
        visit[x][y] += 1
    else:
        visit[x][y] -= 1
    if space[x][y] == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visit[nx][ny] == 0 or visit[nx][ny] == -1:
                dfs(nx, ny)


sec = 0
while max(map(max, space)):
    visit = [[0] * M for _ in range(N)]
    dfs(0, 0)
    for i in range(N):
        for j in range(M):
            if visit[i][j] == -2:
                space[i][j] = 0
    sec += 1
print(sec)
