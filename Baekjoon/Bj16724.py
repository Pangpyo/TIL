# 16724 피리 부는 사나이 G3

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

zone = [list(input()) for _ in range(N)]

parent = [i for i in range(N * M)]
move = [0] * (N * M)
for i in range(N):
    for j in range(M):
        if zone[i][j] == "U":
            move[i * M + j] = (i - 1) * M + j
        elif zone[i][j] == "D":
            move[i * M + j] = (i + 1) * M + j
        elif zone[i][j] == "L":
            move[i * M + j] = i * M + j - 1
        elif zone[i][j] == "R":
            move[i * M + j] = i * M + j + 1


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)


for i in range(M * N):
    union(i, move[i])
for i in range(N * M):
    find(i)
print(len(set(parent)))
