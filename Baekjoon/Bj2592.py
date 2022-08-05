# 2592 대표값 B2


import sys


sys.stdin = open('input.txt')
nums = {}
for i in range(10) :
    n = int(input())
    if n not in nums :
        nums[n] = 1
    else :
        nums[n] += 1
mean = 0
for k, v in nums.items() :
    mean += k*v/10
mode = [k for k, v in nums.items() if v == max(nums.values())]
print(int(mean), mode[0])
