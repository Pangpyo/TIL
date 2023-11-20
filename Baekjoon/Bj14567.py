# 14567 선수과목 (Prerequisite) G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        A, B = map(int, input().split())
        graph[B].append(A)
    D = [0]*(N+1)
    def dfs(n) :
        if D[n] :
            return D[n]
        temp = 1
        for nn in graph[n] :
            temp = max(temp, dfs(nn)+1)
        D[n] = temp
        return temp

    for n in reversed(range(1, N+1)) :
        if not D[n] :
            dfs(n)
    
    return D[1::]

if __name__ == "__main__" :
    print(*solution())