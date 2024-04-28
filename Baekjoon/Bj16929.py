# 16929 Two Dots G4

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    board = tuple(input().rstrip() for _ in range(N))
    visit = [[-1]*M for _ in range(N)]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    answer = "No"
    def dfs(x, y):
        nonlocal answer
        color = board[x][y]
        d = visit[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if board[nx][ny] != color:
                continue
            if visit[nx][ny] >= 0:
                if d - visit[nx][ny] >= 3:
                    answer = "Yes"
                continue
            visit[nx][ny] = d+1
            dfs(nx, ny)
    for x in range(N):
        for y in range(M):
            if visit[x][y] == -1:
                visit[x][y] = 0
                dfs(x, y)
    return answer

if __name__ == "__main__":
    print(solution())