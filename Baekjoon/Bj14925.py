# 14925 목장 건설하기 G4

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if P[i - 1][j - 1]:
                continue
            D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1
            ans = max(ans, D[i][j])
    return ans


if __name__ == "__main__":
    print(solution())