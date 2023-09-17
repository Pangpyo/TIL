# 21940 가운데에서 만나기 G4

import sys


def solution() :
    input = sys.stdin.readline
    N, M = map(int, input().split())

    inf = sys.maxsize
    D = [[inf if i != j else 0 for j in range(N+1)] for i in range(N+1)]
    for _ in range(M) :
        u, v, d = map(int, input().split())
        D[u][v] = min(D[u][v], d)
    K = int(input())
    F = tuple(map(int, input().split()))
    for k in range(1, N+1) :
        for i in range(1, N+1) :
            for j in range(1, N+1) :
                if i == j :
                    continue
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    dist = [0]*(N+1)
    for f in F :
        for i in range(1, N+1) :
            dist[i] = max(dist[i], D[f][i]+D[i][f])
    ans = []
    m = min(dist[1::])
    for i in range(1, N+1) :
        if m == dist[i] :
            ans.append(i)
    return ans

if __name__ == "__main__" :
    print(*solution())