# 16958 텔레포트 G4

import sys


def solution():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    city = tuple(tuple(map(int, input().split())) for _ in range(N))
    INF = sys.maxsize
    graph = [[INF]*N for _ in range(N)]
    for i in range(N):
        s, x, y = city[i]
        graph[i][i] = 0
        for j in range(i+1, N):
            ns, nx, ny = city[j]
            d = abs(x-nx)+abs(y-ny)
            if s == ns == 1:
                d = min(T, d)
            graph[i][j] = d
            graph[j][i] = d
    for k in range(N):
        for i in range(N):
            if k == i:
                continue
            for j in range(N):
                if i == j or k == j:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    M = int(input())
    answer = [0]*M
    for m in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        answer[m] = graph[a][b]
    return answer

if __name__ == "__main__":
    print(*solution(), sep='\n')