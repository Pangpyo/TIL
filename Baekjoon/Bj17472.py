# 17472 다리만들기2 G1

from collections import deque

N, M = map(int, input().split())

sea = [list(map(int, input().split())) for _ in range(N)]

cnt = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, cnt):
    sea[x][y] = -cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if sea[nx][ny] == 1:
            dfs(nx, ny, cnt)


for i in range(N):
    for j in range(M):
        if sea[i][j] == 1:
            dfs(i, j, cnt)
            cnt += 1

inf = 100


ls = []


def distance(n, x, y):
    visit = [[0] * M for _ in range(N)]
    visit[x][y] = 1
    que = deque([(x, y)])
    lines = [inf] * cnt
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if not sea[nx][ny]:
                d = 1
                nnx = nx
                nny = ny
                while 1:
                    nnx = nnx + dx[i]
                    nny = nny + dy[i]
                    if nnx >= N or nnx < 0 or nny >= M or nny < 0:
                        break
                    if sea[nnx][nny]:
                        if sea[nnx][nny] < n and d >= 2:
                            lines[-sea[nnx][nny]] = min(d, lines[-sea[nnx][nny]])
                        break
                    d += 1
            else:
                que.append((nx, ny))
                visit[nx][ny] = 1
    for i in range(n, cnt):
        if lines[i] != inf:
            ls.append((n, i, lines[i]))


isn = 1

for i in range(N):
    for j in range(M):
        if sea[i][j] == -isn:
            distance(isn, i, j)
            isn += 1

ls.sort(key=lambda x: x[2])


parent = [-1] * cnt


def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return True
    else:
        return False


def kruskal():
    ans = 0
    for u, v, d in ls:
        if union(u, v):
            ans += d
    if -parent[1] == cnt - 1:
        return ans
    else:
        return -1


print(kruskal())
