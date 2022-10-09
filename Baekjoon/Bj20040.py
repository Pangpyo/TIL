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


# 노드 x 가 어느 집합에 포함되어 있는지 찾는 연산


def union(x, y, i):
    global ans
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
    else:
        if ans == 0:
            ans = i


# 노드 x와 노드 y가 연결되기 때문에, 노드 x가 포함된 집합과 노드 y가 포함된 집합을 합치는 연산

for i in range(m):
    u, v = map(int, input().split())
    union(u, v, i + 1)
print(ans)
