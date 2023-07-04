# 16678 모독 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    S = [int(input()) for _ in range(N)]
    S.sort()
    h = 1
    ans = 0
    i = 0
    while i < N :
        diff = S[i] - h
        if diff > 0 :
            ans += diff
            h += 1
        elif diff == 0 :
            h += 1
        i += 1

    return ans

if __name__ == "__main__" :
    print(solution())