# 6218 Balanced Lineup G1


import math
import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    h = 1 << (int(math.log2(N)) + 1) +1
    mintree = [0] * h
    maxtree = [0] * h

    def min_build(node, start, end):
        if start == end:
            mintree[node] = A[start]
            return mintree[node]
        mid = (start + end) // 2

        mintree[node] = min(
            min_build(node * 2, start, mid), min_build(node * 2 + 1, mid + 1, end)
        )
        return mintree[node]

    def max_build(node, start, end):
        if start == end:
            maxtree[node] = A[start]
            return maxtree[node]
        mid = (start + end) // 2

        maxtree[node] = max(
            max_build(node * 2, start, mid), max_build(node * 2 + 1, mid + 1, end)
        )
        return maxtree[node]

    def min_query(node, s, e, l, r):
        if r < s or e < l:
            return sys.maxsize
        if l <= s and e <= r:
            return mintree[node]
        m = (s + e) // 2
        return min(
            min_query(node * 2, s, m, l, r),
            min_query(node * 2 + 1, m + 1, e, l, r),
        )

    def max_query(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return maxtree[node]
        m = (s + e) // 2
        return max(
            max_query(node * 2, s, m, l, r),
            max_query(node * 2 + 1, m + 1, e, l, r),
        )

    min_build(1, 0, N - 1)
    max_build(1, 0, N - 1)
    ans = []
    for _ in range(M):
        a, b = map(int, input().split())
        ans.append(str(max_query(1, 0, N - 1, a - 1, b - 1)-min_query(1, 0, N - 1, a - 1, b - 1)))

    return "\n".join(ans)


if __name__ == "__main__":
    print(solution())
