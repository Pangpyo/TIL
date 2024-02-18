# 2836 수상 택시 G3

import sys


def solution() :
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    backs = []
    for _ in range(N) :
        s, e = map(int, input().split())
        if e < s :
            backs.append((e, s))
    backs.sort()
    pre = 0
    answer = 0
    for s, e in backs :
        pre = max(s, pre)
        answer += max(0, e - pre)
        pre = max(pre, e)
    return answer*2+M

if __name__ == "__main__" :
    print(solution())