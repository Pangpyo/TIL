# 11505 구간 곱 구하기 G1
import math
import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    h = 1 << (int(math.log2(N)) + 1) + 1
    tree = [0] * h
    div = 1000000007

    def build(node, start, end):
        if start == end:
            tree[node] = A[start]
            return tree[node]
        mid = (start + end) // 2
        tree[node] = build(node * 2, start, mid) * build(node * 2 + 1, mid + 1, end)
        tree[node] %= div
        return tree[node]

    def query(node, s, e, l, r):
        if r < s or e < l:
            return 1
        if l <= s and e <= r:
            return tree[node]
        m = (s + e) // 2
        return (query(node * 2, s, m, l, r) * query(node * 2 + 1, m + 1, e, l, r)) % div

    def update(node, s, e, idx, value):
        if idx < s or idx > e:
            return
        if s == e:
            tree[node] = value
            return
        m = (s + e) // 2
        update(node * 2, s, m, idx, value)
        update(node * 2 + 1, m + 1, e, idx, value)
        tree[node] = tree[node * 2] * tree[node * 2 + 1] % div

    build(1, 0, N - 1)
    ans = ""
    for i in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 0, N - 1, b - 1, c)
        else:
            ans += str(query(1, 0, N - 1, b - 1, c - 1)) + "\n"

    return ans.rstrip()


if __name__ == "__main__":
    print(solution())
