# 2170 선 긋기 G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort()
    pre = -sys.maxsize
    answer = 0
    for s, e in lines :
        pre = max(s, pre)
        answer += max(0, e - pre)
        pre = max(e, pre)
    return answer

if __name__ == "__main__" :
    print(solution())