# 2098 외판원 순회 G1

import sys

N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]
inf = sys.maxsize
D = [[-1] * (1 << N) for _ in range(N)]


def tsp(u, S):
    if S == (1 << N) - 1:
        if c[u][0]:
            return c[u][0]
        else:
            return inf
    if D[u][S] != -1:
        return D[u][S]
    temp = inf
    for v in range(N):
        if (S & (1 << v)) == 0 and c[u][v]:
            temp = min(temp, c[u][v] + tsp(v, S | (1 << v)))
    D[u][S] = temp
    return temp


print(tsp(0, 1))
