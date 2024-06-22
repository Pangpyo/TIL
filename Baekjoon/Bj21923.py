# 21923 곡예 비행 G4

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    map_ = [tuple(map(int, input().split())) for _ in range(N)]
    INF = sys.maxsize
    map_ = map_[::-1]

    dp = [[-INF]*M for _ in range(N)]
    dp[0][0] = map_[0][0]
    for i in range(N):
        for j in range(M):
            if i == j == 0:
                continue
            u = dp[i-1][j] if i > 0 else -INF
            d = dp[i][j-1] if j > 0 else -INF
            dp[i][j] = max(u, d) + map_[i][j]
    map_ = map_[::-1]
    dp = dp[::-1]
    dp2 = [[-INF]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            u = dp2[i-1][j] if i > 0 else -INF
            d = dp2[i][j-1] if j > 0 else -INF
            dp2[i][j] = max(dp[i][j], u, d) + map_[i][j]
    return dp2[-1][-1]

if __name__ == "__main__":
    print(solution())