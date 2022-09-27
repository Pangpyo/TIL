# 1715 카드 정렬하기 G4


import heapq
import sys

input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

heapq.heapify(nums)
ans = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    ans += a + b
    heapq.heappush(nums, a + b)
print(ans)
