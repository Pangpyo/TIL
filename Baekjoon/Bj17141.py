# 17141 연구소 2 G4

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
            temp[j] = 0
        elif temp[j] == 1:
            empty -= 1
    room.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

inf = sys.maxsize


def bfs(com: tuple):
    que = deque()
    cnt = M
    for c in com:
        x, y = virus[c]
        room[x][y] = 2
        que.append((x, y, 0))
    while que:
        x, y, d = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if room[nx][ny]:
                continue
            room[nx][ny] = 2
            que.append((nx, ny, d + 1))
            cnt += 1
    if cnt == empty:
        return d
    else:
        return inf


ans = inf
for com in combinations(list(range(len(virus))), M):
    nroom = deepcopy(room)
    ans = min(ans, bfs(com))
    room = nroom

print(ans if ans != inf else -1)
