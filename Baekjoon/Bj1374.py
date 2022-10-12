# 1374 강의실 G5

import sys

import heapq

input = sys.stdin.readline
N = int(input())
times = []
for i in range(N):
    n, s, t = map(int, input().split())
    times.append((s, t))


times.sort()
rooms = []
heapq.heappush(rooms, times[0][1])

for i in range(1, N):
    if times[i][0] < rooms[0]:
        heapq.heappush(rooms, times[i][1])
    else:
        heapq.heapreplace(rooms, times[i][1])
print(len(rooms))
