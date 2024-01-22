# 25195 Yes or yes G4

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    answer = "Yes"
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u].append(v)
    S = int(input())
    goms = set(map(int, input().split()))

    def dfs(n) :
        nonlocal answer
        if n in goms :
            return 
        is_last = True
        for nn in graph[n] :
            is_last = False
            dfs(nn)
        if is_last :
            answer = "yes"
    dfs(1)
    return answer

if __name__ == "__main__" :
    print(solution())