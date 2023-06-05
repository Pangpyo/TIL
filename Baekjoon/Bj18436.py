# 18436 수열과 쿼리 37 G1
import math
import sys


def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    N = int(input())
    A = list(map(int, input().split()))
    h = 1 << (int(math.log2(N)) + 1) + 1
    odd_tree = [0] * h
    even_tree = [0] * h
    def odd_build(node, start, end):
        if start == end:
            odd_tree[node] = A[start] % 2
            return odd_tree[node]
        mid = (start + end) // 2
        odd_tree[node] = odd_build(node * 2, start, mid) + odd_build(node * 2 + 1, mid + 1, end)
        return odd_tree[node]

    def odd_query(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return odd_tree[node]
        m = (s + e) // 2
        return (odd_query(node * 2, s, m, l, r) + odd_query(node * 2 + 1, m + 1, e, l, r))

    def odd_update(node, s, e, idx, value):
        if idx < s or idx > e:
            return
        if s == e:
            odd_tree[node] = value % 2
            return
        m = (s + e) // 2
        odd_update(node * 2, s, m, idx, value)
        odd_update(node * 2 + 1, m + 1, e, idx, value)
        odd_tree[node] = odd_tree[node * 2] + odd_tree[node * 2 + 1]

    odd_build(1, 0, N - 1)

    def even_build(node, start, end):
        if start == end:
            even_tree[node] = (A[start]+1) %2
            return even_tree[node]
        mid = (start + end) // 2
        even_tree[node] = even_build(node * 2, start, mid) + even_build(node * 2 + 1, mid + 1, end)
        return even_tree[node]

    def even_query(node, s, e, l, r):
        if r < s or e < l:
            return 0
        if l <= s and e <= r:
            return even_tree[node]
        m = (s + e) // 2
        return (even_query(node * 2, s, m, l, r) + even_query(node * 2 + 1, m + 1, e, l, r))

    def even_update(node, s, e, idx, value):
        if idx < s or idx > e:
            return
        if s == e:
            even_tree[node] = (value+1)%2
            return
        m = (s + e) // 2
        even_update(node * 2, s, m, idx, value)
        even_update(node * 2 + 1, m + 1, e, idx, value)
        even_tree[node] = even_tree[node * 2] + even_tree[node * 2 + 1]

    even_build(1, 0, N - 1)
    ans = []
    Q = int(input())
    for i in range(Q):
        a, b, c = map(int, input().split())
        if a == 1:
            odd_update(1, 0, N - 1, b - 1, c)
            even_update(1, 0, N - 1, b - 1, c)
        elif a == 2:
            ans.append(str(even_query(1, 0, N - 1, b - 1, c - 1)))
        else :
            ans.append(str(odd_query(1, 0, N - 1, b - 1, c - 1)))

    return '\n'.join(ans)


if __name__ == "__main__":
    print(solution())
