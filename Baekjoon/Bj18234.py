# 18234 당근 훔쳐 먹기 G3 

import sys


def solution() :
    input = sys.stdin.readline
    N, T = map(int, input().split())
    carrots = [tuple(map(int, input().split())) for _ in range(N)]
    carrots.sort(key = lambda x: x[1])

    ans = 0
    d = T-N
    for w, p in carrots:
        ans += w + p*d
        d += 1

    return ans

if __name__ == "__main__" :
    print(solution())


