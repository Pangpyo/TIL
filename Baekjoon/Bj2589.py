# 2589 보물섬 G5

from collections import deque


N, M = map(int, input().split())

island = [list(input()) for _ in range(N)]


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    que.append((x, y, 0))
    visit[x][y] = 1
    while que:
        x, y, d = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if island[nx][ny] == "W":
                continue
            que.append((nx, ny, d + 1))
            visit[nx][ny] = 1
    return d


ans = 0

for i in range(N):
    for j in range(M):
        visit = [[0] * M for _ in range(N)]
        if island[i][j] == "L":
            ans = max(ans, bfs(i, j))

print(ans)
