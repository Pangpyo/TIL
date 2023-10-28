# 8901 화학 제품 G5

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    ans = [0]*T
    for t in range(T) :
        A, B, C = map(int, input().split())
        AB, BC, CA = map(int, input().split())
        ab = min(A, B)
        temp = 0
        for i in range(ab+1) :
            nA = A-i
            nB = B-i
            bc = min(nB, C)
            for j in range(bc+1) :
                nC = C - j
                score = i*AB + j*BC + min(nC, nA)*CA
                temp = max(temp, score)
        ans[t] = temp
    return ans

if __name__ == "__main__" :
    print(*solution(), sep='\n')