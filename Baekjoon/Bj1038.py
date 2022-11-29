# 1038 감소하는 수 G5

import sys

sys.setrecursionlimit(10**7)

N = int(input())

nums = []

K = 7


def dfs(n):
    nn = n
    nums.append(n)
    i = 0
    while nn >= 10:
        nn //= 10
        i += 1
    for j in range(nn + 1, 10):
        dfs(j * (10 ** (i + 1)) + n)


for i in range(10):
    dfs(i)

nums.sort()

if N < len(nums):
    print(nums[N])
else:
    print(-1)
