# 18405 경쟁적 전염 G5

from collections import deque


N, K = map(int, input().split())

E = []

virus = []

for i in range(N):
    v = list(map(int, input().split()))
    for j in range(N):
        if v[j]:
            virus.append((v[j], i, j))
    E.append(v)

virus.sort()
que = deque()
for v, x, y in virus:
    que.append((x, y, 0))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

S, X, Y = map(int, input().split())

while que:
    x, y, t = que.popleft()
    if t == S:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if E[nx][ny] == 0:
            E[nx][ny] = E[x][y]
            que.append((nx, ny, t + 1))


print(E[X - 1][Y - 1])
