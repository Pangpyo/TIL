# 17179 케이크자르기 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M, L = map(int, input().split())
    C = [int(input()) for _ in range(M)]
    C.append(L)
    C.sort()
    Q = [int(input()) for _ in range(N)]
    ans = [0]*N
    def cut_cake(q) :
        s, e = 1, L
        ans = 0
        while s <= e :
            mid = (s+e)//2
            pre = 0
            cnt = -1
            for c in C :
                if c - pre >= mid :
                    cnt += 1
                    pre = c
            if cnt >= q :
                ans = mid
                s = mid + 1
            else :
                e = mid - 1
        return ans
    for i, q in enumerate(Q) :
        ans[i] = cut_cake(q)
    return ans

if __name__ == "__main__" :
    print(*solution(), sep="\n")