# 2230 수 고르기 G5

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted([int(input()) for _ in range(N)])


def answer():
    start = 0
    end = 1
    ans = max(nums) - min(nums)
    while start <= end and end < N:
        diff = nums[end] - nums[start]
        if diff >= M:
            start += 1
            ans = min(diff, ans)
            if diff == M:
                return ans
        else:
            end += 1

    return ans


print(answer())
