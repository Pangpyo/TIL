# 11967 불켜기 G2

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

bt = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a, b = map(int, input().split())
    bt[x - 1][y - 1].append((a - 1, b - 1))


que = deque()

que.append((0, 0))

room = [[0] * N for _ in range(N)]
visit = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
room[0][0] = 1
visit[0][0] = 2
cnt = 1
while que:
    x, y = que.popleft()
    if not room[x][y]:
        continue
    for a, b in bt[x][y]:
        if not room[a][b]:
            room[a][b] = 1
            cnt += 1
            if visit[a][b] == 1:
                que.append((a, b))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if visit[nx][ny] == 2:
            continue
        visit[nx][ny] = 1
        if room[nx][ny]:
            que.append((nx, ny))
            visit[nx][ny] = 2

print(cnt)
