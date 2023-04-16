# 2406 안정적인 네트워크 G3

import sys


def solution():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    parent = [-1] * n

    def find(x):
        if parent[x] < 0:
            return x
        y = find(parent[x])
        parent[x] = y
        return y

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        parent[min(x, y)] += parent[max(x, y)]
        parent[max(x, y)] = min(x, y)
        return True

    for i in range(m):
        u, v = map(int, input().split())
        if u == 1 or v == 1:
            continue
        union(u - 1, v - 1)
    costs = [list(map(int, input().split())) for _ in range(n)]

    lines = []

    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            lines.append((i, j, costs[i][j]))
    if n < 3:
        print(0, 0)
        return
    if parent[1] == -n:
        print(0, 0)
        return
    lines.sort(key=lambda x: x[2])
    conn = [0, 0]
    need = []

    for u, v, cost in lines:
        if union(u, v):
            conn[0] += cost
            conn[1] += 1
            need.append((u + 1, v + 1))
        if -parent[1] == n - 1:
            break

    print(*conn)
    for i in range(conn[1]):
        print(*need[i])
    return


if __name__ == "__main__":
    solution()
