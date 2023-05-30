# 1275 커피숍2 G1

import math
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    h = 1 << (int(math.log2(N)) + 1) + 1
    tree = [0] * h

    def build(node, start, end):
        if start == end:
            tree[node] = A[start]
            return tree[node]
        mid = (start + end) // 2
        tree[node] = build(node * 2, start, mid) + build(node * 2 + 1, mid + 1, end)
        return tree[node]

    def query(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return tree[node]
        m = (s + e) // 2
        return (query(node * 2, s, m, l, r) + query(node * 2 + 1, m + 1, e, l, r))

    def update(node, s, e, idx, value):
        if idx < s or idx > e:
            return
        if s == e:
            tree[node] = value
            return
        m = (s + e) // 2
        update(node * 2, s, m, idx, value)
        update(node * 2 + 1, m + 1, e, idx, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

    build(1, 0, N - 1)
    ans = ""
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        ans += str(query(1, 0, N - 1, min(x, y) - 1, max(x, y) - 1)) + "\n"
        update(1, 0, N - 1, a - 1, b)
    return ans.rstrip()

if __name__ == "__main__" :
    print(solution())