# 17025 Icy Perimeter G5

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N = int(input())
    grid = tuple(tuple(input().rstrip() for _ in range(N)))
    visit = [[0]*N for _ in range(N)]
    answer = [0, 0]
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def dfs(x, y) :
        nonlocal A, R
        A += 1
        visit[x][y] = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0 :
                R += 1
                continue
            if grid[nx][ny] == '.' :
                R += 1
                continue
            if visit[nx][ny] :
                continue
            dfs(nx, ny)

    for i in range(N) :
        for j in range(N) :
            if visit[i][j] or grid[i][j] == '.':
                continue
            A, R = 0, 0
            dfs(i, j)
            if A > answer[0] :
                answer[0] = A
                answer[1] = R
            elif A == answer[0] :
                answer[1] = min(answer[1], R)
    
    return answer

if __name__ == "__main__" :
    print(*solution())