# 1959 두 개의 숫자열 D2

from cmath import inf
import sys


sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    ans = -inf
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(abs(N-M)+1) :
        s = 0
        if N > M :
            for j in range(M) :
                s += A[j+i]*B[j]
        else :
            for j in range(N) :
                s += B[j+i]*A[j]
        ans = s if s >= ans else ans
    print('#%d'%t, ans)
