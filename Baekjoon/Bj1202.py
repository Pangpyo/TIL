# 1202 보석 도둑 G2

from collections import deque
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    jewels.append(tuple(map(int, input().split())))

jewels.sort()
jewels = deque(jewels)

print(jewels)

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(tmp_jew, -jewels.popleft()[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jewels:
        break
print(answer)
