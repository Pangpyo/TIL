# 1106 호텔 G5 

import sys


def solution() :
    input = sys.stdin.readline
    C, N = map(int, input().split())
    inf = sys.maxsize
    D = [inf]*(C+1)
    D[0] = 0
    costs = [tuple(map(int, input().split())) for _ in range(N)]
    for i in range(C) :
        for j in range(N) :
            c, person = costs[j]
            for p in range(1, person+1) :
                if i+p > C :
                    break
                D[i+p] = min(D[i+p], D[i]+c)
    return D[C]

if __name__ == "__main__" :
    print(solution())