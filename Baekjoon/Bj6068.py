# 6068 시간 관리하기 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    works = [tuple(map(int, input().split())) for _ in range(N)]
    works.sort(key=lambda x : (-x[1], -x[0]))
    time = sys.maxsize
    for t, s in works :
        time = min(time, s) - t
    if time < 0 :
        return -1
    return time

if __name__ == "__main__" :
    print(solution())