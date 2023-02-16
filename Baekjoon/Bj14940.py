# 14940 쉬운 최단거리 S1

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


M = []

sx, sy = 0, 0

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            sx, sy = (i, j)
    M.append(temp)

inf = sys.maxsize
visit = [[inf] * m for _ in range(n)]
visit[sx][sy] = 0
que = deque()
que.append((sx, sy))

while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if visit[nx][ny] <= visit[x][y] + 1:
            continue
        if M[nx][ny] == 1:
            visit[nx][ny] = visit[x][y] + 1
            que.append((nx, ny))


for i in range(n):
    for j in range(m):
        if visit[i][j] == inf:
            if M[i][j]:
                sys.stdout.write(str(-1))  # 갈 수 있는 땅인데 못가는 경우
            else:
                sys.stdout.write(str(0))  # 못가는 땅인 경우
        else:
            sys.stdout.write(str(visit[i][j]))
        sys.stdout.write(" ")
    sys.stdout.write("\n")
