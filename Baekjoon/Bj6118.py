# 6118 숨바꼭질 S1

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

que = deque()
que.append((1, 0))

visit = [0] * (N + 1)
visit[1] = 1

ans = []

while que:
    n, d = que.popleft()
    for nn in graph[n]:
        if not visit[nn]:
            que.append((nn, d + 1))
            ans.append((nn, d + 1))
            visit[nn] = 1
ans.sort(key=lambda x: (-x[1], x[0]))


answer = [ans[0][0], ans[0][1], 0]

for n, d in ans:
    if d == answer[1]:
        answer[2] += 1
    else:
        break
print(*answer)
