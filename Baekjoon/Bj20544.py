# 20544 공룡게임 G4

def solution():
    N = int(input())
    dp = [[0, 0] for _ in range(1002)]
    dp[0][0] = 0
    dp[0][1] = 1
    dp[1][0] = 1
    dp[1][1] = 0
    dp[2][0] = 1
    dp[2][1] = 0
    dp[3][0] = 2
    dp[3][1] = 1
    MOD = 1_000_000_007
    for i in range(4, N+2):
        dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD
        dp[i][1] = (dp[i-1][1] + dp[i-2][0] + dp[i-2][1]*2 + dp[i-3][0]*2 + dp[i-3][1]*3) % MOD


    return dp[N+1][1]

if __name__ == "__main__":
    print(solution())