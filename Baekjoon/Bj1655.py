# 1655 가운데를 말해요 G2
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())

mid = int(input())
print(mid)
rightheap = []
leftheap = []

for i in range(N - 1):
    temp = int(input())
    if mid <= temp:
        heappush(rightheap, temp)
    else:
        heappush(leftheap, -temp)
    rl = len(rightheap)
    ll = len(leftheap)
    if 0 <= rl - ll <= 1:
        pass
    elif ll + 1 < rl:
        heappush(leftheap, -mid)
        mid = heappop(rightheap)
    else:
        heappush(rightheap, mid)
        mid = -heappop(leftheap)
    print(mid)
