# 10164 격자상의 경로 S2

def solution():
    N, M, K = map(int, input().split())
    K -= 1
    def dp(sx, sy, ex, ey):
        N, M = ex - sx + 1, ey - sy + 1
        dp =[[0]*(M+1) for _ in range(N+1)]
        dp[1][1] = 1
        for i in range(1, N+1):
            for j in range(1, M+1):
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    if K == -1:
        return dp(0, 0, N-1, M-1)
    mx, my = K//M, K%M
    return dp(0, 0, mx, my) * dp(mx, my, N-1, M-1)

if __name__ == "__main__":
    print(solution())