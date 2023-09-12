# 24230 트리 색칠하기 G5

import sys


def solution() :
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    N = int(input())
    colors = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for _ in range(N-1) :
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    ans = 0
    def dfs(n, c, pre) :
        nonlocal ans
        if c != colors[n] :
            ans += 1
            c = colors[n]
        for nn in graph[n] :
            if nn != pre :
                dfs(nn, c, n)
    dfs(0, 0, 0)
    return ans

if __name__ == "__main__" :
    print(solution())