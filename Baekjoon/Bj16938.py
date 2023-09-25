# 16938 캠프 준비 G5

from itertools import combinations


def solution() :
    N, L, R, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    def comb(minV, maxV, total, cnt, n) :
        nonlocal ans
        if cnt >= 2 and L <= total <= R and maxV-minV >= X :
            ans += 1
        
        for i in range(n, N) :
            nminV = min(A[i], minV)
            nmaxV = max(A[i], maxV)
            ntotal = total + A[i]
            if ntotal > R :
                continue
            comb(nminV, nmaxV, ntotal, cnt+1, i+1)
    comb(float('inf'), 0, 0, 0, 0)
    return ans

if __name__ == "__main__" :
    print(solution())