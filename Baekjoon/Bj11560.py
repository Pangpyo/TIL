# 11560 다항식 게임 G4

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = [0]*T
    MAX = 20
    dp = [[0]*(MAX*(MAX+1)//2 + 1) for _ in range(MAX+1)]
    dp[0][0] = 1
    for i in range(1, MAX+1):
        for j in range(i+1):
            for k in range(i*(i-1)//2 + 1):
                dp[i][j+k] += dp[i-1][k]
    for t in range(T):
        k, n = map(int, input().split())
        answer[t] = dp[k][n]
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')