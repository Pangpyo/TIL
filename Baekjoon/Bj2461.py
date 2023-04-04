# 2461 대표 선수 G2

import sys
from heapq import heappop, heappush


def solution():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    nums = []

    minheap = []
    maxv = 0

    for i in range(N):
        temp = sorted(list(map(int, input().split())))
        heappush(minheap, (temp[0], i, 0))
        maxv = max(maxv, temp[0])
        nums.append(temp)
    ans = maxv - minheap[0][0]

    while True:
        v, c, idx = heappop(minheap)
        if idx == M - 1:
            break
        nv = nums[c][idx + 1]
        maxv = max(nv, maxv)
        heappush(minheap, (nv, c, idx + 1))
        ans = min(ans, maxv - minheap[0][0])

    return ans


if __name__ == "__main__":
    print(solution())
