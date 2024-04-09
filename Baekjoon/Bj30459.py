# 30459 현수막 걸기 G5

import sys


def solution():
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = -1
    A.sort(), B.sort()
    AA = set()
    for i, a in enumerate(A):
        for j in range(i+1, N):
            AA.add(A[j]-a)
    def binary_search(a):
        s, e = 0, M-1
        res = -1
        while s <= e:
            m = (s+e)//2
            temp = B[m]*a
            if temp <= 2*R:
                res = temp/2
                s = m + 1
            else :
                e = m - 1
        return res
    for a in AA :
        answer = max(answer, binary_search(a))
    return answer

if __name__ == "__main__":
    print(solution())