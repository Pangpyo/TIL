# 19598 최소 회의실 개수 G5

import heapq
import sys

input = sys.stdin.readline

time = []

for _ in range(int(input())):
    time.append(tuple(map(int, input().split())))

time.sort()

rooms = [time[0][1]]

for s, e in time[1::]:
    if s >= rooms[0]:
        heapq.heapreplace(rooms, e)
    else:
        heapq.heappush(rooms, e)

print(len(rooms))
