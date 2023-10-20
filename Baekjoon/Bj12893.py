# 12893 적의적 G4

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M) :
        u, v = map(lambda x : int(x)-1, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visit = [-1]*N
    ans = 1
    def dfs(n, is_friend) :
        nonlocal ans
        visit[n] = is_friend
        for nn in graph[n] :
            if visit[nn] != -1:
                if visit[nn] == is_friend :
                    ans = 0
            else :
                dfs(nn, int(not is_friend))
    for i in range(N) :
        if visit[i] == -1 :
            dfs(i, 1)
    return ans

if __name__ == "__main__" :
    print(solution())
