# 23740 버스 노선 개편하기 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    lines = list(tuple(map(int, input().split())) for _ in range(N))
    lines.sort()
    pre, end = -1, -1
    cost = 0
    ans = []
    for s, e, c in lines :
        if s <= end :
            end = max(e, end)
            cost = min(cost, c)
        else :
            ans.append((pre, end, cost))
            pre = s
            end = e
            cost = c
    ans.append((pre, end, cost))
    ans[0] = [len(ans)-1]
    return ans

if __name__ == "__main__" :
    [print(*row) for row in solution()]