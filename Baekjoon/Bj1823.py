# 1823 수확 G3

import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(2000)
    N = int(input())
    V = (0,) + tuple(int(input()) for _ in range(N))
    D = [[0]*(N+1) for _ in range(N+1)]
    def dfs(a, b, n) :
        if a == b :
            return n*V[a]
        if D[a][b] :
            return D[a][b]
        temp = max(dfs(a+1, b, n+1) + V[a]*n, dfs(a, b-1, n+1) + V[b]*n)
        D[a][b] = temp
        return temp
    answer = dfs(1, N, 1)
    return answer

if __name__ == "__main__" :
    print(solution())