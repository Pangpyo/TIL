# 1766 문제집 G2


import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
lines = [0] * (N + 1)
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    lines[B] += 1

prob = []


for i in range(1, N + 1):
    if lines[i] == 0:
        heapq.heappush(prob, i)


ans = []
while prob:
    pre = heapq.heappop(prob)
    ans.append(pre)
    for post in graph[pre]:
        lines[post] -= 1
        if lines[post] == 0:
            heapq.heappush(prob, post)
print(*ans)
