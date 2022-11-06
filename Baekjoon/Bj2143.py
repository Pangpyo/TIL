# 2143 두 배열의 합 G3

import sys
import bisect

sys.stdin = open("input.txt")


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


def sumlist(list, l):
    suml = []
    for i in range(l):
        S = 0
        for j in range(i, l):
            S += list[j]
            suml.append(S)
    return suml


AA = sumlist(A, n)
BB = sumlist(B, m)
BB.sort()


def findB(diff):
    idx = bisect.bisect_left(BB, diff)
    ans = 0
    if idx >= len(BB):
        return ans
    if BB[idx] == diff:
        ans = bisect.bisect_right(BB, diff) - idx
    return ans


cnt = 0
for a in AA:
    cnt += findB(T - a)
print(cnt)
