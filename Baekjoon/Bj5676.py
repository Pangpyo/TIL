# 5676 음주코딩 G1 

import math
import sys


def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)
    def build(node, start, end):
        if start == end:
            temp = A[start]
            if temp > 0 :
                tree[node] = 1
            elif temp == 0 :
                tree[node] = 0
            else :
                tree[node] = -1
            return tree[node]
        mid = (start + end) // 2
        tree[node] = build(node * 2, start, mid)*build(node * 2 + 1, mid + 1, end)
        return tree[node]

    def query(node, s, e, l, r):
        if r < s or e < l:
            return 1
        if l <= s and e <= r:
            return tree[node]
        m = (s + e) // 2
        return query(node * 2, s, m, l, r) * query(node * 2 + 1, m + 1, e, l, r)

    def update(node, s, e, idx, value):
        if idx < s or idx > e:
            return
        if s == e:
            tree[node] = value
            return
        m = (s + e) // 2
        update(node * 2, s, m, idx, value)
        update(node * 2 + 1, m + 1, e, idx, value)
        tree[node] = tree[node * 2] * tree[node * 2 + 1]

    try :
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))
        h = 1 << (int(math.log2(N)) + 1) + 1
        tree = [0] * h
        build(1, 0, N - 1)
        ans = []
        for _ in range(Q):
            x, a, b = input().split()
            a = int(a)
            b = int(b)
            
            if x == "C" :
                if b > 0 :
                    b = 1
                elif b == 0 :
                    b = 0
                else :
                    b = -1
                update(1, 0, N - 1, a - 1, b)
            else :
                temp = query(1, 0, N-1, a-1, b-1)
                if temp > 0 :
                    temp = '+'
                elif temp == 0 :
                    temp = '0'
                else :
                    temp = '-'
                ans.append(temp)
        
        return "".join(ans)
    except :
        return None

if __name__ == "__main__" :
    while 1 :
        ans = solution()
        if ans is None :
            break
        print(ans)