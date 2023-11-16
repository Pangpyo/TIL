# 1757 달려달려 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    D = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1) :
        d = int(input())
        D[i][0] = max(D[i][0], D[i-1][0])
        D[i][1] = D[i-1][0] + d
        for j in range(1, M+1) :
            if D[i-1][j-1] :
                D[i][j] = D[i-1][j-1]+d
            if i+j <= N :
                D[i+j][0] = max(D[i][j], D[i+j][0])
    return D[-1][0]

if __name__ == "__main__" : 
    print(solution())