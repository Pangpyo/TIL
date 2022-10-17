# 5639 이진검색트리 G4


from bisect import bisect_left
import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**9)
pre = []
for n in sys.stdin:
    pre.append(int(n))


def post(start, end):
    if start > end:
        return
    div = end + 1
    root = pre[start]
    div = bisect_left(pre, root, start + 1, end + 1)
    post(start + 1, div - 1)
    post(div, end)
    print(pre[start])


post(0, len(pre) - 1)
