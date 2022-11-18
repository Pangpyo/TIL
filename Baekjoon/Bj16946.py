# 16946 벽 부수고 이동하기4 G2


from copy import deepcopy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
answer = deepcopy(maps)

visit = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(n, m):
    que = deque([(n, m)])
    visit[n][m] = 1
    cnt = 1
    wall = []
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if maps[nx][ny]:
                visit[nx][ny] = 1
                wall.append((nx, ny))
            else:
                visit[nx][ny] = 1
                que.append((nx, ny))
                cnt += 1
    for x, y in wall:
        visit[x][y] = 0
        answer[x][y] += cnt
        answer[x][y] %= 10


for i in range(N):
    for j in range(M):
        if not maps[i][j] and not visit[i][j]:
            bfs(i, j)

for a in answer:
    print("".join(map(str, a)))
