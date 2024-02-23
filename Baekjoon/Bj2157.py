# 2157 여행 G4

import sys


def solution() :
    input = sys.stdin.readline 
    N, M, K = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    D = [[-1]*(M+1) for _ in range(N+1)]

    for _ in range(K) :
        u, v, d = map(int, input().split())
        if v > u :
            graph[u][v] = max(graph[u][v], d)
    
    D[1][1] = 0

    for i in range(1, N+1) :
        for j in range(2, M+1) :
            D[i][j] = max(D[i][j], D[i][j-1])
            for k in range(1, i) :
                if graph[k][i] and D[k][j-1] != -1:
                    D[i][j] = max(D[i][j], D[k][j-1]+graph[k][i])

    return D[-1][-1]

if __name__ == "__main__" :
    print(solution())