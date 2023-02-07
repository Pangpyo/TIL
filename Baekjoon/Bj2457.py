# 2457 공주님의 정원 G3

import datetime
import sys

input = sys.stdin.readline

N = int(input())

flowers = []

a = 2022
o = datetime.date(a - 1, 12, 31)

x = (datetime.date(a, 3, 1) - o).days
y = (datetime.date(a, 11, 30) - o).days


for i in range(N):
    sm, sd, em, ed = map(int, input().split())
    start = (datetime.date(a, sm, sd) - o).days
    end = (datetime.date(a, em, ed) - o).days
    flowers.append((start, end))
flowers.sort()


def answer():
    stack = []
    flag = False
    for flower in flowers:
        if not stack:
            a, b = flower
            if a <= x < b:
                stack.append((x, b))
        else:
            a, b = stack[-1]
            na, nb = flower
            if b < nb:
                if na <= a:
                    stack.pop()
                    stack.append((a, nb))
                else:
                    if na <= b:
                        stack.append((b, nb))
        if stack and stack[-1][1] > y:
            flag = True
            break
    if flag:
        return len(stack)
    else:
        return 0


print(answer())
