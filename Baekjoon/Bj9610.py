# 9610 사분면 B3

import sys

sys.stdin = open("input.txt")

N = int(input())


ans = [0]*5
for i in range(N) :
    x, y = map(int, input().split())
    if x > 0 and y > 0 :
        ans[0] += 1
    elif x < 0 and y > 0 :
        ans[1] += 1
    elif x < 0 and y < 0 :
        ans[2] += 1
    elif x > 0 and y < 0 :
        ans[3] += 1
    else :
        ans[4] += 1
print(f'Q1: {ans[0]}\nQ2: {ans[1]}\nQ3: {ans[2]}\nQ4: {ans[3]}\nAXIS: {ans[4]}')
