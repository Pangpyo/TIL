# 11985 오렌지 출하 G5

import sys

def solution() :
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    inf = sys.maxsize
    D = [inf]*(N+1)
    D[0] = 0
    for i in range(1, N+1) :
        min_v = max_v = A[i-1]
        for j in range(1, min(i, M)+1) :
            min_v = min(A[i-j], min_v)
            max_v = max(A[i-j], max_v)
            temp = K+j*(max_v-min_v)
            D[i] = min(D[i-j] + temp, D[i])
    return D[-1]

if __name__ == "__main__" :
    print(solution())