# 18870 좌표압축 S2

from bisect import bisect
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
snums = sorted(list(set(nums)))
znums = []
for i in range(N) :
    znums.append(bisect(snums, nums[i])-1)
print(*znums)