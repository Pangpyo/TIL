# 19238 스타트 택시 G2

from collections import deque
import sys


N, M, F = map(int, input().split())

P = [list(map(int, input().split())) for _ in range(N)]

sx, sy = map(int, input().split())

pgs = [list(map(int, input().split())) for _ in range(M)]


def next_pg(sx, sy):
    D = distance(sx, sy)
    pgs.sort(key=lambda z: (-D[z[0] - 1][z[1] - 1], -z[0], -z[1]))
    return pgs.pop()


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

inf = sys.maxsize


def distance(sx, sy):
    que = deque([(sx, sy)])
    visit = [[0] * N for _ in range(N)]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if P[nx][ny]:
                continue
            visit[nx][ny] = visit[x][y] + 1
            que.append((nx, ny))
    visit[sx][sy] = 0
    return visit


def bfs(x, y, ex, ey):
    if x == ex and y == ey:
        return 0
    que = deque([(x, y, 0)])
    visit = [[0] * N for _ in range(N)]
    visit[x][y] = 1
    while que:
        x, y, d = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if P[nx][ny]:
                continue
            if nx == ex and ny == ey:
                return d + 1
            visit[nx][ny] = 1
            que.append((nx, ny, d + 1))
    return inf


def taxi(sx, sy):
    global F
    while pgs:
        x, y, ex, ey = next_pg(sx, sy)
        x -= 1
        y -= 1
        ex -= 1
        ey -= 1
        gp = bfs(sx, sy, x, y)
        if gp == inf:
            return -1
        else:
            F -= gp
        gd = bfs(x, y, ex, ey)
        if gd > F:
            return -1
        else:
            F += gd
        sx, sy = ex, ey
    return F


print(taxi(sx - 1, sy - 1))
