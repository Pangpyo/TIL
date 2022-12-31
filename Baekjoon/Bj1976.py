# 1976 여행가자 G4

import sys


input = sys.stdin.readline

N = int(input())
M = int(input())

parent = list(range(N))


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


for u in range(N):
    lines = list(map(int, input().split()))
    for v in range(N):
        if u == v:
            continue
        if lines[v]:
            union(u, v)




plan = list(map(int, input().split()))

start = find(plan[0]-1)

def answer():
    for p in plan:
        if find(p - 1) != start:
            return "NO"
    return "YES"


print(answer())
