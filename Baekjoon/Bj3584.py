# 3584 가장 가까운 공통 조상 G4

import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(n):
    if parent[n]:
        ap[parent[n]] = 1
        dfs(parent[n])


def dfs2(n):
    if ap[n]:
        return n
    elif parent[n]:
        return dfs2(parent[n])


for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n + 1)
    for i in range(n - 1):
        p, s = map(int, input().split())
        parent[s] = p
    a, b = map(int, input().split())
    ap = [0] * (n + 1)
    ap[a] = 1
    dfs(a)
    print(dfs2(b))
