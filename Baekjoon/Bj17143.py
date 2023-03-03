# 17143 낚시왕 G1

import sys
from collections import deque

input = sys.stdin.readline

N, M, S = map(int, input().split())

sharks = [()]
sharkd = deque()
sea = [[0] * M for _ in range(N)]
for i in range(1, S + 1):
    r, c, s, d, z = map(int, input().split())
    if d <= 2:
        s = s % (N * 2 - 2)
    else:
        s = s % (M * 2 - 2)
    d -= 1
    sharks.append([s, d, z])
    sharkd.append((r - 1, c - 1))
    sea[r - 1][c - 1] = i

ans = 0


def catch(n):
    temp = 0
    for i in range(N):
        if sea[i][n]:
            temp = sharks[sea[i][n]][2]
            sea[i][n] = 0
            break
    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def move_shark(x, y):
    n = sea[x][y]
    s, d, z = sharks[n]
    sea[x][y] = 0
    for i in range(s):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            d = change_d(d)
        x = x + dx[d]
        y = y + dy[d]
    sharks[n][1] = d
    nsharkd.append((x, y, n))


def change_d(d):
    if d % 2:
        d -= 1
    else:
        d += 1
    return d


def put(x, y, n):
    if not sea[x][y]:
        sea[x][y] = n
        sharkd.append((x, y))
    else:
        if sharks[sea[x][y]][2] < sharks[n][2]:
            sea[x][y] = n


for i in range(M):
    ans += catch(i)
    l = len(sharkd)
    if not l:
        break
    nsharkd = []
    for n in range(l):
        x, y = sharkd.popleft()
        if not sea[x][y]:
            continue
        move_shark(x, y)
        sea[x][y] = 0
    for x, y, n in nsharkd:
        put(x, y, n)


print(ans)
