# 16957 체스판 위의 공 G4

import sys


def solution() :
    input = sys.stdin.readline
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    visit = [[-1]*C for _ in range(R)]

    def dfs(x, y) :
        if visit[x][y] != -1:
            return visit[x][y]
        temp = board[x][y]
        ex, ey = x, y
        visit[x][y] = x*C + y
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0 :
                continue
            if board[nx][ny] < temp :
                temp = board[nx][ny]
                ex = nx
                ey = ny
        if not (ex == x and ey == y) :
            visit[x][y] = dfs(ex, ey)
        return visit[x][y]
    D = [[0]*C for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            xy = dfs(i, j)
            x = xy//C
            y = xy%C
            D[x][y] += 1
    return D

if __name__ == "__main__" :
    for row in solution() :
        print(*row)


