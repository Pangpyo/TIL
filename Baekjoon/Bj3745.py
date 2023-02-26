# 3745 오름세 G2

from bisect import bisect_left as bl
import sys

input = sys.stdin.readline

while 1:
    try:
        N = int(input())
        nums = list(map(int, input().split()))
        D = [nums[0]]
        for i in range(1, N):
            if nums[i] > D[-1]:
                D.append(nums[i])
            elif nums[i] < D[-1]:
                D[bl(D, nums[i])] = nums[i]
        print(len(D))
    except:
        break
