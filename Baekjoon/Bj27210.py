
# 27210 신을 모시는 사당 G5
# A번 - 신을 모시는 사당

import sys


sys.stdin = open("input.txt")

n = int(input())

S = list(map(int, input().split()))

o = [0] * n  # 1을 세어주는 리스트
t = [0] * n  # 2를 세어주는 리스트


for i in range(n):
    if S[i] == 1:  # 1이 들어온 경우
        o[i] = o[i - 1] + 1  # 1리스트는 이전의 1값에 +1
        t[i] = max(0, t[i - 1] - 1)  # 2리스트는 이전의 2값에 -1, 0보다 작아지는 경우 0
    elif S[i] == 2:  # 2가 들어온 경우
        o[i] = max(0, o[i - 1] - 1)  # 1리스트는 이전의 1값에 -1, 0보다 작아지는 경우 0
        t[i] = t[i - 1] + 1  # 2리스트는 이전의 2값에 +1

print(max(max(o), max(t)))  # 최대값을 구해준다
