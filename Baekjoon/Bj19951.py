# 19951 태상이의 훈련소 생활 G5

from itertools import accumulate
import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    D = [0]*N
    for _ in range(M) :
        a, b, k = map(int, input().split())
        D[a-1] += k
        if b < N :
            D[b] -= k
    for i, d in enumerate(accumulate(D)) :
        P[i] += d
    return P

if __name__ == "__main__" :
    print(*solution())