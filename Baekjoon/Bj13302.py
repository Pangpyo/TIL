# 13302 리조트 G4

def solution():
    N, M = map(int, input().split())
    if M:
        h = set(map(int, input().split()))
    else:
        h = []
    INF = float('inf')
    MAX = 20
    dp = [[INF]*(MAX*2+1) for _ in range(N+1)]
    costs = ((10000, 1, 0), (25000, 3, 1), (37000, 5, 2))
    dp[0][0] = 0
    for i in range(N+1):
        if i in h:
            for j in range(MAX*2-3):
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        for j in range(MAX*2-3):
            if dp[i][j] == INF:
                continue
            if i < N and j >= 3:
                dp[i+1][j-3] = min(dp[i][j], dp[i+1][j-3])
            for cost, day, coupon in costs:
                dday = i + day
                if dday >= N+1:
                    continue
                dp[dday][j + coupon] = min(dp[i][j] + cost, dp[dday][j + coupon])                        

    return min(dp[-1])

if __name__ == "__main__":
    print(solution())