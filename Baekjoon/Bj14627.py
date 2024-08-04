# 14627 파닭파닭 S2

import sys


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = tuple(int(input()) for _ in range(N))
    s, e = 1, 1_000_000_001
    use = 0
    while s <= e:
        m = (s+e)//2
        cnt = 0
        for p in P:
            cnt += p//m
        if cnt >= M:
            use = max(use, m)
            s = m + 1
        else:
            e = m - 1
    answer = sum(P) - M*use
    return answer

if __name__ == "__main__":
    print(solution())