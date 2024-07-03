# 6144 Charm Bracelet G5

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    charm = tuple(tuple(map(int, input().split())) for _ in range(N))
    dp = [-1]*(M+1)
    dp[0] = 0
    for w, d in charm:
        for i in reversed(range(1, M+1)):
            if i >= w and dp[i-w] >= 0:
                dp[i] = max(dp[i], dp[i-w]+d)
    return max(dp)

if __name__ == "__main__":
    print(solution())