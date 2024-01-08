# 1911 흙길 보수하기 G5

import sys


def solution() :
    input = sys.stdin.readline
    N, L = map(int, input().split())
    pools = list(tuple(map(int, input().split())) for _ in range(N))
    pools.sort()
    s = 0
    answer = 0
    for l, r in pools :
        s = max(s, l)
        diff = r - s
        cnt = 0
        if diff > 0 :
            cnt += (diff // L) + (1 if diff % L else 0)
        s += cnt * L
        answer += cnt

    return answer

if __name__ == "__main__" :
    print(solution())