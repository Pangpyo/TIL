# 18352 특정 거리의 도시 찾기 S2

from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

cities = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    cities[u].append(v)


def bfs(start):
    visit = [0] * (N + 1)
    que = deque([(start, 0)])
    visit[start] = 1
    ans = []
    while que:
        n, d = que.popleft()
        for nn in cities[n]:
            if visit[nn]:
                continue
            visit[nn] = 1
            if d + 1 == K:
                ans.append(nn)
                continue
            que.append((nn, d + 1))
    if ans:
        ans.sort()
        print(*ans, sep="\n")
    else:
        print(-1)


bfs(X)
