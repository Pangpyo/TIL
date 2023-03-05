# 17142 연구소 3 G3

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
room = []
virus = []
empty = N * N
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            virus.append((i, j))
            empty -= 1
        elif temp[j] == 1:
            empty -= 1
    room.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

inf = sys.maxsize


def bfs(com: tuple):
    que = deque()
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for c in com:
        x, y = virus[c]
        visit[x][y] = 1
        que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if room[nx][ny] == 1 or visit[nx][ny]:
                continue
            que.append((nx, ny))
            if not room[nx][ny]:
                cnt += 1
            visit[nx][ny] = visit[x][y] + 1
    if cnt == empty:
        d = 0
        for i in range(N):
            for j in range(N):
                if room[i][j]:
                    continue
                d = max(d, visit[i][j]-1)
        return d
    else:
        return inf


ans = inf
for com in combinations(list(range(len(virus))), M):
    nroom = deepcopy(room)
    ans = min(ans, bfs(com))
    room = nroom

print(ans if ans != inf else -1)
