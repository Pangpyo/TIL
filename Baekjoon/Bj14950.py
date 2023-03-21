# 14950 정복자 G3

import sys


def solution():
    input = sys.stdin.readline
    N, M, t = map(int, input().split())

    parent = [-1] * (N + 1)

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
        else:
            parent[min(x, y)] += parent[max(x, y)]
            parent[max(x, y)] = min(x, y)
            return True

    lines = sorted(
        [tuple(map(int, input().split())) for _ in range(M)], key=lambda x: x[2]
    )
    ans = sum(range(N - 1)) * t
    for u, v, d in lines:
        if union(u, v):
            ans += d
            if parent[1] == -N:
                return ans


if __name__ == "__main__":
    print(solution())
