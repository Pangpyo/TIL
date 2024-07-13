# 16564 히오스 프로게이머 S1

import sys


def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    X = [int(input()) for _ in range(N)]
    X.sort()
    s, e = 0, 2_000_000_001
    answer = 0
    while s <= e:
        m = (s+e)//2
        use = K
        for x in X:
            if x < m:
                use -= m - x
            else:
                break
        if use >= 0:
            s = m + 1
            answer = max(answer, m)
        else:
            e = m - 1
    return answer

if __name__ == "__main__":
    print(solution())