# 4811 알약 G5

import sys


def solution(N) :
    D = [[0]*(N+1) for _ in range(N*2+1)]
    D[1][1] = 1

    for i in range(2, N*2+1) :
        for j in range(1, N+1) :
            D[i][j] += D[i-1][j-1]
            if i <= j*2 :
                D[i][j] += D[i-1][j]
    return sum(D[-1])

if __name__ == "__main__" :
    input = sys.stdin.readline
    while True :
        N = int(input())
        if not N :
            break
        print(solution(N))