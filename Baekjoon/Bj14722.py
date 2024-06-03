# 14722 우유 도시 G4

import sys

def solutuon():
    input = sys.stdin.readline
    N = int(input())
    map_ = tuple(tuple(map(int, input().split())) for _ in range(N))
    INF = sys.maxsize
    D = [[[-INF]*3 for _ in range(N+1)] for _ in range(N+1)]
    D[0][1][2] = 0
    D[1][0][2] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(3):
                D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k])
                if map_[i-1][j-1] == k:
                    D[i][j][k] = max(D[i][j][k], D[i][j-1][k-1] + 1, D[i-1][j][k-1] + 1)
    return max(D[-1][-1])

if __name__ == "__main__":
    print(solutuon())