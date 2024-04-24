# 14222 배열과 연산 G5

from heapq import heapify, heappop, heappush


def solution():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    idx = 1
    heapify(nums)
    while nums:
        n = heappop(nums)
        if n < idx:
            heappush(nums, n+K)
        elif n == idx:
            idx += 1
        else:
            return 0 
    return 1

if __name__ == "__main__":
    print(solution())