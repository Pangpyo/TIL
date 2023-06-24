# 7983 내일 할거야 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    hwk = [tuple(map(int, input().split())) for _ in range(N)]
    hwk.sort(key = lambda x: (-x[1], -x[0]))
    now = sys.maxsize
    for d, t in hwk :
        now = min(now, t)-d
    return now

if __name__ == "__main__" :
    print(solution())