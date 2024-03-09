# 15681 트리와 쿼리 G5

import sys


def solution() :
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N, R, Q = map(int, input().split())
    visit = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(n) :
        if visit[n] :
            return visit[n]
        visit[n] = 1
        temp = 1
        for nn in graph[n] :
            if visit[nn]:
                continue
            temp += dfs(nn)
        visit[n] = temp
        return temp
    dfs(R)

    answer = []
    for _ in range(Q) :
        q = int(input())
        answer.append(visit[q])
    return answer

if __name__ == "__main__" :
    print(*solution(), sep='\n')