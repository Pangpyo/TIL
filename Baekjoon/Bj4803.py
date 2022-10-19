# 4803 트리 G4

import sys

# input = sys.stdin.readline

sys.stdin = open("input.txt")


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
    else:
        cycle.add(x)


t = 1
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parent = [i for i in range(n + 1)]
    cycle = set()
    for i in range(m):
        u, v = map(int, input().split())
        union(u, v)
    tree = set()
    for i in range(n + 1):
        find(i)
    cycle = set(find(i) for i in cycle)
    tree = set(parent) - cycle - set([0])
    ans = len(tree)
    if ans == 0:
        print(f"Case {t}: No trees.")
    elif ans == 1:
        print(f"Case {t}: There is one tree.")
    else:
        print(f"Case {t}: A forest of {ans} trees.")
    t += 1
