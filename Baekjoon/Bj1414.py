# 1414 불우이웃 돕기 G3

import sys


def solution():
    input = sys.stdin.readline

    N = int(input())

    lines = []
    lan = 0
    for u in range(N):
        temp = input().rstrip()
        for v in range(N):
            d = temp[v]
            if d.isupper():
                d = ord(d) - ord("A") + 27
            elif d.islower():
                d = ord(d) - ord("a") + 1
            else:
                d = 0
            lan += d
            if u == v or d == 0:
                continue
            lines.append((u, v, d))
    lines.sort(key=lambda x: x[2])
    parent = [-1] * N

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

    for u, v, d in lines:
        if union(u, v):
            lan -= d
        if parent[0] == -N:
            break
    if parent[0] == -N:
        return lan
    return -1


if __name__ == "__main__":
    print(solution())
