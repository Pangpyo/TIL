# 11404 플로이드 G4

import sys


def solution() :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    inf = sys.maxsize
    D = [[inf]*n for _ in range(n)]
    for i in range(m) :
        a, b, c = map(int, input().split())
        D[a-1][b-1] = min(D[a-1][b-1], c) if D[a-1][b-1] else c
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if i==j  :
                    continue
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    for i in range(n) :
        for j in range(n) :
            if D[i][j] == inf :
                D[i][j] = 0
    [print(*row) for row in D]

if __name__ == "__main__" :
    solution()