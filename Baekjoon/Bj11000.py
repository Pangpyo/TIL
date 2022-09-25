# 11000 강의실 배정 G5

import sys
sys.stdin = open("input.txt")
import heapq
N = int(input())
times = []
for i in range(N) :
    s, t = map(int, input().split())
    times.append((s, t))

def ans(times) :
    times.sort()
    rooms = []
    heapq.heappush(rooms, times[0][1])

    for i in range(1, N) :
        if times[i][0] < rooms[0] :
            heapq.heappush(rooms, times[i][1])
        else :
            heapq.heapreplace(rooms, times[i][1])

    return len(rooms)
print(ans(times))
