# 13975 파일 합치기3 G4

import heapq
import sys


input = sys.stdin.readline


for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    ans = 0
    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        heapq.heappush(files, a + b)
        ans += a + b
    print(files)
    print(ans)
