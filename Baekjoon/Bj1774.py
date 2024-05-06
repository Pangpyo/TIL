# 1774 우주신과의 교감 G3
import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    nodes = tuple(tuple(map(int, input().split())) for _ in range(N))
    parents = [-1]*N
    def find(x):
        if parents[x] < 0:
            return x
        y = find(parents[x])
        parents[x] = y
        return y
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        parents[min(x, y)] += parents[max(x, y)]
        parents[max(x, y)] = min(x, y)
        return True
    
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, input().split())
        union(u, v)

    lines = []

    def get_distance(u, v):
        ax, ay = nodes[u]
        bx, by = nodes[v]
        return ((ax-bx)**2 + (ay-by)**2)**0.5

    for i in range(N):
        for j in range(i+1, N):
            if find(i) == find(j):
                continue
            lines.append((get_distance(i, j), i, j))
    lines.sort()
    answer = 0
    for d, x, y in lines:
        if union(x, y):
            answer += d
    return f"{answer:.2f}"

if __name__ == "__main__":
    print(solution())