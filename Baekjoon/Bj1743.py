# 1743 음식물 피하기 S1

import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    N, M, K = map(int, input().split())
    map_ = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        map_[x-1][y-1] = 1
    visit = [[0]*M for _ in range(N)]
    
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    def dfs(x, y):
        visit[x][y] = 1
        temp = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not map_[nx][ny] or visit[nx][ny]:
                continue
            temp += dfs(nx, ny)
        return temp
    answer = 0
    for x in range(N):
        for y in range(M):
            if not visit[x][y] and map_[x][y]:
                answer = max(answer, dfs(x, y))

    return answer

if __name__ == "__main__":
    print(solution())