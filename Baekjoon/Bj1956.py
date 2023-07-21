# 1956 운동 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    inf = sys.maxsize
    graph = [[inf]*N for _ in range(N)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        graph[u-1][v-1] = d
    ans = inf
    
    for k in range(N) :
        for i in range(N) :
            for j in range(N) :
                if graph[i][k] == inf or graph[j][k] == inf :
                    continue
                graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])
    for i in range(N) :
        if graph[i][i] == inf :
            continue
        ans = min(ans, graph[i][i])
    return ans if ans != inf else -1

if __name__ == "__main__" :
    print(solution())