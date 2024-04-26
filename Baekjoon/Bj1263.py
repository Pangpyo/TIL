# 1263 시간 관리 G5

import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    tasks = list(tuple(map(int, input().split())) for _ in range(N))
    tasks.sort(key=lambda x: (-x[1], -x[0]))
    time = sys.maxsize
    for t, e in tasks:
        time = min(e-t, time-t)
        if time < 0:
            return -1
    return time

if __name__ == "__main__":
    print(solution())