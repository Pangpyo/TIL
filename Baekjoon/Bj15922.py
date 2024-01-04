# 15922 아우으우아으이야!! G5

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    lines.sort()
    pre = -sys.maxsize
    answer = 0
    for x, y in lines :
        if x < pre :
            if y > pre :
                answer += y - pre
        else :
            answer += y - x
        pre = max(pre, y)
    return answer

if __name__ == "__main__" :
    print(solution())