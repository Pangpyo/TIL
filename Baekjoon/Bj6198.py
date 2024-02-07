# 6198 옥상 정원 꾸미기

import sys


def solution() :
    input = sys.stdin.readline
    N = int(input())
    stack = []
    answer = 0
    for _ in range(N) :
        h = int(input())
        while stack and stack[-1] <= h :
            stack.pop()
        stack.append(h)
        answer += len(stack)-1

    return answer

if __name__ == "__main__" :
    print(solution())