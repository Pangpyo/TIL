# 2411 아이템 먹기 G4

import sys


def solution() :
    input = sys.stdin.readline 
    N, M, A, B = map(int, input().split())
    P = [[0]*M for _ in range(N)]
    for _ in range(A) :
        x, y = map(int, input().split())
        P[x-1][y-1] = 1
    for _ in range(B) :
        x, y = map(int, input().split())
        P[x-1][y-1] = 2
    D = [[[0]*(A+1) for _ in range(M)] for _ in range(N)]
    D[0][0][0] = 1
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            temp = 0
            if P[i][j] == 1 :
                temp = 1
            elif P[i][j] == 2 :
                continue
            if i >= 1 :
                D[i][j][cnt+temp] += D[i-1][j][cnt]
            if j >= 1 :
                D[i][j][cnt+temp] += D[i][j-1][cnt]
            cnt += temp
   
    return D[-1][-1][-1]

if __name__ == "__main__" :
    print(solution())