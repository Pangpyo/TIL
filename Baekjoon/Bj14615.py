# 14615 Defend the CTP!!! G4

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    reversed_graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u].append(v)
        reversed_graph[v].append(u)
    def dfs(x, graph, visit) :
        visit[x] = 1
        for nx in graph[x] :
            if not visit[nx] :
                dfs(nx, graph, visit)
    
    visit = [0]*(N+1)
    dfs(1, graph, visit)

    reversed_visit = [0]*(N+1)
    dfs(N, reversed_graph, reversed_visit)
    Y = "Defend the CTP"
    N = "Destroyed the CTP"
    T = int(input())
    answers = [N]*T
    for t in range(T) :
        C = int(input())
        if visit[C] and reversed_visit[C] :
            answers[t] = Y
    

    return answers

if __name__ == "__main__" :
    print(*solution(), sep='\n')