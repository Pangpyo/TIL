# 14699 관악산 등산 G4

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, M = map(int, input().split())
    H = tuple(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M) :
        u, v = map(lambda x :int(x)-1, input().split())
        if H[u] > H[v] :
            graph[v].append(u)
        else :
            graph[u].append(v)
    
    visit = [0]*N
    def dfs(n) :
        if visit[n] :
            return visit[n]
        temp = 0
        for nn in graph[n] :
            temp = max(temp, dfs(nn))    
        visit[n] = 1 + temp
        return 1 + temp

    for i in range(N) :
        if not visit[i] :
            dfs(i)
    return visit 

if __name__ == "__main__" :
    print(*solution(), sep='\n')