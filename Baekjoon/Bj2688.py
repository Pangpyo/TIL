# 2688 줄어들지 않아 S1

import sys

def solution() :
    input = sys.stdin.readline
    t = int(input())
    D = [[0 if i != 0 else 1]*10 for i in range(65)]
    for i in range(1, 65) :
        for j in range(10) :
            for k in range(j+1) :
                D[i][j] += D[i-1][k]
    ans = [0]*t
    for i in range(t) :
        n = int(input())
        ans[i] = sum(D[n-1])
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")