# 17498 폴짝 게임 G5

import sys


def solution():
    input = sys.stdin.readline
    N, M, D = map(int, input().split())
    board = tuple(tuple(map(int, input().split())) for _ in range(N))
    INF = sys.maxsize
    dp = [[-INF if i != 0 else 0]*M for i in range(N)]
    
    for x in range(1, N):
        for y in range(M):
            for dx in range(1, D+1):
                nx = x - dx
                for dy in range(-D+dx, D+1-dx):
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        dp[x][y] = max(dp[x][y], dp[nx][ny] + board[nx][ny]*board[x][y])
    return max(dp[-1])

if __name__ == "__main__":
    print(solution())