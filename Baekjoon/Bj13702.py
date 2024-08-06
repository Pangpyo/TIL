# 13702 이상한 술집 S2

import sys


def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    drinks = tuple(int(input()) for _ in range(N))
    s, e = 1, max(drinks)
    answer = 0
    while s <= e:
        m = (s+e)//2
        cnt = 0
        for drink in drinks:
            cnt += drink//m
        if cnt >= K:
            answer = max(answer, m)
            s = m + 1
        else:
            e = m - 1
    return answer

if __name__ == "__main__":
    print(solution())