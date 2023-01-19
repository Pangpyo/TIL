# 13565 침투 S2


import sys


input = sys.stdin.readline

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

board = tuple(input().rstrip() for _ in range(N))


visit = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global flag
    if flag:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny >= M or ny < 0:
            continue
        if nx >= N:
            flag = True
            continue
        if visit[nx][ny]:
            continue
        if board[nx][ny] == "1":
            continue
        visit[nx][ny] = 1
        dfs(nx, ny)


flag = False

for i in range(M):
    if flag:
        break
    if not visit[0][i] and board[0][i] == "0":
        dfs(0, i)

if flag:
    print("YES")
else:
    print("NO")
