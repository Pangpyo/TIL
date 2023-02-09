# 5214 환승 G2

import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
tubes = [list(map(int, input().split())) for _ in range(M)]

for i in range(M) :
    for j in range(K) :
        graph[tubes[i][j]].append(i)



def bfs() :
    que = deque([1])
    visit = [-1]*(N+1)
    visit[1] = 1
    visitt = [0]*M
    while que :
        x = que.popleft()
        for t in graph[x] :
            if not visitt[t]:
                for nx in tubes[t] :
                    if visit[nx] == -1:
                        visit[nx] = visit[x] + 1
                        if nx == N :
                            return visit[N]
                        que.append(nx)
                visitt[t] = 1
    return visit[N]

print(bfs())