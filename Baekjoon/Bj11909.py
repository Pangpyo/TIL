# 11909 배열 탈출 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    D = [[inf]*N for _ in range(N)]
    D[0][0] = 0
    for i in range(N) :
        for j in range(N) :
            if i > 0 :
                temp = 0
                if A[i][j] >= A[i-1][j] :
                    temp = A[i][j] - A[i-1][j] + 1
                D[i][j] = min(D[i-1][j] + temp, D[i][j])
            if j > 0 :
                temp = 0
                if A[i][j] >= A[i][j-1] :
                    temp = A[i][j] - A[i][j-1] + 1 
                D[i][j] = min(D[i][j-1] + temp, D[i][j])
    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())