# 17073 나무 위의 빗물 G5

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    cnt = 0
    total = 0
    visit = [0]*(N+1)
    def dfs(n, w) :
        nonlocal cnt, total
        visit[n] = 1
        l = len(graph[n])
        if n != 1 :
            l -= 1
        for nn in graph[n] :
            if not visit[nn] :
                dfs(nn, w/l)
        if not l :
            cnt += 1
            total += w
    dfs(1, W)
    return total/cnt

if __name__ == "__main__" :
    print(solution())