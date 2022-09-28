# 24513 좀비 바이러스 G3

from collections import deque
from pprint import pprint
import sys

imput = sys.stdin.readline

N, M = map(int, input().split())

village = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if village[i][j] == 1:
            x1 = i
            y1 = j
        if village[i][j] == 2:
            x2 = i
            y2 = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x1, y1, x2, y2):
    global bp
    que = deque([(x1, y1), (x2, y2)])
    visit[x1][y1] = 1
    visit[x2][y2] = 1
    while que:
        x, y = que.popleft()
        if village[x][y] == 3:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx >= N
                or nx < 0
                or ny >= M
                or ny < 0
                or village[nx][ny] == 3
                or village[nx][ny] == -1
            ):
                continue
            if village[nx][ny] == village[x][y]:
                continue
            elif village[nx][ny] == 0:
                if visit[nx][ny] == 0:
                    village[nx][ny] = village[x][y]
                    visit[nx][ny] = visit[x][y] + 1
                    que.append((nx, ny))
            else:
                if visit[nx][ny] == visit[x][y] + 1:
                    village[nx][ny] += village[x][y]


visit = [[0] * M for _ in range(N)]
bfs(x1, y1, x2, y2)
pprint(village)
ans = [0, 0, 0]

for i in range(N):
    for j in range(M):
        if village[i][j] == 1:
            ans[0] += 1
        elif village[i][j] == 2:
            ans[1] += 1
        elif village[i][j] == 3:
            ans[2] += 1
print(*ans)
