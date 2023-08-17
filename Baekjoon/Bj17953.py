# 17953 디저트 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    desert = [list(map(int, input().split())) for _ in range(M)]

    D = [[0]*N for _ in range(M)]

    for i in range(M) :
        D[i][0] = desert[i][0]

    for j in range(1, N) :
        for i in range(M) :
            for k in range(M) :
                d = desert[i][j]
                if i == k :
                    d //= 2
                D[i][j] = max(D[i][j], D[k][j-1]+d)
    return max(D[i][-1] for i in range(M))

if __name__ == "__main__" :
    print(solution())