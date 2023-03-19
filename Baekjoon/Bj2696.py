# 2696 중앙값 구하기 G2

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    L = N // 10
    if N % 10:
        L += 1
    left = []
    right = []
    nums = []
    n = 1
    mid = 0
    for i in range(L):
        temp = list(map(int, input().split()))
        for t in temp:
            if n == 1:
                mid = t
                nums.append(mid)
                n += 1
                continue
            if t >= mid:
                heappush(right, t)
            else:
                heappush(left, -t)

            if n % 2:
                rl = len(right)
                ll = len(left)
                if rl > ll:
                    heappush(left, -mid)
                    mid = heappop(right)
                elif rl < ll:
                    heappush(right, mid)
                    mid = -heappop(left)
                nums.append(mid)
            n += 1
    l = len(nums)
    print(l)
    for i in range(l):
        sys.stdout.write(str(nums[i]))
        sys.stdout.write(" ")
        if not (i + 1) % 10 or i == l - 1:
            sys.stdout.write("\n")
