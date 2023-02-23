# 1781 컵라면 G2

from heapq import heappush, heapreplace
import sys


input = sys.stdin.readline

N = int(input())

hw = sorted(
    [tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], -x[1])
)

heap = []
time = 0

for t, v in hw:
    if time < t:
        heappush(heap, v)
    elif time == t:
        if len(heap) < t:
            heappush(heap, v)
        else:
            if v > heap[0]:
                heapreplace(heap, v)
    time = t

print(sum(heap))
