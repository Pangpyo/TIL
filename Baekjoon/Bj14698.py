# 14698 전생했더니 슬라임 연구자였던 건에 대하여 (Hard) G4

import sys


input = sys.stdin.readline

import heapq

for i in range(int(input())):
    N = int(input())
    slimes = list(map(int, input().split()))
    heapq.heapify(slimes)
    ans = 1
    while len(slimes) > 1:
        a = heapq.heappop(slimes)
        b = heapq.heappop(slimes)
        c = a * b
        ans *= c % 1000000007
        heapq.heappush(slimes, c)
    ans %= 1000000007
    print(ans)
