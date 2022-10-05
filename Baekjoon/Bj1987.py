# 1987 알파벳 G4

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0


def dfs(x, y, cnt):
    global ans
    way[ord(board[x][y]) - 65] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            if cnt > ans:
                ans = cnt
            continue
        if not way[ord(board[nx][ny]) - 65]:
            dfs(nx, ny, cnt + 1)
            way[ord(board[nx][ny]) - 65] = False
        else:
            if cnt > ans:
                ans = cnt


way = [False] * 26
dfs(0, 0, 1)
print(ans)
