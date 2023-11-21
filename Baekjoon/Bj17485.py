# 17485 진우의 달 여행 (Large) G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    D = [[[inf if i else 0]*3 for j in range(M+2)] for i in range(N+1)]
    
    for i in range(1, N+1) :
        for j in range(1, M+1) :
            l = min(D[i-1][j-1][1], D[i-1][j-1][2])
            m = min(D[i-1][j][0], D[i-1][j][2])
            r = min(D[i-1][j+1][0], D[i-1][j+1][1])
            D[i][j][0] = l + costs[i-1][j-1]
            D[i][j][1] = m + costs[i-1][j-1]
            D[i][j][2] = r + costs[i-1][j-1]
    return min(map(min, D[-1]))

if __name__ == "__main__" :
    print(solution())