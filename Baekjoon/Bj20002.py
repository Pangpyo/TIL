# 20002 사과나무 G5

import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    D = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            D[i][j] = A[i - 1][j - 1] + D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1]
    ans = -sys.maxsize
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            for k in range(min(i, j)) :
                temp = D[i][j] - D[i-k-1][j] - D[i][j-k-1] + D[i-k-1][j-k-1]
                ans = max(ans, temp)
    return ans


if __name__ == "__main__":
    print(solution())
