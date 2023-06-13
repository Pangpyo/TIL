# 3066 브리징 시그널 G2

from bisect import bisect_left as bl
import sys
def solution() :
    input = sys.stdin.readline
    T = int(input())
    ans = [0]*T
    for t in range(T) :
        N = int(input())
        A = [int(input()) for _ in range(N)]
        Adp = [A[0]]
        for i in range(1, N):
            if Adp[-1] < A[i]:
                Adp.append(A[i])
            else:
                Adp[bl(Adp, A[i])] = A[i]
        ans[t] = len(Adp)
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")