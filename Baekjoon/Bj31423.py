# 31423 신촌 통폐합 계획 G5

import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N = int(input())
    univ = [input().rstrip() for _ in range(N)]
    tree = [[] for _ in range(N)]
    rtree = list(range(N))
    for _ in range(N-1):
        u, v = map(lambda x: int(x)-1, input().split())
        rtree[v] = u
        tree[u].append(v)
    def get_root(n):
        if rtree[n] == n:
            return n
        return get_root(rtree[n])
    root = get_root(1)
    answer = []
    stack = [root]
    while stack:
        n = stack.pop()
        answer.append(univ[n])
        for nn in reversed(tree[n]):
            stack.append(nn)
    return ''.join(answer)

if __name__ == "__main__":
    print(solution())