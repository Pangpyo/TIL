# 28017 게임을 클리어하자 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())    
    D = [list(map(int, input().split())) for _ in range(N)]
    inf = sys.maxsize
    for i in range(1, N) :
        for j in range(M) :
            D[i][j] += min(D[i-1][k] if k != j else inf for k in range(M))
    return min(D[-1])

if __name__ == "__main__" :
    print(solution())
