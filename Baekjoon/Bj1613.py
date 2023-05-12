# 1613 역사 G3 

import sys


def solution():
    input = sys.stdin.readline
    ans = []
    N, K = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    s = int(input())
    for _ in range(s):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if graph[u][v]:
            ans.append("-1")
        elif graph[v][u]:
            ans.append("1")
        else:
            ans.append("0")
    return "\n".join(ans)


if __name__ == "__main__":
    sys.stdout.write(solution())