# 11049 행렬 곱셈 순서 G3
import sys

input = sys.stdin.readline
N = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(N)]

D = [[0] * (N + 1) for _ in range(N + 1)]
inf = sys.maxsize
for i in range(1, N):
    for j in range(1, N - i + 1):
        D[j][i + j] = inf
        for k in range(j, i + j):
            D[j][i + j] = min(
                D[j][i + j],
                D[j][k]
                + D[k + 1][i + j]
                + matrix[j - 1][0] * matrix[k - 1][1] * matrix[i + j - 1][1],
            )

print(D[1][-1])
