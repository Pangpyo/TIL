# 20040 사이클 게임 G4

import sys


input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(0, n)]
ans = 0


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y, i):
    global ans
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
    else:
        if ans == 0:
            ans = i


for i in range(m):
    u, v = map(int, input().split())
    union(u, v, i + 1)
print(ans)
