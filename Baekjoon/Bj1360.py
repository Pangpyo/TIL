# 1360 되돌리기 G5

import sys


sys.stdin = open("input.txt")


N = int(input())
stack = []


def undo(t, s):
    i = 0
    diff = s - t
    for i in range(len(stack)):
        if s > stack[i][2] >= diff:
            stack[i][3] = not stack[i][3]


for i in range(N):
    command, x, s = input().split()
    if command == "type":
        stack.append([1, x, int(s), True])
    elif command == "undo":
        stack.append([2, int(x), int(s), True])

if N == 0:
    pass
else:
    for i in range(N - 1, -1, -1):
        if stack[i][0] == 2 and stack[i][3]:
            undo(stack[i][1], stack[i][2])

    for i in range(N):
        if stack[i][0] == 1 and stack[i][3]:
            print(stack[i][1], end="")
