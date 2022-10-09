# 1197 최소 스패닝 트리 G4

import sys


input = sys.stdin.readline

V, E = map(int, input().split())

parent = [i for i in range(0, V + 1)]

graph = []


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
        return True
    else:
        return False


for i in range(E):
    graph.append(tuple(map(int, input().split())))

graph.sort(key=lambda x: x[2])
ans = 0
for u, v, l in graph:
    if union(u, v):
        ans += l
print(ans)
