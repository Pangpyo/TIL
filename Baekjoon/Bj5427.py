# 5427 불 G4

import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, case):
    visit[x][y] = 0
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:
                if case:
                    return visit[x][y] + 1
                else:
                    continue
            if b[nx][ny] == "#":
                continue
            if visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                que.append((nx, ny))
    return "IMPOSSIBLE"


ans = []
for _ in range(int(input())):
    w, h = map(int, input().split())
    b = []
    fires = []
    start = ()
    visit = [[10**7] * w for _ in range(h)]
    for i in range(h):
        temp = input()
        for j in range(w):
            if temp[j] == "*":
                fires.append((i, j))
                visit[i][j] = 0
            if temp[j] == "@":
                start = (i, j)
                visit[i][j] = 0
        b.append(temp)
    for x, y in fires:
        bfs(x, y, 0)
    ans.append(bfs(*start, 1))

print(*ans, sep="\n")
