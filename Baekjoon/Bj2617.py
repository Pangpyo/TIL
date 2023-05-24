# 2617 구슬찾기 G4 

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    D = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        D[a - 1][b - 1] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if D[i][k] and D[k][j]:
                    D[i][j] = 1
    ans = 0
    for i in range(N):
        f = 0
        e = 0
        for j in range(N):
            if D[i][j]:
                f += D[i][j]
            if D[j][i]:
                e += D[j][i]
        if f >= (N + 1) // 2 or e >= (N + 1) // 2:
            ans += 1
    return ans


if __name__ == "__main__":
    print(solution())
