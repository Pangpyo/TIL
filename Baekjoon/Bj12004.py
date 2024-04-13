# 12004 Closing the Farm (Silver) G4

import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**4)
    N, M = map(int, input().split())
    graph = [[] for _  in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    open_farm = set(range(1, N+1))
    def dfs(x):
        visit[x] = 1
        temp = 1
        for nx in graph[x]:
            if not visit[nx] and nx in open_farm:
                temp += dfs(nx)
        return temp
    answer = ["YES"]*N
    for i in range(N):
        visit = [0]*(N+1)
        conn_farm = 0
        for of in open_farm:
            conn_farm = dfs(of)
            break
        if len(open_farm) != conn_farm:
            answer[i] = "NO"
        close_farm = int(input())
        open_farm.remove(close_farm)
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')