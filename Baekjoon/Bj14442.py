# 14442 벽 부수고 이동하기 2 G3

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

maps = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    que = deque()
    que.append((0, 0, K))
    visit = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visit[0][0][K] = 1
    if N == M == 1:
        return 1
    while que:
        x, y, k = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if maps[nx][ny] == "1":
                if not k:
                    continue
                if visit[nx][ny][k - 1]:
                    continue
                visit[nx][ny][k - 1] = visit[x][y][k] + 1
                if nx == N - 1 and ny == M - 1:
                    return visit[N - 1][M - 1][k - 1]
                que.append((nx, ny, k - 1))
            else:
                if visit[nx][ny][k]:
                    continue
                visit[nx][ny][k] = visit[x][y][k] + 1
                if nx == N - 1 and ny == M - 1:
                    return visit[N - 1][M - 1][k]
                que.append((nx, ny, k))
    return -1


print(bfs())
