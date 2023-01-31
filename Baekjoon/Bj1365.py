# 1365 꼬인 전깃줄 G2

import sys


input = sys.stdin.readline

from bisect import bisect_left as bl


N = int(input())
nums = tuple(map(int, input().split()))

D = [nums[0]]
for i in range(1, N):
    if nums[i] > D[-1]:
        D.append(nums[i])
    elif nums[i] < D[-1]:
        D[bl(D, nums[i])] = nums[i]

print(N - len(D))
