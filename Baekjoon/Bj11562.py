# 11562 백양로 브레이크 G3
import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def floyd():
    inf = sys.maxsize
    D = [[0 if i == j else inf for j in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        u, v, b = map(int, input().split())
        D[u][v] = 0
        D[v][u] = min(int(not b), D[v][u])
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


D = floyd()
ans = []
for i in range(int(input())):
    u, v = map(int, input().split())
    ans.append(str(D[u][v]))

print("\n".join(ans))
