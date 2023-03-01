# 2234 성곽 G3

import sys

input = sys.stdin.readline

M, N = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]

cnt = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
    global w
    visit[x][y] = n
    w += 1
    for i in range(4):  # 좌 상 우 하
        if maps[x][y] & (1 << i):
            continue
        nx = x + dx[i]
        ny = y + dy[i]
        if visit[nx][ny]:
            continue
        dfs(nx, ny)


n = 1

rooms = []
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            w = 0
            dfs(i, j)
            n += 1
            rooms.append(w)

checkvisit = [[0] * M for _ in range(N)]


def check(x, y, n):
    global rs
    checkvisit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if checkvisit[nx][ny]:
            continue
        if visit[nx][ny] == n:
            checkvisit[nx][ny] = 1
            check(nx, ny, n)
        else:
            rs = max(rs, rooms[n - 1] + rooms[visit[nx][ny] - 1])


rs = 0
for i in range(N):
    for j in range(M):
        if not checkvisit[i][j]:
            check(i, j, visit[i][j])

print(len(rooms))
print(max(rooms))
print(rs)
