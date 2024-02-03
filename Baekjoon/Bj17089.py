# 17089 세 친구 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    cnts = [0]*(N+1)
    for _ in range(M) :
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
        cnts[u] += 1
        cnts[v] += 1

    INF = sys.maxsize
    answer = INF
    for i in range(1, N+1) :
        for j in range(i+1, N+1) :
            if not graph[i][j] :
                continue
            for k in range(j+1, N+1) :
                if graph[i][k] and graph[j][k] :
                    answer = min(cnts[i] + cnts[j] + cnts[k]-6, answer)
    
    return answer if answer != INF else -1

if __name__ == "__main__" :
    print(solution())