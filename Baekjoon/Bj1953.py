# 1953 팀배분 G4

import sys


def solution() :
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n+1)]
    teams = [[], []]
    for i in range(1, n+1) :
        line = tuple(map(int, input().split()))
        for l in line[1::] :
            graph[i].append(l)
            graph[l].append(i)
    
    visit = [0]*(n+1)

    def dfs(n, t) :
        visit[n] = 1
        teams[t].append(n)
        for nn in graph[n] :
            if visit[nn] :
                continue
            dfs(nn, int(not t))
    for n in range(1, n+1) :
        if not visit[n] :
            dfs(n, 0)
    for i in range(2) :
        teams[i].sort()
        print(len(teams[i]))
        print(*teams[i])
    return 

if __name__ == "__main__" :
    solution()