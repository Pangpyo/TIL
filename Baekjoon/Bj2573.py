# 2573 빙산 G4

from collections import deque

import sys
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def meltbfs(x, y) :
    visit[x][y] = 1
    que = deque()
    que.append((x, y))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny] > 0 :
                continue
            else :
                if ice[nx][ny] == 0 :
                    visit[nx][ny] = 1
                    que.append((nx, ny))
                else :
                    visit[nx][ny] -= 1
def icedfs(x, y) :
    visitice[x][y] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 :
            continue
        if ice[nx][ny] == 0 :
            continue
        if visitice[nx][ny] == 0 :
            visitice[nx][ny] = 1
            icedfs(nx, ny)
t = 0
while 1 :
    visit = [[0]*M for _ in range(N)]
    visitice = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if not ice[i][j] and visit[i][j] == 0 :
                meltbfs(i, j)
            if ice[i][j] and visitice[i][j] == 0 :
                icedfs(i, j)
                cnt += 1
    if cnt >= 2 :
        break
    for i in range(N) :
        for j in range(M) :
            if ice[i][j] :
                ice[i][j] = max(ice[i][j] + visit[i][j], 0)
    if not max(map(max, ice)) :
        t = 0
        break
    t += 1
print(t)
