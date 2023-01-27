# 17135 캐슬 디펜스 G3


from collections import deque
from copy import deepcopy
from itertools import combinations

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0]
dy = [-1, 0, 1]


def shoot(x, y):
    que = deque([(x, y, 0)])
    visit = [[0] * M for _ in range(N)]
    while que:
        x, y, d = que.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if visit[nx][ny]:
                continue
            if d < D:
                if nboard[nx][ny]:
                    return (nx, ny)
                visit[nx][ny] = 1
                que.append((nx, ny, d + 1))
    return ()


coms = combinations(range(M), 3)
ans = 0
for com in coms:
    nboard = deque(deepcopy(board))
    kill = 0
    for i in range(N):
        go = []
        for y in com:
            go.append(shoot(N, y))
        for a in go:
            if a and nboard[a[0]][a[1]] == 1:
                nboard[a[0]][a[1]] = 0
                kill += 1
        nboard.appendleft([0] * M)
        nboard.pop()
    ans = max(ans, kill)
print(ans)
