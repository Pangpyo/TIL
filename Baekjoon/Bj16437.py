# 16437 양 구출 작전 G3

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N = int(input())
    isWolf = [0]*(N+1)
    cnt = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for i in range(2, N+1) :
        t, a, p = input().split()
        a, p = int(a), int(p)
        isWolf[i] = t == "W"
        cnt[i] = a
        graph[p].append(i)
    def dfs(n) :
        temp = cnt[n]
        if isWolf[n] :
            temp *= -1
        for nn in graph[n] :
            temp += dfs(nn)
        temp = max(temp, 0)
        return temp
    answer = dfs(1)
    return answer

if __name__ == "__main__" :
    print(solution())