# 1826 연료 채우기 G3

from collections import deque
import heapq
import sys

sys.stdin = open("input.txt")


N = int(input())

stations = []


for i in range(N):
    stations.append(tuple(map(int, input().split())))

stations.sort()
stations = deque(stations)
have = []


def answer():
    L, P = map(int, input().split())
    ans = 0
    while stations:
        a, b = stations.popleft()

        while P < a and have:
            P -= heapq.heappop(have)
            ans += 1

        if a > P:
            return -1
        heapq.heappush(have, -b)
        if not stations:
            while L > P and have:
                P -= heapq.heappop(have)
                ans += 1

        if P >= L:
            return ans
    return -1


print(answer())
