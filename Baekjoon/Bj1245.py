# 1245 농장 관리 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    def dfs(x, y):
        visit[x][y] = cnt
        h = mountain[x][y]
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny] or mountain[nx][ny] > h:
                continue
            dfs(nx, ny)
        return 
    
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)

    cnt = 0
    visit = [[0]*M for _ in range(N)]
    for h in reversed(range(501)):
        for i in range(N) :
            for j in range(M) :
                if mountain[i][j] == h and not visit[i][j] and mountain[i][j]:
                    cnt += 1
                    dfs(i, j)
    return cnt

if __name__ == "__main__" :
    print(solution())