# 20168 골목 대장 호석 - 가능성 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M, A, B, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    INF = sys.maxsize
    answer = INF
    def dfs(n, c, mc, visit) :
        nonlocal answer
        if n == B :
            answer = min(mc, answer)
            return
        for nn, nd in graph[n] :
            if visit & (1<<nn) :
                continue
            if nd + c > C :
                continue
            dfs(nn, c+nd, max(mc, nd), visit|(1<<nn))
    dfs(A, 0, 0, 1<<A)
    return answer if answer != INF else -1

if __name__ == "__main__" :
    print(solution())