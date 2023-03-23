# 1937 욕심쟁이 판다 G3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

P = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if visit[x][y]:
        return visit[x][y]
    visit[x][y] = 1
    now = P[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if P[nx][ny] <= now:
            continue
        visit[x][y] = max(dfs(nx, ny) + 1, visit[x][y])
    return visit[x][y]


ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)
