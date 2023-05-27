# 15732 도토리 숨기기 G2

import sys


def solution():
    input = sys.stdin.readline
    N, K, D = map(int, input().split())
    rules = [tuple(map(int, input().split())) for _ in range(K)]
    s, e = 0, N
    ans = e

    def check(mid):
        cnt = 0
        for a, b, c in rules:
            temp = min(b, mid)
            if temp < a:
                continue
            cnt += ((temp - a) // c) + 1
        return cnt >= D

    while s <= e:
        mid = (s + e) // 2
        if check(mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


if __name__ == "__main__":
    print(solution())
