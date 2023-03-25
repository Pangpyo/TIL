# 17244 아맞다우산 G2

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

room = []
start = ()
goods = []
door = ()


for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == "X":
            goods.append((i, j))
        elif temp[j] == "E":
            door = (i, j)
        elif temp[j] == "S":
            start = (i, j)
    room.append(temp)

goods = [start] + goods
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, ex, ey):
    visit = [[0] * M for _ in range(N)]
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if room[nx][ny] == "#" or visit[nx][ny]:
                continue
            visit[nx][ny] = visit[x][y] + 1
            if (nx, ny) == (ex, ey):
                return visit[nx][ny]
            que.append((nx, ny))
    return visit[nx][ny]


l = len(goods)
inf = sys.maxsize
D = [[-1] * (1 << l) for _ in range(l)]

ans = inf


def tsp(n, v):
    global ans
    if v == (1 << l) - 1:
        return bfs(*goods[n], *door)
    if D[n][v] != -1:
        return D[n][v]
    x, y = goods[n]
    temp = inf
    for nn in range(l):
        if v & (1 << nn) == 0:
            temp = min(temp, bfs(x, y, *goods[nn]) + tsp(nn, v | (1 << nn)))
    D[n][v] = temp
    return temp


print(tsp(0, 1))
