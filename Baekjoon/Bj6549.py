# 6549 히스토그램에서 가장 큰 직사각형 P5

import math
import sys

## 세그트리 풀이
def solution() :
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    answers = []
    while True :
        nums = list(map(int, input().split()))
        N = nums[0]
        if not N :
            break
        A = nums[1::]
        h = 1 << (int(math.log2(N))+1) + 1
        tree = [0]*h
        def build(node, start, end) :
            if start == end :
                tree[node] = start
                return start
            mid = (start + end) // 2
            i = build(node*2, start, mid)
            j = build(node*2+1 , mid+1, end)
            tree[node] = i if A[i] < A[j] else j
            return tree[node]
        build(1, 0, N-1)
        def query(node, s, e, l, r):
            if r < s or e < l:
                return -1
            if l <= s and e <= r:
                return tree[node]
            m = (s + e) // 2
            left_max_idx = query(node * 2, s, m, l, r)
            right_max_idx = query(node * 2 + 1, m + 1, e, l, r)
            if left_max_idx == -1 :
                return right_max_idx
            elif right_max_idx == -1 :
                return left_max_idx
            else :
                return left_max_idx if A[left_max_idx] < A[right_max_idx] else right_max_idx
        def width(l, r) :
            idx = query(1, 0, N-1, l, r)
            max_width = (r-l+1) * A[idx]
            if l < idx :
                max_width = max(max_width, width(l, idx-1))
            if idx < r :
                max_width = max(max_width, width(idx+1, r))
            return max_width

        answers.append(width(0, N-1))
    return answers


## 스택 풀이
def solution2() :
    answers = []
    while True :
        nums = list(map(int, input().split()))
        N = nums[0]
        if not N :
            break
        A = nums[1::]
        A.append(-1)
        stack = []
        max_area = 0
        for i, h in enumerate(A) :
            while stack and stack[-1][1] > h:
                si, sh = stack.pop()
                width_start = 0
                if stack :
                    width_start = stack[-1][0]+1
                area = (i - width_start) * sh
                max_area = max(max_area, area)
            else :
                stack.append((i, h))
            
        answers.append(max_area)
    return answers

if __name__ == "__main__" :
    print(*solution2(), sep='\n')