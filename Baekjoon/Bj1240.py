# 1240 노드사이의 거리 G5

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(N - 1):  # 그래프 생성
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))


def dfs(x, v, d, pre):  # dfs를 한다. 이 때 pre를 변수로 받아 직전 노드를 방문하지 않도록 한다.
    global ans  # 글로벌 변수 ans에 노드 길이를 저장한다.
    for nx, l in graph[x]:
        if nx == pre:
            continue
        if nx == v:
            ans = d + l
            return
        dfs(nx, v, d + l, x)


for i in range(M):
    u, v = map(int, input().split())
    ans = 0
    dfs(u, v, 0, 0)
    print(ans)
