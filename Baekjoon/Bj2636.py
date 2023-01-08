# 2636 치즈 G4

from collections import deque

n, m = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    visit = [[0] * m for _ in range(n)]
    que = deque([(0, 0)])
    mc = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            visit[nx][ny] = 1
            if B[nx][ny]:
                B[nx][ny] = 0
                mc += 1
            else:
                que.append((nx, ny))
    return mc


c = sum(map(sum, B))
t = 0
while 1:
    mc = bfs()
    t += 1
    if not c - mc:
        break
    c -= mc

print(t, c, sep="\n")
