# 14846 직사각형과 쿼리 G4

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    D = [[[0]*11 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1) :
        for j in range(1, N+1) :
            D[i][j][A[i-1][j-1]] += 1
            for k in range(1, 11) :
                D[i][j][k] += D[i-1][j][k] + D[i][j-1][k] - D[i-1][j-1][k]
    Q = int(input())
    answer = [0]*Q
    for i in range(Q) :
        sx, sy, ex, ey = map(int, input().split())
        temp = 0
        for j in range(1, 11) :
            if (D[ex][ey][j] - D[sx-1][ey][j] - D[ex][sy-1][j] + D[sx-1][sy-1][j]) > 0 :
                temp += 1
        answer[i] = temp
    return answer

if __name__ == "__main__" :
    print(*solution(), sep="\n")