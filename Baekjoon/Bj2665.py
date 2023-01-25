# 2665 미로만들기 G4

from collections import deque

N = int(input())

room = []
for i in range(N):
    temp = input()
    room.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

que = deque()
que.append((0, 0, 0))
visit = [[N * N] * N for _ in range(N)]
visit[0][0] = 0
while que:
    x, y, b = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        nb = b
        if room[nx][ny] == "0":
            nb += 1
        if nb < visit[nx][ny]:
            visit[nx][ny] = nb
            que.append((nx, ny, nb))

print(visit[-1][-1])
