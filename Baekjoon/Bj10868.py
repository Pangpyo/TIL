# 10868 최솟값 G1

import math
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    h = 1 << (int(math.log2(N)) + 1) + 1
    tree = [0] * h

    def build(node, start, end):
        if start == end:
            tree[node] = A[start]
            return tree[node]
        mid = (start + end) // 2
        tree[node] = min(build(node * 2, start, mid), build(node * 2 + 1, mid + 1, end))
        return tree[node]

    def query(node, s, e, l, r):
        if r < s or e < l:
            return sys.maxsize
        if l <= s and e <= r:
            return tree[node]
        m = (s + e) // 2
        return min(query(node * 2, s, m, l, r), query(node * 2 + 1, m + 1, e, l, r))

    build(1, 0, N - 1)
    ans = ""
    for _ in range(M):
        a, b = map(int, input().split())
        ans += str(query(1, 0, N - 1, a-1, b-1)) + "\n"
    return ans.rstrip()

if __name__ == "__main__" :
    print(solution())