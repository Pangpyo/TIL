# 19542 전단지 돌리기 G3

import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, S, D = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    to_leaf = [-1]*(N+1)
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    def get_leafs(n):
        to_leaf[n] = 0
        temp = 0
        for nn in graph[n]:
            if to_leaf[nn] != -1:
                continue
            temp = max(get_leafs(nn)+1, temp)
        to_leaf[n] = temp
        return temp
    get_leafs(S)
    answer = 0
    visit = [0]*(N+1)
    def dfs(n):
        visit[n] = 1
        for nn in graph[n]:
            if visit[nn]:
                continue
            if to_leaf[nn] >= D:
                dfs(nn)
    dfs(S)
    answer = (sum(visit)-1)*2
    return answer

if __name__ == "__main__":
    print(solution())