# 23324 어려운 모든 정점 쌍 최단거리 G4

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    N, M, K = map(int, input().split())
    a, b = 0, 0
    graph = [[] for _ in range(N+1)]
    for i in range(M) :
        u, v = map(int, input().split())
        d = 0
        if i == K-1 :
            a, b = u, v
            d = 1
        graph[u].append((v, d))
        graph[v].append((u, d))
    visit = [0]*(N+1)
    def dfs(x) :
        visit[x] = 1
        temp = 1
        for xx, d in graph[x] :
            if not visit[xx] and not d:
                temp += dfs(xx)
        return temp

    l = dfs(a)
    if visit[b] :
        return 0
    r = dfs(b)
    return l*r

if __name__ == "__main__" :
    print(solution())