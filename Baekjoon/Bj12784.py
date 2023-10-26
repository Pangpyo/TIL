# 12784 인하니카 공화국 G3

import sys


def solution() :
    input = sys.stdin.readline
    T = int(input())
    inf = sys.maxsize
    def dfs(n) :
        if n != 1 and len(graph[n]) == 1 :
            return inf
        if visit[n] :
            return 0
        temp = 0
        visit[n] = 1
        for nn, nd in graph[n] :
            if visit[nn] :
                continue
            temp += min(nd, dfs(nn))
        return temp
    answer = [0]*T
    for t in range(T) :
        N, M = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        visit = [0]*(N+1)
        for _ in range(M) :
            u, v, d = map(int, input().split())
            graph[u].append((v, d))
            graph[v].append((u, d))
        answer[t] = dfs(1)
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')