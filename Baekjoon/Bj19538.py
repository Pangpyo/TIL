# 19538 루머 G4

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

cnts = [[0, 0] for _ in range(N + 1)]
for i in range(1, N + 1):
    rs = map(int, input().split())
    for r in rs:
        if not r:
            break
        graph[i].append(r)
        cnts[i][1] += 1

M = int(input())

liars = list(map(int, input().split()))
times = [-1] * (N + 1)

que = deque()
for liar in liars:
    times[liar] = 0
    que.append((liar, 0))

while que:
    n, d = que.popleft()
    for nn in graph[n]:
        if times[nn] >= 0:
            continue
        cnts[nn][0] += 1
        if (cnts[nn][0]) * 2 >= cnts[nn][1]:
            times[nn] = d + 1
            que.append((nn, d + 1))

print(*times[1::])
