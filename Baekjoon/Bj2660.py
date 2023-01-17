# 2660 회장뽑기 G5

from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

while 1:
    u, v = map(int, input().split())
    if u == v == -1:
        break
    graph[u].append(v)
    graph[v].append(u)

score = [0] * (N + 1)


def bfs(u):
    que = deque([(u, 0)])
    visit = [0] * (N + 1)
    visit[u] = 1
    while que:
        n, d = que.popleft()
        for nn in graph[n]:
            if not visit[nn]:
                visit[nn] = 1
                que.append((nn, d + 1))
    score[u] = d


for u in range(1, N + 1):
    bfs(u)

ms = min(score[1::])

print(ms, score.count(ms))
for i in range(1, N + 1):
    if score[i] == ms:
        print(i, end=" ")
