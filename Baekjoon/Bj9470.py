# 9470 Strahler 순서 G3

import sys


def solution():
    input = sys.stdin.readline
    T = int(input())
    answer = []
    for _ in range(T):
        K, M, P = map(int, input().split())
        graph = [[] for _ in range(M+1)]
        for _ in range(P):
            a, b = map(int, input().split())
            graph[b].append(a)
        D = [0]*(M+1)
        def dfs(n):
            if D[n]:
                return D[n]
            res = 0
            for nn in graph[n]:
                temp = dfs(nn)
                if temp > res :
                    res = temp
                elif temp == res :
                    res += 1
            if not res :
                res = 1
            D[n] = res
            return res
        answer.append(' '.join(map(str, (K, dfs(M)))))

    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')