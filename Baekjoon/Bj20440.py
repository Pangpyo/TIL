# 20440 니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마 G3
from itertools import accumulate
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    times = []
    nums = set()
    for i in range(N):
        e, x = map(int, input().split())
        nums.add(e)
        nums.add(x)
        times.append((e, x))
    nums = sorted(list(nums))
    dic = {}
    for i, n in enumerate(nums):
        dic[n] = i
    nsums = [0] * len(nums)

    for i in range(N):
        e, x = times[i]
        nsums[dic[e]] += 1
        nsums[dic[x]] -= 1
    ans = 0
    s = 0
    e = 0
    flag = False

    for i, n in enumerate(accumulate(nsums)):
        if n > ans:
            ans = n
            s = i
            flag = True
        if flag and n < ans:
            e = i
            flag = False
    return ans, nums[s], nums[e]


if __name__ == "__main__":
    ans, s, e = solution()
    print(ans)
    print(s, e)
