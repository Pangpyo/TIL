# 6497 전력난 G4

import sys


input = sys.stdin.readline

while 1 :
    m, n = map(int, input().split())
    if m == n == 0 :
        break
    parent = [i for i in range(0, m + 1)]

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


    ans = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        ans += z
        graph.append((x, y, z))


    graph.sort(key=lambda x: x[2])


    for u, v, l in graph:
        if union(u, v):
            ans -= l
    print(ans)
