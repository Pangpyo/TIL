# 22353 항체 인식 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    O = [list(map(int, input().split())) for _ in range(N)]
    A = [list(map(int, input().split())) for _ in range(N)]

    visit = [[0]*M for _ in range(N)]
    YES = "YES"
    NO = "NO"
    if O == A :
        return YES
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def dfs(x, y, a, b) :
        visit[x][y] = 1
        O[x][y] = b
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 :
                continue
            if visit[nx][ny] :
                continue
            if O[nx][ny] == a :
                dfs(nx, ny, a, b)
    for i in range(N) :
        for j in range(M) :
            if O[i][j] != A[i][j] :
                dfs(i, j, O[i][j], A[i][j])
                if O == A :
                    return YES
                else :
                    return NO
    return NO

if __name__ == "__main__" :
    print(solution())