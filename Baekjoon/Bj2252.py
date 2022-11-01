# 2252 줄 세우기 G3

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
lines = [0] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    lines[v] += 1

que = deque()

for i in range(1, N + 1):
    if not lines[i]:
        que.append(i)


while que:
    n = que.popleft()
    for nn in graph[n]:
        lines[nn] -= 1
        if lines[nn] == 0:
            que.append(nn)
    print(n, end=" ")
