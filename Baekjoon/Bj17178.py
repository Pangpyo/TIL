# 17178 줄서기 G5

from collections import deque
import sys


def solution():
    input = sys.stdin.readline
    N = int(input())
    lines = []
    for _ in range(N):
        line = input().rstrip().split()
        temp = []
        for l in line:
            a, n = l.split('-')
            temp.append((a, int(n)))
        lines.append(temp)
    stack = []
    sorted_line = []
    for line in lines:
        for l in line:
            sorted_line.append(l)
    sorted_line.sort()
    idx = 0
    def stack_check():
        nonlocal idx
        if stack and stack[-1] == sorted_line[idx]:
            stack.pop()
            idx += 1
            return True
        return False
    for line in lines:
        que = deque(line)
        while que:
            if que[0] == sorted_line[idx]:
                que.popleft()
                idx += 1
            elif stack_check():
                pass
            else:
                stack.append(que.popleft())
        while stack_check():
            pass
    if stack :
        return "BAD"
    else:
        return "GOOD"

if __name__ == "__main__":
    print(solution())