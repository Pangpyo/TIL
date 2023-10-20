# 17208 카우버거 알바생 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    D = [[-1]*(K+1) for _ in range(M+1)]
    D[0][0] = 0
    for k in range(N) :
        x, y = map(int, input().split())
        for i in reversed(range(M+1)) :
            if i+x > M :
                continue
            for j in reversed(range(K+1)) :
                if j + y > K :
                    continue
                if D[i][j] < 0 :
                    continue
                D[i+x][j+y] = max(D[i][j]+1, D[i+x][j+y])

    return max(map(max, D))

if __name__ == "__main__" :
    print(solution())